import type { WhatsAppJob } from "./whatsapp/types.js";
import { maskPhone } from "./whatsapp/config.js";

type Listener = (jobs: WhatsAppJob[]) => void;

class WhatsAppJobStore {
  private jobs = new Map<string, WhatsAppJob>();
  private listeners = new Set<Listener>();

  add(job: WhatsAppJob): WhatsAppJob {
    this.jobs.set(job.jobId, job);
    this.notify();
    return job;
  }

  update(jobId: string, patch: Partial<WhatsAppJob>): WhatsAppJob | undefined {
    const current = this.jobs.get(jobId);
    if (!current) return undefined;
    const next = { ...current, ...patch, updatedAt: new Date().toISOString() };
    this.jobs.set(jobId, next);
    this.notify();
    return next;
  }

  list(limit = 30): WhatsAppJob[] {
    return [...this.jobs.values()]
      .sort((a, b) => b.createdAt.localeCompare(a.createdAt))
      .slice(0, limit);
  }

  listByChannel(channel: WhatsAppJob["channel"], limit = 30): WhatsAppJob[] {
    return this.list(limit * 2).filter((j) => j.channel === channel).slice(0, limit);
  }

  get(jobId: string): WhatsAppJob | undefined {
    return this.jobs.get(jobId);
  }

  subscribe(fn: Listener): () => void {
    this.listeners.add(fn);
    return () => this.listeners.delete(fn);
  }

  private notify(): void {
    const list = this.list();
    for (const fn of this.listeners) fn(list);
  }
}

export const whatsappJobs = new WhatsAppJobStore();

export function makeJobId(): string {
  return `wa-job-${Date.now()}-${Math.random().toString(36).slice(2, 6)}`;
}

export function textPreview(text: string, max = 48): string {
  const t = text.trim();
  return t.length > max ? `${t.slice(0, max)}…` : t;
}

export { maskPhone };
