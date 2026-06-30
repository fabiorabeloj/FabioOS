import type { Agent } from "../types";
import { ZoneMap } from "./ZoneMap";
import { AgentAvatar } from "./AgentAvatar";

type Props = {
  agents: Agent[];
  selectedId: string | null;
  onSelect: (id: string) => void;
};

export function AgentMap({ agents, selectedId, onSelect }: Props) {
  const byZone = new Map<string, number>();

  return (
    <section className="agent-map panel-tactical pixel-panel pixel-map">
      <div className="pixel-scanlines" aria-hidden />
      <ZoneMap agents={agents} />
      <div className="agent-map__agents">
        {agents.map((agent) => {
          const idx = byZone.get(agent.zone) ?? 0;
          byZone.set(agent.zone, idx + 1);
          return (
            <AgentAvatar
              key={agent.id}
              agent={agent}
              indexInZone={idx}
              selected={selectedId === agent.id}
              onSelect={onSelect}
            />
          );
        })}
      </div>
    </section>
  );
}
