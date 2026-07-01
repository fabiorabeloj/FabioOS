export type WhatsAppChannel = "personal" | "school";

export type WhatsAppPersonalConfig = {
  mode: "draft_only" | "approved_send";
  autoSend: boolean;
  replyToFabio: boolean;
  groupsEnabled: boolean;
  allowedContacts: string[];
  blockedContacts: string[];
  personalEnabled: boolean;
  schoolEnabled: boolean;
  defaultMode: "draft_only" | "supervised";
  schoolAutoMenu: boolean;
  fabioWhatsAppNumber: string;
  evolutionApiUrl: string;
  evolutionInstance: string;
  conversationalEnabled: boolean;
  openRouterModel: string;
};

function parseList(raw: string | undefined): string[] {
  if (!raw?.trim()) return [];
  return raw
    .split(",")
    .map((s) => s.replace(/\D/g, ""))
    .filter(Boolean);
}

export function loadWhatsAppConfig(): WhatsAppPersonalConfig {
  const mode =
    process.env.WHATSAPP_PERSONAL_MODE === "approved_send"
      ? "approved_send"
      : "draft_only";

  const defaultMode =
    process.env.WHATSAPP_DEFAULT_MODE === "supervised" ? "supervised" : "draft_only";

  return {
    mode,
    autoSend: process.env.WHATSAPP_AUTO_SEND === "true",
    replyToFabio: process.env.WHATSAPP_REPLY_TO_FABIO !== "false",
    groupsEnabled: process.env.WHATSAPP_GROUPS_ENABLED === "true",
    allowedContacts: parseList(process.env.WHATSAPP_ALLOWED_CONTACTS),
    blockedContacts: parseList(process.env.WHATSAPP_BLOCKED_CONTACTS),
    personalEnabled: process.env.WHATSAPP_PERSONAL_ENABLED !== "false",
    schoolEnabled: process.env.WHATSAPP_SCHOOL_ENABLED === "true",
    defaultMode,
    schoolAutoMenu: process.env.WHATSAPP_SCHOOL_AUTO_MENU === "true",
    fabioWhatsAppNumber: process.env.FABIO_WHATSAPP_NUMBER ?? "5511982123896",
    evolutionApiUrl: process.env.EVOLUTION_API_URL ?? "http://127.0.0.1:8080",
    evolutionInstance: process.env.EVOLUTION_INSTANCE ?? "fabioos-pessoal",
    conversationalEnabled: process.env.WHATSAPP_CONVERSATIONAL !== "false",
    openRouterModel: process.env.MEGATRON_OPENROUTER_MODEL ?? "openrouter/free",
  };
}

export function maskPhone(phone: string): string {
  const digits = phone.replace(/\D/g, "");
  if (digits.length < 8) return "****";
  const prefix = digits.slice(0, 4);
  const suffix = digits.slice(-4);
  return `${prefix}****${suffix}`;
}

export const CHANNEL_META = {
  personal: {
    agentId: "hermes",
    purpose: "comandos pessoais, triagem, rascunhos, alertas Fabio",
    defaultMode: "draft_only" as const,
  },
  school: {
    agentId: "pietra",
    purpose: "triagem escolar, menu institucional, encaminhamento",
    defaultMode: "supervised" as const,
  },
};
