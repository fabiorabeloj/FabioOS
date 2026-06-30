import type { Agent, AgentPolicy, AgentRuntimeState, Zone } from "../types.js";

const now = () => new Date().toISOString();

function basePolicy(
  partial: Omit<AgentPolicy, "riskLevel" | "riskNotes">,
): AgentPolicy {
  return { ...partial, riskLevel: "safe", riskNotes: [] };
}

export const DEFAULT_POLICIES: Record<string, Omit<AgentPolicy, "riskLevel" | "riskNotes">> = {
  pietra: {
    sandboxMode: "all",
    sandboxScope: "agent",
    workspaceRoot: "~/.openclaw/sandbox/pietra",
    workspaceAccess: "ro",
    dockerSandbox: "enabled",
    browserSandbox: "disabled",
    prunePolicy: "on-idle",
    allowedTools: ["read", "sessions_send", "sessions_history"],
    deniedTools: ["exec", "write", "edit", "apply_patch", "process", "browser", "gateway"],
    toolProfile: "minimal",
    providerPolicy: "inherit",
    sandboxToolPolicy: "strict",
    subagentToolPolicy: "deny-all",
    elevated: "disabled",
    agentDir: "~/.openclaw/agents/pietra/agent",
    authProfile: "local",
  },
  arquivista: {
    sandboxMode: "all",
    sandboxScope: "agent",
    workspaceRoot: "60_Sistemas/OpenClaw/ponte",
    workspaceAccess: "rw",
    dockerSandbox: "enabled",
    browserSandbox: "disabled",
    prunePolicy: "on-idle",
    allowedTools: ["read", "write", "edit"],
    deniedTools: ["exec", "process", "browser", "gateway"],
    toolProfile: "coding",
    providerPolicy: "inherit",
    sandboxToolPolicy: "filesystem-mutation",
    subagentToolPolicy: "deny-all",
    elevated: "disabled",
    agentDir: "~/.openclaw/agents/arquivista/agent",
    authProfile: "local",
  },
  codex: {
    sandboxMode: "all",
    sandboxScope: "agent",
    workspaceRoot: "c:/Users/user/Desktop/FabioOs/FabioOs",
    workspaceAccess: "rw",
    dockerSandbox: "enabled",
    browserSandbox: "disabled",
    prunePolicy: "manual",
    allowedTools: ["read", "write", "edit", "apply_patch", "exec", "process"],
    deniedTools: ["browser", "gateway"],
    toolProfile: "coding",
    providerPolicy: "openrouter-minimal",
    sandboxToolPolicy: "shell-restricted",
    subagentToolPolicy: "inherit",
    elevated: "restricted",
    agentDir: "~/.openclaw/agents/codex/agent",
    authProfile: "local",
  },
  pesquisador: {
    sandboxMode: "all",
    sandboxScope: "agent",
    workspaceRoot: "60_Sistemas/RAG",
    workspaceAccess: "ro",
    dockerSandbox: "disabled",
    browserSandbox: "isolated",
    prunePolicy: "on-idle",
    allowedTools: ["read", "browser"],
    deniedTools: ["exec", "write", "edit", "apply_patch", "process"],
    toolProfile: "minimal",
    providerPolicy: "inherit",
    sandboxToolPolicy: "read-only",
    subagentToolPolicy: "deny-all",
    elevated: "disabled",
    agentDir: "~/.openclaw/agents/pesquisador/agent",
    authProfile: "local",
  },
  supervisor: {
    sandboxMode: "off",
    sandboxScope: "global",
    workspaceRoot: "60_Sistemas/FabioOS",
    workspaceAccess: "ro",
    dockerSandbox: "disabled",
    browserSandbox: "disabled",
    prunePolicy: "never",
    allowedTools: ["read", "sessions_list", "sessions_history", "session_status"],
    deniedTools: ["write", "edit", "apply_patch", "exec", "process"],
    toolProfile: "audit",
    providerPolicy: "inherit",
    sandboxToolPolicy: "n/a",
    subagentToolPolicy: "deny-all",
    elevated: "disabled",
    agentDir: "~/.openclaw/agents/supervisor/agent",
    authProfile: "local",
  },
};

export const TOOL_FILTER_CHAIN = [
  "1. Tool profile",
  "2. Provider tool profile",
  "3. Global tool policy",
  "4. Provider tool policy (runtime)",
  "5. Agent-specific tool policy",
  "6. Agent provider policy",
  "7. Sandbox tool policy",
  "8. Subagent tool policy",
];

export function buildInitialAgents(): Agent[] {
  const seeds: Array<{
    id: string;
    name: string;
    role: string;
    state: AgentRuntimeState;
    task: string;
    zone: Zone;
  }> = [
    {
      id: "pietra",
      name: "Pietra",
      role: "Atendimento escolar, mensagens de responsáveis e triagem inicial",
      state: "idle",
      task: "Aguardando mensagens",
      zone: "WhatsApp",
    },
    {
      id: "arquivista",
      name: "Arquivista",
      role: "Captura, limpeza e arquivamento de conhecimento no Obsidian",
      state: "idle",
      task: "Monitorando inbox",
      zone: "Inbox",
    },
    {
      id: "codex",
      name: "Codex",
      role: "Programação, GitHub, manutenção técnica e refatoração",
      state: "idle",
      task: "Repositório estável",
      zone: "GitHub",
    },
    {
      id: "pesquisador",
      name: "Pesquisador",
      role: "Pesquisa, RAG, banco vetorial e organização conceitual",
      state: "idle",
      task: "Índice vetorial pronto",
      zone: "RAG",
    },
    {
      id: "supervisor",
      name: "Supervisor",
      role: "Validação humana, segurança, revisão de risco e aprovação final",
      state: "idle",
      task: "Fila de aprovações vazia",
      zone: "Aprovação Humana",
    },
  ];

  return seeds.map((s) => ({
    ...s,
    updatedAt: now(),
    policy: basePolicy(DEFAULT_POLICIES[s.id]!),
  }));
}
