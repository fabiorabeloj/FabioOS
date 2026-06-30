import type { AgentRuntimeState, RiskLevel } from "../types";

export type PixelColorKey =
  | "."
  | "K"
  | "W"
  | "C"
  | "B"
  | "G"
  | "Y"
  | "R"
  | "P"
  | "O"
  | "S"
  | "D"
  | "M"
  | "A";

export type PixelFrame = string[];

export type PixelSpriteFrames = {
  idle: PixelFrame[];
  walk1: PixelFrame[];
  walk2: PixelFrame[];
  thinking: PixelFrame[];
  executing: PixelFrame[];
  approval: PixelFrame[];
  done: PixelFrame[];
  error: PixelFrame[];
  danger: PixelFrame[];
};

export type PixelSpriteDefinition = {
  id: string;
  name: string;
  scale: number;
  palette: Record<PixelColorKey, string>;
  frames: PixelSpriteFrames;
};

export type PixelAnimKey =
  | "idle"
  | "walk1"
  | "walk2"
  | "thinking"
  | "executing"
  | "approval"
  | "done"
  | "error"
  | "danger";

export type PixelVisualState = AgentRuntimeState | "walking" | "danger";

export function resolvePixelAnim(
  state: AgentRuntimeState,
  riskLevel: RiskLevel,
  isWalking: boolean,
): PixelAnimKey {
  if (riskLevel === "danger") return "danger";
  if (isWalking) return "walk1";
  switch (state) {
    case "idle":
      return "idle";
    case "thinking":
      return "thinking";
    case "executing":
      return "executing";
    case "waiting_approval":
      return "approval";
    case "done":
      return "done";
    case "error":
      return "error";
    default:
      return "idle";
  }
}

export function resolveAnimClass(
  anim: PixelAnimKey,
  isWalking: boolean,
): string {
  if (isWalking) return "pixel-anim--walk";
  const map: Record<PixelAnimKey, string> = {
    idle: "pixel-anim--idle",
    walk1: "pixel-anim--walk",
    walk2: "pixel-anim--walk",
    thinking: "pixel-anim--thinking",
    executing: "pixel-anim--executing",
    approval: "pixel-anim--approval",
    done: "pixel-anim--done",
    error: "pixel-anim--error",
    danger: "pixel-anim--danger",
  };
  return map[anim];
}
