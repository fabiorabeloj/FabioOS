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
import { homeZoneFor } from "./agents/agentVisualClasses.js";
import { refreshAllRisks, refreshAgentRisk } from "./risk.js";
import { resolveMaestroAgentId } from "./maestro/aliases.js";

const now = () => new Date().toISOString();

type AgentMeta = {
  eventSource?: "real" | "sim" | "idle";
  jobId?: string;
  fromZone?: Zone;
  toZone?: Zone;
};

type Listener = (agent: Agent) => void;
type MatrixListener = () => void;

class AgentStore {
  private agents = new Map<string, Agent>();
  private listeners = new Set<Listener>();
  private matrixListeners = new Set<MatrixListener>();
  private maestroMode = false;
  private maestroGeneratedAt: string | null = null;
  private maestroSource: string | null = null;

  constructor(seed: Agent[]) {
    const withRisk = refreshAllRisks(seed);
    for (const a of withRisk) {
      this.agents.set(a.id, { ...a, homeZone: a.homeZone ?? homeZoneFor(a.id, a.layer) });
    }
  }

  resolveAgentId(id: string): string {
    return resolveMaestroAgentId(id);
  }

  isMaestroMode(): boolean {
    return this.maestroMode;
  }

  maestroMeta(): { generatedAt: string | null; source: string | null } {
    return {
      generatedAt: this.maestroGeneratedAt,
      source: this.maestroSource,
    };
  }

  syncFromMaestro(agents: Agent[], generatedAt: string, source: string): void {
    const withRisk = refreshAllRisks(agents);
    this.agents.clear();
    for (const a of withRisk) {
      this.agents.set(a.id, {
        ...a,
        homeZone: a.homeZone ?? homeZoneFor(a.id, a.layer),
      });
    }
    this.maestroMode = true;
    this.maestroGeneratedAt = generatedAt;
    this.maestroSource = source;
    for (const fn of this.matrixListeners) fn();
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
    const agents = this.maestroMode
      ? this.list()
      : buildFullCatalog(this.agents);
    const counts = {
      active: agents.filter((a) => a.status === "active").length,
      planned: agents.filter((a) => a.status === "planned").length,
      inactive: agents.filter((a) => a.status === "inactive").length,
      total: agents.length,
    };
    const catalog: AgentCatalog = {
      agents,
      layers: Object.keys(LAYER_LABELS) as AgentLayer[],
      counts,
    };
    if (this.maestroMode) {
      catalog.maestro = {
        synced: true,
        generatedAt: this.maestroGeneratedAt,
        source: this.maestroSource,
      };
    }
    return catalog;
  }

  catalogAgents(): Agent[] {
    return this.catalog().agents;
  }

  get(id: string): Agent | undefined {
    const resolved = this.resolveAgentId(id);
    const a = this.agents.get(resolved);
    if (a) {
      const [refreshed] = refreshAllRisks([a]);
      return refreshed;
    }
    if (this.maestroMode) return undefined;
    return buildFullCatalog(this.agents).find((c) => c.id === resolved);
  }

  private persist(agent: Agent): Agent {
    const [final] = refreshAllRisks([agent]);
    this.agents.set(final.id, final);
    for (const fn of this.listeners) fn(final);
    for (const fn of this.matrixListeners) fn();
    return final;
  }

  update(id: string, patch: AgentStateUpdate): Agent {
    return this.updateWithMeta(id, patch, {});
  }

  updateWithMeta(id: string, patch: AgentStateUpdate, meta: AgentMeta): Agent {
    const resolved = this.resolveAgentId(id);
    const current = this.agents.get(resolved);
    if (!current) throw new Error(`Agent not found: ${id}`);
    return this.persist({
      ...current,
      ...patch,
      ...meta,
      homeZone: current.homeZone ?? homeZoneFor(resolved, current.layer),
      updatedAt: now(),
    });
  }

  resetToHome(id: string): Agent {
    const resolved = this.resolveAgentId(id);
    const current = this.agents.get(resolved);
    if (!current) throw new Error(`Agent not found: ${id}`);
    const home = current.homeZone ?? homeZoneFor(resolved, current.layer);
    return this.updateWithMeta(resolved, { zone: home, state: "idle" }, { eventSource: "idle" });
  }

  updatePolicy(id: string, patch: AgentPolicyUpdate): Agent {
    const resolved = this.resolveAgentId(id);
    const current = this.agents.get(resolved);
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
    "Personal WhatsApp",
    "Message Intake",
    "Draft Reply",
    "Awaiting Fabio",
    "Approved",
    "Sent",
    "Blocked",
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
