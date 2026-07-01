import fs from "node:fs";
import path from "node:path";

export function startMaestroWatcher(
  filePath: string,
  onChange: () => void,
): () => void {
  let timer: ReturnType<typeof setTimeout> | undefined;
  let watcher: fs.FSWatcher | undefined;

  const schedule = () => {
    if (timer) clearTimeout(timer);
    timer = setTimeout(() => {
      try {
        onChange();
      } catch (err) {
        console.error("[maestro-watcher]", err);
      }
    }, 300);
  };

  try {
    watcher = fs.watch(path.dirname(filePath), (_event, filename) => {
      if (!filename) return;
      if (path.basename(filePath) === filename) {
        schedule();
      }
    });
  } catch (err) {
    console.error("[maestro-watcher] falha ao observar arquivo:", err);
  }

  return () => {
    if (timer) clearTimeout(timer);
    watcher?.close();
  };
}
