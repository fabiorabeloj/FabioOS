import path from "node:path";
import { resolveFabioOsRoot } from "../fabioos/paths.js";

export function resolveMegatronV1(): string {
  return path.join(resolveFabioOsRoot(), "60_Sistemas", "MEGATRON", "v1");
}

export function resolveIntakeQueueSample(): string {
  return path.join(resolveMegatronV1(), "examples", "intake_queue.sample.json");
}

export function resolveIntakeQueueLive(): string {
  return path.join(resolveMegatronV1(), "state", "intake_queue.json");
}

export function resolveIntakeLog(): string {
  return path.join(resolveMegatronV1(), "state", "intake_log.jsonl");
}

export function resolveArquivistaScript(): string {
  return path.join(resolveMegatronV1(), "arquivista_intake.py");
}

export function resolveIntakeFlowScript(): string {
  return path.join(resolveMegatronV1(), "intake_flow.py");
}

export function resolveCoordenacaoScript(): string {
  return path.join(resolveMegatronV1(), "coordenacao.py");
}

export function resolveUniversalAdapterScript(): string {
  return path.join(
    resolveFabioOsRoot(),
    "60_Sistemas",
    "FabioOS",
    "scripts",
    "universal_intake_adapter.py",
  );
}

export function resolveIntakeCommandExtractScript(): string {
  return path.join(
    resolveFabioOsRoot(),
    "60_Sistemas",
    "FabioOS",
    "scripts",
    "intake_command_extract.py",
  );
}

export function resolveGmailFakeExample(): string {
  return path.join(resolveFabioOsRoot(), "60_Sistemas", "FabioOS", "examples", "intake_gmail_fake.json");
}

export function resolveIntakeSpecPath(): string {
  return path.join(
    resolveFabioOsRoot(),
    "60_Sistemas",
    "FabioOS",
    "specs",
    "2026-07-01_MEGATRON_Core_Spec_v0.1.md",
  );
}
