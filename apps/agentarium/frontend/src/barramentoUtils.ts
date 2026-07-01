import type { BarramentoMessage } from "./types";

export const BARRAMENTO_AGENTS = [
  "todos",
  "claude",
  "codex",
  "cursor",
  "megatron",
  "lead",
] as const;

export type BarramentoAgentFilter = (typeof BARRAMENTO_AGENTS)[number] | "all";

export const AGENT_AVATAR: Record<
  string,
  { label: string; bg: string; color: string; name: string }
> = {
  claude: { label: "C", bg: "#6d28d9", color: "#f5f3ff", name: "Claude" },
  codex: { label: "X", bg: "#0f172a", color: "#4ade80", name: "Codex" },
  cursor: { label: "▣", bg: "#1e3a5f", color: "#38bdf8", name: "Cursor" },
  megatron: { label: "M", bg: "#450a0a", color: "#fca5a5", name: "MEGATRON" },
  lead: { label: "L", bg: "#4338ca", color: "#e0e7ff", name: "Lead" },
  todos: { label: "∞", bg: "#334155", color: "#cbd5e1", name: "Todos" },
};

export const TIPO_LABELS: Record<string, string> = {
  ordem: "ORDEM",
  handoff: "HANDOFF",
  ack: "ACK",
  aviso: "AVISO",
  bloqueio: "BLOQUEIO",
};

export function agentAvatar(id: string) {
  const key = id.toLowerCase();
  return (
    AGENT_AVATAR[key] ?? {
      label: key.slice(0, 1).toUpperCase(),
      bg: "#475569",
      color: "#f8fafc",
      name: id,
    }
  );
}

export function tipoBadgeClass(tipo: string): string {
  const t = tipo.toLowerCase();
  if (t === "ordem") return "barramento-badge--ordem";
  if (t === "handoff") return "barramento-badge--handoff";
  if (t === "ack") return "barramento-badge--ack";
  if (t === "bloqueio") return "barramento-badge--bloqueio";
  return "barramento-badge--aviso";
}

export function formatBarramentoTime(ts: string): string {
  const normalized = ts.includes("T") ? ts : ts.replace(" ", "T");
  const withZone = /Z|[+-]\d{2}:\d{2}$/.test(normalized) ? normalized : `${normalized}:00`;
  const d = new Date(withZone);
  if (Number.isNaN(d.getTime())) return ts;
  return d.toLocaleString("pt-BR", {
    day: "2-digit",
    month: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  });
}

export function matchesBarramentoFilter(
  entry: BarramentoMessage,
  filter: BarramentoAgentFilter,
): boolean {
  if (filter === "all") return true;
  const f = filter.toLowerCase();
  return entry.de.toLowerCase() === f || entry.para.toLowerCase() === f;
}

export function uniqueBarramentoActors(entries: BarramentoMessage[]): string[] {
  const set = new Set<string>();
  for (const e of entries) {
    set.add(e.de.toLowerCase());
    set.add(e.para.toLowerCase());
  }
  return [...set].sort((a, b) => a.localeCompare(b));
}
