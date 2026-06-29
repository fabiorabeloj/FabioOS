---
tipo: wiki
area: wiki
projeto: FabioOS
status: ativo
tags: [conceito, banco-vetorial, embeddings, chroma, qdrant, memoria, fase-12]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Banco Vetorial

## Função

Banco de dados que armazena **embeddings** (vetores numéricos que representam o significado de um texto) e permite **busca por similaridade**. É a infraestrutura que torna o [[wiki/conceitos/rag|RAG]] possível: a pergunta vira vetor, e o banco devolve os trechos mais próximos semanticamente.

## Contexto

No FabioOS, cada chunk de nota é convertido em vetor por um modelo de embedding **local** (`bge-m3`, forte em PT-BR) e gravado com metadados (caminho, cabeçalho, tags, wikilinks). A busca usa distância de cosseno.

| Tecnologia | Papel no FabioOS |
|---|---|
| **Chroma** | Banco vetorial da v1 (local, embutido) — ver [[60_Sistemas/RAG/Arquitetura_RAG_FabioOS]] |
| **Qdrant** | Caminho de escala futuro (Docker, filtros avançados, acesso concorrente) |

## Como usar

- A implementação e a decisão Chroma→Qdrant estão em [[60_Sistemas/RAG/Arquitetura_RAG_FabioOS]].
- O índice local fica em `60_Sistemas/RAG/fabioos_db/` (gitignored — regenerável via `ingest_vault.py`).
- Não indexar dados sensíveis: a ingestão exclui `sources/_inbox/`, logs Pietra, `.venv/` e logs runtime.

## Relações

- [[wiki/conceitos/rag]]
- [[60_Sistemas/RAG/Arquitetura_RAG_FabioOS]]
- [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]]

## Próximas ações

- [ ] Avaliar migração para Qdrant quando a Interface/multiagentes exigirem concorrência
- [ ] Reindexação incremental por hash (hoje a ingestão é reindex limpo)
