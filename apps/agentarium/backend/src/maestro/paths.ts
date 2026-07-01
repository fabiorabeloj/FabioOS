import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

/** Caminho canonico do estado exportado pelo Maestro. */
export function resolveMaestroStatePath(): string {
  if (process.env.MAESTRO_STATE_PATH) {
    return path.resolve(process.env.MAESTRO_STATE_PATH);
  }
  if (process.env.FABIOOS_ROOT) {
    return path.join(
      path.resolve(process.env.FABIOOS_ROOT),
      "60_Sistemas",
      "MEGATRON",
      "v1",
      "state",
      "maestro_state.json",
    );
  }
  // backend/src/maestro -> repo root (5 niveis)
  const repoRoot = path.resolve(__dirname, "..", "..", "..", "..", "..");
  return path.join(
    repoRoot,
    "60_Sistemas",
    "MEGATRON",
    "v1",
    "state",
    "maestro_state.json",
  );
}
