import type { Agent } from "../types";
import { STATE_LABELS, RISK_LABELS } from "../types";
import { PolicyBadges } from "./PolicyBadges";

type Props = {
  agent: Agent | null;
};

export function AgentInspector({ agent }: Props) {
  if (!agent) {
    return (
      <aside className="agent-inspector panel-tactical">
        <h2>Agent Inspector</h2>
        <p className="muted">Clique em um agente no mapa ou na matriz.</p>
      </aside>
    );
  }

  const p = agent.policy;

  return (
    <aside className="agent-inspector panel-tactical">
      <h2>Agent Inspector</h2>
      <PolicyBadges policy={p} />

      <dl className="inspector-dl">
        <dt>Name</dt>
        <dd>{agent.name}</dd>
        <dt>Role</dt>
        <dd>{agent.role}</dd>
        <dt>State</dt>
        <dd>{STATE_LABELS[agent.state]}</dd>
        <dt>Task</dt>
        <dd>{agent.task}</dd>
        <dt>Zone</dt>
        <dd>{agent.zone}</dd>
        <dt>UpdatedAt</dt>
        <dd>{new Date(agent.updatedAt).toLocaleString("pt-BR")}</dd>
      </dl>

      <h3 className="inspector-sub">POLICY</h3>
      <dl className="inspector-dl">
        <dt>Sandbox mode</dt>
        <dd>{p.sandboxMode}</dd>
        <dt>Sandbox scope</dt>
        <dd>{p.sandboxScope}</dd>
        <dt>Workspace root</dt>
        <dd className="mono">{p.workspaceRoot}</dd>
        <dt>Workspace access</dt>
        <dd>{p.workspaceAccess}</dd>
        <dt>Docker sandbox</dt>
        <dd>{p.dockerSandbox}</dd>
        <dt>Browser sandbox</dt>
        <dd>{p.browserSandbox}</dd>
        <dt>Prune policy</dt>
        <dd>{p.prunePolicy}</dd>
        <dt>Tool profile</dt>
        <dd>{p.toolProfile ?? "—"}</dd>
        <dt>Provider policy</dt>
        <dd>{p.providerPolicy ?? "—"}</dd>
        <dt>Sandbox tool policy</dt>
        <dd>{p.sandboxToolPolicy ?? "—"}</dd>
        <dt>Subagent tool policy</dt>
        <dd>{p.subagentToolPolicy ?? "—"}</dd>
        <dt>Allowed tools</dt>
        <dd className="mono">{p.allowedTools.join(", ")}</dd>
        <dt>Denied tools</dt>
        <dd className="mono">{p.deniedTools.join(", ")}</dd>
        <dt>Elevated</dt>
        <dd>{p.elevated}</dd>
        <dt>AgentDir</dt>
        <dd className="mono">{p.agentDir}</dd>
        <dt>Auth profile</dt>
        <dd>{p.authProfile}</dd>
        <dt>Credential risk</dt>
        <dd>
          <span className={`risk-pill risk-pill--${p.riskLevel}`}>
            {RISK_LABELS[p.riskLevel]}
          </span>
        </dd>
      </dl>

      <h3 className="inspector-sub">RISK NOTES</h3>
      {p.riskNotes.length === 0 ? (
        <p className="muted">Nenhum alerta ativo.</p>
      ) : (
        <ul className="risk-notes">
          {p.riskNotes.map((n) => (
            <li key={n}>{n}</li>
          ))}
        </ul>
      )}
    </aside>
  );
}
