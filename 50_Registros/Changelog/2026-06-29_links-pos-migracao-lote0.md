---
tipo: changelog
area: 50_Registros
projeto: FabioOS
status: registrado
data: 2026-06-29
tags: [fabios, obsidian, links, migracao, codex, claude]
---

# Changelog - Links pos-migracao lote 0

## Contexto

Claude registrou ordens para o Codex em `60_Sistemas/FabioOS/Ordens_Arquiteto_Para_Codex_2026-06-29.md`.

A primeira ordem era auditar e corrigir wikilinks antigos:

- `[[wiki/...]]` -> `[[40_Wiki/_compat_wiki/...]]`
- `[[sources/...]]` -> `[[05_Raw_Sources/_compat_sources/...]]`

## Resultado do lote

- Busca executada: `rg -n "\[\[(wiki|sources)/" --glob "*.md"`
- Ocorrencias encontradas fora do arquivo de ordens antes da triagem: `7`
- Pendencias operacionais apos arquivar a duplicata: `5` arquivos
- Links corrigidos neste lote: `0`
- Ancora alterada: `0`
- Pasta `wiki/` recriada na raiz: encontrada com `wiki/conceitos/rag.md`
- A duplicata era identica a `40_Wiki/_compat_wiki/conceitos/rag.md`
- Acao: duplicata preservada em `90_Arquivo/Descartes_Visuais_Obsidian_2026-06-29/wiki_recriado_pos_migracao_2026-06-29/`
- Observacao: a pasta `wiki/` foi recriada uma segunda vez durante a rodada; a copia identica foi preservada em `90_Arquivo/Descartes_Visuais_Obsidian_2026-06-29/wiki_recriado_pos_migracao_2026-06-29_02/`

## Decisao

Nao houve correcao automatica dos links restantes porque eles apareceram em arquivos ja modificados por outra frente e/ou dentro da zona RAG/Cursor.

Pela regra anti-colisao, o Codex registrou a auditoria e preservou a duplicata recriada fora da raiz, mas nao editou os arquivos sujos de outra frente.

## Pendencias encontradas para handoff

- `60_Sistemas/RAG/README_Scripts_RAG.md`
- `60_Sistemas/RAG/Arquitetura_RAG_FabioOS.md`
- `60_Sistemas/FabioOS/Frente_Cursor_Documentacao_2026-06-29.md`
- `60_Sistemas/Cursor/README_Cursor_FabioOS.md`
- `50_Registros/Sessoes/2026-06-29_cursor-sessao-validacao-rag.md`

O arquivo de ordens do Claude tambem contem exemplos literais de `[[wiki/...]]` e `[[sources/...]]`; estes foram preservados como texto de instrucao.

## Limites respeitados

- Sem RAG reindex.
- Sem tocar `fabioos_db`.
- Sem editar scripts RAG.
- Sem tocar `60_Sistemas/MEGATRON/`.
- Sem tocar `60_Sistemas/MCP_FabioOS/`.
- Sem runtime, OpenClaw, n8n, WhatsApp ou Google.
- Sem push.
