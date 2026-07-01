import { store } from "../store.js";
import { eventLog } from "../eventLog.js";
import { whatsappJobs } from "../whatsappJobs.js";
import { simulationStatus } from "../simulator.js";
import { loadWhatsAppConfig } from "./config.js";

export type CommandResult = {
  isCommand: true;
  command: string;
  response: string;
};

export function parseCommand(text: string): { command: string; args: string } | null {
  const t = text.trim();
  if (!t.startsWith("/")) return null;
  const parts = t.split(/\s+/);
  const command = parts[0].toLowerCase();
  const args = parts.slice(1).join(" ");
  return { command, args };
}

export function executeFabioCommand(command: string, _args: string): string {
  const agents = store.listActive();
  const jobs = whatsappJobs.list(50);
  const pending = jobs.filter(
    (j) => j.approvalState === "draft_only" || j.approvalState === "awaiting_human",
  );
  const sim = simulationStatus();
  const lastEvent = eventLog.list(1)[0];

  switch (command) {
    case "/status": {
      const cfg = loadWhatsAppConfig();
      return [
        "MEGATRON STATUS",
        `Backend: online`,
        `Simulation: ${sim.running ? "on" : "off"}`,
        `Resposta WPP Fabio: ${cfg.replyToFabio ? "ON" : "OFF"}`,
        `Envio a terceiros: ${cfg.autoSend ? "ON" : "OFF"}`,
        `Agentes ativos: ${agents.length}`,
        `Jobs ativos: ${jobs.length}`,
        `Pendencias Fabio: ${pending.length}`,
        lastEvent
          ? `Ultimo evento: ${lastEvent.message} (${lastEvent.timestamp})`
          : "Ultimo evento: nenhum",
      ].join("\n");
    }

    case "/oi":
      return "Oi, Fabio. Sou o MEGATRON — assistente do FabioOS. Pode falar comigo normalmente.";

    case "/agentes":
      return [
        "AGENTES ATIVOS",
        ...agents.map((a) => `- ${a.name} (${a.id}) · ${a.zone} · ${a.state}`),
      ].join("\n");

    case "/jobs":
      if (jobs.length === 0) return "Nenhum job WhatsApp registrado.";
      return [
        "JOBS WHATSAPP",
        ...jobs.slice(0, 10).map(
          (j) =>
            `- ${j.jobId} · ${j.channel} · ${j.agentId} · ${j.approvalState} · ${j.textPreview}`,
        ),
      ].join("\n");

    case "/pendencias":
      if (pending.length === 0) return "Nenhuma pendencia aguardando Fabio.";
      return [
        "PENDENCIAS",
        ...pending.map(
          (j, i) =>
            `${i + 1}. ${j.contactName} (${j.channel}) — ${j.category} — ${j.jobId}`,
        ),
      ].join("\n");

    case "/resumo": {
      const recent = eventLog.list(8);
      if (recent.length === 0) return "Nenhum evento recente.";
      return [
        "RESUMO RECENTE",
        ...recent.map((e) => `- [${e.channel}] ${e.message}`),
      ].join("\n");
    }

    case "/tarefa":
      return "Use: /tarefa <seu prompt>\nExemplo: /tarefa revisar Agentarium e corrigir inbox";

    case "/prompt":
      return "Use: /prompt <seu pedido>\nAlias de /tarefa";

    case "/tarefas": {
      const taskJobs = jobs.filter((j) => j.category === "task" || j.textPreview.length > 10).slice(0, 8);
      if (taskJobs.length === 0) return "Nenhuma tarefa recente no canal WPP.";
      return [
        "TAREFAS RECENTES (WPP)",
        ...taskJobs.map((j, i) => `${i + 1}. ${j.jobId} · ${j.textPreview}`),
        "",
        "Arquivos em: 00_Inbox/Processar/Tarefas_WPP/",
      ].join("\n");
    }

    case "/help":
      return [
        "MEGATRON — WhatsApp pessoal",
        "",
        "PROMPTS E TAREFAS (principal):",
        "  Envie texto normal ou prefixo:",
        "  tarefa: revisar prova 9A",
        "  prompt: organizar inbox FabioOS",
        "  fabioos: implementar X",
        "",
        "COMANDOS:",
        "/tarefa <texto> — registrar tarefa",
        "/prompt <texto> — idem",
        "/tarefas — listar recentes",
        "/status /pendencias /help",
        "",
        "Tarefas viram arquivos em Tarefas_WPP/ para o Cursor executar.",
      ].join("\n");

    case "/aprovar": {
      const cfg = loadWhatsAppConfig();
      return cfg.autoSend
        ? "Aprovacao registrada. Envio real ainda requer WHATSAPP_AUTO_SEND=true e canSend."
        : "Aprovacao simulada. WHATSAPP_AUTO_SEND=false — nada enviado externamente.";
    }

    default:
      return `Comando desconhecido: ${command}\nDigite /help`;
  }
}

export function handlePersonalCommand(text: string): CommandResult | null {
  const parsed = parseCommand(text);
  if (!parsed) return null;
  return {
    isCommand: true,
    command: parsed.command,
    response: executeFabioCommand(parsed.command, parsed.args),
  };
}
