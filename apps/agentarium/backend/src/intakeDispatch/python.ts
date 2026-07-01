import { execFile } from "node:child_process";
import { promisify } from "node:util";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { resolveFabioOsRoot } from "../fabioos/paths.js";

const execFileAsync = promisify(execFile);

export function resolvePython(): string {
  return process.env.FABIOOS_PYTHON ?? "python";
}

export async function runPython(
  scriptPath: string,
  args: string[] = [],
): Promise<{ stdout: string; stderr: string; code: number }> {
  const root = resolveFabioOsRoot();
  try {
    const { stdout, stderr } = await execFileAsync(resolvePython(), [scriptPath, ...args], {
      cwd: root,
      encoding: "utf8",
      maxBuffer: 4 * 1024 * 1024,
    });
    return { stdout: stdout ?? "", stderr: stderr ?? "", code: 0 };
  } catch (err: unknown) {
    const e = err as { stdout?: string; stderr?: string; code?: number; message?: string };
    return {
      stdout: e.stdout ?? "",
      stderr: e.stderr ?? e.message ?? "",
      code: typeof e.code === "number" ? e.code : 1,
    };
  }
}

export async function runPythonJson<T>(scriptPath: string, args: string[] = []): Promise<T> {
  const { stdout, stderr, code } = await runPython(scriptPath, args);
  if (code !== 0) {
    throw new Error(stderr.trim() || `Python exit ${code}: ${scriptPath}`);
  }
  const trimmed = stdout.trim();
  if (!trimmed) throw new Error(`Empty stdout: ${scriptPath}`);
  return JSON.parse(trimmed) as T;
}

export async function runPythonWithTempInput(
  scriptPath: string,
  args: string[],
  payload: unknown,
): Promise<{ stdout: string; stderr: string; code: number }> {
  const tmp = path.join(os.tmpdir(), `fabioos-intake-${Date.now()}.json`);
  fs.writeFileSync(tmp, JSON.stringify(payload, null, 2), "utf8");
  try {
    return await runPython(scriptPath, [...args, "--input", tmp]);
  } finally {
    try {
      fs.unlinkSync(tmp);
    } catch {
      /* ignore */
    }
  }
}
