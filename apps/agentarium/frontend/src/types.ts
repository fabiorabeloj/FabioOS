import type { AgentVisualClass } from "./agentVisualClasses";

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
  | "Personal WhatsApp"
  | "Message Intake"
  | "Draft Reply"
  | "Awaiting Fabio"
  | "Approved"
  | "Sent"
  | "Blocked"
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

export type MaestroRawStatus = "ativo" | "planejado" | "gated";

export type Agent = {
  id: string;
  name: string;
  layer: AgentLayer;
  status: AgentStatus;
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

export type EventLogEntry = {
  id: string;
  timestamp: string;
  channel: "WHATSAPP" | "SYSTEM" | "AGENT" | "SIM";
  agentId?: string;
  jobId?: string;
  source?: string;
  fromZone?: string;
  toZone?: string;
  message: string;
  maskedPhone?: string;
  approvalState?: string;
};

export type WhatsAppMessageCategory =
  | "family"
  | "school"
  | "work"
  | "friend"
  | "finance"
  | "service"
  | "unknown"
  | "sensitive";

export type WhatsAppApprovalState =
  | "draft_only"
  | "awaiting_human"
  | "approved"
  | "sent"
  | "blocked";

export type WhatsAppJob = {
  jobId: string;
  messageId: string;
  conversationId: string;
  contactName: string;
  fromMasked: string;
  direction: "incoming" | "outgoing";
  textPreview: string;
  category: WhatsAppMessageCategory;
  urgency: string;
  approvalState: WhatsAppApprovalState;
  agentId: string;
  channel: "personal" | "school";
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

export type PietraRisco = "baixo" | "medio" | "alto" | "critico";

export type PietraResumo = {
  total: number;
  por_risco: Partial<Record<PietraRisco, number>>;
  sensiveis: number;
  pendentes: number;
};

export type PietraPersona = {
  nome_bot?: string;
  saudacao?: string;
  tom?: string;
  horario_atendimento?: string;
  fora_horario?: string;
  fallback?: string;
  encerramento?: string;
  handoff?: string;
};

export type PietraSession = {
  tenant: string;
  remetente: string;
  categoria: string | null;
  slots: Record<string, string>;
  aguardando_slot?: string | null;
  fallback?: number;
  estado: string;
  primeiro_texto?: string | null;
  historico: { de: string; txt: string }[];
  criado: string;
  atualizado?: string;
};

export type PietraCartao = {
  id: string;
  tenant: string;
  vertical: string;
  ts: string;
  remetente: string;
  midia?: string;
  categoria: string;
  setor: string;
  risco: PietraRisco;
  prioridade: string;
  acao: string;
  bloqueado: boolean;
  resposta_sugerida: string | null;
  texto: string;
  slots?: Record<string, string>;
};

export type PietraUiAction = "responder" | "encaminhar" | "pedir_dados" | "arquivar";

export type PietraCartaoUi = {
  action: PietraUiAction;
  at: string;
  note?: string;
};

export type PietraInboxSnapshot = {
  scannedAt: string;
  generatedAt: string | null;
  source: string | null;
  tenant: string;
  vertical: string;
  specPath: string;
  statePath: string;
  coresRisco: Record<PietraRisco, string>;
  acoes: string[];
  resumo: PietraResumo;
  cards: PietraCartao[];
  persona: PietraPersona;
  sessions: PietraSession[];
  uiState: Record<string, PietraCartaoUi>;
  fallbackMode: boolean;
};

export type IntakeExtracao = {
  serie: string | null;
  tema: string | null;
  prazo: string | null;
  produto: string | null;
  confianca: number;
};

export type IntakeCard = {
  id: string;
  source: string;
  received_at: string;
  sender: string;
  subject: string;
  raw_content_ref: string;
  summary: string;
  domain: string;
  sensitivity: string;
  urgency: string;
  suggested_agent: string;
  suggested_action: string;
  alerta: boolean;
  requires_human_approval: boolean;
  rag_permitido: boolean;
  status: string;
  log_ref: string;
  nota_ref?: string;
  extracao?: IntakeExtracao;
};

export type IntakeQueueJson = {
  generated_at: string;
  gerado_por: string;
  contrato: string;
  resumo: { total: number; aguardando_fabio: number; sensiveis: number };
  cores_status: Record<string, string>;
  fila: IntakeCard[];
};

export type CoordenacaoSnapshot = {
  gerado_em: string;
  barramento: { total: number; abertas: number };
  velocidade: Record<string, string>;
  pendentes_entre_agentes: Array<{
    ts: string;
    de: string;
    para: string;
    tipo: string;
    status: string;
    mensagem: string;
  }>;
  fila_aguardando_fabio: Array<{
    id: string;
    domain: string;
    sensitivity: string;
    urgency: string;
    action: string;
  }>;
  frentes_ativas: Array<{ frente: string; dono: string; estado: string }>;
};

export type IntakeDispatchSnapshot = {
  scannedAt: string;
  sourcePath: string;
  fallbackMode: boolean;
  specPath: string;
  queue: IntakeQueueJson;
  pending: IntakeCard[];
  coordenacao: CoordenacaoSnapshot | null;
  coordenacaoError?: string;
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

export const RAW_STATUS_LABELS: Record<MaestroRawStatus, string> = {
  ativo: "ATIVO",
  planejado: "PLANEJADO",
  gated: "GATED",
};

export const ZONES: Zone[] = [
  "Personal WhatsApp",
  "Message Intake",
  "Draft Reply",
  "Awaiting Fabio",
  "Approved",
  "Sent",
  "Blocked",
  "Classificação",
  "Inbox",
  "Obsidian",
  "WhatsApp",
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
  "Personal WhatsApp": { x: 1, y: 2, w: 11, h: 11, color: "#15803d" },
  "Message Intake": { x: 13, y: 2, w: 11, h: 11, color: "#0d9488" },
  "Draft Reply": { x: 25, y: 2, w: 11, h: 11, color: "#0891b2" },
  "Awaiting Fabio": { x: 37, y: 2, w: 11, h: 11, color: "#ca8a04" },
  Approved: { x: 49, y: 2, w: 9, h: 11, color: "#65a30d" },
  Sent: { x: 59, y: 2, w: 9, h: 11, color: "#22c55e" },
  Blocked: { x: 69, y: 2, w: 9, h: 11, color: "#dc2626" },
  Classificação: { x: 1, y: 15, w: 14, h: 13, color: "#8b5cf6" },
  Inbox: { x: 16, y: 15, w: 14, h: 13, color: "#6366f1" },
  Obsidian: { x: 31, y: 15, w: 14, h: 13, color: "#a78bfa" },
  WhatsApp: { x: 46, y: 15, w: 14, h: 13, color: "#2563eb" },
  GitHub: { x: 61, y: 15, w: 14, h: 13, color: "#64748b" },
  n8n: { x: 76, y: 15, w: 14, h: 13, color: "#f97316" },
  RAG: { x: 1, y: 30, w: 14, h: 13, color: "#06b6d4" },
  "Aprovação Humana": { x: 16, y: 30, w: 14, h: 13, color: "#eab308" },
  Concluído: { x: 31, y: 30, w: 28, h: 13, color: "#22c55e" },
  Erro: { x: 61, y: 30, w: 14, h: 13, color: "#ef4444" },
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

export const AGENT_SHORT_NAMES: Record<string, string> = {
  megatron: "MEGATRON",
  hermes: "HERMES",
  pietra: "PIETRA",
  arquivista: "ARQUIV",
  codex: "CODEX",
  pesquisador: "PESQ",
  supervisor: "SUPER",
  guardiao: "GUARD",
  roteador: "ROTA",
  memoria: "MEM",
};

export { AGENT_VISUAL_CLASSES, getVisualClass } from "./agentVisualClasses";
export type { AgentVisualClass };

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

export function originBadge(agent: Agent): string {
  if (agent.status === "planned") return "PLAN";
  if (agent.lastEventSource === "sim") return "SIM";
  if (agent.lastEventSource === "real") return "REAL";
  return "IDLE";
}
