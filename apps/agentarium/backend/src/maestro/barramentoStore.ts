import type { MaestroBarramentoEntry } from "./types.js";

export type BarramentoSnapshot = {
  entries: MaestroBarramentoEntry[];
  generatedAt: string | null;
  count: number;
};

class BarramentoStore {
  private entries: MaestroBarramentoEntry[] = [];
  private generatedAt: string | null = null;

  replace(entries: MaestroBarramentoEntry[], generatedAt: string): void {
    this.entries = [...entries];
    this.generatedAt = generatedAt;
  }

  snapshot(): BarramentoSnapshot {
    return {
      entries: this.entries,
      generatedAt: this.generatedAt,
      count: this.entries.length,
    };
  }
}

export const barramentoStore = new BarramentoStore();
