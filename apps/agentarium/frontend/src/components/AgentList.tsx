import type { Agent } from "../types";
import { STATE_LABELS, RISK_LABELS } from "../types";

type Props = {
  agents: Agent[];
  selectedId: string | null;
  onSelect: (id: string) => void;
};

export function AgentList({ agents, selectedId, onSelect }: Props) {
  return (
    <aside className="agent-list panel-tactical">
      <h2>Operacional</h2>
      <ul>
        {agents.map((a) => (
          <li key={a.id}>
            <button
              type="button"
              className={`agent-list__btn agent-list__btn--${a.policy.riskLevel} ${selectedId === a.id ? "agent-list__btn--selected" : ""}`}
              onClick={() => onSelect(a.id)}
            >
              <header>
                <strong>{a.name}</strong>
                <span className={`risk-pill risk-pill--${a.policy.riskLevel}`}>
                  {RISK_LABELS[a.policy.riskLevel]}
                </span>
              </header>
              <span className={`badge badge--${a.state}`}>
                {STATE_LABELS[a.state]}
              </span>
              <p className="agent-list__task">{a.task}</p>
              <footer>
                <span>{a.zone}</span>
              </footer>
            </button>
          </li>
        ))}
      </ul>
    </aside>
  );
}
