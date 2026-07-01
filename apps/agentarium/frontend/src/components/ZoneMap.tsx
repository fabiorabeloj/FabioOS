import type { CSSProperties } from "react";
import type { Agent, Zone } from "../types";
import { ZONES, ZONE_LAYOUT } from "../types";

const ZONE_CLASS: Record<Zone, string> = {
  "Personal WhatsApp": "zone--personal-wa",
  "Message Intake": "zone--intake",
  "Draft Reply": "zone--draft",
  "Awaiting Fabio": "zone--awaiting",
  Approved: "zone--approved",
  Sent: "zone--sent",
  Blocked: "zone--blocked",
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
    <div className="zone-map zone-map--pixel zone-map--v05" aria-label="Mapa tatico de zonas">
      {ZONES.map((zone) => {
        const z = ZONE_LAYOUT[zone];
        const count = counts.get(zone) ?? 0;
        const busy = active.get(zone) ?? 0;
        const shortLabel = zone.length > 14 ? zone.replace("Personal ", "P. ").slice(0, 12) : zone;
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
            <span className="zone__label pixel-label">{shortLabel}</span>
            <span className="zone__meta">
              {count > 0 && <span className="zone__count pixel-badge">{count}</span>}
              {busy > 0 && (
                <span className="zone__active pixel-badge pixel-badge--state pixel-badge--executing">
                  LIVE
                </span>
              )}
            </span>
          </div>
        );
      })}
    </div>
  );
}
