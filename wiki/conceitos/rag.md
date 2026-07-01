---
tipo: wiki
area: wiki
projeto: FabioOS
status: ativo
tags:
  - conceito
  - rag
  - recuperacao-semantica
  - memoria
  - fase-12
criado_em: 2026-06-27
atualizado_em: 2026-06-29
---

# RAG — Recuperação Aumentada por Geração

## Função

RAG (*Retrieval-Augmented Generation*) é a camada de **memória semântica** do FabioOS: recupera trechos relevantes do vault por **significado** (não por palavra-chave) e os entrega como contexto para uma resposta fundamentada e rastreável.

## Contexto

No [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON|Modelo Formal]], RAG é uma **camada auxiliar da memória**, não um fim. Ele **consulta** o conhecimento organizado no Obsidian — não o substitui. É o primeiro tijolo cognitivo que o MEGATRON consome.

```
pergunta → embedding local → busca top-k no banco vetorial → contexto → resposta com fontes
```

## Como usar

- **Arquitetura e decisões da implementação:** [[60_Sistemas/RAG/Arquitetura_RAG_FabioOS]] (Chroma + `bge-m3` local + Claude).
- **Banco vetorial subjacente:** [[wiki/conceitos/banco-vetorial]].
- **Regra de qualidade:** se não houver fonte suficiente, o sistema declara ignorância (Regra da Ignorância Explícita) em vez de alucinar.
- **Scripts e comandos:** [[60_Sistemas/RAG/README_Scripts_RAG]] — venv, `query_rag.py`, `batch_validate_rag.py`.
- **Validação (2026-06-29):** 10/10 perguntas de aceitação em modo recuperação — [[60_Sistemas/RAG/Relatorio_Validacao_RAG_2026-06-29_Cursor]]; evidência JSON em `validacao_pos_ranking_2026-06-29.json`.
- **Sessão Cursor:** inventário completo em [[50_Registros/Sessoes/2026-06-29_cursor-sessao-validacao-rag]].

## Relações

- [[60_Sistemas/RAG/Arquitetura_RAG_FabioOS]]
- [[wiki/conceitos/banco-vetorial]]
- [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]]
- [[60_Sistemas/RAG/README_Scripts_RAG]]
- [[60_Sistemas/RAG/Relatorio_Validacao_RAG_2026-06-29_Cursor]]
- [[50_Registros/Sessoes/2026-06-29_cursor-sessao-validacao-rag]]

## Próximas ações

- [x] Concluir a validação da Fase 12 (consultas em modo recuperação) — 10/10 em 2026-06-29
- [x] Conectar o RAG ao grafo (Fase 13) e ao MEGATRON v0
- [ ] Claude/Codex decidir promoção da Fase 12 para piloto
- [ ] Reindexação incremental após novos docs (LLM Wiki, matriz de aptidão)
