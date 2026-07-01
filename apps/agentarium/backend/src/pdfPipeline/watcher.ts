import fs from "node:fs";
import path from "node:path";

export function startPdfPipelineWatcher(
  watchDirs: string[],
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
          console.error("[pdf-pipeline-watcher]", err);
        }
      }, 400),
    );
  };

  for (const dir of watchDirs) {
    try {
      fs.mkdirSync(dir, { recursive: true });
      const watcher = fs.watch(dir, (_event, filename) => {
        if (!filename) return;
        if (filename.endsWith(".json") || filename.endsWith(".pdf")) {
          schedule(`${dir}:${filename}`);
        }
      });
      watchers.push(watcher);
    } catch (err) {
      console.error("[pdf-pipeline-watcher] falha ao observar", dir, err);
    }
  }

  return () => {
    for (const t of timers.values()) clearTimeout(t);
    for (const w of watchers) w.close();
  };
}

export function watchPdfPipelinePaths(eventsDir: string, dropDir: string): () => void {
  return startPdfPipelineWatcher([eventsDir, dropDir], () => {});
}
