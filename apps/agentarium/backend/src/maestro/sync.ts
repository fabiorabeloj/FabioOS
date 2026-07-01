import { store } from "../store.js";
import { eventLog } from "../eventLog.js";
import { buildSecurityMatrix } from "../risk.js";
import type { WsMessage } from "../types.js";
import { loadMaestroState, maestroStateExists } from "./loader.js";
import { mapBarramentoEvents, maestroAgentToAgent } from "./mapping.js";
import { resolveMaestroStatePath } from "./paths.js";
import type { MaestroSyncStatus } from "./types.js";
import { startMaestroWatcher } from "./watcher.js";
import { barramentoStore } from "./barramentoStore.js";

type Broadcaster = (msg: WsMessage) => void;

let lastStatus: MaestroSyncStatus = {
  ok: false,
  path: resolveMaestroStatePath(),
  generatedAt: null,
  source: null,
  agentCount: 0,
  activeCount: 0,
  barramentoCount: 0,
};

export function getMaestroSyncStatus(): MaestroSyncStatus {
  return { ...lastStatus };
}

export function applyMaestroStateFromFile(filePath?: string): MaestroSyncStatus {
  const path = filePath ?? resolveMaestroStatePath();

  try {
    const state = loadMaestroState(path);
    const preserved = new Map(store.list().map((a) => [a.id, a]));
    const agents = state.agents.map((m) =>
      maestroAgentToAgent(m, preserved.get(m.id)),
    );

    store.syncFromMaestro(agents, state.generatedAt, state.source);

    const barramentoRaw = state.barramento ?? [];
    barramentoStore.replace(barramentoRaw, state.generatedAt);
    const barramentoEvents = mapBarramentoEvents(barramentoRaw);
    eventLog.replaceMaestroBarramentoEvents(barramentoEvents);

    eventLog.append({
      channel: "SYSTEM",
      source: "maestro-sync",
      message: `[MAESTRO] Roster sincronizado (${state.counts?.active ?? agents.filter((a) => a.status === "active").length} ativos / ${agents.length} total) — ${state.generatedAt}`,
    });

    lastStatus = {
      ok: true,
      path,
      generatedAt: state.generatedAt,
      source: state.source,
      agentCount: agents.length,
      activeCount: agents.filter((a) => a.status === "active").length,
      barramentoCount: barramentoEvents.length,
    };
  } catch (err) {
    lastStatus = {
      ok: false,
      path,
      generatedAt: null,
      source: null,
      agentCount: 0,
      activeCount: 0,
      barramentoCount: 0,
      error: err instanceof Error ? err.message : String(err),
    };
  }

  return { ...lastStatus };
}

function broadcastAfterSync(broadcast: Broadcaster): void {
  broadcast({ type: "catalog", catalog: store.catalog() });
  broadcast({ type: "snapshot", agents: store.listActive() });
  broadcast({
    type: "security_matrix",
    matrix: buildSecurityMatrix(store.catalogAgents()),
  });
  broadcast({ type: "event_log_snapshot", entries: eventLog.list(200) });
  broadcast({ type: "barramento_snapshot", barramento: barramentoStore.snapshot() });
}

export function getBarramentoSnapshot() {
  return barramentoStore.snapshot();
}

export function initMaestroIntegration(broadcast: Broadcaster): () => void {
  const path = resolveMaestroStatePath();

  if (maestroStateExists(path)) {
    const status = applyMaestroStateFromFile(path);
    if (status.ok) {
      broadcastAfterSync(broadcast);
    }
  } else {
    lastStatus = {
      ok: false,
      path,
      generatedAt: null,
      source: null,
      agentCount: 0,
      activeCount: 0,
      barramentoCount: 0,
      error: "maestro_state.json nao encontrado — usando roster legado",
    };
  }

  return startMaestroWatcher(path, () => {
    const status = applyMaestroStateFromFile(path);
    if (status.ok) {
      broadcastAfterSync(broadcast);
    }
  });
}
