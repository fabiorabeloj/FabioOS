import type { AgentLayer, Zone } from "./types";

export type AgentVisualClass = {
  visualClass: string;
  operationalRole: string;
  primaryLane: string;
  homeZone: Zone;
  signatureItem: string;
  colorIdentity: string;
  approvalRequirement: string;
};

export const AGENT_VISUAL_CLASSES: Record<string, AgentVisualClass> = {
  megatron: {
    visualClass: "Command Core / Overlord Console",
    operationalRole: "Orquestracao central e roteamento tactico",
    primaryLane: "Command",
    homeZone: "Classificação",
    signatureItem: "nucleo luminoso / antena",
    colorIdentity: "vermelho escuro / ciano / preto / aco",
    approvalRequirement: "required for destructive or external actions",
  },
  hermes: {
    visualClass: "Personal Messenger / Courier",
    operationalRole: "WhatsApp pessoal, triagem e rascunhos",
    primaryLane: "Personal Intake",
    homeZone: "Personal WhatsApp",
    signatureItem: "envelope / balao de fala",
    colorIdentity: "verde escuro / branco / ciano / preto",
    approvalRequirement: "required before sending",
  },
  pietra: {
    visualClass: "School Liaison / Institutional Messenger",
    operationalRole: "Atendimento escolar institucional",
    primaryLane: "School Intake",
    homeZone: "Classificação",
    signatureItem: "cracha / livro formal",
    colorIdentity: "azul / branco / dourado discreto",
    approvalRequirement: "required for institutional replies",
  },
  arquivista: {
    visualClass: "Archive Keeper / Vault Scribe",
    operationalRole: "Obsidian, arquivos e memoria",
    primaryLane: "Knowledge Intake",
    homeZone: "Inbox",
    signatureItem: "caixa / pergaminho",
    colorIdentity: "marrom / verde musgo / cinza",
    approvalRequirement: "none for read-only archive",
  },
  codex: {
    visualClass: "Terminal Knight / Code Operator",
    operationalRole: "Programacao, GitHub e scripts",
    primaryLane: "Technical Execution",
    homeZone: "GitHub",
    signatureItem: "visor ciano / terminal",
    colorIdentity: "preto / ciano / verde terminal",
    approvalRequirement: "required for exec and push",
  },
  pesquisador: {
    visualClass: "Radar Mage / Vector Scholar",
    operationalRole: "RAG, pesquisa e fontes",
    primaryLane: "Research",
    homeZone: "RAG",
    signatureItem: "lupa / radar / orbe",
    colorIdentity: "roxo / ciano / branco",
    approvalRequirement: "none for read-only research",
  },
  supervisor: {
    visualClass: "Shield Auditor / Human Approval Guard",
    operationalRole: "Aprovacao, bloqueio e auditoria",
    primaryLane: "Human Approval",
    homeZone: "Aprovação Humana",
    signatureItem: "escudo / olho / selo",
    colorIdentity: "aco / vermelho escuro / dourado",
    approvalRequirement: "is the approval gate",
  },
  guardiao: {
    visualClass: "Security Sentinel / Sandbox Warden",
    operationalRole: "Sandbox, permissoes e riscos",
    primaryLane: "Security",
    homeZone: "GitHub",
    signatureItem: "cadeado / grade",
    colorIdentity: "vermelho / cinza / preto / amarelo",
    approvalRequirement: "alerts only — no external send",
  },
  roteador: {
    visualClass: "Signal Router / Switchboard Operator",
    operationalRole: "Classificar mensagens e comandos",
    primaryLane: "Routing",
    homeZone: "Classificação",
    signatureItem: "setas / placas",
    colorIdentity: "laranja / azul / branco",
    approvalRequirement: "none for classification",
  },
  memoria: {
    visualClass: "Memory Crystal / Archive Core",
    operationalRole: "Continuidade e contexto",
    primaryLane: "Memory",
    homeZone: "Obsidian",
    signatureItem: "cristal / no de grafo",
    colorIdentity: "violeta / azul / branco",
    approvalRequirement: "required for state file writes",
  },
};

const MAESTRO_VISUAL_ALIASES: Record<string, string> = {
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

export function getVisualClass(agentId: string): AgentVisualClass | undefined {
  return (
    AGENT_VISUAL_CLASSES[agentId] ??
    AGENT_VISUAL_CLASSES[MAESTRO_VISUAL_ALIASES[agentId] ?? ""]
  );
}

export function homeZoneFor(agentId: string, _layer: AgentLayer): Zone {
  const resolved = MAESTRO_VISUAL_ALIASES[agentId] ?? agentId;
  return AGENT_VISUAL_CLASSES[resolved]?.homeZone ?? "Classificação";
}
