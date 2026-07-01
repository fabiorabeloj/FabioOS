import type {
  Agent,
  AgentCatalog,
  BarramentoSnapshot,
  IntakeDispatchSnapshot,
  PdfPipelineSnapshot,
  PietraInboxSnapshot,
} from "../types";
import type { WhatsAppOperationsStatus } from "../whatsappTypes";

type Props = {
  agents: Agent[];
  catalog: AgentCatalog | null;
  barramento: BarramentoSnapshot | null;
  pdfPipeline: PdfPipelineSnapshot | null;
  pietraInbox: PietraInboxSnapshot | null;
  intakeDispatch: IntakeDispatchSnapshot | null;
  whatsappStatus: WhatsAppOperationsStatus | null;
  connected: boolean;
  onNavigate: (tab: string) => void;
  onRefresh: () => void;
};

type Row = {
  id: string;
  label: string;
  tab: string;
  detail: string;
  ok: boolean;
};

function buildRows(props: Props): Row[] {
  const rows: Row[] = [];

  rows.push({
    id: "intake",
    label: "Intake / Mesa de despacho",
    tab: "despacho",
    detail: props.intakeDispatch
      ? props.intakeDispatch.fallbackMode
        ? "sample (fila live ausente)"
        : `${props.intakeDispatch.pending.length} aguardando Fabio · ${props.intakeDispatch.queue.fila.length} na fila`
      : "sem dados",
    ok: Boolean(props.intakeDispatch && props.intakeDispatch.queue?.fila),
  });

  rows.push({
    id: "whatsapp",
    label: "WhatsApp (Hermes)",
    tab: "operacional",
    detail: props.whatsappStatus
      ? `pessoal ${props.whatsappStatus.personal.connected ? "conectado" : "desconectado"} · escola ${props.whatsappStatus.school.connected ? "conectado" : "desconectado"}`
      : "sem dados",
    ok: Boolean(props.whatsappStatus?.personal.connected || props.whatsappStatus?.school.connected),
  });

  rows.push({
    id: "pietra",
    label: "PietraOS Inbox",
    tab: "pietra",
    detail: props.pietraInbox
      ? `${props.pietraInbox.cards.length} card(s)${props.pietraInbox.fallbackMode ? " · sample" : ""}`
      : "sem dados",
    ok: Boolean(props.pietraInbox),
  });

  rows.push({
    id: "barramento",
    label: "Barramento multiagente",
    tab: "barramento",
    detail: props.barramento ? `${props.barramento.count} mensagem(ns) aberta(s)` : "sem dados",
    ok: Boolean(props.barramento),
  });

  rows.push({
    id: "pdf",
    label: "PDF Pipeline",
    tab: "pdf",
    detail: props.pdfPipeline ? `${props.pdfPipeline.eventCount} evento(s)` : "sem dados",
    ok: Boolean(props.pdfPipeline),
  });

  rows.push({
    id: "agents",
    label: "Agentes (store)",
    tab: "operacional",
    detail: `${props.agents.length} ativo(s) · catalogo ${props.catalog?.counts.planned ?? 0} planejado(s)`,
    ok: props.agents.length > 0,
  });

  return rows;
}

export function MegatronCockpitPanel(props: Props) {
  const { connected, onNavigate, onRefresh } = props;
  const rows = buildRows(props);

  return (
    <section className="megatron-cockpit pixel-panel pixel-border">
      <header className="megatron-cockpit__header">
        <div>
          <h2>MEGATRON</h2>
          <p className="pixel-label megatron-cockpit__meta">
            Integracoes reais deste Agentarium · {connected ? "WebSocket" : "HTTP polling"}
          </p>
        </div>
        <button type="button" className="btn btn-tactical pixel-button" onClick={onRefresh}>
          Atualizar
        </button>
      </header>

      <p className="muted megatron-cockpit__hint">
        Cada linha abaixo corresponde a uma aba/API existente no backend. Nada aqui e inferido de Docker ou URLs
        externas.
      </p>

      <table className="megatron-cockpit__table">
        <thead>
          <tr>
            <th>Integracao</th>
            <th>Estado</th>
            <th>Detalhe</th>
            <th />
          </tr>
        </thead>
        <tbody>
          {rows.map((row) => (
            <tr key={row.id}>
              <td>{row.label}</td>
              <td>
                <span className={`megatron-svc__state ${row.ok ? "megatron-svc--ok-text" : ""}`}>
                  {row.ok ? "com dados" : "vazio / offline"}
                </span>
              </td>
              <td className="muted">{row.detail}</td>
              <td>
                <button type="button" className="btn pixel-button" onClick={() => onNavigate(row.tab)}>
                  Abrir
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {props.intakeDispatch?.fallbackMode && (
        <p className="megatron-cockpit__warn">
          Intake usa arquivo sample — fila live em{" "}
          <code>60_Sistemas/MEGATRON/v1/state/intake_queue.json</code> ausente. Rode{" "}
          <code>python intake_flow.py</code> ou use a mesa de despacho.
        </p>
      )}
    </section>
  );
}
