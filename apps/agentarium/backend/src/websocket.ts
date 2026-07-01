import { WebSocketServer, type WebSocket } from "ws";
import type { Server } from "node:http";
import type { Agent, WsMessage } from "./types.js";
import { store } from "./store.js";
import { buildSecurityMatrix } from "./risk.js";
import { eventLog } from "./eventLog.js";
import { whatsappJobs } from "./whatsappJobs.js";
import { getBarramentoSnapshot } from "./maestro/sync.js";
import { getPdfPipelineSnapshot, refreshPdfPipelineSnapshot } from "./pdfPipeline/sync.js";
import { getPietraInboxSnapshot } from "./pietraInbox/sync.js";
import { getIntakeDispatchSnapshot } from "./intakeDispatch/sync.js";

function matrixPayload() {
  return buildSecurityMatrix(store.catalogAgents());
}

export function attachWebSocket(server: Server): WebSocketServer {
  const wss = new WebSocketServer({ server, path: "/ws" });
  attachedWss = wss;

  wss.on("connection", (socket) => {
    send(socket, { type: "snapshot", agents: store.listActive() });
    send(socket, { type: "security_matrix", matrix: matrixPayload() });
    send(socket, { type: "catalog", catalog: store.catalog() });
    send(socket, { type: "event_log_snapshot", entries: eventLog.list() });
    send(socket, { type: "barramento_snapshot", barramento: getBarramentoSnapshot() });
    const pipeline = getPdfPipelineSnapshot();
    if (pipeline) {
      send(socket, { type: "pdf_pipeline_snapshot", pipeline });
    }
    const pietraInbox = getPietraInboxSnapshot();
    if (pietraInbox) {
      send(socket, { type: "pietra_inbox_snapshot", inbox: pietraInbox });
    }
    const intakeDispatch = getIntakeDispatchSnapshot();
    if (intakeDispatch) {
      send(socket, { type: "intake_dispatch_snapshot", dispatch: intakeDispatch });
    }
    send(socket, { type: "whatsapp_jobs", jobs: whatsappJobs.list() });
  });

  store.subscribe((agent) => {
    broadcast(wss, { type: "agent_updated", agent });
  });

  store.subscribeMatrix(() => {
    broadcast(wss, { type: "security_matrix", matrix: matrixPayload() });
  });

  eventLog.subscribe((entry) => {
    broadcast(wss, { type: "event_log", entry });
  });

  whatsappJobs.subscribe((jobs) => {
    broadcast(wss, { type: "whatsapp_jobs", jobs });
  });

  return wss;
}

function send(socket: WebSocket, msg: WsMessage): void {
  if (socket.readyState === socket.OPEN) {
    socket.send(JSON.stringify(msg));
  }
}

function broadcast(wss: WebSocketServer, msg: WsMessage): void {
  const raw = JSON.stringify(msg);
  for (const client of wss.clients) {
    if (client.readyState === client.OPEN) {
      client.send(raw);
    }
  }
}

let attachedWss: WebSocketServer | null = null;

export function broadcastWs(msg: WsMessage): void {
  if (attachedWss) broadcast(attachedWss, msg);
}

export function broadcastAgent(agent: Agent): void {
  void agent;
}
