---
tipo: changelog
area: 50_Registros
projeto: PRIMUS
status: concluido
classe_dado: interno
criado_em: 2026-07-01
tags: [primus, changelog, dnd, catalogo, obsidian]
---

# Changelog - Catalogo DND Core sem Stubs Massivos

## Entrega

- Removida a camada massiva `Stubs/` da wiki ativa.
- Criado catalogo consolidado dos livros oficiais DND Core.
- Criada ADR determinando que registros brutos nao viram bolinhas no Obsidian.
- Atualizados MOC, README, SPEC, plano, log e registro de frentes.

## Decisao

O Obsidian e para conhecimento processado e conectado.

SQLite/JSONL/indices sao para registros brutos e catalogo tecnico.

## Arquivos Principais

- [[40_Wiki/PRIMUS/Fontes_Oficiais_DND/Catalogo_DND_Core_Consolidado]]
- [[50_Registros/Decisoes/ADR_2026-07-01_Catalogo_DND_Core_Sem_Stubs_Massivos]]

## Limites

- Sem RAG/reindex.
- Sem push.
- Sem texto integral de livro.
