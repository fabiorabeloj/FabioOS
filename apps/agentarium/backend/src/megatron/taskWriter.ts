import fs from "node:fs";
import path from "node:path";
import type { CapturedTask } from "../whatsapp/taskCapture.js";
import type { WhatsAppMessageInput } from "../whatsapp/types.js";
import { maskPhone } from "../whatsapp/config.js";

function fabioOsRoot(): string {
  if (process.env.FABIOOS_ROOT) return process.env.FABIOOS_ROOT;
  return path.resolve(process.cwd(), "../../..");
}

function tasksDir(): string {
  if (process.env.MEGATRON_TASKS_DIR) return process.env.MEGATRON_TASKS_DIR;
  return path.join(fabioOsRoot(), "00_Inbox", "Processar", "Tarefas_WPP");
}

function inboxLogPath(): string {
  if (process.env.MEGATRON_INBOX_PATH) return process.env.MEGATRON_INBOX_PATH;
  return path.join(fabioOsRoot(), "00_Inbox", "Processar", "Megatron_Canal_Fabio.md");
}

function ensureDir(dir: string): void {
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
}

export function writeTaskFile(
  input: WhatsAppMessageInput,
  jobId: string,
  task: CapturedTask,
): string {
  const dir = tasksDir();
  ensureDir(dir);

  const ts = new Date(input.timestamp || Date.now()).toISOString();
  const local = new Date(ts).toLocaleString("pt-BR");
  const file = path.join(dir, `${jobId}.md`);

  const body = [
    "---",
    "tipo: tarefa",
    "area: 00_Inbox",
    "projeto: FabioOS",
    "canal: megatron-whatsapp",
    `job_id: ${jobId}`,
    `agente_sugerido: ${task.suggestedAgent}`,
    `status: pendente`,
    `criado_em: ${ts.split("T")[0]}`,
    "---",
    "",
    `# Tarefa WhatsApp · ${jobId}`,
    "",
    "| Campo | Valor |",
    "|---|---|",
    `| Data | ${local} |`,
    `| De | ${input.contactName ?? "Fabio"} (${maskPhone(input.from)}) |`,
    `| Agente sugerido | ${task.suggestedAgentLabel} (\`${task.suggestedAgent}\`) |`,
    `| Origem | ${task.source} |`,
    "",
    "## Prompt / tarefa",
    "",
    task.prompt,
    "",
    "## Instrucao para agentes (Cursor, Codex, Claude)",
    "",
    "1. Ler o prompt acima.",
    "2. Executar no escopo FabioOS.",
    "3. Registrar resultado no changelog ou inbox.",
    "",
    "## Cursor — frase pronta",
    "",
    "```",
    `Leia 00_Inbox/Processar/Tarefas_WPP/${jobId}.md e execute a tarefa.`,
    "```",
    "",
  ].join("\n");

  fs.writeFileSync(file, body, "utf8");
  appendTaskIndex(jobId, task, local);
  appendInboxLog(input, jobId, task, local);
  return file;
}

function appendTaskIndex(jobId: string, task: CapturedTask, local: string): void {
  const indexFile = path.join(tasksDir(), "_INDEX.md");
  if (!fs.existsSync(indexFile)) {
    fs.writeFileSync(
      indexFile,
      "# Indice — Tarefas WhatsApp (MEGATRON)\n\n| Data | Job | Agente | Resumo |\n|---|---|---|---|\n",
      "utf8",
    );
  }
  const row = `| ${local} | ${jobId} | ${task.suggestedAgent} | ${task.title.replace(/\|/g, "/")} |\n`;
  fs.appendFileSync(indexFile, row, "utf8");
}

function appendInboxLog(
  input: WhatsAppMessageInput,
  jobId: string,
  task: CapturedTask,
  local: string,
): void {
  const file = inboxLogPath();
  ensureDir(path.dirname(file));

  if (!fs.existsSync(file)) {
    fs.writeFileSync(
      file,
      [
        "---",
        "tipo: inbox",
        "area: 00_Inbox",
        "projeto: FabioOS",
        "canal: megatron-whatsapp",
        "status: ativo",
        "---",
        "",
        "# MEGATRON — Canal Fabio → Agentes",
        "",
        "Prompts e tarefas do WhatsApp. Cada tarefa também vive em `Tarefas_WPP/{jobId}.md`.",
        "",
        "Frase no Cursor: `Leia 00_Inbox/Processar/Megatron_Canal_Fabio.md e execute a ultima tarefa.`",
        "",
      ].join("\n"),
      "utf8",
    );
  }

  const block = [
    "",
    `## ${local} | ${jobId} | TAREFA`,
    "",
    `- **Agente sugerido:** ${task.suggestedAgentLabel}`,
    `- **Arquivo:** \`Tarefas_WPP/${jobId}.md\``,
    "",
    task.prompt,
    "",
    "---",
    "",
  ].join("\n");

  fs.appendFileSync(file, block, "utf8");
}
