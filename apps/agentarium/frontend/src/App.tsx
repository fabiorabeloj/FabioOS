import { useMemo, useState } from "react";
import { AgentMap } from "./components/AgentMap";
import { AgentList } from "./components/AgentList";
import { SecurityMatrixPanel } from "./components/SecurityMatrix";
import { AgentInspector } from "./components/AgentInspector";
import { useAgents } from "./hooks/useAgents";
import "./App.css";

export default function App() {
  const { agents, matrix, connected, error, refetch } = useAgents();
  const [selectedId, setSelectedId] = useState<string | null>(null);

  const selected = useMemo(
    () => agents.find((a) => a.id === selectedId) ?? null,
    [agents, selectedId],
  );

  return (
    <div className="app app--tactical">
      <header className="app__header">
        <div>
          <h1>MEGATRON Tactical Agentarium</h1>
          <p className="app__subtitle">
            Presenca · governanca · seguranca operacional — FabioOS / OpenClaw
          </p>
        </div>
        <div className="app__status">
          <span
            className={`dot ${connected ? "dot--ok" : "dot--warn"}`}
            title={connected ? "WebSocket conectado" : "Fallback HTTP"}
          />
          {connected ? "Tempo real" : "Polling"}
          <button type="button" className="btn btn-tactical" onClick={() => refetch()}>
            Atualizar
          </button>
        </div>
      </header>

      {error && (
        <div className="banner banner--error" role="alert">
          {error}
        </div>
      )}

      {!error && agents.length === 0 && (
        <div className="banner banner--warn" role="status">
          Nenhum agente carregado. Inicie backend + frontend.
        </div>
      )}

      <SecurityMatrixPanel
        matrix={matrix}
        selectedId={selectedId}
        onSelect={setSelectedId}
      />

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

      <footer className="app__footer">
        v0.2 · OpenClaw multi-agent sandbox · estado operacional separado da animacao
      </footer>
    </div>
  );
}
