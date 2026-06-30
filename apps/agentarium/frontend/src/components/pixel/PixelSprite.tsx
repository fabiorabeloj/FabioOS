import { useEffect, useState } from "react";
import type { PixelColorKey, PixelFrame } from "../../pixel/pixelTypes";

type Props = {
  frame: PixelFrame;
  palette: Record<PixelColorKey, string>;
  scale?: number;
  className?: string;
};

export function PixelSprite({ frame, palette, scale = 3, className = "" }: Props) {
  const cols = Math.max(...frame.map((row) => row.length), 1);

  return (
    <div
      className={`pixel-sprite ${className}`.trim()}
      style={{
        gridTemplateColumns: `repeat(${cols}, ${scale}px)`,
        gridTemplateRows: `repeat(${frame.length}, ${scale}px)`,
      }}
      aria-hidden
    >
      {frame.flatMap((row, y) =>
        row.split("").map((key, x) => {
          const color = palette[key as PixelColorKey] ?? "transparent";
          const transparent = key === "." || color === "transparent";
          return (
            <span
              key={`${x}-${y}`}
              className={`pixel-sprite__cell ${transparent ? "pixel-sprite__cell--empty" : ""}`}
              style={transparent ? undefined : { backgroundColor: color }}
            />
          );
        }),
      )}
    </div>
  );
}

export function useFrameCycle(
  frames: PixelFrame[],
  intervalMs: number,
  enabled = true,
): PixelFrame {
  const [index, setIndex] = useState(0);

  useEffect(() => {
    if (!enabled || frames.length <= 1) {
      setIndex(0);
      return;
    }
    const id = window.setInterval(() => {
      setIndex((i) => (i + 1) % frames.length);
    }, intervalMs);
    return () => window.clearInterval(id);
  }, [frames, intervalMs, enabled]);

  return frames[index] ?? frames[0];
}
