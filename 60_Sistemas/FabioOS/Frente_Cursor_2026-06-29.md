---
tipo: registro-operacional
area: 60_Sistemas
projeto: FabioOS
status: concluido
tags: [cursor, frente, validacao-rag, multiagente, sem-colisao]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Frente Cursor — Validacao RAG pos-ranking

## Funcao

Declarar frente isolada do Cursor para nao colidir com Codex (`LLM_WIKI_OPERACIONAL`, `MATRIZ_APTIDAO_IAS`) nem com Claude (`MCP_FABIOOS`).

Este arquivo e a declaracao de lock local. Codex pode fundir a linha correspondente em [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]] quando conveniente.

## Frente

| Campo | Valor |
|---|---|
| ID | `CURSOR_VALIDACAO_RAG` |
| Dono | Cursor |
| Inicio | 2026-06-29 |
| Estado | concluida |
| Resultado | [[60_Sistemas/RAG/Relatorio_Validacao_RAG_2026-06-29_Cursor]] |

## Artefatos autorizados (somente novos ou RAG read-only)

- `60_Sistemas/RAG/scripts/batch_validate_rag.py` (novo)
- `60_Sistemas/RAG/scripts/query_rag.py` (cache get_model)
- `60_Sistemas/RAG/Relatorio_Validacao_RAG_2026-06-29_Cursor.md` (novo)
- `60_Sistemas/RAG/validacao_pos_ranking_*.json` (novo, saida da batch)
- `50_Registros/Changelog/2026-06-29_validacao-rag-pos-ranking-cursor.md` (novo)
- Este arquivo

## Proibido nesta frente

- Reindexar ou apagar `60_Sistemas/RAG/fabioos_db/`
- Editar `STATUS.md`, `NEXT_ACTIONS.md`, `40_Wiki/_compat_wiki/indices/mapa-fabios.md`, `60_Sistemas/FabioOS/bootstrap/CLAUDE.md`, `Registro_Frentes_Ativas.md`
- Tocar `60_Sistemas/MCP_FabioOS/`, OpenClaw runtime, n8n, credenciais
- Commit ou push sem autorizacao humana
- Chamar API externa (`--generate` desligado)

## Criterio de concluido

- 10 perguntas reais executadas em modo recuperacao
- Testes de seguranca 4.5 executados
- Relatorio e changelog gerados
- Resultado comparado com relatorio de 2026-06-27

## Documentacao Obsidian (frente sucessora)

Ver [[60_Sistemas/FabioOS/Frente_Cursor_Documentacao_2026-06-29]] e [[50_Registros/Sessoes/2026-06-29_cursor-sessao-validacao-rag]].
