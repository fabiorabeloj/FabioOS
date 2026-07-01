import fs from "node:fs";
import path from "node:path";
import type { WhatsAppAnalysis, WhatsAppMessageInput } from "../whatsapp/types.js";
import { maskPhone } from "../whatsapp/config.js";

function fabioOsRoot(): string {
  if (process.env.FABIOOS_ROOT) return process.env.FABIOOS_ROOT;
  return path.resolve(process.cwd(), "../../..");
}

function inboxPath(): string {
  if (process.env.MEGATRON_INBOX_PATH) return process.env.MEGATRON_INBOX_PATH;
  if (process.env.HERMES_INBOX_PATH) return process.env.HERMES_INBOX_PATH;
  return path.join(fabioOsRoot(), "00_Inbox", "Processar", "Megatron_Canal_Fabio.md");
}

function stripPrefix(text: string): string {
  return text.replace(/^(fabioos|tarefa|prompt|pedido)[,:\s]+/i, "").trim() || text;
}

/** Triagem simples (nao-tarefa) — mensagens de terceiros etc. */
export function appendMegatronInbox(
  input: WhatsAppMessageInput,
  jobId: string,
  analysis: WhatsAppAnalysis,
): string {
  const file = inboxPath();
  const dir = path.dirname(file);
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

  const ts = new Date(input.timestamp || Date.now()).toISOString();
  const local = new Date(ts).toLocaleString("pt-BR");
  const cleanText = stripPrefix(input.text);
  const contact = input.contactName ?? "Contato";
  const masked = maskPhone(input.from);

  const agents =
    analysis.routedAgents.filter((a) => a !== "hermes").join(", ") || "Cursor (geral)";

  const block = [
    "",
    `## ${local} | ${jobId} | TRIAGEM`,
    "",
    `- **Canal:** WhatsApp pessoal (MEGATRON)`,
    `- **De:** ${contact} (${masked})`,
    `- **Categoria:** ${analysis.category} | **Urgencia:** ${analysis.urgency}`,
    `- **Encaminhar para:** ${agents}`,
    "",
    cleanText,
    "",
    "---",
    "",
  ].join("\n");

  if (!fs.existsSync(file)) {
    fs.writeFileSync(
      file,
      "# MEGATRON — Canal Fabio → Agentes\n\nVer também `Tarefas_WPP/` para prompts estruturados.\n",
      "utf8",
    );
  }
  fs.appendFileSync(file, block, "utf8");
  return file;
}

/** Alias legado */
export const appendHermesInbox = appendMegatronInbox;
