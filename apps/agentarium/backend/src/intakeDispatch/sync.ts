import path from "node:path";
import fs from "node:fs";
import type { WsMessage } from "../types.js";
import { buildIntakeDispatchSnapshot } from "./reader.js";
import type { IntakeDispatchSnapshot } from "./types.js";
import { resolveIntakeQueueLive, resolveIntakeQueueSample } from "./paths.js";

type Broadcaster = (msg: WsMessage) => void;

let lastSnapshot: IntakeDispatchSnapshot | null = null;

export function getIntakeDispatchSnapshot(): IntakeDispatchSnapshot | null {
  return lastSnapshot;
}

export async function refreshIntakeDispatchSnapshot(): Promise<IntakeDispatchSnapshot> {
  lastSnapshot = await buildIntakeDispatchSnapshot();
  return lastSnapshot;
}

export function startIntakeDispatchWatcher(onChange: () => void): () => void {
  const timers = new Map<string, ReturnType<typeof setTimeout>>();
  const watchers: fs.FSWatcher[] = [];
  const watchPaths = [
    path.dirname(resolveIntakeQueueLive()),
    path.dirname(resolveIntakeQueueSample()),
  ];

  const schedule = (key: string) => {
    const prev = timers.get(key);
    if (prev) clearTimeout(prev);
    timers.set(
      key,
      setTimeout(() => {
        try {
          onChange();
        } catch (err) {
          console.error("[intake-dispatch-watcher]", err);
        }
      }, 400),
    );
  };

  for (const watchPath of watchPaths) {
    try {
      fs.mkdirSync(watchPath, { recursive: true });
      const watcher = fs.watch(watchPath, (_event, filename) => {
        if (!filename) return;
        if (filename.endsWith(".json") || filename.endsWith(".jsonl")) {
          schedule(`${watchPath}:${filename}`);
        }
      });
      watchers.push(watcher);
    } catch (err) {
      console.error("[intake-dispatch-watcher] falha", watchPath, err);
    }
  }

  return () => {
    for (const t of timers.values()) clearTimeout(t);
    for (const w of watchers) w.close();
  };
}

export function initIntakeDispatchIntegration(broadcast: Broadcaster): () => void {
  const push = async () => {
    const snapshot = await refreshIntakeDispatchSnapshot();
    broadcast({ type: "intake_dispatch_snapshot", dispatch: snapshot });
  };

  void push();
  return startIntakeDispatchWatcher(() => {
    void push();
  });
}
