import { buildInitialActiveAgents } from "../agents/fabioAgents.js";

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

/** @deprecated policies live in fabioAgents.ts */
export function buildInitialAgents() {
  return buildInitialActiveAgents();
}
