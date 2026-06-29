---
tipo: relatorio-operacional
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, coordenacao, multiagente, git, handoff]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Relatorio de Coordenacao sem Colisao - 2026-06-27

## Funcao

Separar zonas de trabalho entre Codex e Claude apos o incidente de coordenacao na Fase 12 RAG.

## Estado confirmado

| Item | Estado |
|---|---|
| Branch | `main` |
| Ultimo commit local | `0df90b8 fix: reforçar segurança e robustez dos scripts RAG` |
| RAG Chroma | restaurado |
| Chunks RAG | `1795` |
| Caminhos proibidos no indice | nenhum |
| Commit/push por Codex nesta frente | nao |

## Zonas de posse recomendadas

| Zona | Dono recomendado | Pode fazer | Nao fazer |
|---|---|---|---|
| RAG DB (`fabioos_db`) | Ninguem sem novo lock | consultar estado, ler relatorio | reindexar, apagar, matar processo |
| Scripts RAG | Claude apenas se for commitar com OK | revisar diff, stage explicito | alterar sem registrar frente |
| Coordenacao multiagente | Codex | relatorios, prompts, locks | commitar sem OK |
| Commits tematicos | Claude | preparar grupos, scan, pedir OK | `git add -A`, push |
| OpenClaw/WhatsApp docs | Claude ou Codex com lock | revisar docs | mexer em runtime sem lock |
| Obsidian local | Humano/Codex com cuidado | documentar configuracao | commitar backup local sem decisao |

## Working tree por tema

### RAG

- `60_Sistemas/RAG/scripts/ingest_vault.py`
- `60_Sistemas/RAG/scripts/query_rag.py`
- `60_Sistemas/RAG/Relatorio_Validacao_Parcial_RAG_2026-06-26.md`
- `60_Sistemas/RAG/Relatorio_Validacao_RAG_2026-06-27.md`
- `60_Sistemas/RAG/RAG.md`

Regra: nao reindexar nem apagar DB. Se mexer em scripts, registrar frente ativa.

### Coordenacao / retomada

- `60_Sistemas/FabioOS/bootstrap/CLAUDE.md`
- `60_Sistemas/Scripts/60_Sistemas/Scripts/start_fabioos.ps1`
- `50_Registros/Changelog/2026-06-27_retomada-ambiente-fabioos.md`
- `50_Registros/Changelog/2026-06-27_validacao-rag-continuidade.md`
- `60_Sistemas/FabioOS/STATUS.md`
- `60_Sistemas/FabioOS/NEXT_ACTIONS.md`
- `60_Sistemas/FabioOS/Registro_Frentes_Ativas.md`
- `60_Sistemas/FabioOS/Incidente_Coordenacao_RAG_2026-06-27.md`
- `60_Sistemas/FabioOS/Prompt_Retomada_Claude_2026-06-29.md`
- `60_Sistemas/FabioOS/Prompt_Para_Claude_Coordenacao_2026-06-27.md`
- `60_Sistemas/FabioOS/Relatorio_Coordenacao_Sem_Colisao_2026-06-27.md`
- protocolos de retomada, contexto e limpeza segura

Regra: Codex pode manter estes arquivos; Claude deve ler antes de agir.

### OpenClaw / WhatsApp

- `60_Sistemas/OpenClaw/OpenClaw.md`
- `60_Sistemas/OpenClaw/Sistema_OpenClaw.md`
- `60_Sistemas/OpenClaw/setup/EVOLUTION_API_SETUP.md`
- `60_Sistemas/OpenClaw/Diagnostico_OpenClaw_Local_2026-06-27.md`
- `60_Sistemas/OpenClaw/Relatorio_Ativacao_OpenClaw_Companion_2026-06-27.md`
- `60_Sistemas/OpenClaw/Relatorio_Ativacao_WhatsApp_Pessoal_2026-06-27.md`
- `60_Sistemas/OpenClaw/Roteiro_Ativacao_OpenClaw_Evolution_2026-06-27.md`
- `60_Sistemas/n8n/Workflows/FabioOS_WhatsApp_Pietra.json`
- `60_Sistemas/n8n/Workflows/FabioOS_WhatsApp_Pietra.md`
- `40_Wiki/_compat_wiki/sistemas/openclaw.md`

Regra: documentacao pode ser preparada; runtime e envio externo exigem confirmacao humana.

### Higiene de vault / wiki

- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/PRIMUS.md`
- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/30_Conhecimento/FabioOS.md`
- `40_Wiki/_compat_wiki/conceitos/rag.md`
- `40_Wiki/_compat_wiki/conceitos/banco-vetorial.md`
- `40_Wiki/_compat_wiki/indices/mapa-fabios.md`
- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Painel_Pendencias_FabioOS.md`

Regra: stage explicito; revisar frontmatter e links antes de commit.

### Local / Obsidian

- `.obsidian/graph.json.backup-2026-06-27-graph-colors-fabios.json`
- `60_Sistemas/Obsidian/Graph_View_Cores_FabioOS.md`

Regra: nao commitar backup local sem decisao; documentacao Obsidian pode ser commitavel se nao contiver dados sensiveis.

## Ordem recomendada para Claude

1. Ler este relatorio e o Registro de Frentes Ativas.
2. Nao tocar em RAG DB.
3. Preparar commits por tema sem executar commit ate OK humano.
4. Priorizar commit de coordenacao/locks antes de qualquer nova execucao.
5. Depois separar RAG scripts, RAG relatorios, OpenClaw e higiene wiki.

## Ordem recomendada para Codex

1. Nao iniciar nova ingestao.
2. Nao matar processo.
3. Manter apenas coordenacao e verificacoes read-only.
4. Se precisar editar artefato compartilhado, registrar nova frente no `Registro_Frentes_Ativas.md`.

## Proxima acao humana

Enviar a Claude o prompt em [[60_Sistemas/FabioOS/Prompt_Para_Claude_Coordenacao_2026-06-27]].
