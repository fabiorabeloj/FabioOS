import type { Agent, AgentLayer, AgentPolicy, Zone } from "../types.js";
import { AGENT_LAYERS } from "../types.js";
import { LAYER_LABELS } from "../agents/fabioAgents.js";
import { homeZoneFor } from "../agents/agentVisualClasses.js";
import { MAESTRO_VISUAL_ALIASES } from "./aliases.js";
import type { MaestroAgentJson, MaestroBarramentoEntry } from "./types.js";
import type { EventLogEntry } from "../eventLog.js";

const now = () => new Date().toISOString();

const MAESTRO_HOME_ZONES: Partial<Record<string, Zone>> = {
  arquivista: "Inbox",
  rag: "RAG",
  grafo: "RAG",
  reasoningbank: "Obsidian",
  barramento: "Classificação",
  pesquisador: "RAG",
  documentalista: "WhatsApp",
  interface: "Classificação",
  atendente: "Personal WhatsApp",
  programador: "GitHub",
  automacao: "n8n",
  banco: "RAG",
  laboratorio: "n8n",
  coletor_visual: "RAG",
  navegador: "GitHub",
  infra: "GitHub",
};

function isAgentLayer(value: string): value is AgentLayer {
  return (AGENT_LAYERS as readonly string[]).includes(value);
}

function defaultMaestroPolicy(id: string): Omit<AgentPolicy, "riskLevel" | "riskNotes"> {
  return {
    sandboxMode: "unknown",
    sandboxScope: "maestro",
    workspaceRoot: "FabioOS vault",
    workspaceAccess: "ro",
    dockerSandbox: "unknown",
    browserSandbox: "unknown",
    prunePolicy: "maestro-sourced",
    allowedTools: ["read"],
    deniedTools: ["exec", "process", "write", "edit"],
    elevated: "disabled",
    agentDir: `60_Sistemas/MEGATRON/agents/${id}`,
    authProfile: "unknown",
  };
}

function homeForMaestroAgent(id: string, layer: AgentLayer): Zone {
  return MAESTRO_HOME_ZONES[id] ?? homeZoneFor(MAESTRO_VISUAL_ALIASES[id] ?? id, layer);
}

export function maestroAgentToAgent(
  m: MaestroAgentJson,
  preserved?: Agent,
): Agent {
  const layer: AgentLayer = isAgentLayer(m.layer) ? m.layer : "technical";
  const home = homeForMaestroAgent(m.id, layer);
  const gated = m.rawStatus === "gated";

  const base: Agent = {
    id: m.id,
    name: m.name,
    layer,
    status: m.status === "active" ? "active" : "planned",
    rawStatus: m.rawStatus,
    role: m.role,
    responsibilities: m.capabilities,
    inputs: [],
    outputs: m.capabilities,
    requiresApprovalFor: gated ? ["external_action", "secrets"] : [],
    essential: m.status === "active",
    catalogZone: LAYER_LABELS[layer] ?? m.layer,
    state: preserved?.state ?? "idle",
    task: preserved?.task ?? m.role,
    zone: preserved?.zone ?? home,
    homeZone: home,
    lastEventSource: "real",
    updatedAt: preserved?.updatedAt ?? now(),
    policy: {
      ...defaultMaestroPolicy(m.id),
      riskLevel: "safe",
      riskNotes: [],
    },
  };

  return base;
}

function parseBarramentoTimestamp(ts: string): string {
  const normalized = ts.includes("T") ? ts : ts.replace(" ", "T");
  const withZone = /Z|[+-]\d{2}:\d{2}$/.test(normalized) ? normalized : `${normalized}:00`;
  const d = new Date(withZone);
  if (Number.isNaN(d.getTime())) {
    return new Date().toISOString();
  }
  return d.toISOString();
}

function barramentoAgentId(de: string): string | undefined {
  const map: Record<string, string> = {
    claude: "barramento",
    codex: "programador",
    cursor: "interface",
    lead: "barramento",
    todos: "barramento",
  };
  return map[de] ?? de;
}

export function barramentoToEventLog(
  entry: MaestroBarramentoEntry,
  index: number,
): EventLogEntry {
  const agentId = barramentoAgentId(entry.de);
  return {
    id: `maestro-barr-${index}-${entry.ts.replace(/\D/g, "").slice(0, 14)}`,
    timestamp: parseBarramentoTimestamp(entry.ts),
    channel: "AGENT",
    agentId,
    source: "maestro-barramento",
    message: `[${entry.tipo}] ${entry.de} → ${entry.para}: ${entry.mensagem}`,
    approvalState: entry.status,
  };
}

export function mapBarramentoEvents(
  barramento: MaestroBarramentoEntry[],
): EventLogEntry[] {
  return [...barramento]
    .reverse()
    .map((entry, index) => barramentoToEventLog(entry, index));
}
