import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { loadWhatsAppConfig } from "./config.js";

export type EvolutionSendResult = {
  ok: boolean;
  error?: string;
  remoteJid?: string;
};

function readEvolutionApiKey(): string | null {
  if (process.env.EVOLUTION_API_KEY?.trim()) {
    return process.env.EVOLUTION_API_KEY.trim();
  }
  const file =
    process.env.EVOLUTION_API_KEY_FILE?.trim() ||
    path.join(os.homedir(), ".fabioos", "secrets", "evolution_api_key.txt");
  try {
    return fs.readFileSync(file, "utf8").trim();
  } catch {
    return null;
  }
}

export async function sendEvolutionText(
  number: string,
  text: string,
): Promise<EvolutionSendResult> {
  const config = loadWhatsAppConfig();
  const apiKey = readEvolutionApiKey();
  if (!apiKey) {
    return { ok: false, error: "Evolution API key not found" };
  }

  const digits = number.replace(/\D/g, "");
  if (!digits) {
    return { ok: false, error: "Invalid destination number" };
  }

  const base = config.evolutionApiUrl.replace(/\/$/, "");
  const url = `${base}/message/sendText/${config.evolutionInstance}`;

  try {
    const res = await fetch(url, {
      method: "POST",
      headers: {
        apikey: apiKey,
        "Content-Type": "application/json; charset=utf-8",
      },
      body: JSON.stringify({ number: digits, text }),
    });

    if (!res.ok) {
      const body = await res.text();
      return { ok: false, error: `Evolution HTTP ${res.status}: ${body.slice(0, 200)}` };
    }

    const data = (await res.json()) as { key?: { remoteJid?: string } };
    return { ok: true, remoteJid: data.key?.remoteJid };
  } catch (err) {
    const msg = err instanceof Error ? err.message : String(err);
    return { ok: false, error: msg };
  }
}
