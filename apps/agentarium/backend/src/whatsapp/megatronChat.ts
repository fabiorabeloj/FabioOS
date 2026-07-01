import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { loadWhatsAppConfig } from "./config.js";
import { textPreview } from "../whatsappJobs.js";

export type MegatronChatResult = {
  text: string;
  source: "openrouter" | "fallback";
  model?: string;
};

const SYSTEM_PROMPT = `Voce e o MEGATRON, assistente pessoal do Fabio no FabioOS.
Fabio usa este canal principalmente para ENVIAR PROMPTS E TAREFAS para agentes no Cursor.
Responda em portugues do Brasil, linguagem natural, 2 a 5 linhas.
Se a mensagem parecer tarefa/pedido: confirme que foi registrada e diga que os agentes no Cursor podem executar.
Nao invente que ja executou no PC. Nao use o nome Hermes — voce e MEGATRON.`;

function readOpenRouterKey(): string | null {
  const fromEnv = process.env.OPENROUTER_API_KEY?.trim().replace(/^\uFEFF/, "");
  if (fromEnv) {
    return fromEnv;
  }
  const file =
    process.env.OPENROUTER_API_KEY_FILE?.trim() ||
    path.join(os.homedir(), ".fabioos", "secrets", "openrouter_api_key.txt");
  try {
    return fs.readFileSync(file, "utf8").trim().replace(/^\uFEFF/, "") || null;
  } catch {
    return null;
  }
}

export function getOpenRouterStatus(): {
  configured: boolean;
  model: string;
  conversationalEnabled: boolean;
} {
  const config = loadWhatsAppConfig();
  return {
    configured: Boolean(readOpenRouterKey()),
    model: config.openRouterModel,
    conversationalEnabled: config.conversationalEnabled,
  };
}

function fallbackReply(userText: string): string {
  const t = userText.trim().toLowerCase();
  if (/^(oi|ol[aá]|hey|e a[ií]|bom dia|boa tarde|boa noite)\b/.test(t)) {
    return "Oi, Fabio! MEGATRON aqui. Pode falar normalmente — estou ouvindo.";
  }
  if (/\?$/.test(t) || /^(como|qual|quando|onde|por que|pq|me explica|o que)/.test(t)) {
    return [
      "Boa pergunta.",
      "Com IA completa (OpenRouter), consigo elaborar melhor.",
      "Por ora: registrei no FabioOS. Se quiser acao no vault ou codigo, abra o Cursor e diga para continuar a partir da inbox.",
    ].join(" ");
  }
  return `Entendi. Registrei como pedido no FabioOS — abra o Cursor para executar, ou reenvie com prefixo "tarefa:" para arquivo dedicado.`;
}

export async function generateMegatronReply(
  userText: string,
  context?: { jobId?: string; category?: string },
): Promise<MegatronChatResult> {
  const config = loadWhatsAppConfig();
  if (!config.conversationalEnabled) {
    return {
      text: `Recebido (job ${context?.jobId ?? "—"}). Modo conversacional desligado.`,
      source: "fallback",
    };
  }

  const key = readOpenRouterKey();
  if (!key) {
    return { text: fallbackReply(userText), source: "fallback" };
  }

  const userContent = [
    context?.category ? `Categoria detectada: ${context.category}.` : "",
    context?.jobId ? `Job: ${context.jobId}.` : "",
    `Mensagem do Fabio: ${userText}`,
  ]
    .filter(Boolean)
    .join("\n");

  try {
    const res = await fetch("https://openrouter.ai/api/v1/chat/completions", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${key}`,
        "Content-Type": "application/json",
        "HTTP-Referer": "http://127.0.0.1:3847",
        "X-Title": "MEGATRON Agentarium",
      },
      body: JSON.stringify({
        model: config.openRouterModel,
        max_tokens: 320,
        temperature: 0.7,
        messages: [
          { role: "system", content: SYSTEM_PROMPT },
          { role: "user", content: userContent },
        ],
      }),
    });

    if (!res.ok) {
      const errBody = await res.text();
      return {
        text: `${fallbackReply(userText)}\n\n(IA indisponivel: HTTP ${res.status})`,
        source: "fallback",
      };
    }

    const data = (await res.json()) as {
      choices?: Array<{ message?: { content?: string } }>;
      model?: string;
    };
    const content = data.choices?.[0]?.message?.content?.trim();
    if (!content) {
      return { text: fallbackReply(userText), source: "fallback" };
    }
    return { text: content, source: "openrouter", model: data.model ?? config.openRouterModel };
  } catch {
    return { text: fallbackReply(userText), source: "fallback" };
  }
}
