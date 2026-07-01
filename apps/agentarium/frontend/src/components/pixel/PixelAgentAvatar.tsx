import type { Agent } from "../../types";
import { RISK_LABELS, STATE_LABELS, AGENT_SHORT_NAMES, originBadge } from "../../types";
import { getAgentSprite } from "../../pixel/agentSprites";
import {
  resolveAnimClass,
  resolvePixelAnim,
  type PixelAnimKey,
} from "../../pixel/pixelTypes";
import { useWalkPhase, useWalking } from "../../hooks/useWalking";
import { PixelSprite, useFrameCycle } from "./PixelSprite";
import { PixelShadow } from "./PixelShadow";
import { PixelStatusEffect } from "./PixelStatusEffect";

type Props = {
  agent: Agent;
  className?: string;
};

const FRAME_INTERVAL: Record<PixelAnimKey, number> = {
  idle: 1200,
  walk1: 220,
  walk2: 220,
  thinking: 600,
  executing: 400,
  approval: 700,
  done: 900,
  error: 500,
  danger: 450,
};

export function PixelAgentAvatar({ agent, className = "" }: Props) {
  const sprite = getAgentSprite(agent.id);
  const isWalking = useWalking(agent.zone);
  const walkPhase = useWalkPhase(isWalking);

  const animKey = resolvePixelAnim(agent.state, agent.policy.riskLevel, isWalking);
  const animClass = resolveAnimClass(animKey, isWalking);

  let frameSet = sprite.frames[animKey];
  if (isWalking) {
    frameSet =
      walkPhase === 0 ? sprite.frames.walk1 : sprite.frames.walk2;
  }

  const frame = useFrameCycle(
    frameSet,
    FRAME_INTERVAL[animKey],
    frameSet.length > 1 || isWalking,
  );

  const stateShort = STATE_LABELS[agent.state]
    .slice(0, 4)
    .toUpperCase()
    .replace(/\s/g, "");

  const shortName = AGENT_SHORT_NAMES[agent.id] ?? agent.name.slice(0, 6).toUpperCase();
  const origin = originBadge(agent);

  return (
    <div className={`pixel-avatar ${animClass} ${className}`.trim()}>
      <PixelStatusEffect state={agent.state} riskLevel={agent.policy.riskLevel} />
      {isWalking && agent.lastFromZone && agent.lastToZone && (
        <div className="pixel-avatar__route pixel-label" title={agent.task}>
          {agent.lastFromZone.slice(0, 4)}→{agent.lastToZone.slice(0, 4)}
        </div>
      )}
      <div className="pixel-avatar__sprite-wrap">
        <PixelSprite
          frame={frame}
          palette={sprite.palette}
          scale={sprite.scale}
        />
      </div>
      <PixelShadow width={sprite.scale * 10} />
      <div className="pixel-avatar__label pixel-label">{shortName}</div>
      <div className="pixel-avatar__badges">
        <span className={`pixel-badge pixel-badge--origin pixel-badge--origin-${origin.toLowerCase()}`}>
          {origin}
        </span>
        <span className={`pixel-badge pixel-badge--state pixel-badge--${agent.state}`}>
          {stateShort}
        </span>
        <span
          className={`pixel-badge pixel-badge--risk pixel-badge--${agent.policy.riskLevel}`}
        >
          {RISK_LABELS[agent.policy.riskLevel]}
        </span>
      </div>
    </div>
  );
}
