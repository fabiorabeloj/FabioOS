export type IntakeSensitivity =
  | "public"
  | "internal"
  | "private"
  | "restricted"
  | "no_rag"
  | "forbidden_external";

export type IntakeStatus =
  | "captured"
  | "classified"
  | "waiting_approval"
  | "approved"
  | "executing"
  | "executed"
  | "archived"
  | "blocked"
  | "failed";

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
  sensitivity: IntakeSensitivity | string;
  urgency: string;
  suggested_agent: string;
  suggested_action: string;
  alerta: boolean;
  requires_human_approval: boolean;
  rag_permitido: boolean;
  status: IntakeStatus | string;
  log_ref: string;
  nota_ref?: string;
  extracao?: IntakeExtracao;
};

export type IntakeQueueJson = {
  generated_at: string;
  gerado_por: string;
  contrato: string;
  resumo: {
    total: number;
    aguardando_fabio: number;
    sensiveis: number;
  };
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

export type IntakeActionResult = {
  ok: boolean;
  message: string;
  blocked?: boolean;
  notaRef?: string;
  item?: IntakeCard;
};
