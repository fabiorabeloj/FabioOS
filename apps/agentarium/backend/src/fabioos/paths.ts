import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

/** Raiz do vault FabioOS (repo). */
export function resolveFabioOsRoot(): string {
  if (process.env.FABIOOS_ROOT) {
    return path.resolve(process.env.FABIOOS_ROOT);
  }
  return path.resolve(__dirname, "..", "..", "..", "..", "..");
}

export function resolveInboxPdfsDir(): string {
  if (process.env.PDF_DROP_DIR) {
    return path.resolve(process.env.PDF_DROP_DIR);
  }
  return path.join(resolveFabioOsRoot(), "00_Inbox", "pdfs");
}

export function resolvePdfEventsDir(): string {
  return path.join(resolveInboxPdfsDir(), "_events");
}

export function resolvePdfDropLog(): string {
  return path.join(
    resolveFabioOsRoot(),
    "60_Sistemas",
    "FabioOS",
    "logs",
    "pdf_drop_events.jsonl",
  );
}
