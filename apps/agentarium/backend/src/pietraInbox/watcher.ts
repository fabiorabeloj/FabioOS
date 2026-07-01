import path from "node:path";
import fs from "node:fs";

export function startPietraInboxWatcher(
  watchPaths: string[],
  onChange: () => void,
): () => void {
  const timers = new Map<string, ReturnType<typeof setTimeout>>();
  const watchers: fs.FSWatcher[] = [];

  const schedule = (key: string) => {
    const prev = timers.get(key);
    if (prev) clearTimeout(prev);
    timers.set(
      key,
      setTimeout(() => {
        try {
          onChange();
        } catch (err) {
          console.error("[pietra-inbox-watcher]", err);
        }
      }, 400),
    );
  };

  for (const watchPath of watchPaths) {
    try {
      fs.mkdirSync(watchPath, { recursive: true });
      const watcher = fs.watch(watchPath, (_event, filename) => {
        if (!filename) return;
        if (filename.endsWith(".jsonl") || filename.endsWith(".json")) {
          schedule(`${watchPath}:${filename}`);
        }
      });
      watchers.push(watcher);
    } catch (err) {
      console.error("[pietra-inbox-watcher] falha", watchPath, err);
    }
  }

  // ui state log dir
  const uiDir = path.dirname(watchPaths[0] ?? "");
  if (uiDir) {
    try {
      const logDir = path.join(path.dirname(uiDir), "FabioOS", "logs");
      fs.mkdirSync(logDir, { recursive: true });
      const w = fs.watch(logDir, (_e, f) => {
        if (f?.includes("pietra_inbox_ui_state")) schedule(`ui:${f}`);
      });
      watchers.push(w);
    } catch {
      /* optional */
    }
  }

  return () => {
    for (const t of timers.values()) clearTimeout(t);
    for (const w of watchers) w.close();
  };
}
