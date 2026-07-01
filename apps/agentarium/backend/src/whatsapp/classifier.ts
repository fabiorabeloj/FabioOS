import type {
  WhatsAppActionType,
  WhatsAppMessageCategory,
  WhatsAppMessageInput,
  WhatsAppMessageUrgency,
} from "./types.js";

const SCHOOL = /escola|professor|prof|turma|bimestre|prova|reuni[aã]o|secretaria|aluno|matr[ií]cula/i;
const WORK = /projeto|trabalho|reuni[aã]o|cliente|prazo|entrega|fabioos|cursor|github|codigo|c[oó]digo/i;
const FINANCE = /pix|boleto|pagamento|cobran[cç]a|fatura|banco|cart[aã]o|dinheiro|transfer/i;
const FAMILY = /m[aã]e|pai|filh|fam[ií]lia|irm[aã]|av[oó]|casa|jantar|anivers/i;
const FRIEND = /oi|ol[aá]|beleza|bora|festa|churrasco|caf[eé]/i;
const SENSITIVE = /processo|advogad|m[eé]dico|diagn[oó]stico|depress|ansied|briga|triste|urgente demais|pol[ií]cia/i;
const URGENT = /urgente|agora|imediato|socorro|emerg/i;

export function classifyMessage(input: WhatsAppMessageInput): {
  category: WhatsAppMessageCategory;
  urgency: WhatsAppMessageUrgency;
  action: WhatsAppActionType;
} {
  const text = input.text.toLowerCase();

  let category: WhatsAppMessageCategory = "unknown";
  if (SENSITIVE.test(text)) category = "sensitive";
  else if (SCHOOL.test(text)) category = "school";
  else if (FINANCE.test(text)) category = "finance";
  else if (WORK.test(text)) category = "work";
  else if (FAMILY.test(text)) category = "family";
  else if (FRIEND.test(text)) category = "friend";
  else if (/servi[cç]o|suporte|atendimento|loja|entrega/.test(text)) category = "service";

  let urgency: WhatsAppMessageUrgency = "normal";
  if (URGENT.test(text)) urgency = "urgent";
  else if (category === "sensitive" || category === "finance") urgency = "high";
  else if (category === "unknown") urgency = "low";

  let action: WhatsAppActionType = "draft_reply";
  if (category === "school") action = "forward_to_agent";
  else if (category === "work") action = "forward_to_agent";
  else if (category === "finance") action = "requires_human";
  else if (category === "sensitive") action = "requires_human";
  else if (category === "unknown") action = "summarize";
  else if (/registre|inbox|anot/.test(text)) action = "archive_to_obsidian";

  return { category, urgency, action };
}
