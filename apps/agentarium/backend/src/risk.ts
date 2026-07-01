import type { Agent, AgentPolicy, RiskLevel, SecurityMatrix, SecurityMatrixRow } from "./types.js";
import { TOOL_FILTER_CHAIN } from "./policies/defaultPolicies.js";

const WRITE_TOOLS = new Set(["write", "edit", "apply_patch"]);
const EXEC_TOOLS = new Set(["exec", "process"]);

function toolAllowed(policy: AgentPolicy, tool: string): boolean {
  if (policy.deniedTools.includes(tool)) return false;
  return policy.allowedTools.includes(tool);
}

/** Regras minimas de risco por agente (OpenClaw sandbox/tools). */
export function evaluateAgentRisk(agent: Agent): { riskLevel: RiskLevel; riskNotes: string[] } {
  const { policy } = agent;
  const notes: string[] = [];
  let level: RiskLevel = "safe";

  const bump = (next: RiskLevel, note: string) => {
    notes.push(note);
    const order: RiskLevel[] = ["safe", "warning", "danger"];
    if (order.indexOf(next) > order.indexOf(level)) {
      level = next;
    }
  };

  if (toolAllowed(policy, "exec") && policy.sandboxMode === "off") {
    bump("danger", "Shell execution without sandbox.");
  }

  if (toolAllowed(policy, "process") && policy.workspaceAccess === "rw") {
    bump("warning", "Process control with writable workspace.");
  }

  for (const t of WRITE_TOOLS) {
    if (toolAllowed(policy, t)) {
      bump("warning", "Filesystem mutation enabled.");
      break;
    }
  }

  if (policy.elevated === "enabled") {
    bump("danger", "Elevated mode enabled.");
  }

  if (policy.authProfile === "default-fallback") {
    bump("warning", "Agent is reading through default/main auth profile.");
  }

  if (toolAllowed(policy, "exec") && policy.sandboxMode !== "off") {
    bump("warning", "exec permitted — monitor sandbox strength.");
  }

  if (agent.rawStatus === "gated") {
    bump("warning", "GATED — aguardando segredos/chaves do Fabio.");
  }

  return { riskLevel: level, riskNotes: notes };
}

export function applySharedAgentDirChecks(agents: Agent[]): Agent[] {
  const dirMap = new Map<string, string[]>();
  for (const a of agents) {
    const dir = a.policy.agentDir;
    const list = dirMap.get(dir) ?? [];
    list.push(a.id);
    dirMap.set(dir, list);
  }

  return agents.map((a) => {
    const peers = dirMap.get(a.policy.agentDir) ?? [];
    if (peers.length <= 1) return a;
    const notes = [
      ...a.policy.riskNotes.filter((n) => !n.includes("Shared agentDir")),
      "Shared agentDir detected. OpenClaw recommends unique auth stores per agent.",
    ];
    return {
      ...a,
      policy: {
        ...a.policy,
        riskLevel: "danger" as RiskLevel,
        riskNotes: notes,
      },
    };
  });
}

export function refreshAgentRisk(agent: Agent): Agent {
  const { riskLevel, riskNotes } = evaluateAgentRisk(agent);
  return {
    ...agent,
    policy: { ...agent.policy, riskLevel, riskNotes },
  };
}

export function refreshAllRisks(agents: Agent[]): Agent[] {
  const withRisk = agents.map(refreshAgentRisk);
  return applySharedAgentDirChecks(withRisk);
}

export function buildSecurityMatrix(agents: Agent[]): SecurityMatrix {
  const refreshed = refreshAllRisks(agents);
  const globalAlerts: string[] = [];

  const dirCounts = new Map<string, number>();
  for (const a of refreshed) {
    dirCounts.set(a.policy.agentDir, (dirCounts.get(a.policy.agentDir) ?? 0) + 1);
  }
  for (const [dir, count] of dirCounts) {
    if (count > 1) {
      globalAlerts.push(`Shared agentDir: ${dir} (${count} agents)`);
    }
  }

  const rows: SecurityMatrixRow[] = refreshed.map((a) => ({
    id: a.id,
    name: a.name,
    status: a.status,
    layer: a.layer,
    sandboxMode: a.policy.sandboxMode,
    workspaceAccess: a.policy.workspaceAccess,
    exec: toolAllowed(a.policy, "exec"),
    write:
      toolAllowed(a.policy, "write") ||
      toolAllowed(a.policy, "edit") ||
      toolAllowed(a.policy, "apply_patch"),
    elevated: a.policy.elevated,
    riskLevel: a.policy.riskLevel,
    riskNotes: a.policy.riskNotes,
  }));

  return {
    rows,
    globalAlerts,
    toolFilterChain: TOOL_FILTER_CHAIN,
  };
}
