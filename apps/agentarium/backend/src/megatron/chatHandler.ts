import path from "node:path";
import { generateMegatronReply, getOpenRouterStatus, type ChatTurn } from "../whatsapp/megatronChat.js";
import { submitNaturalCommand } from "../intakeDispatch/actions.js";
import { runPythonJson } from "../intakeDispatch/python.js";
import { resolveFabioOsRoot } from "../fabioos/paths.js";
import { eventLog } from "../eventLog.js";

export type MegatronChatResponse = {
  ok: boolean;
  reply: string;
  source: "openrouter" | "fallback" | "bridge";
  model?: string;
  intake?: { ok: boolean; message: string; cardId?: string };
};

const TASK_PREFIX = /^tarefa\s*:/i;

// Ponte determinística (custo-zero): status/fila/aprovar/barramento/tarefa
// respondidos com dado REAL do sistema; só conversa cai no OpenRouter.
type BridgeReply = { handled: boolean; reply: string; tipo: string };

function resolveChatBridgeScript(): string {
  return path.join(resolveFabioOsRoot(), "60_Sistemas", "MEGATRON", "v1", "chat_bridge.py");
}

// Memória de conversa (multi-turno) — vive no processo, cap de 24 turnos.
const chatHistory: ChatTurn[] = [];

function remember(user: string, assistant: string) {
  chatHistory.push({ role: "user", content: user }, { role: "assistant", content: assistant });
  while (chatHistory.length > 24) chatHistory.shift();
}

async function fetchSystemContext(): Promise<string | undefined> {
  try {
    const r = await runPythonJson<{ contexto?: string }>(resolveChatBridgeScript(), ["--contexto"]);
    return r.contexto || undefined;
  } catch {
    return undefined;
  }
}

export function getMegatronChatStatus() {
  return getOpenRouterStatus();
}

export async function handleMegatronChat(message: string): Promise<MegatronChatResponse> {
  const trimmed = message.trim();
  if (trimmed.length < 1) {
    return { ok: false, reply: "Mensagem vazia.", source: "fallback" };
  }

  // 1) tenta o cérebro real primeiro (chat_bridge.py) — exceto o prefixo "tarefa:"
  //    que já tem fluxo próprio via submitNaturalCommand.
  if (!TASK_PREFIX.test(trimmed)) {
    try {
      const bridge = await runPythonJson<BridgeReply>(resolveChatBridgeScript(), [trimmed]);
      if (bridge.handled && bridge.reply) {
        eventLog.append({
          channel: "SYSTEM",
          source: "megatron-chat",
          agentId: "megatron",
          message: `[CHAT] Fabio: ${trimmed.slice(0, 120)} → bridge/${bridge.tipo}`,
        });
        remember(trimmed, bridge.reply); // LLM lembra do que a ponte fez
        return { ok: true, reply: bridge.reply, source: "bridge" };
      }
    } catch {
      // ponte indisponível → segue para o fluxo LLM normalmente
    }
  }

  let intake: MegatronChatResponse["intake"];
  let chatText = trimmed;

  if (TASK_PREFIX.test(trimmed)) {
    const commandText = trimmed.replace(TASK_PREFIX, "").trim();
    if (commandText.length >= 4) {
      const intakeResult = await submitNaturalCommand(commandText);
      intake = {
        ok: intakeResult.ok,
        message: intakeResult.message,
        cardId: intakeResult.item?.id,
      };
      chatText = commandText;
    }
  }

  const result = await generateMegatronReply(chatText, {
    category: intake ? "agentarium_chat_intake" : "agentarium_chat",
    jobId: intake?.cardId,
    systemContext: await fetchSystemContext(), // olhos: estado real em toda resposta
    history: chatHistory,                      // memória: conversa multi-turno
  });

  let reply = result.text;
  if (intake) {
    const intakeLine = intake.ok
      ? `[INTAKE] ${intake.message}`
      : `[INTAKE ERRO] ${intake.message}`;
    reply = `${intakeLine}\n\n${reply}`;
  }

  eventLog.append({
    channel: "SYSTEM",
    source: "megatron-chat",
    agentId: "megatron",
    message: `[CHAT] Fabio: ${trimmed.slice(0, 120)} → ${result.source}${intake ? " + intake" : ""}`,
  });

  remember(trimmed, reply);

  return {
    ok: true,
    reply,
    source: result.source,
    model: result.model,
    intake,
  };
}
