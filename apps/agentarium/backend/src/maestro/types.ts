export type MaestroRawStatus = "ativo" | "planejado" | "gated";

export type MaestroAgentJson = {
  id: string;
  name: string;
  layer: string;
  status: "active" | "planned";
  rawStatus: MaestroRawStatus;
  role: string;
  capabilities: string[];
};

export type MaestroBarramentoEntry = {
  ts: string;
  de: string;
  para: string;
  tipo: string;
  status?: string;
  mensagem: string;
};

export type MaestroStateJson = {
  generatedAt: string;
  source: string;
  agents: MaestroAgentJson[];
  counts?: { active: number; planned: number; total: number };
  barramento: MaestroBarramentoEntry[];
};

export type MaestroSyncStatus = {
  ok: boolean;
  path: string;
  generatedAt: string | null;
  source: string | null;
  agentCount: number;
  activeCount: number;
  barramentoCount: number;
  error?: string;
};
