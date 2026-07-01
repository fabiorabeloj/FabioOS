import fs from "node:fs";
import path from "node:path";
import type { PdfDropEvent, PdfPipelineSnapshot, StirlingProbeStatus } from "./types.js";
import {
  resolveFabioOsRoot,
  resolveInboxPdfsDir,
  resolvePdfEventsDir,
} from "../fabioos/paths.js";

const IGNORED = new Set(["_events", "_processed", "_failed"]);
const STIRLING_URL = process.env.STIRLING_URL ?? "http://127.0.0.1:8081/";

function countPendingPdfs(dropDir: string): number {
  if (!fs.existsSync(dropDir)) return 0;
  let count = 0;
  const walk = (dir: string) => {
    for (const name of fs.readdirSync(dir, { withFileTypes: true })) {
      if (name.name.startsWith(".")) continue;
      const full = path.join(dir, name.name);
      if (name.isDirectory()) {
        if (IGNORED.has(name.name)) continue;
        walk(full);
      } else if (name.isFile() && name.name.toLowerCase().endsWith(".pdf")) {
        count += 1;
      }
    }
  };
  walk(dropDir);
  return count;
}

function readEventJson(filePath: string): PdfDropEvent | null {
  try {
    const raw = fs.readFileSync(filePath, "utf8");
    return JSON.parse(raw) as PdfDropEvent;
  } catch {
    return null;
  }
}

export function loadPdfDropEvents(): PdfDropEvent[] {
  const eventsDir = resolvePdfEventsDir();
  if (!fs.existsSync(eventsDir)) return [];

  const events: PdfDropEvent[] = [];
  for (const name of fs.readdirSync(eventsDir)) {
    if (!name.endsWith(".json")) continue;
    const parsed = readEventJson(path.join(eventsDir, name));
    if (parsed?.event_id) events.push(parsed);
  }

  return events.sort(
    (a, b) => new Date(b.detected_at).getTime() - new Date(a.detected_at).getTime(),
  );
}

async function probeStirling(): Promise<{ status: StirlingProbeStatus; detail: string }> {
  try {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 2500);
    const res = await fetch(STIRLING_URL, { signal: controller.signal });
    clearTimeout(timer);
    if (res.status === 401 || res.status === 403) {
      return { status: "auth_required", detail: `HTTP ${res.status} — configure Stirling auth` };
    }
    if (res.ok) {
      return { status: "online", detail: `HTTP ${res.status}` };
    }
    return { status: "unknown", detail: `HTTP ${res.status}` };
  } catch (err) {
    const msg = err instanceof Error ? err.message : String(err);
    if (msg.includes("abort") || msg.includes("ECONNREFUSED") || msg.includes("fetch failed")) {
      return { status: "offline", detail: "Stirling nao responde em :8081" };
    }
    return { status: "unknown", detail: msg };
  }
}

function buildBlockers(stirling: StirlingProbeStatus, pending: number, events: number): string[] {
  const blockers: string[] = [];
  if (stirling === "offline") {
    blockers.push("Stirling offline — OCR pesado indisponivel (pypdf local segue na zona Maestro)");
  }
  if (pending > 0 && events === 0) {
    blockers.push("PDFs na pasta sem evento — rode watch_pdf_drop.py --once");
  }
  return blockers;
}

export async function buildPdfPipelineSnapshot(): Promise<PdfPipelineSnapshot> {
  const dropDir = resolveInboxPdfsDir();
  const eventsDir = resolvePdfEventsDir();
  const events = loadPdfDropEvents();
  const pendingPdfCount = countPendingPdfs(dropDir);
  const stirlingProbe = await probeStirling();

  return {
    scannedAt: new Date().toISOString(),
    dropFolder: dropDir,
    eventsFolder: eventsDir,
    pendingPdfCount,
    eventCount: events.length,
    events,
    stirling: {
      url: STIRLING_URL,
      status: stirlingProbe.status,
      detail: stirlingProbe.detail,
    },
    blockers: buildBlockers(stirlingProbe.status, pendingPdfCount, events.length),
    specPath: path.join(
      resolveFabioOsRoot(),
      "60_Sistemas",
      "FabioOS",
      "specs",
      "2026-06-30_pipeline-pdf-aprende.md",
    ),
  };
}
