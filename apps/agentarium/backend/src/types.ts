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
  role: string;
  state: AgentRuntimeState;
  task: string;
  zone: Zone;
  updatedAt: string;
  policy: AgentPolicy;
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
  | { type: "security_matrix"; matrix: SecurityMatrix };
