import fs from "node:fs";
import path from "node:path";
import type { IntakeActionResult, IntakeQueueJson, IntakeExtracao, IntakeCard } from "./types.js";
import {
  loadQueueFile,
  recalcResumo,
  saveQueueFile,
  isSensitiveCard,
} from "./reader.js";
import {
  resolveArquivistaScript,
  resolveIntakeFlowScript,
  resolveIntakeLog,
  resolveIntakeQueueLive,
  resolveUniversalAdapterScript,
  resolveIntakeCommandExtractScript,
  resolveGmailFakeExample,
} from "./paths.js";
import { runPython, runPythonJson, runPythonWithTempInput } from "./python.js";

async function extractStructuredFields(text: string): Promise<IntakeExtracao | null> {
  try {
    return await runPythonJson<IntakeExtracao>(resolveIntakeCommandExtractScript(), [
      "--text",
      text,
    ]);
  } catch {
    return null;
  }
}

function applyExtraction(card: IntakeCard, text: string, ext: IntakeExtracao | null): void {
  if (!ext || ext.confianca <= 0) return;
  card.extracao = ext;

  const parts = [ext.produto, ext.serie, ext.tema, ext.prazo].filter(Boolean);
  if (parts.length === 0) return;

  if (ext.produto && ext.serie) {
    const subj = `${String(ext.produto).charAt(0).toUpperCase()}${String(ext.produto).slice(1)} ${ext.serie}`;
    card.subject = ext.tema ? `${subj} — ${ext.tema}` : subj;
  }

  const structured = [
    ext.produto ? String(ext.produto).charAt(0).toUpperCase() + String(ext.produto).slice(1) : null,
    ext.serie,
    ext.tema ? `sobre ${ext.tema}` : null,
    ext.prazo ? `(${ext.prazo})` : null,
  ]
    .filter(Boolean)
    .join(" ");

  if (structured && !card.summary.toLowerCase().includes(structured.slice(0, 12).toLowerCase())) {
    card.summary = card.summary ? `${structured} — ${card.summary}` : structured;
  }
}

function appendLogLine(entry: Record<string, string>): void {
  const logPath = resolveIntakeLog();
  fs.mkdirSync(path.dirname(logPath), { recursive: true });
  fs.appendFileSync(logPath, JSON.stringify(entry) + "\n", "utf8");
}

async function ensureLiveQueue(): Promise<IntakeQueueJson> {
  const livePath = resolveIntakeQueueLive();
  let queue = loadQueueFile(livePath);
  if (!queue) {
    const { code, stderr, stdout } = await runPython(resolveIntakeFlowScript(), []);
    if (code !== 0) {
      throw new Error(stderr.trim() || stdout.trim() || "intake_flow falhou");
    }
    queue = loadQueueFile(livePath);
  }
  if (!queue) {
    throw new Error("intake_queue.json ausente apos intake_flow.py");
  }
  return queue;
}

export async function approveIntakeItem(id: string): Promise<IntakeActionResult> {
  await ensureLiveQueue();
  const cardBefore = loadQueueFile(resolveIntakeQueueLive())?.fila.find((c) => c.id === id);
  if (!cardBefore) {
    return { ok: false, message: `Item ${id} nao encontrado na fila live.` };
  }
  if (cardBefore.status !== "waiting_approval") {
    return { ok: false, message: `Item ${id} nao esta aguardando aprovacao (${cardBefore.status}).` };
  }

  const { stdout, stderr, code } = await runPython(resolveArquivistaScript(), ["--aprovar", id]);
  const out = (stdout + "\n" + stderr).trim();
  const queueAfter = loadQueueFile(resolveIntakeQueueLive());
  const cardAfter = queueAfter?.fila.find((c) => c.id === id);

  if (isSensitiveCard(cardBefore)) {
    return {
      ok: true,
      blocked: true,
      message: out || "Item sensivel escalado — nao gravou nota (trava §3).",
      item: cardAfter,
    };
  }

  if (cardAfter?.status === "executed" && cardAfter.nota_ref) {
    return {
      ok: true,
      message: out || `Gravado: ${cardAfter.nota_ref}`,
      notaRef: cardAfter.nota_ref,
      item: cardAfter,
    };
  }

  return { ok: code === 0, message: out || "Aprovacao processada.", item: cardAfter };
}

export async function rejectIntakeItem(id: string): Promise<IntakeActionResult> {
  const livePath = resolveIntakeQueueLive();
  const queue = loadQueueFile(livePath);
  if (!queue) {
    return { ok: false, message: "Fila live ausente." };
  }
  const item = queue.fila.find((c) => c.id === id && c.status === "waiting_approval");
  if (!item) {
    return { ok: false, message: `Item ${id} nao encontrado ou ja processado.` };
  }
  item.status = "archived";
  queue.resumo = recalcResumo(queue.fila);
  saveQueueFile(livePath, queue);
  appendLogLine({
    ts: new Date().toISOString(),
    quem: "Agentarium (rejeicao Fabio)",
    o_que: `REJEITOU ${id} (${item.domain}/${item.sensitivity})`,
    onde: "intake_queue.json",
    proximo: "status=archived",
  });
  return { ok: true, message: `Item ${id} arquivado.`, item };
}

export async function submitNaturalCommand(text: string): Promise<IntakeActionResult> {
  const trimmed = text.trim();
  if (trimmed.length < 4) {
    return { ok: false, message: "Comando muito curto." };
  }

  const payload = {
    items: [
      {
        source: "manual",
        sender: "Fabio (comando Agentarium)",
        subject: "",
        texto: trimmed,
        received_at: new Date().toISOString(),
      },
    ],
  };

  const { stdout, stderr, code } = await runPythonWithTempInput(
    resolveUniversalAdapterScript(),
    ["--stdout"],
    payload,
  );

  if (code !== 0) {
    return { ok: false, message: stderr.trim() || stdout.trim() || `adapter exit ${code}` };
  }

  let partial: IntakeQueueJson;
  try {
    partial = JSON.parse(stdout) as IntakeQueueJson;
  } catch {
    return { ok: false, message: "Adapter nao retornou JSON valido." };
  }

  const card = partial.fila[0];
  if (!card) {
    return { ok: false, message: "Nenhum card gerado pelo adapter." };
  }

  const ext = await extractStructuredFields(trimmed);
  applyExtraction(card, trimmed, ext);

  const livePath = resolveIntakeQueueLive();
  let queue = loadQueueFile(livePath);
  if (!queue) {
    queue = {
      generated_at: new Date().toISOString(),
      gerado_por: "Agentarium comando natural",
      contrato: partial.contrato ?? "MEGATRON Core Spec v0.1",
      resumo: { total: 0, aguardando_fabio: 0, sensiveis: 0 },
      cores_status: partial.cores_status ?? {},
      fila: [],
    };
  }

  queue.fila = [card, ...queue.fila.filter((c) => c.id !== card.id)];
  queue.generated_at = new Date().toISOString();
  queue.gerado_por = "Agentarium + universal_intake_adapter";
  queue.resumo = recalcResumo(queue.fila);
  saveQueueFile(livePath, queue);

  appendLogLine({
    ts: new Date().toISOString(),
    quem: "Agentarium (comando natural)",
    o_que: `PENDENCIA ${card.id} ${card.domain}/${card.urgency}/${card.suggested_action}`,
    onde: "intake_queue.json",
    proximo: "humano aprova/rejeita na mesa de despacho",
  });

  return {
    ok: true,
    message: `Pendencia criada: ${card.domain}/${card.urgency} → ${card.suggested_action}`,
    item: card,
  };
}

export async function refreshIntakeQueueFromFlow(): Promise<IntakeActionResult> {
  const { stdout, stderr, code } = await runPython(resolveIntakeFlowScript(), []);
  if (code !== 0) {
    return { ok: false, message: stderr.trim() || stdout.trim() || "intake_flow falhou" };
  }
  return { ok: true, message: stdout.trim() || "Fila regenerada via intake_flow.py" };
}

export async function importGmailFakeDryRun(): Promise<IntakeActionResult> {
  const fakePath = resolveGmailFakeExample();
  const { stdout, stderr, code } = await runPython(resolveUniversalAdapterScript(), [
    "--stdout",
    "--input",
    fakePath,
  ]);

  if (code !== 0) {
    return { ok: false, message: stderr.trim() || stdout.trim() || `adapter exit ${code}` };
  }

  let partial: IntakeQueueJson;
  try {
    partial = JSON.parse(stdout) as IntakeQueueJson;
  } catch {
    return { ok: false, message: "Adapter nao retornou JSON valido." };
  }

  const cards = partial.fila ?? [];
  if (cards.length === 0) {
    return { ok: false, message: "Nenhum card no payload Gmail fake." };
  }

  for (const card of cards) {
    const texto = card.summary || card.subject || "";
    const ext = await extractStructuredFields(texto);
    applyExtraction(card, texto, ext);
  }

  const livePath = resolveIntakeQueueLive();
  let queue = loadQueueFile(livePath);
  if (!queue) {
    queue = {
      generated_at: new Date().toISOString(),
      gerado_por: "Agentarium import Gmail fake",
      contrato: partial.contrato ?? "MEGATRON Core Spec v0.1",
      resumo: { total: 0, aguardando_fabio: 0, sensiveis: 0 },
      cores_status: partial.cores_status ?? {},
      fila: [],
    };
  }

  const ids = new Set(cards.map((c) => c.id));
  queue.fila = [...cards, ...queue.fila.filter((c) => !ids.has(c.id))];
  queue.generated_at = new Date().toISOString();
  queue.gerado_por = "Agentarium + gmail fake dry-run";
  queue.resumo = recalcResumo(queue.fila);
  saveQueueFile(livePath, queue);

  appendLogLine({
    ts: new Date().toISOString(),
    quem: "Agentarium (Gmail fake dry-run)",
    o_que: `IMPORT ${cards.length} card(s) de intake_gmail_fake.json`,
    onde: "intake_queue.json",
    proximo: "humano aprova/rejeita na mesa de despacho",
  });

  return {
    ok: true,
    message: `${cards.length} card(s) importados do Gmail fake (dry-run, sem OAuth).`,
    item: cards[0],
  };
}
