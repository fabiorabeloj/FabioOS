---
tipo: decisao
area: wiki
projeto: FabioOS
status: revisar
tags: [anthropic, claude, privacidade, conectores, fabios]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
fonte: sources/email/_restrito/2026-06-27_gmail_anthropic_privacidade.md
indexacao: revisar
---

# Email Anthropic - Privacidade e Claude

## Resumo

E-mail da Anthropic informou atualizacoes de privacidade para contas Claude Free, Pro e Max. Os pontos mais relevantes para o FabioOS sao tarefas de varias etapas, aplicativos conectados, fluxo de dados com terceiros, verificacao de identidade e controles sobre uso de conversas/sessoes para treinamento ou melhoria de modelos.

## Impacto no FabioOS

O FabioOS esta caminhando para usar agentes, conectores, OpenClaw, Gmail, Google Drive, RAG e possivelmente outros modelos. Isso torna necessario um protocolo explicito de privacidade por provedor.

## Decisao proposta

Antes de ativar conectores amplos ou automacoes externas com Claude/Anthropic:

1. revisar configuracoes de privacidade da conta Claude;
2. diferenciar uso pessoal, trabalho e FabioOS;
3. evitar enviar fontes sensiveis brutas a modelos externos;
4. preferir resumos sanitizados quando o conteudo tiver terceiros;
5. registrar no FabioOS quais provedores podem receber quais classes de dados.

## Tarefas

| Tarefa | Prioridade | Contexto |
|---|---|---|
| Criar matriz de privacidade por provedor IA | alta | Claude, Codex/OpenAI, Gemini, OpenRouter |
| Revisar configuracoes da conta Claude | media | Controle de uso de conversas e sessoes |
| Definir politica para aplicativos conectados | alta | Gmail, Drive, OpenClaw, n8n |

## Links internos

- [[60_Sistemas/FabioOS/Protocolo_Ingestao_Memoria_Pessoal_Profissional]]
- [[60_Sistemas/FabioOS/Decisao_Roteamento_Email_Google_Gemini_OpenClaw_2026-06-27]]
- [[60_Sistemas/FabioOS/Protocolo_Lideranca_e_Economia_Multiagente]]
