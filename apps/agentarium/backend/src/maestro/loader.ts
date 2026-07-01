import fs from "node:fs";
import type { MaestroStateJson } from "./types.js";
import { resolveMaestroStatePath } from "./paths.js";

export function loadMaestroState(filePath?: string): MaestroStateJson {
  const path = filePath ?? resolveMaestroStatePath();
  const raw = fs.readFileSync(path, "utf8");
  return JSON.parse(raw) as MaestroStateJson;
}

export function maestroStateExists(filePath?: string): boolean {
  try {
    fs.accessSync(filePath ?? resolveMaestroStatePath(), fs.constants.R_OK);
    return true;
  } catch {
    return false;
  }
}
