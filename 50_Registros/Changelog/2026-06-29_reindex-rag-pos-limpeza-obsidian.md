---
tipo: changelog
area: 50_Registros
projeto: FabioOS
status: registrado
tags: [fabios, changelog, rag, reindexacao, obsidian]
criado_em: 2026-06-29
agente: Codex
---

# Changelog — Reindex RAG pos-limpeza Obsidian

## Resumo

Reindexado o `fabioos_db` apos a limpeza visual da raiz do Obsidian para remover caminhos antigos do indice RAG.

## Resultado

- Corpus operacional: `1206` chunks.
- Validacao: `10/10` perguntas boas.
- Seguranca: `0` falhas.
- Modo: recuperacao local, sem `--generate`, sem API externa.

## Ajustes

- `ingest_vault.py` passou a usar corpus operacional de alto sinal.
- `query_rag.py` passou a priorizar o caminho real do Painel de Pendencias arquivado.
- `batch_validate_rag.py` foi atualizado para validar os caminhos reais pos-limpeza.

## Limites

- `fabioos_db/` continua fora do Git.
- Reindexacao incremental ainda pendente.
- Promocao da Fase 12 para piloto depende de revisao do Claude.
