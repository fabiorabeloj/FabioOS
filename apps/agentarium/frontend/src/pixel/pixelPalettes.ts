import type { PixelColorKey } from "./pixelTypes";

export const pixelPalette: Record<PixelColorKey, string> = {
  ".": "transparent",
  K: "#020617",
  W: "#e5e7eb",
  C: "#22d3ee",
  B: "#3b82f6",
  G: "#22c55e",
  Y: "#facc15",
  R: "#ef4444",
  P: "#a855f7",
  O: "#f97316",
  S: "#94a3b8",
  D: "#111827",
  M: "#92400e",
  A: "#ca8a04",
};

export function mergePalette(
  overrides: Partial<Record<PixelColorKey, string>>,
): Record<PixelColorKey, string> {
  return { ...pixelPalette, ...overrides };
}
