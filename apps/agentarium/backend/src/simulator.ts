import type { AgentStateKind, Zone } from "./types.js";
import { store } from "./store.js";

type SimStep = {
  state: AgentStateKind;
  task: string;
  zone: Zone;
  delayMs?: number;
};

const FLOWS: Record<string, SimStep[]> = {
  pietra: [
    { state: "executing", task: "Lendo mensagem de responsável", zone: "WhatsApp" },
    { state: "thinking", task: "Classificando intenção", zone: "Classificação" },
    { state: "waiting_approval", task: "Resposta aguardando Fabio", zone: "Aprovação Humana" },
    { state: "done", task: "Atendimento encerrado", zone: "Concluído" },
    { state: "idle", task: "Aguardando mensagens", zone: "WhatsApp" },
  ],
  arquivista: [
    { state: "executing", task: "Triando captura bruta", zone: "Inbox" },
    { state: "thinking", task: "Normalizando metadados", zone: "Classificação" },
    { state: "executing", task: "Gravando nota no vault", zone: "Obsidian" },
    { state: "done", task: "Arquivo concluído", zone: "Concluído" },
    { state: "idle", task: "Monitorando inbox", zone: "Inbox" },
  ],
  codex: [
    { state: "thinking", task: "Analisando diff pendente", zone: "GitHub" },
    { state: "executing", task: "Aplicando refatoração", zone: "GitHub" },
    { state: "executing", task: "Workflow CI via n8n", zone: "n8n" },
    { state: "done", task: "PR pronto para revisão", zone: "Concluído" },
    { state: "idle", task: "Repositório estável", zone: "GitHub" },
  ],
  pesquisador: [
    { state: "thinking", task: "Consultando embeddings", zone: "RAG" },
    { state: "executing", task: "Rankeando fontes", zone: "RAG" },
    { state: "executing", task: "Sintetizando conceitos", zone: "Obsidian" },
    { state: "done", task: "Nota wiki atualizada", zone: "Concluído" },
    { state: "idle", task: "Índice vetorial pronto", zone: "RAG" },
  ],
  supervisor: [
    { state: "thinking", task: "Revisando risco de commit", zone: "Aprovação Humana" },
    { state: "executing", task: "Scan de segredos", zone: "GitHub" },
    { state: "waiting_approval", task: "Aguardando OK humano", zone: "Aprovação Humana" },
    { state: "done", task: "Validação registrada", zone: "Concluído" },
    { state: "idle", task: "Fila de aprovações vazia", zone: "Aprovação Humana" },
  ],
};

let timer: ReturnType<typeof setInterval> | null = null;
const indices = new Map<string, number>();

export function simulationStatus(): { running: boolean; intervalMs: number } {
  return { running: timer !== null, intervalMs: SIM_INTERVAL_MS };
}

const SIM_INTERVAL_MS = 4500;

export function startSimulation(): void {
  if (timer) return;
  for (const id of Object.keys(FLOWS)) {
    indices.set(id, 0);
  }
  timer = setInterval(tickSimulation, SIM_INTERVAL_MS);
  tickSimulation();
}

export function stopSimulation(): void {
  if (timer) {
    clearInterval(timer);
    timer = null;
  }
}

function tickSimulation(): void {
  for (const [agentId, steps] of Object.entries(FLOWS)) {
    const idx = indices.get(agentId) ?? 0;
    const step = steps[idx % steps.length];
    indices.set(agentId, (idx + 1) % steps.length);
    store.update(agentId, step);
  }
}

/** Injeta um passo de erro simulado (demo). */
export function simulateError(agentId: string): void {
  store.update(agentId, {
    state: "error",
    task: "Falha simulada — verificar logs",
    zone: "Erro",
  });
}
