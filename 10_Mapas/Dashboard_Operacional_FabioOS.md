---
tipo: dashboard
area: 10_Mapas
projeto: FabioOS
status: gerado
gerado_por: dashboard_fabioos.py
atualizado_em: 2026-06-28 22:15:00
tags: [fabios, dashboard, python, automacao, status]
---

# Dashboard Operacional FabioOS

> Gerado automaticamente por `60_Sistemas/FabioOS/scripts/dashboard_fabioos.py`.
> Fonte local apenas: Git, Markdown do vault, RAG DB, auditoria do Grafo e config Codex sem exibir segredos.

## Estado Git

- Branch/status: `## main...origin/main [ahead 57]`
- HEAD local: `86dc93b`
- Arquivos modificados/untracked: `15`
- Ultimo changelog: `2026-06-28_estrutura-profissional-fabios-megatron.md`

## Frentes ativas

- MCP_FABIOOS (Claude): em andamento
- INTERINATO_CODEX (Codex): em andamento

## Camadas cognitivas

| Camada | Estado |
|---|---|
| RAG local | presente, 1795 chunks |
| Grafo local | 840 nos, 2680 arestas, 0 arestas orfas, 0 nos isolados, 100.0% conectados |
| MCP FabioOS | registrado no config global do Codex |
| Radar Tecnologico | 1 analise(s), ultima: 2026-06-28_prompt-arquiteturas-de-mercado-fabioos.md |
| Workflows n8n versionados | 2 JSON |

## Workflows n8n versionados

- FabioOS_Webhook_Inbox.json
- FabioOS_WhatsApp_Pietra.json

## Pendencias

- Pendencias abertas no Painel: `24`
- Pendencias abertas em NEXT_ACTIONS: `30`

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
- Criar matriz de dominios/dados/permissoes com base na camada profissional do FabioOS.
- Usar o catalogo de caminhos demonstrados para avaliar novos anuncios, ferramentas, prints e prompts antes de instalar ou assinar.
- Aplicar o Radar Tecnologico em pelo menos 3 materiais reais antes de promover nova ferramenta ao roadmap. (`radar_tecnologico.py` implementado; falta rodar 3 casos reais)
- Avaliar subfases candidatas 20.5, 21.5, 22.5, 23.5, 24, 25 e 26 antes de inflar o roadmap oficial.
- Rodar scan de segredos antes de qualquer commit.
- Decidir se a memoria consolidada do piloto pode entrar no RAG/Grafo.
- Investigar falhas do GitHub Actions `Auto Changelog`.

## Inconsistencias detectadas

- RAG aparece como validado no painel, mas NEXT_ACTIONS ainda pede reexecucao das 10 perguntas.
- n8n tem pendencia de reconciliar nomes/status de workflows documentados vs ambiente real.

## Proxima acao recomendada

- Resolver primeiro as inconsistencias detectadas antes de ativar automacoes externas.
- Manter Python para auditorias locais e n8n para bordas externas com credencial/aprovacao.
