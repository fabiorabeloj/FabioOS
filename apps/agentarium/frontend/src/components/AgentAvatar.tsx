import type { Agent } from "../types";
import { ZONE_LAYOUT, AGENT_EMOJI, STATE_LABELS } from "../types";
import { PolicyBadges } from "./PolicyBadges";

type Props = {
  agent: Agent;
  indexInZone: number;
  selected: boolean;
  onSelect: (id: string) => void;
};

export function AgentAvatar({ agent, indexInZone, selected, onSelect }: Props) {
  const layout = ZONE_LAYOUT[agent.zone] ?? ZONE_LAYOUT.Erro;
  const offsetX = (indexInZone % 2) * 8;
  const offsetY = Math.floor(indexInZone / 2) * 12;
  const left = layout.x + layout.w / 2 - 4 + offsetX;
  const top = layout.y + layout.h / 2 - 6 + offsetY;

  return (
    <button
      type="button"
      className={`avatar avatar--${agent.state} avatar--risk-${agent.policy.riskLevel} ${selected ? "avatar--selected" : ""}`}
      style={{ left: `${left}%`, top: `${top}%` }}
      title={`${agent.name} — ${agent.task}`}
      onClick={() => onSelect(agent.id)}
    >
      <div className="avatar__glyph">{AGENT_EMOJI[agent.id] ?? "🤖"}</div>
      <div className="avatar__body">
        <strong>{agent.name}</strong>
        <span className={`badge badge--${agent.state}`}>
          {STATE_LABELS[agent.state]}
        </span>
        <PolicyBadges policy={agent.policy} compact />
        <p className="avatar__task">{agent.task}</p>
      </div>
    </button>
  );
}
