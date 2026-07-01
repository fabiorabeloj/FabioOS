import type { AgentStateKind, Zone } from "./types.js";
import { store } from "./store.js";
import { eventLog } from "./eventLog.js";

type SimStep = {
  state: AgentStateKind;
  task: string;
  zone: Zone;
};

const FLOWS: Record<string, SimStep[]> = {
  hermes: [
    { state: "executing", task: "Sim: mensagem pessoal recebida", zone: "Personal WhatsApp" },
    { state: "thinking", task: "Sim: triagem", zone: "Message Intake" },
    { state: "waiting_approval", task: "Sim: rascunho aguardando Fabio", zone: "Awaiting Fabio" },
    { state: "idle", task: "Aguardando mensagens pessoais", zone: "Personal WhatsApp" },
  ],
  pietra: [
    { state: "executing", task: "Sim: mensagem escolar", zone: "Classificação" },
    { state: "waiting_approval", task: "Sim: resposta institucional", zone: "Aprovação Humana" },
    { state: "idle", task: "Aguardando mensagens escolares", zone: "Classificação" },
  ],
  arquivista: [
    { state: "executing", task: "Sim: triando captura", zone: "Inbox" },
    { state: "executing", task: "Sim: arquivando", zone: "Obsidian" },
    { state: "idle", task: "Monitorando inbox", zone: "Inbox" },
  ],
  codex: [
    { state: "executing", task: "Sim: refatoracao", zone: "GitHub" },
    { state: "done", task: "Sim: PR pronto", zone: "Concluído" },
    { state: "idle", task: "Repositorio estavel", zone: "GitHub" },
  ],
  pesquisador: [
    { state: "thinking", task: "Sim: consultando RAG", zone: "RAG" },
    { state: "done", task: "Sim: sintese pronta", zone: "Obsidian" },
    { state: "idle", task: "Indice vetorial pronto", zone: "RAG" },
  ],
  supervisor: [
    { state: "waiting_approval", task: "Sim: fila de aprovacao", zone: "Aprovação Humana" },
    { state: "idle", task: "Fila de aprovacoes vazia", zone: "Aprovação Humana" },
  ],
};

let timer: ReturnType<typeof setInterval> | null = null;
const indices = new Map<string, number>();

export function simulationStatus(): { running: boolean; intervalMs: number } {
  return { running: timer !== null, intervalMs: SIM_INTERVAL_MS };
}

const SIM_INTERVAL_MS = 8000;

export function startSimulation(): void {
  if (timer) return;
  for (const id of Object.keys(FLOWS)) {
    indices.set(id, 0);
  }
  timer = setInterval(tickSimulation, SIM_INTERVAL_MS);
}

export function stopSimulation(): void {
  if (timer) {
    clearInterval(timer);
    timer = null;
  }
}

function tickSimulation(): void {
  for (const [agentId, steps] of Object.entries(FLOWS)) {
    if (!store.get(agentId)) continue;
    const idx = indices.get(agentId) ?? 0;
    const step = steps[idx % steps.length];
    const prev = store.get(agentId);
    indices.set(agentId, (idx + 1) % steps.length);
    store.updateWithMeta(agentId, step, {
      eventSource: "sim",
      fromZone: prev?.zone,
      toZone: step.zone,
    });
    eventLog.append({
      channel: "SIM",
      agentId,
      fromZone: prev?.zone,
      toZone: step.zone,
      message: `[SIM] ${agentId} · ${prev?.zone ?? "?"} → ${step.zone}`,
    });
  }
}

export function simulateError(agentId: string): void {
  store.updateWithMeta(agentId, {
    state: "error",
    task: "Falha simulada — verificar logs",
    zone: "Erro",
  }, { eventSource: "sim" });
}
