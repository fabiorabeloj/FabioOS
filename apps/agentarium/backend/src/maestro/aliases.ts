/** IDs taticos do Agentarium/WhatsApp → IDs do roster Maestro. */
export const TACTICAL_AGENT_ALIASES: Record<string, string> = {
  hermes: "atendente",
  pietra: "documentalista",
  codex: "programador",
  megatron: "interface",
  supervisor: "barramento",
  guardiao: "barramento",
  roteador: "automacao",
  memoria: "reasoningbank",
};

export function resolveMaestroAgentId(id: string): string {
  return TACTICAL_AGENT_ALIASES[id] ?? id;
}

/** Visual class lookup: Maestro id → id tatico com pixel art. */
export const MAESTRO_VISUAL_ALIASES: Record<string, string> = {
  atendente: "hermes",
  documentalista: "pietra",
  programador: "codex",
  interface: "megatron",
  barramento: "supervisor",
  automacao: "roteador",
  reasoningbank: "memoria",
  arquivista: "arquivista",
  pesquisador: "pesquisador",
};
