import { generateMegatronReply, getOpenRouterStatus } from "../whatsapp/megatronChat.js";
import { submitNaturalCommand } from "../intakeDispatch/actions.js";
import { eventLog } from "../eventLog.js";

export type MegatronChatResponse = {
  ok: boolean;
  reply: string;
  source: "openrouter" | "fallback";
  model?: string;
  intake?: { ok: boolean; message: string; cardId?: string };
};

const TASK_PREFIX = /^tarefa\s*:/i;

export function getMegatronChatStatus() {
  return getOpenRouterStatus();
}

export async function handleMegatronChat(message: string): Promise<MegatronChatResponse> {
  const trimmed = message.trim();
  if (trimmed.length < 1) {
    return { ok: false, reply: "Mensagem vazia.", source: "fallback" };
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

  return {
    ok: true,
    reply,
    source: result.source,
    model: result.model,
    intake,
  };
}
