import type { WhatsAppJob } from "../types";

type Props = {
  jobs: WhatsAppJob[];
  onSelectJob?: (jobId: string) => void;
};

export function WhatsAppIntakePanel({ jobs, onSelectJob }: Props) {
  return (
    <section className="wa-intake panel-tactical pixel-panel pixel-border">
      <h2 className="wa-intake__title">Personal WhatsApp Intake</h2>
      <p className="wa-intake__hint muted">
        Modo draft_only — nenhum envio automatico. Telefones mascarados.
      </p>
      <ul className="wa-intake__list">
        {jobs.length === 0 && (
          <li className="wa-intake__empty muted">Nenhuma mensagem registrada.</li>
        )}
        {jobs.slice(0, 20).map((j) => (
          <li key={j.jobId} className="wa-intake__item">
            <button
              type="button"
              className="wa-intake__row"
              onClick={() => onSelectJob?.(j.jobId)}
            >
              <div className="wa-intake__head">
                <strong>{j.contactName}</strong>
                <span className="mono">{j.fromMasked}</span>
              </div>
              <div className="wa-intake__meta">
                <span className="pixel-badge">{j.category}</span>
                <span className="pixel-badge pixel-badge--state">{j.urgency}</span>
                <span className="pixel-badge pixel-badge--risk pixel-badge--safe">
                  {j.approvalState}
                </span>
              </div>
              <div className="wa-intake__agents">
                Agente: <strong>{j.agentId}</strong> · job:{" "}
                <span className="mono">{j.jobId}</span>
              </div>
              <p className="wa-intake__preview">{j.textPreview}</p>
              {j.autoSendBlocked && (
                <span className="wa-intake__blocked pixel-badge pixel-badge--risk pixel-badge--warning">
                  AUTO-SEND BLOCKED
                </span>
              )}
            </button>
          </li>
        ))}
      </ul>
    </section>
  );
}
