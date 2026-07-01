import type { WhatsAppJobExtended, WhatsAppOperationsStatus } from "../whatsappTypes";

type Props = {
  status: WhatsAppOperationsStatus | null;
  jobs: WhatsAppJobExtended[];
};

function ConnBadge({ connected, label }: { connected: boolean; label: string }) {
  return (
    <span className={`wa-ops__conn wa-ops__conn--${connected ? "on" : "off"}`}>
      {label}: {connected ? "CONNECTED" : "DISCONNECTED"}
    </span>
  );
}

export function WhatsAppOperationsPanel({ status, jobs }: Props) {
  if (!status) {
    return (
      <section className="wa-ops panel-tactical pixel-panel pixel-border">
        <h2>WhatsApp Operations</h2>
        <p className="muted">Carregando status...</p>
      </section>
    );
  }

  const personalJobs = jobs.filter((j) => j.channel === "personal").slice(0, 5);
  const schoolJobs = jobs.filter((j) => j.channel === "school").slice(0, 5);
  const pending = jobs.filter(
    (j) => j.approvalState === "draft_only" || j.approvalState === "awaiting_human",
  );

  return (
    <section className="wa-ops panel-tactical pixel-panel pixel-border">
      <h2>WhatsApp Operations</h2>
      <div className="wa-ops__global">
        <span className="pixel-badge">autoSend: {status.autoSend ? "ON" : "OFF"}</span>
        <span className="pixel-badge">groups: {status.groupsEnabled ? "ON" : "OFF"}</span>
        <span className="pixel-badge pixel-badge--risk pixel-badge--warning">
          pending Fabio: {status.pendingFabio}
        </span>
      </div>

      <div className="wa-ops__channels">
        <div className="wa-ops__channel">
          <h3>Personal — Hermes</h3>
          <ConnBadge connected={status.personal.connected} label="PERSONAL WPP" />
          <dl className="wa-ops__dl">
            <dt>Enabled</dt><dd>{status.personal.enabled ? "sim" : "nao"}</dd>
            <dt>Mode</dt><dd>{status.personal.mode}</dd>
            <dt>Commands</dt><dd>/status /help /jobs ...</dd>
            <dt>Last job</dt><dd className="mono">{status.personal.lastJobId ?? "—"}</dd>
          </dl>
          <ul className="wa-ops__jobs">
            {personalJobs.map((j) => (
              <li key={j.jobId}>
                <span className="mono">{j.jobId.slice(-8)}</span> · {j.textPreview.slice(0, 40)}
                · <strong>{j.approvalState}</strong>
                {j.isCommand && " · CMD"}
              </li>
            ))}
          </ul>
        </div>

        <div className="wa-ops__channel">
          <h3>School — Pietra</h3>
          <ConnBadge connected={status.school.connected} label="SCHOOL WPP" />
          <dl className="wa-ops__dl">
            <dt>Enabled</dt><dd>{status.school.enabled ? "sim" : "nao (celular escola pendente)"}</dd>
            <dt>Mode</dt><dd>{status.school.mode}</dd>
            <dt>Auto menu</dt><dd>{status.school.autoMenu ? "sim" : "nao"}</dd>
            <dt>Last job</dt><dd className="mono">{status.school.lastJobId ?? "—"}</dd>
          </dl>
          <ul className="wa-ops__jobs">
            {schoolJobs.length === 0 && (
              <li className="muted">Nenhum job escolar ainda.</li>
            )}
            {schoolJobs.map((j) => (
              <li key={j.jobId}>
                <span className="mono">{j.jobId.slice(-8)}</span> · {j.category} · {j.approvalState}
              </li>
            ))}
          </ul>
        </div>
      </div>

      {pending.length > 0 && (
        <div className="wa-ops__pending">
          <h3>Awaiting Fabio</h3>
          <ul>
            {pending.slice(0, 8).map((j) => (
              <li key={j.jobId}>
                [{j.channel}] {j.contactName} — {j.approvalState} — {j.jobId}
              </li>
            ))}
          </ul>
        </div>
      )}
    </section>
  );
}
