import { store } from "../store.js";
import { eventLog } from "../eventLog.js";
import { whatsappJobs, makeJobId, maskPhone, textPreview } from "../whatsappJobs.js";
import { loadWhatsAppConfig } from "./config.js";
import { channelState } from "./channelState.js";
import {
  classifySchoolMessage,
  buildSchoolRoutePlan,
} from "./schoolHandler.js";
import type { WhatsAppMessageInput } from "./types.js";
import { scheduleAgentUpdates } from "./shared.js";

export function handleSchoolWhatsAppMessage(input: WhatsAppMessageInput) {
  const config = loadWhatsAppConfig();
  const jobId = makeJobId();
  const sourceTag =
    input.source === "manual_test" ? "MANUAL_TEST" : "SCHOOL-WPP";

  if (!config.schoolEnabled) {
    return {
      ok: false,
      jobId,
      agentId: "pietra",
      channel: "school" as const,
      approvalState: "blocked",
      message: "School WhatsApp channel disabled (WHATSAPP_SCHOOL_ENABLED=false)",
      blocked: true,
      autoSend: config.autoSend,
      canSend: false,
    };
  }

  const classified = classifySchoolMessage(input.text);
  const approvalState = classified.requiresApproval ? "awaiting_human" : "draft_only";
  const routedAgents = ["pietra"];
  if (classified.category === "discipline" || classified.category === "sensitive") {
    routedAgents.push("supervisor");
  }

  const agentUpdates = buildSchoolRoutePlan(input, classified.category);

  whatsappJobs.add({
    jobId,
    messageId: input.messageId,
    conversationId: input.conversationId,
    contactName: input.contactName ?? "Responsavel",
    fromMasked: maskPhone(input.from),
    direction: input.direction,
    textPreview: textPreview(input.text),
    category: classified.category,
    urgency: classified.urgency,
    approvalState,
    agentId: "pietra",
    channel: "school",
    routedAgents,
    source: input.source ?? "whatsapp",
    provider: input.provider ?? "evolution_api",
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
    autoSendBlocked: !config.autoSend,
    suggestedReply: classified.suggestedReply,
    canSend: false,
  });

  channelState.recordMessage("school", jobId);

  eventLog.append({
    channel: "WHATSAPP",
    agentId: "pietra",
    jobId,
    source: sourceTag,
    fromZone: "WhatsApp",
    toZone: "Classificação",
    message: `[SCHOOL-WPP] Pietra · ${classified.category}`,
    maskedPhone: maskPhone(input.from),
    approvalState,
  });

  scheduleAgentUpdates(
    agentUpdates.map((s) => ({ ...s, state: s.state })),
    jobId,
    sourceTag,
    approvalState,
  );

  return {
    ok: true,
    jobId,
    agentId: "pietra",
    channel: "school" as const,
    approvalState,
    message: "Routed to Pietra. Suggested reply is draft_only — not sent.",
    category: classified.category,
    suggestedReply: classified.suggestedReply,
    blocked: false,
    autoSend: config.autoSend,
    canSend: false,
  };
}
