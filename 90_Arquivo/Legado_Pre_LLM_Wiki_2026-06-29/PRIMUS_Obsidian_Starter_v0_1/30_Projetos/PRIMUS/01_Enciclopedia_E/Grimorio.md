---
project: PRIMUS
object: book
type: index
status: draft
face: E
book: Grimorio
tags: [primus, grimorio, jogador]
---

# Livro I — Grimório

Função: tudo que entra diretamente na ficha ou na experiência do jogador.

## Seções

- Espécies, raças e linhagens
- Classes e subclasses
- Antecedentes
- Talentos
- Equipamentos
- Itens
- Magias
- Poderes
- Idiomas
- Proficiências

## Entradas do Grimório

```dataview
TABLE type, name, source_pdf, page, confidence
FROM "30_Projetos/PRIMUS"
WHERE project = "PRIMUS" AND object = "CatalogEntry" AND book = "Grimorio"
SORT type ASC, name ASC
```
