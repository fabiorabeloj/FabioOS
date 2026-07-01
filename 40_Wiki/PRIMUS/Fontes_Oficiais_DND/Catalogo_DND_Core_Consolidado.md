---
tipo: catalogo
area: 40_Wiki
projeto: PRIMUS
status: ativo
classe_dado: Restricted
criado_em: 2026-07-01
tags: [primus, dnd, catalogo, restricted, official-core, obsidian]
---

# Catalogo DND Core Consolidado

## Funcao

Representar os livros oficiais DND Core no Obsidian sem criar uma bolha solta para cada registro.

Este catalogo substitui a estrategia de `10603` stubs individuais.

## Decisao

Livro oficial nao vira milhares de notas.

Ele entra no FabioOS como:

```text
PDF / PRIMUS Index
  -> indice seguro consolidado
  -> catalogo por livro/categoria
  -> selecao de candidatos
  -> nota promovida somente com V(E)
```

## Contagem Tecnica

| Livro | Book key | Registros no PRIMUS Index |
|---|---|---:|
| Livro do Jogador 2014 | `phb` | 3880 |
| Guia do Mestre 2014 | `dmg` | 3629 |
| Manual dos Monstros 2014 | `mm` | 3094 |
| **Total** |  | **10603** |

## Navegacao Segura

- [[40_Wiki/PRIMUS/Fontes_Oficiais_DND/DND_Core_PHB_2014_Index_Seguro]]
- [[40_Wiki/PRIMUS/Fontes_Oficiais_DND/DND_Core_DMG_2014_Index_Seguro]]
- [[40_Wiki/PRIMUS/Fontes_Oficiais_DND/DND_Core_MM_2014_Index_Seguro]]
- [[40_Wiki/PRIMUS/Fontes_Oficiais_DND/Wikilinks_DND_Core_PRIMUS]]

## Politica de Nos

| Tipo | Vira nota individual? | Regra |
|---|---|---|
| Registro bruto de indice | nao | fica em SQLite/indice consolidado |
| Stub automatico massivo | nao | gera ruido no grafo |
| Conceito recorrente | sim | se for util e transformativo |
| Item/arma/magia/criatura especifica | talvez | somente se entrar em CatalogPool ou missao |
| Faccao/lugar/procedimento relevante | sim | apos V(E) |
| Conteudo oficial textual | nao | manter restrito |

## Promocao Correta

Um registro so vira nota quando responder:

1. por que isso importa para o PRIMUS?
2. que problema, tensao, missao ou decisao ele gera?
3. qual fonte/pagina sustenta a entrada?
4. qual parte e autoral/transformativa?
5. qual parte permanece restrita?

## Proximo Lote Recomendado

Promover poucas notas fortes:

- 10 armas ou equipamentos como papeis taticos;
- 10 criaturas como funcoes de encontro;
- 10 procedimentos de mundo/campanha;
- 5 estruturas de faccao, renome ou recompensa.

## Links

- [[40_Wiki/_MOCs/MOC_PRIMUS]]
- [[40_Wiki/PRIMUS/Fontes_Oficiais_DND/README]]
- [[80_Specs/PRIMUS/Spec_Markdownizacao_Segura_Livros_PRIMUS]]
- [[50_Registros/Decisoes/ADR_2026-07-01_Catalogo_DND_Core_Sem_Stubs_Massivos]]
