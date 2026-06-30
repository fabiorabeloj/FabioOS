export type AgentRuntimeState =
  | "idle"
  | "thinking"
  | "executing"
  | "waiting_approval"
  | "done"
  | "error";

export type AgentLayer =
  | "command"
  | "security"
  | "technical"
  | "knowledge"
  | "school"
  | "finance"
  | "interface"
  | "personal";

export type AgentStatus = "active" | "inactive" | "planned";

export type Zone =
  | "WhatsApp"
  | "Inbox"
  | "Classificação"
  | "Obsidian"
  | "GitHub"
  | "n8n"
  | "RAG"
  | "Aprovação Humana"
  | "Concluído"
  | "Erro";

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

export type AgentCatalog = {
  agents: Agent[];
  layers: AgentLayer[];
  counts: { active: number; planned: number; inactive: number; total: number };
};

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

export const LAYER_LABELS: Record<AgentLayer, string> = {
  command: "Comando",
  security: "Seguranca",
  technical: "Tecnico",
  knowledge: "Conhecimento",
  school: "Escola",
  finance: "Financeiro",
  interface: "Interface",
  personal: "Pessoal",
};

export const STATUS_LABELS: Record<AgentStatus, string> = {
  active: "ATIVO",
  inactive: "INATIVO",
  planned: "PLANEJADO",
};

export const ZONES: Zone[] = [
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
];

export const ZONE_LAYOUT: Record<
  Zone,
  { x: number; y: number; w: number; h: number; color: string }
> = {
  WhatsApp: { x: 2, y: 4, w: 18, h: 22, color: "#25D366" },
  Inbox: { x: 22, y: 4, w: 18, h: 22, color: "#6366f1" },
  Classificação: { x: 42, y: 4, w: 18, h: 22, color: "#8b5cf6" },
  Obsidian: { x: 62, y: 4, w: 18, h: 22, color: "#a78bfa" },
  GitHub: { x: 2, y: 30, w: 18, h: 22, color: "#64748b" },
  n8n: { x: 22, y: 30, w: 18, h: 22, color: "#f97316" },
  RAG: { x: 42, y: 30, w: 18, h: 22, color: "#06b6d4" },
  "Aprovação Humana": { x: 62, y: 30, w: 18, h: 22, color: "#eab308" },
  Concluído: { x: 22, y: 56, w: 36, h: 22, color: "#22c55e" },
  Erro: { x: 62, y: 56, w: 18, h: 22, color: "#ef4444" },
};

export const STATE_LABELS: Record<AgentRuntimeState, string> = {
  idle: "Ocioso",
  thinking: "Pensando",
  executing: "Executando",
  waiting_approval: "Aguardando aprovacao",
  done: "Concluido",
  error: "Erro",
};

export const RISK_LABELS: Record<RiskLevel, string> = {
  safe: "SAFE",
  warning: "WARN",
  danger: "DANGER",
};

export const AGENT_EMOJI: Record<string, string> = {
  pietra: "🎓",
  arquivista: "📚",
  codex: "⚙️",
  pesquisador: "🔍",
  supervisor: "🛡️",
};

export function hasExec(policy: AgentPolicy): boolean {
  return (
    policy.allowedTools.includes("exec") && !policy.deniedTools.includes("exec")
  );
}

export function hasWrite(policy: AgentPolicy): boolean {
  return policy.allowedTools.some(
    (t) =>
      ["write", "edit", "apply_patch"].includes(t) &&
      !policy.deniedTools.includes(t),
  );
}
