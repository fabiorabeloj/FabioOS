export type WhatsAppMessageCategory =
  | "family"
  | "school"
  | "work"
  | "friend"
  | "finance"
  | "service"
  | "unknown"
  | "sensitive";

export type WhatsAppMessageUrgency = "low" | "normal" | "high" | "urgent";

export type WhatsAppActionType =
  | "summarize"
  | "draft_reply"
  | "create_task"
  | "archive_to_obsidian"
  | "forward_to_agent"
  | "requires_human"
  | "ignore";

export type WhatsAppApprovalState =
  | "draft_only"
  | "awaiting_human"
  | "approved"
  | "sent"
  | "blocked";

export type WhatsAppChannel = "personal" | "school";

export type WhatsAppSchoolCategory =
  | "greeting"
  | "student_identification"
  | "homework"
  | "test"
  | "substitute_test"
  | "absence"
  | "content_question"
  | "schedule"
  | "complaint"
  | "discipline"
  | "sensitive"
  | "unknown";

export type WhatsAppMessageInput = {
  messageId: string;
  conversationId: string;
  contactName?: string;
  from: string;
  direction: "incoming" | "outgoing";
  text: string;
  timestamp: string;
  source?: string;
  provider?: string;
  isGroup?: boolean;
  channel?: WhatsAppChannel;
};

export type WhatsAppAnalysis = {
  category: WhatsAppMessageCategory;
  urgency: WhatsAppMessageUrgency;
  action: WhatsAppActionType;
  approvalState: WhatsAppApprovalState;
  routedAgents: string[];
  summary: string;
  draftReply?: string;
  blocked: boolean;
  blockReason?: string;
};

export type WhatsAppJob = {
  jobId: string;
  messageId: string;
  conversationId: string;
  contactName: string;
  fromMasked: string;
  direction: "incoming" | "outgoing";
  textPreview: string;
  category: WhatsAppMessageCategory | WhatsAppSchoolCategory | string;
  urgency: WhatsAppMessageUrgency | string;
  approvalState: WhatsAppApprovalState;
  agentId: string;
  channel: WhatsAppChannel;
  routedAgents: string[];
  source: string;
  provider: string;
  createdAt: string;
  updatedAt: string;
  autoSendBlocked: boolean;
  isCommand?: boolean;
  commandResponse?: string;
  suggestedReply?: string;
  canSend?: boolean;
};
