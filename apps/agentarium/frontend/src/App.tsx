import { useMemo, useState } from "react";
import { AgentMap } from "./components/AgentMap";
import { AgentList } from "./components/AgentList";
import { SecurityMatrixPanel } from "./components/SecurityMatrix";
import { AgentInspector } from "./components/AgentInspector";
import { AgentCatalogPanel } from "./components/AgentCatalog";
import { EventLog } from "./components/EventLog";
import { WhatsAppIntakePanel } from "./components/WhatsAppIntakePanel";
import { WhatsAppOperationsPanel } from "./components/WhatsAppOperationsPanel";
import { BarramentoPanel } from "./components/BarramentoPanel";
import { PdfPipelinePanel } from "./components/PdfPipelinePanel";
import { PietraInboxPanel } from "./components/PietraInboxPanel";
import { MegatronCockpitPanel } from "./components/MegatronCockpitPanel";
import { MegatronChatPanel } from "./components/MegatronChatPanel";
import { IntakeDispatchPanel } from "./components/IntakeDispatchPanel";
import { useAgents } from "./hooks/useAgents";
import "./App.css";
import "./pixel/animations.css";

type Tab = "cockpit" | "operacional" | "catalog" | "barramento" | "pdf" | "pietra" | "despacho";

export default function App() {
  const {
    agents,
    catalog,
    matrix,
    eventLog,
    barramento,
    pdfPipeline,
    pietraInbox,
    intakeDispatch,
    whatsappJobs,
    whatsappStatus,
    connected,
    error,
    refetch,
    apiBase,
    resolveAgent,
  } = useAgents();
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [tab, setTab] = useState<Tab>("cockpit");

  const selected = useMemo(
    () => resolveAgent(selectedId),
    [resolveAgent, selectedId],
  );

  return (
    <div className="app app--tactical app--v05">
      <header className="app__header pixel-panel pixel-border">
        <div>
          <h1>MEGATRON Tactical Agentarium</h1>
          <p className="app__subtitle">
            v1.0.0 · prompt de comando MEGATRON
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
          className={`pixel-button app__tab ${tab === "cockpit" ? "app__tab--active" : ""}`}
          onClick={() => setTab("cockpit")}
        >
          MEGATRON
        </button>
        <button
          type="button"
          className={`pixel-button app__tab ${tab === "operacional" ? "app__tab--active" : ""}`}
          onClick={() => setTab("operacional")}
        >
          Operacional
        </button>
        <button
          type="button"
          className={`pixel-button app__tab ${tab === "barramento" ? "app__tab--active" : ""}`}
          onClick={() => setTab("barramento")}
        >
          Barramento
          {barramento && barramento.count > 0 && (
            <span className="app__tab-count">{barramento.count}</span>
          )}
        </button>
        <button
          type="button"
          className={`pixel-button app__tab ${tab === "pdf" ? "app__tab--active" : ""}`}
          onClick={() => setTab("pdf")}
        >
          PDF Pipeline
          {pdfPipeline && pdfPipeline.eventCount > 0 && (
            <span className="app__tab-count">{pdfPipeline.eventCount}</span>
          )}
        </button>
        <button
          type="button"
          className={`pixel-button app__tab ${tab === "despacho" ? "app__tab--active" : ""}`}
          onClick={() => setTab("despacho")}
        >
          Aguardando Fabio
          {intakeDispatch && intakeDispatch.pending.length > 0 && (
            <span className="app__tab-count">{intakeDispatch.pending.length}</span>
          )}
        </button>
        <button
          type="button"
          className={`pixel-button app__tab ${tab === "pietra" ? "app__tab--active" : ""}`}
          onClick={() => setTab("pietra")}
        >
          PietraOS Inbox
          {pietraInbox && pietraInbox.cards.length > 0 && (
            <span className="app__tab-count">{pietraInbox.cards.length}</span>
          )}
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

      {tab === "cockpit" ? (
        <div className="app__layout app__layout--cockpit">
          <MegatronChatPanel apiBase={apiBase} onIntakeCreated={refetch} />
          <details className="megatron-cockpit__details">
            <summary className="pixel-label">Integracoes reais (status)</summary>
            <MegatronCockpitPanel
              agents={agents}
              catalog={catalog}
              barramento={barramento}
              pdfPipeline={pdfPipeline}
              pietraInbox={pietraInbox}
              intakeDispatch={intakeDispatch}
              whatsappStatus={whatsappStatus}
              connected={connected}
              onNavigate={(t) => setTab(t as Tab)}
              onRefresh={refetch}
            />
          </details>
        </div>
      ) : tab === "operacional" ? (
        <div className="app__layout app__layout--v05">
          <div className="app__main-col">
            <AgentMap
              agents={agents}
              selectedId={selectedId}
              onSelect={setSelectedId}
            />
            <div className="app__bottom-panels">
              <WhatsAppOperationsPanel status={whatsappStatus} jobs={whatsappJobs} />
              <EventLog entries={eventLog} />
              <WhatsAppIntakePanel
                jobs={whatsappJobs}
                onSelectJob={(id) => {
                  const job = whatsappJobs.find((j) => j.jobId === id);
                  if (job) setSelectedId(job.agentId);
                }}
              />
            </div>
          </div>
          <div className="app__side">
            <AgentList
              agents={agents}
              selectedId={selectedId}
              onSelect={setSelectedId}
            />
            <AgentInspector agent={selected} />
          </div>
        </div>
      ) : tab === "barramento" ? (
        <div className="app__layout app__layout--barramento">
          <BarramentoPanel barramento={barramento} connected={connected} />
        </div>
      ) : tab === "pdf" ? (
        <div className="app__layout app__layout--pdf">
          <PdfPipelinePanel pipeline={pdfPipeline} connected={connected} />
        </div>
      ) : tab === "despacho" ? (
        <div className="app__layout app__layout--despacho">
          <IntakeDispatchPanel
            dispatch={intakeDispatch}
            connected={connected}
            apiBase={apiBase}
            onRefresh={refetch}
          />
        </div>
      ) : tab === "pietra" ? (
        <div className="app__layout app__layout--pietra">
          <PietraInboxPanel
            inbox={pietraInbox}
            connected={connected}
            apiBase={apiBase}
            onRefresh={refetch}
          />
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
        v1.0.0 · cockpit · despacho {intakeDispatch?.pending.length ?? 0} · pietra {pietraInbox?.cards.length ?? 0} ·
        pdf {pdfPipeline?.eventCount ?? 0} · barramento {barramento?.count ?? 0}
      </footer>
    </div>
  );
}
