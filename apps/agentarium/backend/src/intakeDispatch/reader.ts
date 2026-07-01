import fs from "node:fs";
import path from "node:path";
import type { CoordenacaoSnapshot, IntakeCard, IntakeDispatchSnapshot, IntakeQueueJson } from "./types.js";
import {
  resolveCoordenacaoScript,
  resolveIntakeQueueLive,
  resolveIntakeQueueSample,
  resolveIntakeSpecPath,
} from "./paths.js";
import { runPythonJson } from "./python.js";

const SENSITIVE = new Set(["restricted", "forbidden_external", "no_rag"]);

export function loadQueueFile(filePath: string): IntakeQueueJson | null {
  if (!fs.existsSync(filePath)) return null;
  try {
    return JSON.parse(fs.readFileSync(filePath, "utf8")) as IntakeQueueJson;
  } catch {
    return null;
  }
}

export function saveQueueFile(filePath: string, queue: IntakeQueueJson): void {
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  fs.writeFileSync(filePath, JSON.stringify(queue, null, 2) + "\n", "utf8");
}

export function recalcResumo(fila: IntakeCard[]): IntakeQueueJson["resumo"] {
  return {
    total: fila.length,
    aguardando_fabio: fila.filter((i) => i.status === "waiting_approval").length,
    sensiveis: fila.filter((i) =>
      ["private", "restricted", "no_rag", "forbidden_external"].includes(String(i.sensitivity)),
    ).length,
  };
}

export function isSensitiveCard(card: IntakeCard): boolean {
  return SENSITIVE.has(String(card.sensitivity));
}

export async function loadCoordenacao(): Promise<{
  data: CoordenacaoSnapshot | null;
  error?: string;
}> {
  try {
    const data = await runPythonJson<CoordenacaoSnapshot>(resolveCoordenacaoScript(), ["--json"]);
    return { data };
  } catch (err) {
    return {
      data: null,
      error: err instanceof Error ? err.message : String(err),
    };
  }
}

export async function buildIntakeDispatchSnapshot(): Promise<IntakeDispatchSnapshot> {
  const livePath = resolveIntakeQueueLive();
  const samplePath = resolveIntakeQueueSample();
  const live = loadQueueFile(livePath);
  const sample = loadQueueFile(samplePath);
  const queue = live ?? sample;
  const fallbackMode = !live && !!sample;
  const sourcePath = live ? livePath : samplePath;

  const pending = (queue?.fila ?? []).filter((i) => i.status === "waiting_approval");
  const coord = await loadCoordenacao();

  return {
    scannedAt: new Date().toISOString(),
    sourcePath,
    fallbackMode,
    specPath: resolveIntakeSpecPath(),
    queue: queue ?? {
      generated_at: "",
      gerado_por: "",
      contrato: "MEGATRON Core Spec v0.1",
      resumo: { total: 0, aguardando_fabio: 0, sensiveis: 0 },
      cores_status: {},
      fila: [],
    },
    pending,
    coordenacao: coord.data,
    coordenacaoError: coord.error,
  };
}
