---
tipo: checklist
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, git, precommit, multiagente, seguranca]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Checklist Pre-Commit sem Colisao - 2026-06-27

## Funcao

Ajudar Claude a preparar commits tematicos sem apagar, sobrescrever ou misturar trabalho de Codex, RAG, OpenClaw e Obsidian local.

## Regra central

```text
Stage explicito por arquivo.
Sem git add -A.
Sem push.
Sem reindexar RAG.
Sem matar processos.
```

## 1. Antes de qualquer stage

- [ ] Ler `60_Sistemas/FabioOS/Registro_Frentes_Ativas.md`.
- [ ] Confirmar que `COMMITS_TEMATICOS` ainda e a frente ativa de Claude.
- [ ] Rodar `git status --short`.
- [ ] Conferir se nao ha processo de ingestao RAG em andamento.
- [ ] Confirmar que `60_Sistemas/RAG/fabioos_db/` nao sera tocado.
- [ ] Confirmar que logs `.log` e `.venv/` seguem ignorados.

## 2. Grupos recomendados

### A - Coordenacao e retomada

Possiveis arquivos:

- `CLAUDE.md`
- `start_fabioos.ps1`
- `50_Registros/Changelog/2026-06-27_retomada-ambiente-fabioos.md`
- `50_Registros/Changelog/2026-06-27_validacao-rag-continuidade.md`
- `60_Sistemas/FabioOS/Protocolo_Gestao_Contexto_IA.md`
- `60_Sistemas/FabioOS/Protocolo_Limpeza_Segura_FabioOS_PC.md`
- `60_Sistemas/FabioOS/Protocolo_Retomada_Ambiente_FabioOS.md`
- `60_Sistemas/FabioOS/Registro_Frentes_Ativas.md`
- `60_Sistemas/FabioOS/STATUS.md`
- `60_Sistemas/FabioOS/NEXT_ACTIONS.md`
- `60_Sistemas/FabioOS/Prompt_Retomada_Claude_2026-06-29.md`
- `60_Sistemas/FabioOS/Prompt_Para_Claude_Coordenacao_2026-06-27.md`
- `60_Sistemas/FabioOS/Relatorio_Coordenacao_Sem_Colisao_2026-06-27.md`
- `60_Sistemas/FabioOS/Incidente_Coordenacao_RAG_2026-06-27.md`
- `60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente.md`

Mensagem sugerida:

```text
docs: fortalecer coordenacao multiagente e retomada do FabioOS
```

### B - RAG validado e ranking operacional

Possiveis arquivos:

- `60_Sistemas/RAG/scripts/ingest_vault.py`
- `60_Sistemas/RAG/scripts/query_rag.py`
- `60_Sistemas/RAG/Relatorio_Validacao_Parcial_RAG_2026-06-26.md`
- `60_Sistemas/RAG/Relatorio_Validacao_RAG_2026-06-27.md`
- `60_Sistemas/RAG/RAG.md`

Mensagem sugerida:

```text
fix: restaurar validacao RAG e priorizar status operacional
```

Bloqueio:

- [ ] Nao stagear `60_Sistemas/RAG/fabioos_db/`.
- [ ] Nao stagear `.venv/`.
- [ ] Nao stagear logs `.log`.

### C - OpenClaw / WhatsApp

Possiveis arquivos:

- `60_Sistemas/OpenClaw/OpenClaw.md`
- `60_Sistemas/OpenClaw/Sistema_OpenClaw.md`
- `60_Sistemas/OpenClaw/setup/EVOLUTION_API_SETUP.md`
- `60_Sistemas/OpenClaw/Diagnostico_OpenClaw_Local_2026-06-27.md`
- `60_Sistemas/OpenClaw/Relatorio_Ativacao_OpenClaw_Companion_2026-06-27.md`
- `60_Sistemas/OpenClaw/Relatorio_Ativacao_WhatsApp_Pessoal_2026-06-27.md`
- `60_Sistemas/OpenClaw/Roteiro_Ativacao_OpenClaw_Evolution_2026-06-27.md`
- `60_Sistemas/n8n/Workflows/FabioOS_WhatsApp_Pietra.json`
- `60_Sistemas/n8n/Workflows/FabioOS_WhatsApp_Pietra.md`
- `wiki/sistemas/openclaw.md`

Mensagem sugerida:

```text
docs: registrar ativacao OpenClaw e preparar ponte WhatsApp
```

### D - Higiene wiki / frontmatter

Possiveis arquivos:

- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/PRIMUS.md`
- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/30_Conhecimento/FabioOS.md`
- `wiki/conceitos/rag.md`
- `wiki/conceitos/banco-vetorial.md`
- `wiki/indices/mapa-fabios.md`
- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Painel_Pendencias_FabioOS.md`

Mensagem sugerida:

```text
docs: corrigir frontmatter e paginas conceituais do vault
```

### E - Obsidian local

Possiveis arquivos:

- `60_Sistemas/Obsidian/Graph_View_Cores_FabioOS.md`

Nao stagear sem decisao:

- `.obsidian/graph.json.backup-2026-06-27-graph-colors-fabios.json`

Mensagem sugerida, se aprovado:

```text
docs: documentar configuracao visual do Obsidian
```

## 3. Scan obrigatorio por commit

Antes de cada commit:

- [ ] Rodar scan de segredos somente nos arquivos staged.
- [ ] Classificar falsos positivos sem exibir valores.
- [ ] Se houver credencial real, parar.
- [ ] Mostrar `git diff --cached --name-only`.
- [ ] Mostrar mensagem de commit.
- [ ] Aguardar OK humano.

## 4. Itens que nao devem entrar agora

- `60_Sistemas/RAG/fabioos_db/`
- `60_Sistemas/RAG/.venv/`
- `60_Sistemas/RAG/*.log`
- `.obsidian/graph.json.backup-*` sem decisao humana
- qualquer `.env`, token, segredo ou credencial local

## 5. Validacao final antes de encerrar

- [ ] `git status --short` nao mostra arquivos staged inesperados.
- [ ] `Registro_Frentes_Ativas.md` atualizado se a frente terminar.
- [ ] `STATUS.md` atualizado se algum commit mudar o estado.
- [ ] Sem push.

## Relacoes

- [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]]
- [[60_Sistemas/FabioOS/Relatorio_Coordenacao_Sem_Colisao_2026-06-27]]
- [[60_Sistemas/FabioOS/Incidente_Coordenacao_RAG_2026-06-27]]
