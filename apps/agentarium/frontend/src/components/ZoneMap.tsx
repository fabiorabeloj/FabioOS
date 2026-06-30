import type { CSSProperties } from "react";
import type { Agent, Zone } from "../types";
import { ZONES, ZONE_LAYOUT } from "../types";

const ZONE_CLASS: Record<Zone, string> = {
  WhatsApp: "zone--whatsapp",
  Inbox: "zone--inbox",
  Classificação: "zone--classificacao",
  Obsidian: "zone--obsidian",
  GitHub: "zone--github",
  n8n: "zone--n8n",
  RAG: "zone--rag",
  "Aprovação Humana": "zone--aprovacao",
  Concluído: "zone--concluido",
  Erro: "zone--erro",
};

type Props = {
  agents: Agent[];
};

export function ZoneMap({ agents }: Props) {
  const counts = new Map<Zone, number>();
  const active = new Map<Zone, number>();

  for (const a of agents) {
    counts.set(a.zone, (counts.get(a.zone) ?? 0) + 1);
    if (a.state !== "idle" && a.state !== "done") {
      active.set(a.zone, (active.get(a.zone) ?? 0) + 1);
    }
  }

  return (
    <div className="zone-map zone-map--pixel" aria-label="Mapa tatico de zonas">
      {ZONES.map((zone) => {
        const z = ZONE_LAYOUT[zone];
        const count = counts.get(zone) ?? 0;
        const busy = active.get(zone) ?? 0;
        return (
          <div
            key={zone}
            className={`zone pixel-border zone-tile ${ZONE_CLASS[zone]}`}
            style={{
              left: `${z.x}%`,
              top: `${z.y}%`,
              width: `${z.w}%`,
              height: `${z.h}%`,
              "--zone-accent": z.color,
            } as CSSProperties}
          >
            <span className="zone__label pixel-label">{zone}</span>
            <span className="zone__meta">
              <span className="zone__count pixel-badge">{count} ops</span>
              {busy > 0 && (
                <span className="zone__active pixel-badge pixel-badge--state pixel-badge--executing">
                  {busy} live
                </span>
              )}
            </span>
          </div>
        );
      })}
    </div>
  );
}
