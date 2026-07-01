import type { WhatsAppMessageInput, WhatsAppSchoolCategory } from "./types.js";

const SCHOOL_MENU = `Ola. Sou a assistente de triagem do Professor Fabio.
Para encaminhar sua mensagem, escolha uma opcao:
1. Atividades e tarefas
2. Provas e recuperacoes
3. Conteudo de aula
4. Faltas ou justificativas
5. Falar com o professor
6. Outros assuntos

Mensagem recebida. Resposta sera preparada pelo professor.`;

const SAFE_RECEIPT = `Mensagem recebida. Vou encaminhar ao professor e ele respondera assim que possivel.`;

export function classifySchoolMessage(text: string): {
  category: WhatsAppSchoolCategory;
  urgency: "low" | "normal" | "high";
  requiresApproval: boolean;
  suggestedReply: string;
} {
  const t = text.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");

  let category: WhatsAppSchoolCategory = "unknown";
  let urgency: "low" | "normal" | "high" = "normal";
  let requiresApproval = true;
  let suggestedReply = SAFE_RECEIPT;

  if (/^(oi|ola|bom dia|boa tarde|boa noite|hello)/.test(t)) {
    category = "greeting";
    suggestedReply = SCHOOL_MENU;
    requiresApproval = true;
  } else if (/prova|avaliacao|simulado|gabarito|recuperacao|substitutiva|segunda chamada/.test(t)) {
    category = /substitut|segunda chamada|perdeu a prova/.test(t) ? "substitute_test" : "test";
    urgency = "normal";
  } else if (/falta|ausente|justificativa|atestado/.test(t)) {
    category = "absence";
  } else if (/tarefa|atividade|dever|lição|licao|homework/.test(t)) {
    category = "homework";
  } else if (/conteudo|materia|explicar|nao entendi|duvida/.test(t)) {
    category = "content_question";
  } else if (/horario|que horas|feriado|recesso/.test(t)) {
    category = "schedule";
    urgency = "low";
  } else if (/reclam|briga|conflito|bullying|agress/.test(t)) {
    category = "complaint";
    urgency = "high";
    requiresApproval = true;
  } else if (/suspens|expuls|disciplin|advert/.test(t)) {
    category = "discipline";
    urgency = "high";
  } else if (/medico|remedio|laudo|financeiro|mensalidade|boleto/.test(t)) {
    category = "sensitive";
    urgency = "high";
  } else if (/aluno|turma|serie|filho|filha|meu filho/.test(t)) {
    category = "student_identification";
    suggestedReply = `${SAFE_RECEIPT}\n\nPor favor informe: nome do aluno, turma e assunto.`;
  }

  return { category, urgency, requiresApproval, suggestedReply };
}

export function buildSchoolRoutePlan(
  input: WhatsAppMessageInput,
  category: WhatsAppSchoolCategory,
) {
  const steps: Array<{
    agentId: string;
    zone: import("../types.js").Zone;
    fromZone: import("../types.js").Zone;
    state: "thinking" | "executing" | "waiting_approval";
    task: string;
    delayMs: number;
  }> = [];

  steps.push({
    agentId: "pietra",
    zone: "WhatsApp",
    fromZone: "WhatsApp",
    state: "executing",
    task: "Mensagem escolar recebida",
    delayMs: 0,
  });
  steps.push({
    agentId: "pietra",
    zone: "Classificação",
    fromZone: "WhatsApp",
    state: "thinking",
    task: `Classificando: ${category}`,
    delayMs: 500,
  });

  if (category === "discipline" || category === "sensitive" || category === "complaint") {
    steps.push({
      agentId: "supervisor",
      zone: "Aprovação Humana",
      fromZone: "Classificação",
      state: "waiting_approval",
      task: "Escolar sensivel — aguarda Fabio",
      delayMs: 1200,
    });
  }

  steps.push({
    agentId: "pietra",
    zone: "Awaiting Fabio",
    fromZone: "Classificação",
    state: "waiting_approval",
    task: "Rascunho institucional pronto",
    delayMs: 2000,
  });

  return steps;
}

export { SCHOOL_MENU, SAFE_RECEIPT };
