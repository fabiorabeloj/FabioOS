---
type: sistema
area: FabioOS
source: ChatGPT
status: avaliacao
tags: [fabioos, hermes, agentes, ia, openclaw]
created: 2026-06-23
---

# Hermes Agent

## Resumo

Hermes Agent é um agente de IA externo que pode ser avaliado para uso futuro no FabioOS.

Ele não é o classificador interno do sistema. O classificador interno será o [[Arquivista FabioOS]].

## Função possível no FabioOS

Hermes Agent pode futuramente:

- enviar conteúdo para o webhook do FabioOS;
- atuar como agente persistente;
- lembrar projetos;
- criar habilidades;
- operar junto com OpenClaw;
- alimentar o Obsidian indiretamente via n8n.

## Arquitetura correta

```text
Hermes Agent → Webhook FabioOS → n8n → OpenRouter → GitHub → Obsidian