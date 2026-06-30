import { useMemo, useState } from "react";
import { AgentMap } from "./components/AgentMap";
import { AgentList } from "./components/AgentList";
import { SecurityMatrixPanel } from "./components/SecurityMatrix";
import { AgentInspector } from "./components/AgentInspector";
import { AgentCatalogPanel } from "./components/AgentCatalog";
import { useAgents } from "./hooks/useAgents";
import "./App.css";
import "./pixel/animations.css";

type Tab = "operacional" | "catalog";

export default function App() {
  const { agents, catalog, matrix, connected, error, refetch, resolveAgent } =
    useAgents();
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [tab, setTab] = useState<Tab>("operacional");

  const selected = useMemo(
    () => resolveAgent(selectedId),
    [resolveAgent, selectedId],
  );

  return (
    <div className="app app--tactical">
      <header className="app__header pixel-panel pixel-border">
        <div>
          <h1>MEGATRON Tactical Agentarium</h1>
          <p className="app__subtitle">
            Presenca · governanca · catalogo multiagente — FabioOS / OpenClaw
          </p>
        </div>
        <div className="app__status">
          <span
            className={`dot ${connected ? "dot--ok" : "dot--warn"}`}
            title={connected ? "WebSocket conectado" : "Fallback HTTP"}
          />
          {connected ? "Tempo real" : "Polling"}
          <button type="button" className="btn btn-tactical pixel-button" onClick={() => refetch()}>
            Atualizar
          </button>
        </div>
      </header>

      <nav className="app__tabs pixel-panel pixel-border">
        <button
          type="button"
          className={`pixel-button app__tab ${tab === "operacional" ? "app__tab--active" : ""}`}
          onClick={() => setTab("operacional")}
        >
          Operacional
        </button>
        <button
          type="button"
          className={`pixel-button app__tab ${tab === "catalog" ? "app__tab--active" : ""}`}
          onClick={() => setTab("catalog")}
        >
          Agent Catalog
          {catalog && (
            <span className="app__tab-count">{catalog.counts.planned}</span>
          )}
        </button>
      </nav>

      {error && (
        <div className="banner banner--error" role="alert">
          {error}
        </div>
      )}

      {!error && agents.length === 0 && tab === "operacional" && (
        <div className="banner banner--warn" role="status">
          Nenhum agente ativo. Inicie backend + frontend.
        </div>
      )}

      <SecurityMatrixPanel
        matrix={matrix}
        selectedId={selectedId}
        onSelect={setSelectedId}
      />

      {tab === "operacional" ? (
        <div className="app__layout">
          <AgentMap
            agents={agents}
            selectedId={selectedId}
            onSelect={setSelectedId}
          />
          <div className="app__side">
            <AgentList
              agents={agents}
              selectedId={selectedId}
              onSelect={setSelectedId}
            />
            <AgentInspector agent={selected} />
          </div>
        </div>
      ) : (
        <div className="app__layout app__layout--catalog">
          <AgentCatalogPanel
            catalog={catalog}
            selectedId={selectedId}
            onSelect={setSelectedId}
          />
          <div className="app__side">
            <AgentInspector agent={selected} />
          </div>
        </div>
      )}

      <footer className="app__footer pixel-label">
        v0.3 · Pixel Ops + Agent Catalog · {catalog?.counts.total ?? 27} agentes FabioOS
      </footer>
    </div>
  );
}
