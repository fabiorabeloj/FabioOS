import { loadWhatsAppConfig, CHANNEL_META } from "./config.js";
import { channelState } from "./channelState.js";
import { whatsappJobs } from "../whatsappJobs.js";

export function getWhatsAppStatus() {
  const config = loadWhatsAppConfig();
  const channels = channelState.all();
  const jobs = whatsappJobs.list(100);

  const lastPersonal = jobs.find((j) => j.channel === "personal");
  const lastSchool = jobs.find((j) => j.channel === "school");
  const pendingFabio = jobs.filter(
    (j) => j.approvalState === "draft_only" || j.approvalState === "awaiting_human",
  ).length;

  return {
    autoSend: config.autoSend,
    replyToFabio: config.replyToFabio,
    conversationalEnabled: config.conversationalEnabled,
    openRouterModel: config.openRouterModel,
    groupsEnabled: config.groupsEnabled,
    defaultMode: config.defaultMode,
    pendingFabio,
    personal: {
      enabled: config.personalEnabled,
      agentId: CHANNEL_META.personal.agentId,
      mode: config.mode,
      autoSend: config.autoSend,
      commandsEnabled: true,
      connected: channels.personal.connected,
      lastMessageAt: channels.personal.lastMessageAt ?? lastPersonal?.createdAt ?? null,
      lastJobId: channels.personal.lastJobId ?? lastPersonal?.jobId ?? null,
    },
    school: {
      enabled: config.schoolEnabled,
      agentId: CHANNEL_META.school.agentId,
      mode: config.defaultMode,
      autoSend: config.autoSend,
      autoMenu: config.schoolAutoMenu,
      connected: channels.school.connected,
      lastMessageAt: channels.school.lastMessageAt ?? lastSchool?.createdAt ?? null,
      lastJobId: channels.school.lastJobId ?? lastSchool?.jobId ?? null,
    },
  };
}
