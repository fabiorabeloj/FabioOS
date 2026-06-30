import type { AgentRuntimeState, RiskLevel } from "../../types";

type Props = {
  state: AgentRuntimeState;
  riskLevel: RiskLevel;
};

export function PixelStatusEffect({ state, riskLevel }: Props) {
  if (riskLevel === "danger") {
    return (
      <div className="pixel-status-effect pixel-status-effect--danger" aria-hidden>
        <span className="pixel-status-effect__mark pixel-status-effect__mark--x">X</span>
      </div>
    );
  }

  switch (state) {
    case "thinking":
      return (
        <div className="pixel-status-effect pixel-status-effect--thinking" aria-hidden>
          <span className="pixel-status-effect__dot" />
          <span className="pixel-status-effect__dot" />
          <span className="pixel-status-effect__dot" />
        </div>
      );
    case "executing":
      return (
        <div className="pixel-status-effect pixel-status-effect--executing" aria-hidden>
          <div className="pixel-status-effect__bits">
            <span>1</span>
            <span>0</span>
            <span>1</span>
          </div>
          <div className="pixel-status-effect__scan" />
        </div>
      );
    case "waiting_approval":
      return (
        <div className="pixel-status-effect pixel-status-effect--approval" aria-hidden>
          <span className="pixel-status-effect__mark">!</span>
        </div>
      );
    case "done":
      return (
        <div className="pixel-status-effect pixel-status-effect--done" aria-hidden>
          <span className="pixel-status-effect__mark pixel-status-effect__mark--check">v</span>
        </div>
      );
    case "error":
      return (
        <div className="pixel-status-effect pixel-status-effect--error" aria-hidden>
          <span className="pixel-status-effect__mark pixel-status-effect__mark--x">X</span>
        </div>
      );
    default:
      return null;
  }
}
