import type { WhatsAppMessageInput } from "./types.js";
import { parseCommand } from "./commands.js";
import { resolveMaestroAgentId } from "../maestro/aliases.js";

export type CapturedTask = {
  prompt: string;
  title: string;
  suggestedAgent: string;
  suggestedAgentLabel: string;
  source: "explicit_prefix" | "command" | "implicit";
};

const GREETING_ONLY =
  /^(oi|ol[aá]|hey|e a[ií]|bom dia|boa tarde|boa noite|tudo bem|obrigado|valeu)\b[!.\s]*$/i;

const EXPLICIT_PREFIX = /^(fabioos|tarefa|prompt|pedido|task)[,:\s]+/i;

const ACTION_VERBS =
  /^(preciso|implementa|cria|criar|revisa|revisar|organiza|organizar|faz|fazer|adiciona|adicionar|corrige|corrigir|escreve|escrever|atualiza|atualizar|configura|configurar|monta|montar|liga|ligar|documenta|planeja|analisa|verifica|arruma|conserta|deploy|commit|push|refatora|testa|gera|gerar)\b/i;

export function isFabioSender(input: WhatsAppMessageInput, fabioNumber: string): boolean {
  const from = input.from.replace(/\D/g, "");
  const fabio = fabioNumber.replace(/\D/g, "");
  return from === fabio || input.direction === "outgoing";
}

export function normalizePrompt(text: string): string {
  return text.replace(EXPLICIT_PREFIX, "").trim() || text.trim();
}

export function parseTaskCommand(text: string): { prompt: string } | null {
  const parsed = parseCommand(text);
  if (!parsed) return null;
  if (parsed.command === "/tarefa" || parsed.command === "/prompt") {
    const prompt = parsed.args.trim();
    if (!prompt) return null;
    return { prompt };
  }
  return null;
}

function suggestAgent(prompt: string): { id: string; label: string } {
  const t = prompt.toLowerCase();
  if (/escola|turma|prova|aluno|geografia|filosofia|pietra|professor/.test(t)) {
    return { id: resolveMaestroAgentId("pietra"), label: "Documentalista (escola)" };
  }
  if (/codigo|cursor|github|commit|bug|script|api|backend|frontend|refator|implement|deploy|teste/.test(t)) {
    return { id: resolveMaestroAgentId("codex"), label: "Programador (codigo)" };
  }
  if (/organiz|vault|obsidian|wiki|inbox|arquiv|document|nota/.test(t)) {
    return { id: "arquivista", label: "Arquivista (vault)" };
  }
  if (/n8n|workflow|automac|docker|evolution|whatsapp|megatron|agentarium/.test(t)) {
    return { id: resolveMaestroAgentId("codex"), label: "Programador (sistemas)" };
  }
  return { id: resolveMaestroAgentId("megatron"), label: "Interface / Cursor (geral)" };
}

export function detectTask(
  input: WhatsAppMessageInput,
  fabioNumber: string,
  forcedPrompt?: string,
): CapturedTask | null {
  if (!isFabioSender(input, fabioNumber)) return null;

  const raw = input.text.trim();
  if (!raw) return null;

  if (forcedPrompt) {
    const prompt = forcedPrompt.trim();
    const agent = suggestAgent(prompt);
    return {
      prompt,
      title: prompt.length > 72 ? `${prompt.slice(0, 72)}…` : prompt,
      suggestedAgent: agent.id,
      suggestedAgentLabel: agent.label,
      source: "command",
    };
  }

  if (GREETING_ONLY.test(raw)) return null;
  if (raw.startsWith("/")) return null;

  const hasExplicitPrefix = EXPLICIT_PREFIX.test(raw);
  const prompt = normalizePrompt(raw);
  const hasAction = ACTION_VERBS.test(prompt);
  const longEnough = prompt.length >= 15;

  if (!hasExplicitPrefix && !hasAction && !longEnough) return null;

  const agent = suggestAgent(prompt);
  return {
    prompt,
    title: prompt.length > 72 ? `${prompt.slice(0, 72)}…` : prompt,
    suggestedAgent: agent.id,
    suggestedAgentLabel: agent.label,
    source: hasExplicitPrefix ? "explicit_prefix" : "implicit",
  };
}

export function buildTaskConfirmation(task: CapturedTask, jobId: string, _taskFile: string): string {
  return [
    "Tarefa capturada.",
    "",
    `"${task.title}"`,
    "",
    `ID: ${jobId}`,
    `Agente sugerido: ${task.suggestedAgentLabel}`,
    "",
    "No Cursor, digite:",
    `Leia 00_Inbox/Processar/Tarefas_WPP/${jobId}.md e execute.`,
  ].join("\n");
}
