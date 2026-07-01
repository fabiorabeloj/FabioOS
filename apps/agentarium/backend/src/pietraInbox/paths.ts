import path from "node:path";
import { resolveFabioOsRoot } from "../fabioos/paths.js";

export function resolvePietraBase(): string {
  if (process.env.PIETRA_BASE) {
    return path.resolve(process.env.PIETRA_BASE);
  }
  return path.join(resolveFabioOsRoot(), "60_Sistemas", "Pietra");
}

export function defaultPietraTenant(): string {
  return process.env.PIETRA_TENANT ?? "colegio-pietra";
}

export function resolveTenantDir(tenant?: string): string {
  const t = tenant ?? defaultPietraTenant();
  return path.join(resolvePietraBase(), "tenants", t);
}

export function resolveTenantPietraState(tenant?: string): string {
  return path.join(resolveTenantDir(tenant), "pietra_state.json");
}

export function resolveTenantAtendimentos(tenant?: string): string {
  return path.join(resolveTenantDir(tenant), "atendimentos.jsonl");
}

export function resolveTenantSessionsDir(tenant?: string): string {
  return path.join(resolveTenantDir(tenant), "sessions");
}

export function resolvePietraUiStatePath(): string {
  return path.join(
    resolveFabioOsRoot(),
    "60_Sistemas",
    "FabioOS",
    "logs",
    "pietra_inbox_ui_state.json",
  );
}

export function resolvePietraSpecPath(): string {
  return path.join(
    resolveFabioOsRoot(),
    "60_Sistemas",
    "FabioOS",
    "specs",
    "2026-06-30_inbox-operacional-pietraos.md",
  );
}
