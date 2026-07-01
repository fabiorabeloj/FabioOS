import type { WsMessage } from "../types.js";
import { resolveInboxPdfsDir, resolvePdfEventsDir } from "../fabioos/paths.js";
import { buildPdfPipelineSnapshot } from "./reader.js";
import type { PdfPipelineSnapshot } from "./types.js";
import { startPdfPipelineWatcher } from "./watcher.js";

type Broadcaster = (msg: WsMessage) => void;

let lastSnapshot: PdfPipelineSnapshot | null = null;

export function getPdfPipelineSnapshot(): PdfPipelineSnapshot | null {
  return lastSnapshot;
}

export async function refreshPdfPipelineSnapshot(): Promise<PdfPipelineSnapshot> {
  lastSnapshot = await buildPdfPipelineSnapshot();
  return lastSnapshot;
}

export function initPdfPipelineIntegration(broadcast: Broadcaster): () => void {
  const eventsDir = resolvePdfEventsDir();
  const dropDir = resolveInboxPdfsDir();

  const push = async () => {
    const snapshot = await refreshPdfPipelineSnapshot();
    broadcast({ type: "pdf_pipeline_snapshot", pipeline: snapshot });
  };

  void push();

  return startPdfPipelineWatcher([eventsDir, dropDir], () => {
    void push();
  });
}
