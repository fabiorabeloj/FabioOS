export type PietraRisco = "baixo" | "medio" | "alto" | "critico";

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

export type PietraStateJson = {
  generatedAt: string;
  source: string;
  tenant: string;
  vertical: string;
  cores_risco: Record<PietraRisco, string>;
  acoes: string[];
  resumo: PietraResumo;
  fila: PietraCartao[];
  persona: PietraPersona;
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
