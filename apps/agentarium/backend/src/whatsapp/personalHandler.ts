import { store } from "../store.js";
import { eventLog } from "../eventLog.js";
import { whatsappJobs, makeJobId, maskPhone, textPreview } from "../whatsappJobs.js";
import { loadWhatsAppConfig, CHANNEL_META } from "./config.js";
import { channelState } from "./channelState.js";
import { buildRoutePlan } from "./router.js";
import { handlePersonalCommand } from "./commands.js";
import type { WhatsAppMessageInput } from "./types.js";
import { scheduleAgentUpdates } from "./shared.js";

export type WhatsAppHandleResult = {
  ok: boolean;
  jobId: string;
  agentId: string;
  channel: "personal";
  approvalState: string;
  message: string;
  analysis?: ReturnType<typeof buildRoutePlan>["analysis"];
  blocked?: boolean;
  blockReason?: string;
  isCommand?: boolean;
  replyToFabio?: string;
  autoSend: boolean;
  canSend: boolean;
};

export function handlePersonalWhatsAppMessage(
  input: WhatsAppMessageInput,
): WhatsAppHandleResult {
  const config = loadWhatsAppConfig();
  const jobId = makeJobId();
  const sourceTag =
    input.source === "manual_test" || input.messageId.startsWith("wa-test")
      ? "MANUAL_TEST"
      : "PERSONAL-WPP";

  if (!config.personalEnabled) {
    return {
      ok: false,
      jobId,
      agentId: "hermes",
      channel: "personal",
      approvalState: "blocked",
      message: "Personal WhatsApp channel disabled",
      blocked: true,
      autoSend: false,
      canSend: false,
    };
  }

  const cmd = handlePersonalCommand(input.text.trim());
  if (cmd) {
    whatsappJobs.add({
      jobId,
      messageId: input.messageId,
      conversationId: input.conversationId,
      contactName: input.contactName ?? "Fabio",
      fromMasked: maskPhone(input.from),
      direction: input.direction,
      textPreview: input.text,
      category: "command",
      urgency: "low",
      approvalState: "draft_only",
      agentId: "hermes",
      channel: "personal",
      routedAgents: ["hermes", "megatron"],
      source: input.source ?? "whatsapp",
      provider: input.provider ?? "evolution_api",
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      autoSendBlocked: true,
      isCommand: true,
      commandResponse: cmd.response,
      canSend: false,
    });

    channelState.recordMessage("personal", jobId);

    store.updateWithMeta("hermes", {
      state: "executing",
      task: `Comando ${cmd.command}`,
      zone: "Personal WhatsApp",
    }, { eventSource: "real", jobId });

    eventLog.append({
      channel: "WHATSAPP",
      agentId: "hermes",
      jobId,
      source: "COMMAND",
      message: `[COMMAND] ${cmd.command} -> Fabio`,
      approvalState: "draft_only",
    });

    return {
      ok: true,
      jobId,
      agentId: "hermes",
      channel: "personal",
      approvalState: "draft_only",
      message: "Command processed. Reply prepared for Fabio (not auto-sent externally).",
      isCommand: true,
      replyToFabio: cmd.response,
      blocked: false,
      autoSend: config.autoSend,
      canSend: false,
    };
  }

  if (input.isGroup && !config.groupsEnabled) {
    whatsappJobs.add({
      jobId,
      messageId: input.messageId,
      conversationId: input.conversationId,
      contactName: input.contactName ?? "Grupo",
      fromMasked: maskPhone(input.from),
      direction: input.direction,
      textPreview: textPreview(input.text),
      category: "unknown",
      urgency: "low",
      approvalState: "blocked",
      agentId: "hermes",
      channel: "personal",
      routedAgents: ["hermes"],
      source: input.source ?? "whatsapp",
      provider: input.provider ?? "evolution_api",
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      autoSendBlocked: true,
      canSend: false,
    });

    eventLog.append({
      channel: "WHATSAPP",
      agentId: "hermes",
      jobId,
      source: "BLOCKED",
      message: "[BLOCKED] Grupo — WHATSAPP_GROUPS_ENABLED=false",
      maskedPhone: maskPhone(input.from),
      approvalState: "blocked",
    });

    return {
      ok: true,
      jobId,
      agentId: "hermes",
      channel: "personal",
      approvalState: "blocked",
      message: "Group blocked.",
      blocked: true,
      blockReason: "groups_disabled",
      autoSend: config.autoSend,
      canSend: false,
    };
  }

  const { analysis, agentUpdates } = buildRoutePlan(input);

  whatsappJobs.add({
    jobId,
    messageId: input.messageId,
    conversationId: input.conversationId,
    contactName: input.contactName ?? "Contato",
    fromMasked: maskPhone(input.from),
    direction: input.direction,
    textPreview: textPreview(input.text),
    category: analysis.category,
    urgency: analysis.urgency,
    approvalState: analysis.approvalState,
    agentId: "hermes",
    channel: "personal",
    routedAgents: analysis.routedAgents,
    source: input.source ?? "whatsapp",
    provider: input.provider ?? "evolution_api",
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
    autoSendBlocked: !config.autoSend,
    suggestedReply: analysis.draftReply,
    canSend: false,
  });

  channelState.recordMessage("personal", jobId);

  eventLog.append({
    channel: "WHATSAPP",
    agentId: "hermes",
    jobId,
    source: sourceTag,
    fromZone: "Personal WhatsApp",
    toZone: "Message Intake",
    message: `[PERSONAL-WPP] MEGATRON · ${analysis.category}`,
    maskedPhone: maskPhone(input.from),
    approvalState: analysis.approvalState,
  });

  scheduleAgentUpdates(agentUpdates, jobId, sourceTag, analysis.approvalState);

  return {
    ok: true,
    jobId,
    agentId: "hermes",
    channel: "personal",
    approvalState: analysis.approvalState,
    message: "Routed to MEGATRON canal pessoal.",
    analysis,
    blocked: false,
    replyToFabio: analysis.draftReply
      ? analysis.draftReply
      : undefined,
    autoSend: config.autoSend,
    canSend: false,
  };
}

export { CHANNEL_META };
