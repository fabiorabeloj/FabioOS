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

export type AgentLayer = (typeof AGENT_LAYERS)[number];

export const AGENT_STATUSES = ["active", "inactive", "planned"] as const;
export type AgentStatus = (typeof AGENT_STATUSES)[number];

export const ZONES = [
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

export type Agent = {
  id: string;
  name: string;
  layer: AgentLayer;
  status: AgentStatus;
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

export type WsMessage =
  | { type: "snapshot"; agents: Agent[] }
  | { type: "agent_updated"; agent: Agent }
  | { type: "security_matrix"; matrix: SecurityMatrix }
  | { type: "catalog"; catalog: AgentCatalog };
