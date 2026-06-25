---
project: PRIMUS
object: book
type: index
status: draft
face: E
book: Atlas
tags: [primus, atlas, mundo]
---

# Livro IV — Atlas

Função: mundo consultável e gerador de sementes de missão.

## Regra

Atlas descreve o mundo; não executa o jogo.

## Inclui

- regiões
- biomas
- assentamentos
- rotas
- dungeons como blueprints
- locais notáveis
- facções e organizações

## Entradas

```dataview
TABLE type, name, region, mission_seeds, confidence
FROM "30_Projetos/PRIMUS"
WHERE project = "PRIMUS" AND object = "CatalogEntry" AND book = "Atlas"
SORT type ASC, name ASC
```
