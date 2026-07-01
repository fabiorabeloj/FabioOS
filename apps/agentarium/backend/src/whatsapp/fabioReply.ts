import { eventLog } from "../eventLog.js";
import { whatsappJobs } from "../whatsappJobs.js";
import { maskPhone, loadWhatsAppConfig } from "./config.js";
import { textPreview } from "../whatsappJobs.js";
import { sendEvolutionText } from "./evolutionSend.js";
import { generateMegatronReply } from "./megatronChat.js";
import {
  buildTaskConfirmation,
  isFabioSender,
  type CapturedTask,
} from "./taskCapture.js";
import type { WhatsAppMessageInput } from "./types.js";
import type { WhatsAppHandleResult } from "./personalHandler.js";

export type FabioDeliveryResult = {
  sent: boolean;
  text?: string;
  error?: string;
  chatSource?: "openrouter" | "fallback" | "task";
};

async function buildReplyText(
  input: WhatsAppMessageInput,
  result: WhatsAppHandleResult,
  fabioNumber: string,
  task?: CapturedTask | null,
  taskFile?: string,
): Promise<{ text: string | null; chatSource?: FabioDeliveryResult["chatSource"] }> {
  if (result.blocked) return { text: null };

  if (result.isCommand && result.replyToFabio) {
    return { text: `[MEGATRON]\n${result.replyToFabio}` };
  }

  if (isFabioSender(input, fabioNumber) && task && taskFile) {
    return {
      text: `[MEGATRON]\n${buildTaskConfirmation(task, result.jobId, taskFile)}`,
      chatSource: "task",
    };
  }

  if (isFabioSender(input, fabioNumber)) {
    const chat = await generateMegatronReply(input.text, {
      jobId: result.jobId,
      category: result.analysis?.category,
    });
    return { text: `[MEGATRON]\n${chat.text}`, chatSource: chat.source };
  }

  return {
    text: [
      "[MEGATRON · aviso]",
      `Nova mensagem de ${maskPhone(input.from)}`,
      textPreview(input.text, 120),
      "",
      `Job: ${result.jobId}`,
      "Resposta ao contato: draft_only (nao enviada).",
    ].join("\n"),
  };
}

export async function deliverReplyToFabio(
  input: WhatsAppMessageInput,
  result: WhatsAppHandleResult,
  options?: { task?: CapturedTask | null; taskFile?: string },
): Promise<FabioDeliveryResult> {
  const config = loadWhatsAppConfig();
  if (!config.replyToFabio) {
    return { sent: false };
  }

  const built = await buildReplyText(
    input,
    result,
    config.fabioWhatsAppNumber,
    options?.task,
    options?.taskFile,
  );
  if (!built.text) {
    return { sent: false };
  }

  const send = await sendEvolutionText(config.fabioWhatsAppNumber, built.text);
  if (!send.ok) {
    eventLog.append({
      channel: "WHATSAPP",
      agentId: "canal-wpp-pessoal",
      jobId: result.jobId,
      source: "REPLY",
      message: `[REPLY] Falha ao enviar para Fabio: ${send.error}`,
      approvalState: result.approvalState,
    });
    return { sent: false, text: built.text, error: send.error, chatSource: built.chatSource };
  }

  whatsappJobs.update(result.jobId, {
    autoSendBlocked: false,
    canSend: true,
    commandResponse: result.isCommand ? result.replyToFabio : built.text,
  });

  const sourceTag =
    built.chatSource === "task"
      ? "TASK"
      : built.chatSource === "openrouter"
        ? "CHAT-IA"
        : "REPLY";

  eventLog.append({
    channel: "WHATSAPP",
    agentId: "canal-wpp-pessoal",
    jobId: result.jobId,
    source: sourceTag,
    message: `[${sourceTag}] Resposta MEGATRON enviada para Fabio`,
    approvalState: result.approvalState,
  });

  return { sent: true, text: built.text, chatSource: built.chatSource };
}
