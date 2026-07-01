import type { Zone } from "../types.js";
import type {
  WhatsAppAnalysis,
  WhatsAppMessageCategory,
  WhatsAppMessageInput,
} from "./types.js";
import { classifyMessage } from "./classifier.js";

export type RoutePlan = {
  analysis: WhatsAppAnalysis;
  agentUpdates: Array<{
    agentId: string;
    zone: Zone;
    fromZone: Zone;
    state: "thinking" | "executing" | "waiting_approval" | "idle" | "done";
    task: string;
    delayMs: number;
  }>;
};

export function buildRoutePlan(input: WhatsAppMessageInput): RoutePlan {
  const { category, urgency, action } = classifyMessage(input);
  const routedAgents = ["hermes"];
  const agentUpdates: RoutePlan["agentUpdates"] = [];

  const push = (
    agentId: string,
    zone: Zone,
    fromZone: Zone,
    state: RoutePlan["agentUpdates"][0]["state"],
    task: string,
    delayMs: number,
  ) => {
    if (!routedAgents.includes(agentId)) routedAgents.push(agentId);
    agentUpdates.push({ agentId, zone, fromZone, state, task, delayMs });
  };

  push("hermes", "Personal WhatsApp", "Personal WhatsApp", "executing", "Mensagem recebida", 0);
  push("hermes", "Message Intake", "Personal WhatsApp", "thinking", "Triando mensagem pessoal", 400);
  push("hermes", "Classificação", "Message Intake", "executing", `Classificando: ${category}`, 900);

  if (category === "school") {
    push("pietra", "Classificação", "Classificação", "thinking", "Mensagem escolar detectada", 1200);
    push("supervisor", "Aprovação Humana", "Classificação", "waiting_approval", "Escola aguarda Fabio", 1800);
  } else if (category === "work") {
    push("roteador", "Classificação", "Classificação", "executing", "Roteando para projeto", 1200);
  } else if (/codigo|github|cursor|script|bug|commit/i.test(input.text)) {
    push("codex", "GitHub", "Classificação", "thinking", "Assunto tecnico detectado", 1200);
  } else if (category === "finance") {
    push("supervisor", "Aprovação Humana", "Classificação", "waiting_approval", "Financeiro sensivel", 1200);
  } else if (category === "sensitive") {
    push("supervisor", "Aprovação Humana", "Classificação", "waiting_approval", "Conteudo sensivel", 1200);
  } else if (category === "unknown") {
    push("roteador", "Classificação", "Message Intake", "thinking", "Contato desconhecido", 1200);
  }

  push("hermes", "Draft Reply", "Classificação", "waiting_approval", "Rascunho pronto — sem envio", 2200);
  push("hermes", "Awaiting Fabio", "Draft Reply", "waiting_approval", "Aguardando aprovacao humana", 2800);

  const draftReply = buildDraftReply(category, input.text);
  const analysis: WhatsAppAnalysis = {
    category,
    urgency,
    action,
    approvalState: "draft_only",
    routedAgents,
    summary: summarize(input.text, category),
    draftReply,
    blocked: false,
  };

  return { analysis, agentUpdates };
}

function summarize(text: string, category: WhatsAppMessageCategory): string {
  const preview = text.length > 80 ? `${text.slice(0, 80)}…` : text;
  return `[${category}] ${preview}`;
}

function buildDraftReply(category: WhatsAppMessageCategory, text: string): string {
  if (category === "family" || category === "friend") {
    return "Oi! Vi sua mensagem. Te respondo em breve.";
  }
  if (category === "work") {
    return "Recebi. Vou revisar e retorno assim que possivel.";
  }
  if (category === "school") {
    return "[Rascunho institucional — Pietra revisara antes de qualquer envio]";
  }
  if (category === "sensitive" || category === "finance") {
    return "[Sem rascunho automatico — requer aprovacao do Supervisor]";
  }
  return `Rascunho: recebi sua mensagem sobre "${text.slice(0, 40)}…"`;
}
