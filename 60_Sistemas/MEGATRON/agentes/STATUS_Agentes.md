---
tipo: painel
area: 60_Sistemas
projeto: FabioOS
sistema: MEGATRON
status: gerado
gerado_por: agent.dashboard
atualizado_em: 2026-06-26 20:04:36
---

# STATUS dos Agentes MEGATRON

> Gerado automaticamente pelo agente Dashboard em 2026-06-26 20:04:36. Não editar à mão.

## Agentes

| Agente | Última execução | Ação |
|---|---|---|
| SafeCommit | 2026-06-26 20:04:36 | diagnostico |
| Arquivista | 2026-06-26 20:03:04 | nota_criada |
| Inbox | 2026-06-26 20:03:03 | triagem |
| RAG | 2026-06-26 20:03:05 | consulta |
| Dashboard | 2026-06-26 20:03:06 | painel_gerado |

## Situação geral

- **Pendências abertas (Painel):** 25
- **Arquivos com mudança no Git:** 18
- **Último changelog:** `2026-06-26_especificacao-agentes-megatron`

## Pendências críticas (amostra)

- **[Fase 10]** Importar `FabioOS_Webhook_Inbox.json` no n8n → configurar credencial Obsidian API → ativar → testar com curl
- **[Fase 11]** Instalar Evolution API (Docker porta 8080) → criar instância → QR Code WhatsApp → webhook→n8n → importar `FabioOS_WhatsApp_Pietra.json` → ativar → testar
- **[n8n]** Reconciliar nomes: changelog cita "webhook-inbox", mas o n8n real tem `FabioOS — Webhook Arquivista` (ativo) e `FabioOS — Captura para Obsidian` (inativo)
- **[Segurança]** Migrar `GITHUB_TOKEN` hardcoded em `~/.claude/settings.json` para variável de ambiente
- **[Ingestão]** Implementar `/ingest-drive-doc` (depende de MCP Google Drive) e `/ingest-repo`

## Próxima ação recomendada

- Rodar SafeCommit e revisar o commit pendente.

## Relações

- [[60_Sistemas/MEGATRON/agentes/Registro_Agentes]]
- [[90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Painel_Pendencias_FabioOS]]
