import Fastify from "fastify";
import cors from "@fastify/cors";
import { store, isValidState, isValidZone } from "./store.js";
import { attachWebSocket } from "./websocket.js";
import {
  startSimulation,
  stopSimulation,
  simulationStatus,
  simulateError,
} from "./simulator.js";
import type { AgentStateUpdate, AgentPolicyUpdate } from "./types.js";
import { buildSecurityMatrix } from "./risk.js";

const PORT = Number(process.env.PORT ?? 3847);
const HOST = process.env.HOST ?? "127.0.0.1";
const AUTO_SIM = process.env.AGENTARIUM_AUTO_SIM !== "false";

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
  }));

  app.get("/agents", async () => ({
    agents: store.list(),
  }));

  app.get("/agents/:id", async (req, reply) => {
    const { id } = req.params as { id: string };
    const agent = store.get(id);
    if (!agent) {
      return reply.status(404).send({ error: "Agent not found" });
    }
    return { agent };
  });

  app.get("/security/matrix", async () => buildSecurityMatrix(store.list()));

  app.post("/agents/:id/policy", async (req, reply) => {
    const { id } = req.params as { id: string };
    const body = req.body as AgentPolicyUpdate;
    try {
      const agent = store.updatePolicy(id, body);
      return { agent, matrix: buildSecurityMatrix(store.list()) };
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
      const agent = store.update(id, body);
      return { agent };
    } catch {
      return reply.status(404).send({ error: "Agent not found" });
    }
  });

  /** Eventos reais futuros: n8n, OpenClaw, scripts locais */
  app.post("/events", async (req, reply) => {
    const body = req.body as {
      agentId: string;
      state?: string;
      task?: string;
      zone?: string;
      source?: string;
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
      const agent = store.update(body.agentId, {
        state: body.state as AgentStateUpdate["state"],
        task: body.task,
        zone: body.zone as AgentStateUpdate["zone"],
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
  if (AUTO_SIM) {
    startSimulation();
    app.log.info("Simulation mode enabled (set AGENTARIUM_AUTO_SIM=false to disable)");
  }
  app.log.info(`Agentarium backend http://${HOST}:${PORT}  ws://${HOST}:${PORT}/ws`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
