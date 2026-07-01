import Fastify from "fastify";
import cors from "@fastify/cors";
import { store, isValidState, isValidZone } from "./store.js";
import { attachWebSocket, broadcastWs } from "./websocket.js";
import {
  startSimulation,
  stopSimulation,
  simulationStatus,
  simulateError,
} from "./simulator.js";
import type { AgentStateUpdate, AgentPolicyUpdate } from "./types.js";
import { buildSecurityMatrix } from "./risk.js";
import { eventLog } from "./eventLog.js";
import { whatsappJobs } from "./whatsappJobs.js";
import { handlePersonalWhatsAppMessage } from "./whatsapp/personalHandler.js";
import { handleSchoolWhatsAppMessage } from "./whatsapp/schoolMessageHandler.js";
import { getWhatsAppStatus } from "./whatsapp/status.js";
import type { WhatsAppMessageInput } from "./whatsapp/types.js";
import { loadWhatsAppConfig } from "./whatsapp/config.js";
import { channelState } from "./whatsapp/channelState.js";
import { deliverReplyToFabio } from "./whatsapp/fabioReply.js";
import { getVisualClass } from "./agents/agentVisualClasses.js";
import { appendMegatronInbox } from "./hermes/inboxWriter.js";
import { writeTaskFile } from "./megatron/taskWriter.js";
import {
  detectTask,
  parseTaskCommand,
} from "./whatsapp/taskCapture.js";
import {
  initMaestroIntegration,
  getMaestroSyncStatus,
  applyMaestroStateFromFile,
  getBarramentoSnapshot,
} from "./maestro/sync.js";
import { initPdfPipelineIntegration, refreshPdfPipelineSnapshot } from "./pdfPipeline/sync.js";
import {
  initPietraInboxIntegration,
  refreshPietraInboxSnapshot,
  applyPietraCardAction,
  getPietraInboxSnapshot,
} from "./pietraInbox/sync.js";
import type { PietraUiAction } from "./types.js";
import {
  initIntakeDispatchIntegration,
  refreshIntakeDispatchSnapshot,
} from "./intakeDispatch/sync.js";
import {
  approveIntakeItem,
  rejectIntakeItem,
  submitNaturalCommand,
  refreshIntakeQueueFromFlow,
  importGmailFakeDryRun,
} from "./intakeDispatch/actions.js";
import { getMegatronChatStatus, handleMegatronChat } from "./megatron/chatHandler.js";

const PORT = Number(process.env.PORT ?? 3847);
const HOST = process.env.HOST ?? "127.0.0.1";
const AUTO_SIM = process.env.AGENTARIUM_AUTO_SIM === "true";

export async function buildApp() {
  const app = Fastify({ logger: true });

  await app.register(cors, { origin: true });

  app.addHook("onSend", async (_request, reply, payload) => {
    const ct = reply.getHeader("content-type");
    if (
      typeof ct === "string" &&
      ct.includes("application/json") &&
      !ct.includes("charset")
    ) {
      reply.header("content-type", "application/json; charset=utf-8");
    }
    return payload;
  });

  app.get("/health", async () => ({
    ok: true,
    service: "agentarium-backend",
    product: "MEGATRON Tactical Agentarium",
    version: "1.0.0",
    maestro: getMaestroSyncStatus(),
  }));

  app.get("/agents", async () => ({
    agents: store.listActive(),
  }));

  app.get("/catalog", async () => store.catalog());

  app.get("/agents/:id", async (req, reply) => {
    const { id } = req.params as { id: string };
    const agent = store.get(id);
    if (!agent) {
      return reply.status(404).send({ error: "Agent not found" });
    }
    return { agent, visualClass: getVisualClass(id) ?? null };
  });

  app.get("/agents/:id/class", async (req, reply) => {
    const { id } = req.params as { id: string };
    const visualClass = getVisualClass(id);
    if (!visualClass) {
      return reply.status(404).send({ error: "Visual class not found" });
    }
    return { visualClass };
  });

  app.get("/security/matrix", async () => buildSecurityMatrix(store.catalogAgents()));

  app.get("/events/log", async (req) => {
    const limit = Number((req.query as { limit?: string }).limit ?? 50);
    return { entries: eventLog.list(limit) };
  });

  app.get("/integrations/maestro/status", async () => ({
    ...getMaestroSyncStatus(),
    maestroMode: store.isMaestroMode(),
    catalog: store.isMaestroMode() ? store.catalog().counts : null,
  }));

  app.get("/integrations/maestro/barramento", async () => getBarramentoSnapshot());

  app.get("/integrations/pdf-pipeline/status", async () => refreshPdfPipelineSnapshot());

  app.get("/integrations/pietra-inbox/status", async (req) => {
    const q = req.query as { tenant?: string };
    return refreshPietraInboxSnapshot(q.tenant);
  });

  app.post("/integrations/pietra-inbox/cards/:id/action", async (req, reply) => {
    const { id } = req.params as { id: string };
    const body = req.body as { action?: PietraUiAction; note?: string };
    const valid: PietraUiAction[] = ["responder", "encaminhar", "pedir_dados", "arquivar"];
    if (!body?.action || !valid.includes(body.action)) {
      return reply.status(400).send({ error: "action invalida" });
    }
    const snapshot = getPietraInboxSnapshot();
    const card = snapshot?.cards.find((c) => c.id === id);
    if (!card) {
      return reply.status(404).send({ error: "cartao nao encontrado" });
    }
    if (card.bloqueado && body.action === "responder") {
      return reply.status(403).send({ error: "cartao bloqueado — nao responder automaticamente" });
    }
    const inbox = applyPietraCardAction(id, body.action, body.note);
    broadcastWs({ type: "pietra_inbox_snapshot", inbox });
    eventLog.append({
      channel: "SYSTEM",
      source: "pietra-inbox-ui",
      agentId: "documentalista",
      message: `[PIETRA] ${body.action} em ${id} (${card.categoria}/${card.risco})`,
    });
    return { ok: true, inbox };
  });

  app.get("/integrations/megatron/chat/status", async () => getMegatronChatStatus());

  app.post("/integrations/megatron/chat", async (req, reply) => {
    const body = req.body as { message?: string };
    if (!body?.message?.trim()) {
      return reply.status(400).send({ ok: false, error: "message required" });
    }
    const result = await handleMegatronChat(body.message);
    broadcastWs({
      type: "event_log",
      entry: eventLog.list(1)[0],
    });
    if (result.intake?.ok) {
      const dispatch = await refreshIntakeDispatchSnapshot();
      broadcastWs({ type: "intake_dispatch_snapshot", dispatch });
    }
    return result;
  });

  app.get("/integrations/intake-dispatch/status", async () => refreshIntakeDispatchSnapshot());

  app.post("/integrations/intake-dispatch/refresh-flow", async (_req, reply) => {
    const result = await refreshIntakeQueueFromFlow();
    const dispatch = await refreshIntakeDispatchSnapshot();
    broadcastWs({ type: "intake_dispatch_snapshot", dispatch });
    if (!result.ok) return reply.status(500).send(result);
    eventLog.append({
      channel: "SYSTEM",
      source: "intake-dispatch",
      agentId: "arquivista",
      message: `[INTAKE] ${result.message}`,
    });
    return { ...result, dispatch };
  });

  app.post("/integrations/intake-dispatch/command", async (req, reply) => {
    const body = req.body as { text?: string };
    if (!body?.text?.trim()) {
      return reply.status(400).send({ error: "text required" });
    }
    const result = await submitNaturalCommand(body.text);
    const dispatch = await refreshIntakeDispatchSnapshot();
    broadcastWs({ type: "intake_dispatch_snapshot", dispatch });
    eventLog.append({
      channel: "SYSTEM",
      source: "intake-command",
      agentId: "megatron",
      message: `[INTAKE] comando: ${body.text.slice(0, 80)}`,
    });
    if (!result.ok) return reply.status(400).send(result);
    return { ...result, dispatch };
  });

  app.post("/integrations/intake-dispatch/import-gmail-fake", async (_req, reply) => {
    const result = await importGmailFakeDryRun();
    const dispatch = await refreshIntakeDispatchSnapshot();
    broadcastWs({ type: "intake_dispatch_snapshot", dispatch });
    eventLog.append({
      channel: "SYSTEM",
      source: "intake-gmail-fake",
      agentId: "megatron",
      message: `[INTAKE] ${result.message}`,
    });
    if (!result.ok) return reply.status(400).send(result);
    return { ...result, dispatch };
  });

  app.post("/integrations/intake-dispatch/cards/:id/approve", async (req, reply) => {
    const { id } = req.params as { id: string };
    const result = await approveIntakeItem(id);
    const dispatch = await refreshIntakeDispatchSnapshot();
    broadcastWs({ type: "intake_dispatch_snapshot", dispatch });
    eventLog.append({
      channel: "SYSTEM",
      source: "intake-approve",
      agentId: "arquivista",
      message: result.blocked
        ? `[INTAKE] bloqueado sensivel ${id}`
        : `[INTAKE] aprovado ${id}${result.notaRef ? ` → ${result.notaRef}` : ""}`,
    });
    if (!result.ok) return reply.status(400).send(result);
    return { ...result, dispatch };
  });

  app.post("/integrations/intake-dispatch/cards/:id/reject", async (req, reply) => {
    const { id } = req.params as { id: string };
    const result = await rejectIntakeItem(id);
    const dispatch = await refreshIntakeDispatchSnapshot();
    broadcastWs({ type: "intake_dispatch_snapshot", dispatch });
    eventLog.append({
      channel: "SYSTEM",
      source: "intake-reject",
      agentId: "megatron",
      message: `[INTAKE] rejeitado ${id}`,
    });
    if (!result.ok) return reply.status(400).send(result);
    return { ...result, dispatch };
  });

  app.post("/integrations/maestro/sync", async () => {
    const status = applyMaestroStateFromFile();
    if (status.ok) {
      broadcastWs({ type: "catalog", catalog: store.catalog() });
      broadcastWs({ type: "snapshot", agents: store.listActive() });
      broadcastWs({
        type: "security_matrix",
        matrix: buildSecurityMatrix(store.catalogAgents()),
      });
      broadcastWs({ type: "event_log_snapshot", entries: eventLog.list(200) });
      broadcastWs({ type: "barramento_snapshot", barramento: getBarramentoSnapshot() });
    }
    return status;
  });

  app.get("/integrations/whatsapp/status", async () => getWhatsAppStatus());

  app.get("/integrations/whatsapp/jobs", async (req) => {
    const q = req.query as { channel?: string; limit?: string };
    const limit = Number(q.limit ?? 30);
    if (q.channel === "personal" || q.channel === "school") {
      return { jobs: whatsappJobs.listByChannel(q.channel, limit) };
    }
    return { jobs: whatsappJobs.list(limit) };
  });

  app.get("/integrations/whatsapp/config", async () => ({
    config: loadWhatsAppConfig(),
  }));

  async function processPersonal(body: WhatsAppMessageInput) {
    const config = loadWhatsAppConfig();
    let input: WhatsAppMessageInput = {
      ...body,
      channel: "personal",
      direction: body.direction ?? "incoming",
      timestamp: body.timestamp ?? new Date().toISOString(),
      source: body.source ?? "whatsapp",
      provider: body.provider ?? "evolution_api",
    };

    const taskCmd = parseTaskCommand(input.text);
    if (taskCmd) {
      input = { ...input, text: taskCmd.prompt };
    }

    const result = handlePersonalWhatsAppMessage(input);

    let taskFile: string | undefined;
    const task = detectTask(input, config.fabioWhatsAppNumber, taskCmd?.prompt);

    if (task && !result.blocked) {
      try {
        taskFile = writeTaskFile(input, result.jobId, task);
        whatsappJobs.update(result.jobId, {
          category: "task",
          suggestedReply: task.prompt,
        });
        store.updateWithMeta(task.suggestedAgent, {
          state: "executing",
          task: task.title,
          zone: "Message Intake",
        }, { eventSource: "real", jobId: result.jobId });
        eventLog.append({
          channel: "WHATSAPP",
          agentId: "canal-wpp-pessoal",
          jobId: result.jobId,
          source: "TASK",
          message: `[TASK] Capturada -> ${task.suggestedAgent}: ${task.title}`,
          approvalState: "draft_only",
        });
      } catch (err) {
        eventLog.append({
          channel: "WHATSAPP",
          agentId: "canal-wpp-pessoal",
          jobId: result.jobId,
          source: "ERROR",
          message: `[ERROR] Falha ao gravar tarefa: ${err instanceof Error ? err.message : String(err)}`,
        });
      }
    } else if (result.analysis && !result.blocked && !result.isCommand) {
      try {
        taskFile = appendMegatronInbox(input, result.jobId, result.analysis);
      } catch {
        /* ignore */
      }
    }

    const delivery = await deliverReplyToFabio(input, result, { task, taskFile });

    const replyNote = delivery.sent
      ? task
        ? "Tarefa capturada e confirmacao enviada no WhatsApp."
        : "Resposta enviada para Fabio no WhatsApp."
      : delivery.error
        ? `Resposta nao enviada: ${delivery.error}`
        : "Resposta nao enviada (WHATSAPP_REPLY_TO_FABIO=false).";

    const replyText = delivery.text?.replace(/^\[MEGATRON\]\n?/, "") ?? result.replyToFabio;
    const cursorHint = taskFile
      ? `Leia ${taskFile.includes("Tarefas_WPP") ? `00_Inbox/Processar/Tarefas_WPP/${result.jobId}.md` : "00_Inbox/Processar/Megatron_Canal_Fabio.md"} e execute.`
      : "Leia 00_Inbox/Processar/Megatron_Canal_Fabio.md no Cursor";

    return {
      ...result,
      message: delivery.sent ? replyNote : result.message,
      replyToFabio: replyText,
      sentToFabio: delivery.sent,
      deliveryError: delivery.error,
      chatSource: delivery.chatSource,
      taskCaptured: !!task,
      taskFile,
      suggestedAgent: task?.suggestedAgent,
      cursorHint,
    };
  }

  app.post("/integrations/whatsapp/personal/message", async (req, reply) => {
    const body = req.body as WhatsAppMessageInput;
    if (!body?.messageId || !body?.from || !body?.text) {
      return reply.status(400).send({ error: "messageId, from and text required" });
    }
    return reply.send(await processPersonal(body));
  });

  app.post("/integrations/whatsapp/school/message", async (req, reply) => {
    const body = req.body as WhatsAppMessageInput;
    if (!body?.messageId || !body?.from || !body?.text) {
      return reply.status(400).send({ error: "messageId, from and text required" });
    }
    const result = handleSchoolWhatsAppMessage({
      ...body,
      channel: "school",
      direction: body.direction ?? "incoming",
      timestamp: body.timestamp ?? new Date().toISOString(),
      source: body.source ?? "whatsapp",
      provider: body.provider ?? "evolution_api",
    });
    return reply.send(result);
  });

  /** Legado — roteia para personal */
  app.post("/integrations/whatsapp/message", async (req, reply) => {
    const body = req.body as WhatsAppMessageInput;
    if (!body?.messageId || !body?.from || !body?.text) {
      return reply.status(400).send({ error: "messageId, from and text required" });
    }
    return reply.send(await processPersonal(body));
  });

  /** Marcar canal Evolution como conectado (chamar apos QR scan) */
  app.post("/integrations/whatsapp/connected", async (req) => {
    const body = req.body as { channel?: "personal" | "school" };
    const ch = body?.channel ?? "personal";
    channelState.setConnected(ch, true);
    return { ok: true, channel: ch, connected: true };
  });

  app.post("/agents/:id/policy", async (req, reply) => {
    const { id } = req.params as { id: string };
    const body = req.body as AgentPolicyUpdate;
    try {
      const agent = store.updatePolicy(id, body);
      return { agent, matrix: buildSecurityMatrix(store.catalogAgents()) };
    } catch {
      return reply.status(404).send({ error: "Agent not found" });
    }
  });

  app.post("/agents/:id/state", async (req, reply) => {
    const { id } = req.params as { id: string };
    const body = req.body as AgentStateUpdate;

    if (body.state !== undefined && !isValidState(body.state)) {
      return reply.status(400).send({ error: "Invalid state" });
    }
    if (body.zone !== undefined && !isValidZone(body.zone)) {
      return reply.status(400).send({ error: "Invalid zone" });
    }

    try {
      const agent = store.updateWithMeta(id, body, { eventSource: "real" });
      return { agent };
    } catch {
      return reply.status(404).send({ error: "Agent not found" });
    }
  });

  app.post("/events", async (req, reply) => {
    const body = req.body as {
      agentId: string;
      state?: string;
      task?: string;
      zone?: string;
      source?: string;
      jobId?: string;
      fromZone?: string;
      toZone?: string;
    };

    if (!body?.agentId) {
      return reply.status(400).send({ error: "agentId required" });
    }
    if (body.state !== undefined && !isValidState(body.state)) {
      return reply.status(400).send({ error: "Invalid state" });
    }
    if (body.zone !== undefined && !isValidZone(body.zone)) {
      return reply.status(400).send({ error: "Invalid zone" });
    }

    try {
      const agent = store.updateWithMeta(body.agentId, {
        state: body.state as AgentStateUpdate["state"],
        task: body.task,
        zone: body.zone as AgentStateUpdate["zone"],
      }, {
        eventSource: body.source?.includes("sim") ? "sim" : "real",
        jobId: body.jobId,
        fromZone: body.fromZone as AgentStateUpdate["zone"],
        toZone: body.toZone as AgentStateUpdate["zone"],
      });
      return { ok: true, agent, source: body.source ?? "external" };
    } catch {
      return reply.status(404).send({ error: "Agent not found" });
    }
  });

  app.post("/simulation/start", async () => {
    startSimulation();
    return { ok: true, ...simulationStatus() };
  });

  app.post("/simulation/stop", async () => {
    stopSimulation();
    return { ok: true, ...simulationStatus() };
  });

  app.get("/simulation/status", async () => simulationStatus());

  app.post("/simulation/error/:id", async (req, reply) => {
    const { id } = req.params as { id: string };
    if (!store.get(id)) {
      return reply.status(404).send({ error: "Agent not found" });
    }
    simulateError(id);
    return { ok: true };
  });

  return app;
}

async function main() {
  const app = await buildApp();
  await app.listen({ port: PORT, host: HOST });
  attachWebSocket(app.server);
  const stopMaestroWatcher = initMaestroIntegration(broadcastWs);
  const stopPdfWatcher = initPdfPipelineIntegration(broadcastWs);
  const stopPietraWatcher = initPietraInboxIntegration(broadcastWs);
  const stopIntakeWatcher = initIntakeDispatchIntegration(broadcastWs);
  const stopWatchers = () => {
    stopMaestroWatcher();
    stopPdfWatcher();
    stopPietraWatcher();
    stopIntakeWatcher();
  };
  process.on("SIGINT", stopWatchers);
  process.on("SIGTERM", stopWatchers);
  if (AUTO_SIM) {
    startSimulation();
    app.log.info("Simulation enabled (AGENTARIUM_AUTO_SIM=true)");
  } else {
    app.log.info("Simulation disabled — agents move only on real events");
  }
  const maestro = getMaestroSyncStatus();
  if (maestro.ok) {
    app.log.info(
      `Maestro sync OK — ${maestro.activeCount}/${maestro.agentCount} agents, ${maestro.barramentoCount} barramento events`,
    );
  } else {
    app.log.warn(`Maestro sync skipped: ${maestro.error ?? "unknown"}`);
  }
  app.log.info(`Agentarium v0.9.0 http://${HOST}:${PORT}  ws://${HOST}:${PORT}/ws`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
