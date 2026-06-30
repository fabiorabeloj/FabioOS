import type { AgentPolicy } from "../types";
import { hasExec, hasWrite, RISK_LABELS } from "../types";

type Props = {
  policy: AgentPolicy;
  compact?: boolean;
};

export function PolicyBadges({ policy, compact }: Props) {
  const exec = hasExec(policy);
  const fs = policy.workspaceAccess.toUpperCase();
  const sbx = policy.sandboxMode.toUpperCase();
  const elev = policy.elevated.toUpperCase();
  const risk = RISK_LABELS[policy.riskLevel];

  return (
    <div className={`pixel-badges ${compact ? "pixel-badges--compact" : ""}`}>
      <span className="pixel-badge">[SBX: {sbx}]</span>
      <span className="pixel-badge">[FS: {fs}]</span>
      <span className={`pixel-badge ${exec ? "pixel-badge--warn" : ""}`}>
        [EXEC: {exec ? "YES" : "NO"}]
      </span>
      <span className={`pixel-badge ${hasWrite(policy) ? "pixel-badge--warn" : ""}`}>
        [WRITE: {hasWrite(policy) ? "YES" : "NO"}]
      </span>
      <span className="pixel-badge">[ELEV: {elev}]</span>
      <span className={`pixel-badge pixel-badge--${policy.riskLevel}`}>
        [RISK: {risk}]
      </span>
    </div>
  );
}
