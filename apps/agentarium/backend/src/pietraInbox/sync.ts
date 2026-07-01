import type { WsMessage } from "../types.js";
import path from "node:path";
import {
  defaultPietraTenant,
  resolvePietraUiStatePath,
  resolveTenantDir,
} from "./paths.js";
import { buildPietraInboxSnapshot, saveUiAction } from "./reader.js";
import type { PietraInboxSnapshot, PietraUiAction } from "./types.js";
import { startPietraInboxWatcher } from "./watcher.js";

type Broadcaster = (msg: WsMessage) => void;

let lastSnapshot: PietraInboxSnapshot | null = null;
let currentTenant = defaultPietraTenant();

export function getPietraInboxSnapshot(): PietraInboxSnapshot | null {
  return lastSnapshot;
}

export function refreshPietraInboxSnapshot(tenant?: string): PietraInboxSnapshot {
  currentTenant = tenant ?? currentTenant;
  lastSnapshot = buildPietraInboxSnapshot(currentTenant);
  return lastSnapshot;
}

export function applyPietraCardAction(
  cardId: string,
  action: PietraUiAction,
  note?: string,
): PietraInboxSnapshot {
  saveUiAction(cardId, action, note);
  return refreshPietraInboxSnapshot();
}

export function initPietraInboxIntegration(broadcast: Broadcaster): () => void {
  const tenant = defaultPietraTenant();
  const tenantDir = resolveTenantDir(tenant);
  const uiLogDir = path.dirname(resolvePietraUiStatePath());

  const push = () => {
    const snapshot = refreshPietraInboxSnapshot(tenant);
    broadcast({ type: "pietra_inbox_snapshot", inbox: snapshot });
  };

  push();

  return startPietraInboxWatcher([tenantDir, uiLogDir], push);
}
