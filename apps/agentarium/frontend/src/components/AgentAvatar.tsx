import type { Agent } from "../types";
import { ZONE_LAYOUT, STATE_LABELS } from "../types";
import { PolicyBadges } from "./PolicyBadges";
import { PixelAgentAvatar } from "./pixel/PixelAgentAvatar";

type Props = {
  agent: Agent;
  indexInZone: number;
  selected: boolean;
  onSelect: (id: string) => void;
};

export function AgentAvatar({ agent, indexInZone, selected, onSelect }: Props) {
  const layout = ZONE_LAYOUT[agent.zone] ?? ZONE_LAYOUT.Erro;
  const offsetX = (indexInZone % 2) * 10;
  const offsetY = Math.floor(indexInZone / 2) * 14;
  const left = layout.x + layout.w / 2 - 6 + offsetX;
  const top = layout.y + layout.h / 2 - 10 + offsetY;

  return (
    <button
      type="button"
      className={`pixel-avatar-btn avatar avatar--${agent.state} avatar--risk-${agent.policy.riskLevel} ${selected ? "avatar--selected" : ""}`}
      style={{ left: `${left}%`, top: `${top}%` }}
      title={`${agent.name} — ${agent.task}`}
      onClick={() => onSelect(agent.id)}
    >
      <PixelAgentAvatar agent={agent} />
      <p className="avatar__task pixel-label">{agent.task}</p>
      <PolicyBadges policy={agent.policy} compact />
      <span className="sr-only">
        {STATE_LABELS[agent.state]} — {agent.zone}
      </span>
    </button>
  );
}
