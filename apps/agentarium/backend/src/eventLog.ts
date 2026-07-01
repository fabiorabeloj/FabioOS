export type EventLogEntry = {
  id: string;
  timestamp: string;
  channel: "WHATSAPP" | "SYSTEM" | "AGENT" | "SIM";
  agentId?: string;
  jobId?: string;
  source?: string;
  fromZone?: string;
  toZone?: string;
  message: string;
  maskedPhone?: string;
  approvalState?: string;
};

type Listener = (entry: EventLogEntry) => void;

class EventLogStore {
  private entries: EventLogEntry[] = [];
  private listeners = new Set<Listener>();
  private maxEntries = 200;

  append(partial: Omit<EventLogEntry, "id" | "timestamp">): EventLogEntry {
    const entry: EventLogEntry = {
      ...partial,
      id: `evt-${Date.now()}-${Math.random().toString(36).slice(2, 7)}`,
      timestamp: new Date().toISOString(),
    };
    this.entries.unshift(entry);
    if (this.entries.length > this.maxEntries) {
      this.entries.length = this.maxEntries;
    }
    for (const fn of this.listeners) fn(entry);
    return entry;
  }

  list(limit = 50): EventLogEntry[] {
    return this.entries.slice(0, limit);
  }

  /** Substitui eventos AGENT vindos do barramento Maestro; preserva WHATSAPP/SYSTEM/SIM. */
  replaceMaestroBarramentoEvents(incoming: EventLogEntry[]): void {
    const kept = this.entries.filter((e) => e.source !== "maestro-barramento");
    this.entries = [...incoming, ...kept];
    if (this.entries.length > this.maxEntries) {
      this.entries.length = this.maxEntries;
    }
  }

  subscribe(fn: Listener): () => void {
    this.listeners.add(fn);
    return () => this.listeners.delete(fn);
  }
}

export const eventLog = new EventLogStore();
