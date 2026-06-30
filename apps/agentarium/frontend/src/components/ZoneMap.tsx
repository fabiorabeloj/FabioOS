import { ZONES, ZONE_LAYOUT } from "../types";

export function ZoneMap() {
  return (
    <div className="zone-map" aria-label="Mapa de zonas operacionais">
      {ZONES.map((zone) => {
        const z = ZONE_LAYOUT[zone];
        return (
          <div
            key={zone}
            className="zone"
            style={{
              left: `${z.x}%`,
              top: `${z.y}%`,
              width: `${z.w}%`,
              height: `${z.h}%`,
              borderColor: z.color,
            }}
          >
            <span className="zone__label" style={{ color: z.color }}>
              {zone}
            </span>
          </div>
        );
      })}
    </div>
  );
}
