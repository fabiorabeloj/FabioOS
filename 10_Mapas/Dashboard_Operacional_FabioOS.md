---
tipo: dashboard
area: 10_Mapas
projeto: FabioOS
status: gerado
gerado_por: dashboard_fabioos.py
atualizado_em: 2026-06-28 14:10:19
tags: [fabios, dashboard, python, automacao, status]
---

# Dashboard Operacional FabioOS

> Gerado automaticamente por `60_Sistemas/FabioOS/scripts/dashboard_fabioos.py`.
> Fonte local apenas: Git, Markdown do vault, RAG DB, auditoria do Grafo e config Codex sem exibir segredos.

## Estado Git

- Branch/status: `## main...origin/main [ahead 55]`
- HEAD local: `4646739`
- Arquivos modificados/untracked: `3`
- Ultimo changelog: `2026-06-28_matriz-automatizacoes-python-n8n.md`

## Frentes ativas

- MCP_FABIOOS (Claude): em andamento
- INTERINATO_CODEX (Codex): em andamento

## Camadas cognitivas

| Camada | Estado |
|---|---|
| RAG local | presente, 1795 chunks |
| Grafo local | 840 nos, 2680 arestas, 0 arestas orfas, 0 nos isolados, 100.0% conectados |
| MCP FabioOS | registrado no config global do Codex |
| Workflows n8n versionados | 2 JSON |

## Workflows n8n versionados

- FabioOS_Webhook_Inbox.json
- FabioOS_WhatsApp_Pietra.json

## Pendencias

- Pendencias abertas no Painel: `24`
- Pendencias abertas em NEXT_ACTIONS: `26`

### Amostra do Painel

- **[Fase 10]** Importar `FabioOS_Webhook_Inbox.json` no n8n → configurar credencial Obsidian API → ativar → testar com curl
- **[Fase 11]** Instalar Evolution API (Docker porta 8080) → criar instância → QR Code WhatsApp → webhook→n8n → importar `FabioOS_WhatsApp_Pietra.json` → ativar → testar
- **[n8n]** Reconciliar nomes: changelog cita "webhook-inbox", mas o n8n real tem `FabioOS — Webhook Arquivista` (ativo) e `FabioOS — Captura para Obsidian` (inativo)
- **[Segurança]** Migrar `GITHUB_TOKEN` hardcoded em `~/.claude/settings.json` para variável de ambiente
- **[Ingestão]** Implementar `/ingest-drive-doc` (depende de MCP Google Drive) e `/ingest-repo`
- **[Wiki]** Criar páginas: `conceitos/rag.md`, `conceitos/llm-wiki.md`, `sistemas/mcp-servers.md`, `projetos/trader.md`
- **[Arquitetura]** Derivar ontologia operacional do `00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON.md` quando iniciar Fase 13 — Grafo
- **[RAG]** Reexecutar as 10 perguntas do `60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG.md` apos ajuste de ranking/recencia

### Amostra do NEXT_ACTIONS

- Preparar handoff para Claude retornar em 2026-06-29 13:00.
- Rodar scan de segredos antes de qualquer commit.
- Decidir se a memoria consolidada do piloto pode entrar no RAG/Grafo.
- Investigar falhas do GitHub Actions `Auto Changelog`.
- Criar matriz de privacidade por provedor IA.
- Solicitar exportacao do ChatGPT se Fabio quiser absorver conversas antigas.
- Verificar se existe conector/autorizacao do Gmail de trabalho.
- Ler [[60_Sistemas/FabioOS/Interinato_Codex_2026-06-27_a_2026-06-29]].

## Inconsistencias detectadas

- RAG aparece como validado no painel, mas NEXT_ACTIONS ainda pede reexecucao das 10 perguntas.
- n8n tem pendencia de reconciliar nomes/status de workflows documentados vs ambiente real.

## Proxima acao recomendada

- Resolver primeiro as inconsistencias detectadas antes de ativar automacoes externas.
- Manter Python para auditorias locais e n8n para bordas externas com credencial/aprovacao.
