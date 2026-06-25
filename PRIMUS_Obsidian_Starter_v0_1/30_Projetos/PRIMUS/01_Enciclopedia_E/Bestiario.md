---
project: PRIMUS
object: book
type: index
status: draft
face: E
book: Bestiario
tags: [primus, bestiario, entidades]
---

# Livro II — Bestiário

Função: tudo que age no mundo.

## Inclui

- criaturas
- NPCs
- chefes
- deuses
- avatares
- entidades extraplanares

## Entradas

```dataview
TABLE type, name, cr, source_pdf, page, confidence
FROM "30_Projetos/PRIMUS"
WHERE project = "PRIMUS" AND object = "CatalogEntry" AND book = "Bestiario"
SORT type ASC, name ASC
```
