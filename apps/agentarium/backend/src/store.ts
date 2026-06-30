import type {
  Agent,
  AgentPolicyUpdate,
  AgentRuntimeState,
  AgentStateUpdate,
  AgentCatalog,
  AgentLayer,
  Zone,
} from "./types.js";
import { buildInitialActiveAgents, buildFullCatalog, LAYER_LABELS } from "./agents/fabioAgents.js";
import { refreshAllRisks, refreshAgentRisk } from "./risk.js";

const now = () => new Date().toISOString();

type Listener = (agent: Agent) => void;
type MatrixListener = () => void;

class AgentStore {
  private agents = new Map<string, Agent>();
  private listeners = new Set<Listener>();
  private matrixListeners = new Set<MatrixListener>();

  constructor(seed: Agent[]) {
    const withRisk = refreshAllRisks(seed);
    for (const a of withRisk) {
      this.agents.set(a.id, { ...a });
    }
  }

  list(): Agent[] {
    return refreshAllRisks([...this.agents.values()]).sort((a, b) =>
      a.id.localeCompare(b.id),
    );
  }

  listActive(): Agent[] {
    return this.list().filter((a) => a.status === "active");
  }

  catalog(): AgentCatalog {
    const agents = buildFullCatalog(this.agents);
    const counts = {
      active: agents.filter((a) => a.status === "active").length,
      planned: agents.filter((a) => a.status === "planned").length,
      inactive: agents.filter((a) => a.status === "inactive").length,
      total: agents.length,
    };
    return {
      agents,
      layers: Object.keys(LAYER_LABELS) as AgentLayer[],
      counts,
    };
  }

  catalogAgents(): Agent[] {
    return this.catalog().agents;
  }

  get(id: string): Agent | undefined {
    const a = this.agents.get(id);
    if (a) {
      const [refreshed] = refreshAllRisks([a]);
      return refreshed;
    }
    return buildFullCatalog(this.agents).find((c) => c.id === id);
  }

  private persist(agent: Agent): Agent {
    const [final] = refreshAllRisks([agent]);
    this.agents.set(final.id, final);
    for (const fn of this.listeners) fn(final);
    for (const fn of this.matrixListeners) fn();
    return final;
  }

  update(id: string, patch: AgentStateUpdate): Agent {
    const current = this.agents.get(id);
    if (!current) throw new Error(`Agent not found: ${id}`);
    return this.persist({
      ...current,
      ...patch,
      updatedAt: now(),
    });
  }

  updatePolicy(id: string, patch: AgentPolicyUpdate): Agent {
    const current = this.agents.get(id);
    if (!current) throw new Error(`Agent not found: ${id}`);
    const merged = {
      ...current,
      policy: { ...current.policy, ...patch },
      updatedAt: now(),
    };
    return this.persist(merged);
  }

  subscribe(fn: Listener): () => void {
    this.listeners.add(fn);
    return () => this.listeners.delete(fn);
  }

  subscribeMatrix(fn: MatrixListener): () => void {
    this.matrixListeners.add(fn);
    return () => this.matrixListeners.delete(fn);
  }
}

export const store = new AgentStore(buildInitialActiveAgents());

export function isValidState(s: string): s is AgentRuntimeState {
  return ["idle", "thinking", "executing", "waiting_approval", "done", "error"].includes(
    s,
  );
}

export function isValidZone(z: string): z is Zone {
  return [
    "WhatsApp",
    "Inbox",
    "Classificação",
    "Obsidian",
    "GitHub",
    "n8n",
    "RAG",
    "Aprovação Humana",
    "Concluído",
    "Erro",
  ].includes(z);
}

export { refreshAgentRisk };
