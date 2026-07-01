import type { WhatsAppJob, WhatsAppApprovalState } from "./types";

export type WhatsAppChannelStatus = {
  enabled: boolean;
  agentId: string;
  mode: string;
  autoSend: boolean;
  commandsEnabled?: boolean;
  autoMenu?: boolean;
  connected: boolean;
  lastMessageAt: string | null;
  lastJobId: string | null;
};

export type WhatsAppOperationsStatus = {
  autoSend: boolean;
  groupsEnabled: boolean;
  defaultMode: string;
  pendingFabio: number;
  personal: WhatsAppChannelStatus;
  school: WhatsAppChannelStatus;
};

export type WhatsAppJobExtended = WhatsAppJob & {
  channel: "personal" | "school";
  isCommand?: boolean;
  commandResponse?: string;
  suggestedReply?: string;
  canSend?: boolean;
};

export type WhatsAppApprovalStateExt = WhatsAppApprovalState;
