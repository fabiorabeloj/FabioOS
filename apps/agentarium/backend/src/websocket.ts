import { WebSocketServer, type WebSocket } from "ws";
import type { Server } from "node:http";
import type { Agent, WsMessage } from "./types.js";
import { store } from "./store.js";
import { buildSecurityMatrix } from "./risk.js";

function matrixPayload() {
  return buildSecurityMatrix(store.catalogAgents());
}

export function attachWebSocket(server: Server): WebSocketServer {
  const wss = new WebSocketServer({ server, path: "/ws" });

  wss.on("connection", (socket) => {
    send(socket, { type: "snapshot", agents: store.listActive() });
    send(socket, { type: "security_matrix", matrix: matrixPayload() });
    send(socket, { type: "catalog", catalog: store.catalog() });
  });

  store.subscribe((agent) => {
    broadcast(wss, { type: "agent_updated", agent });
  });

  store.subscribeMatrix(() => {
    broadcast(wss, { type: "security_matrix", matrix: matrixPayload() });
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

export function broadcastAgent(agent: Agent): void {
  void agent;
}
