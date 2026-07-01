import type { EventLogEntry } from "./eventLog.js";
import type { WhatsAppJob } from "./whatsapp/types.js";
import type { PietraInboxSnapshot } from "./pietraInbox/types.js";

export const AGENT_STATES = [
  "idle",
  "thinking",
  "executing",
  "waiting_approval",
  "done",
  "error",
] as const;

export type AgentRuntimeState = (typeof AGENT_STATES)[number];
/** @deprecated use AgentRuntimeState */
export type AgentStateKind = AgentRuntimeState;

export const AGENT_LAYERS = [
  "command",
  "security",
  "technical",
  "knowledge",
  "school",
  "finance",
  "interface",
  "personal",
] as const;

import type { IntakeDispatchSnapshot } from "./intakeDispatch/types.js";

export type AgentLayer = (typeof AGENT_LAYERS)[number];

export const AGENT_STATUSES = ["active", "inactive", "planned"] as const;
export type AgentStatus = (typeof AGENT_STATUSES)[number];

export const ZONES = [
  "Personal WhatsApp",
  "Message Intake",
  "Draft Reply",
  "Awaiting Fabio",
  "Approved",
  "Sent",
  "Blocked",
  "WhatsApp",
  "Inbox",
  "Classificação",
  "Obsidian",
  "GitHub",
  "n8n",
  "RAG",
  "Aprovação Humana",
  "Concluído",
  "Erro",
] as const;

export type Zone = (typeof ZONES)[number];

export type SandboxMode = "off" | "all" | "non-main" | "unknown";
export type WorkspaceAccess = "rw" | "ro" | "none" | "unknown";
export type RiskLevel = "safe" | "warning" | "danger";
export type ElevatedMode = "disabled" | "enabled" | "restricted" | "unknown";
export type AuthProfile = "local" | "default-fallback" | "unknown";

export type AgentPolicy = {
  sandboxMode: SandboxMode;
  sandboxScope: string;
  workspaceRoot: string;
  workspaceAccess: WorkspaceAccess;
  dockerSandbox: string;
  browserSandbox: string;
  prunePolicy: string;
  allowedTools: string[];
  deniedTools: string[];
  toolProfile?: string;
  providerPolicy?: string;
  sandboxToolPolicy?: string;
  subagentToolPolicy?: string;
  elevated: ElevatedMode;
  agentDir: string;
  authProfile: AuthProfile;
  riskLevel: RiskLevel;
  riskNotes: string[];
};

export type MaestroRawStatus = "ativo" | "planejado" | "gated";

export type Agent = {
  id: string;
  name: string;
  layer: AgentLayer;
  status: AgentStatus;
  /** Status bruto do Maestro (ativo/planejado/gated). */
  rawStatus?: MaestroRawStatus;
  role: string;
  responsibilities: string[];
  inputs: string[];
  outputs: string[];
  requiresApprovalFor: string[];
  essential: boolean;
  catalogZone: string;
  state: AgentRuntimeState;
  task: string;
  zone: Zone;
  updatedAt: string;
  policy: AgentPolicy;
  homeZone?: Zone;
  lastEventSource?: "real" | "sim" | "idle";
  lastJobId?: string;
  lastFromZone?: Zone;
  lastToZone?: Zone;
};

export type FabioAgentDefinition = {
  id: string;
  name: string;
  layer: AgentLayer;
  role: string;
  responsibilities: string[];
  inputs: string[];
  outputs: string[];
  status: AgentStatus;
  catalogZone: string;
  mapZone: Zone;
  requiresApprovalFor: string[];
  essential: boolean;
  initialTask: string;
  policyTemplate: Omit<AgentPolicy, "riskLevel" | "riskNotes">;
};

export type AgentCatalog = {
  agents: Agent[];
  layers: AgentLayer[];
  counts: { active: number; planned: number; inactive: number; total: number };
  maestro?: {
    synced: boolean;
    generatedAt: string | null;
    source: string | null;
  };
};

export type AgentStateUpdate = {
  state?: AgentRuntimeState;
  task?: string;
  zone?: Zone;
};

export type AgentPolicyUpdate = Partial<
  Pick<
    AgentPolicy,
    | "sandboxMode"
    | "sandboxScope"
    | "workspaceRoot"
    | "workspaceAccess"
    | "dockerSandbox"
    | "browserSandbox"
    | "prunePolicy"
    | "allowedTools"
    | "deniedTools"
    | "toolProfile"
    | "providerPolicy"
    | "sandboxToolPolicy"
    | "subagentToolPolicy"
    | "elevated"
    | "agentDir"
    | "authProfile"
  >
>;

export type SecurityMatrixRow = {
  id: string;
  name: string;
  status: AgentStatus;
  layer: AgentLayer;
  sandboxMode: SandboxMode;
  workspaceAccess: WorkspaceAccess;
  exec: boolean;
  write: boolean;
  elevated: ElevatedMode;
  riskLevel: RiskLevel;
  riskNotes: string[];
};

export type SecurityMatrix = {
  rows: SecurityMatrixRow[];
  globalAlerts: string[];
  toolFilterChain: string[];
};

export type BarramentoMessage = {
  ts: string;
  de: string;
  para: string;
  tipo: string;
  status?: string;
  mensagem: string;
};

export type BarramentoSnapshot = {
  entries: BarramentoMessage[];
  generatedAt: string | null;
  count: number;
};

export type PdfDropEvent = {
  event_id: string;
  detected_at: string;
  status: string;
  source: string;
  source_pdf: string;
  file_name: string;
  size_bytes: number;
  sha256: string;
  target_agent: string;
  spec: string;
  next_action: string;
  safety?: {
    ocr_executed?: boolean;
    rag_reindexed?: boolean;
    content_copied?: boolean;
    requires_sensitive_data_gate?: boolean;
    requires_human_curation_before_rag?: boolean;
  };
  extraction?: {
    method?: string;
    pages?: number;
    chars?: number;
    output_gitignored?: string;
    rag_reindexed?: boolean;
  };
};

export type StirlingProbeStatus =
  | "online"
  | "auth_required"
  | "offline"
  | "unknown";

export type PdfPipelineSnapshot = {
  scannedAt: string;
  dropFolder: string;
  eventsFolder: string;
  pendingPdfCount: number;
  eventCount: number;
  events: PdfDropEvent[];
  stirling: {
    url: string;
    status: StirlingProbeStatus;
    detail: string;
  };
  blockers: string[];
  specPath: string;
};

export type WsMessage =
  | { type: "snapshot"; agents: Agent[] }
  | { type: "agent_updated"; agent: Agent }
  | { type: "security_matrix"; matrix: SecurityMatrix }
  | { type: "catalog"; catalog: AgentCatalog }
  | { type: "event_log"; entry: EventLogEntry }
  | { type: "event_log_snapshot"; entries: EventLogEntry[] }
  | { type: "barramento_snapshot"; barramento: BarramentoSnapshot }
  | { type: "pdf_pipeline_snapshot"; pipeline: PdfPipelineSnapshot }
  | { type: "pietra_inbox_snapshot"; inbox: PietraInboxSnapshot }
  | { type: "intake_dispatch_snapshot"; dispatch: IntakeDispatchSnapshot }
  | { type: "whatsapp_jobs"; jobs: WhatsAppJob[] };

export type {
  PietraRisco,
  PietraCartao,
  PietraResumo,
  PietraPersona,
  PietraSession,
  PietraStateJson,
  PietraUiAction,
  PietraCartaoUi,
  PietraInboxSnapshot,
} from "./pietraInbox/types.js";

export type {
  IntakeCard,
  IntakeQueueJson,
  IntakeDispatchSnapshot,
  IntakeActionResult,
  CoordenacaoSnapshot,
} from "./intakeDispatch/types.js";

export type { EventLogEntry, WhatsAppJob };
