import { useCallback, useEffect, useRef, useState } from "react";
import type { Agent, AgentCatalog, AgentLayer, SecurityMatrix, WsMessage } from "../types";

const API_BASE = (import.meta.env.VITE_API_BASE as string | undefined)?.replace(/\/$/, "") ?? "/api";
const WS_BASE =
  (import.meta.env.VITE_WS_BASE as string | undefined) ??
  `${window.location.protocol === "https:" ? "wss:" : "ws:"}//${window.location.host}/ws`;

function mergeAgent(list: Agent[], updated: Agent): Agent[] {
  const idx = list.findIndex((a) => a.id === updated.id);
  if (idx === -1) return [...list, updated].sort((a, b) => a.id.localeCompare(b.id));
  const next = [...list];
  next[idx] = updated;
  return next;
}

function mergeCatalogAgents(catalog: AgentCatalog, updated: Agent): AgentCatalog {
  return {
    ...catalog,
    agents: mergeAgent(catalog.agents, updated),
  };
}

export function useAgents() {
  const [agents, setAgents] = useState<Agent[]>([]);
  const [catalog, setCatalog] = useState<AgentCatalog | null>(null);
  const [matrix, setMatrix] = useState<SecurityMatrix | null>(null);
  const [connected, setConnected] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const wsRef = useRef<WebSocket | null>(null);

  const fetchAgents = useCallback(async () => {
    try {
      const [agentsRes, matrixRes, catalogRes] = await Promise.all([
        fetch(`${API_BASE}/agents`),
        fetch(`${API_BASE}/security/matrix`),
        fetch(`${API_BASE}/catalog`),
      ]);
      if (!agentsRes.ok) throw new Error(`HTTP ${agentsRes.status} /agents`);
      const agentsData = (await agentsRes.json()) as { agents: Agent[] };
      setAgents(agentsData.agents);
      if (matrixRes.ok) {
        setMatrix((await matrixRes.json()) as SecurityMatrix);
      }
      if (catalogRes.ok) {
        setCatalog((await catalogRes.json()) as AgentCatalog);
      }
      setError(null);
    } catch (e) {
      const msg = e instanceof Error ? e.message : "Falha ao carregar";
      setError(`${msg} (${API_BASE})`);
    }
  }, []);

  useEffect(() => {
    fetchAgents();
    const poll = setInterval(fetchAgents, 20000);

    const ws = new WebSocket(WS_BASE);
    wsRef.current = ws;

    ws.onopen = () => setConnected(true);
    ws.onclose = () => setConnected(false);
    ws.onerror = () => setConnected(false);

    ws.onmessage = (ev) => {
      try {
        const msg = JSON.parse(ev.data as string) as WsMessage;
        if (msg.type === "snapshot") {
          setAgents(msg.agents);
          setError(null);
        } else if (msg.type === "agent_updated") {
          setAgents((prev) => mergeAgent(prev, msg.agent));
          setCatalog((prev) => (prev ? mergeCatalogAgents(prev, msg.agent) : prev));
        } else if (msg.type === "security_matrix") {
          setMatrix(msg.matrix);
        } else if (msg.type === "catalog") {
          setCatalog(msg.catalog);
        }
      } catch {
        /* ignore */
      }
    };

    return () => {
      clearInterval(poll);
      ws.close();
    };
  }, [fetchAgents]);

  const resolveAgent = useCallback(
    (id: string | null): Agent | null => {
      if (!id) return null;
      return (
        agents.find((a) => a.id === id) ??
        catalog?.agents.find((a) => a.id === id) ??
        null
      );
    },
    [agents, catalog],
  );

  return {
    agents,
    catalog,
    matrix,
    connected,
    error,
    refetch: fetchAgents,
    apiBase: API_BASE,
    resolveAgent,
  };
}

export function filterCatalogByLayer(
  catalog: AgentCatalog | null,
  layer: AgentLayer | "all",
): Agent[] {
  if (!catalog) return [];
  if (layer === "all") return catalog.agents;
  return catalog.agents.filter((a) => a.layer === layer);
}
