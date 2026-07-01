import { store } from "../store.js";
import { eventLog } from "../eventLog.js";
import type { AgentRuntimeState, Zone } from "../types.js";

type Step = {
  agentId: string;
  zone: Zone;
  fromZone: Zone;
  state: AgentRuntimeState;
  task: string;
  delayMs: number;
};

export function scheduleAgentUpdates(
  agentUpdates: Step[],
  jobId: string,
  sourceTag: string,
  approvalState: string,
): void {
  for (const step of agentUpdates) {
    const { fromZone, zone } = step;
    setTimeout(() => {
      store.updateWithMeta(step.agentId, {
        state: step.state,
        task: step.task,
        zone: step.zone,
      }, {
        eventSource: "real",
        jobId,
        fromZone,
        toZone: zone,
      });

      eventLog.append({
        channel: "WHATSAPP",
        agentId: step.agentId,
        jobId,
        source: sourceTag,
        fromZone,
        toZone: zone,
        message: `${step.agentId} · ${fromZone} → ${zone}`,
        approvalState,
      });
    }, step.delayMs);
  }
}
