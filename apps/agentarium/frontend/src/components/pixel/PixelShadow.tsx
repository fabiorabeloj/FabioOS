type Props = {
  width?: number;
  className?: string;
};

export function PixelShadow({ width = 36, className = "" }: Props) {
  return (
    <div
      className={`pixel-shadow ${className}`.trim()}
      style={{ width }}
      aria-hidden
    />
  );
}
