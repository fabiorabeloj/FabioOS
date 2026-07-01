import type { Agent } from "../types";
import { LAYER_LABELS, STATE_LABELS, RISK_LABELS, STATUS_LABELS, getVisualClass } from "../types";
import { PolicyBadges } from "./PolicyBadges";

type Props = {
  agent: Agent | null;
};

export function AgentInspector({ agent }: Props) {
  if (!agent) {
    return (
      <aside className="agent-inspector panel-tactical pixel-panel pixel-border">
        <h2>Agent Inspector</h2>
        <p className="muted">Clique em um agente no mapa ou na matriz.</p>
      </aside>
    );
  }

  const p = agent.policy;
  const visualClass = getVisualClass(agent.id);

  return (
    <aside className="agent-inspector panel-tactical pixel-panel pixel-border">
      <h2>Agent Inspector</h2>
      <PolicyBadges policy={p} />

      {visualClass && (
        <>
          <h3 className="inspector-sub">AGENT CLASS</h3>
          <dl className="inspector-dl inspector-dl--class">
            <dt>Visual class</dt>
            <dd>{visualClass.visualClass}</dd>
            <dt>Operational role</dt>
            <dd>{visualClass.operationalRole}</dd>
            <dt>Primary lane</dt>
            <dd>{visualClass.primaryLane}</dd>
            <dt>Home zone</dt>
            <dd>{visualClass.homeZone}</dd>
            <dt>Signature item</dt>
            <dd>{visualClass.signatureItem}</dd>
            <dt>Color identity</dt>
            <dd>{visualClass.colorIdentity}</dd>
            <dt>Approval requirement</dt>
            <dd>{visualClass.approvalRequirement}</dd>
          </dl>
        </>
      )}

      <dl className="inspector-dl">
        <dt>Name</dt>
        <dd>{agent.name}</dd>
        <dt>Status</dt>
        <dd>
          <span className={`catalog-badge catalog-badge--${agent.status}`}>
            {STATUS_LABELS[agent.status]}
          </span>
        </dd>
        <dt>Layer</dt>
        <dd>{LAYER_LABELS[agent.layer]}</dd>
        <dt>Essential</dt>
        <dd>{agent.essential ? "Sim" : "Opcional"}</dd>
        <dt>Role</dt>
        <dd>{agent.role}</dd>
        <dt>Catalog zone</dt>
        <dd>{agent.catalogZone}</dd>
        <dt>State</dt>
        <dd>{STATE_LABELS[agent.state]}</dd>
        <dt>Task</dt>
        <dd>{agent.task}</dd>
        <dt>Runtime zone</dt>
        <dd>{agent.zone}</dd>
        {agent.homeZone && (
          <>
            <dt>Home zone</dt>
            <dd>{agent.homeZone}</dd>
          </>
        )}
        {agent.lastJobId && (
          <>
            <dt>Last job</dt>
            <dd className="mono">{agent.lastJobId}</dd>
          </>
        )}
        {agent.lastFromZone && agent.lastToZone && (
          <>
            <dt>Last route</dt>
            <dd>{agent.lastFromZone} → {agent.lastToZone}</dd>
          </>
        )}
        <dt>UpdatedAt</dt>
        <dd>{new Date(agent.updatedAt).toLocaleString("pt-BR")}</dd>
      </dl>

      <h3 className="inspector-sub">RESPONSIBILITIES</h3>
      <ul className="inspector-list">
        {agent.responsibilities.map((r) => (
          <li key={r}>{r}</li>
        ))}
      </ul>

      <h3 className="inspector-sub">INPUTS / OUTPUTS</h3>
      <dl className="inspector-dl">
        <dt>Inputs</dt>
        <dd>{agent.inputs.join(", ")}</dd>
        <dt>Outputs</dt>
        <dd>{agent.outputs.join(", ")}</dd>
      </dl>

      <h3 className="inspector-sub">REQUIRES APPROVAL FOR</h3>
      {agent.requiresApprovalFor.length === 0 ? (
        <p className="muted">Nenhuma aprovacao obrigatoria definida.</p>
      ) : (
        <ul className="inspector-list">
          {agent.requiresApprovalFor.map((r) => (
            <li key={r}>{r}</li>
          ))}
        </ul>
      )}

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
