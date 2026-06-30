---
tipo: board
area: 30_Projetos
projeto: PRIMUS
status: prototipo-operacional
fonte: [[80_Specs/PRIMUS/Spec_Cantina_Conflict_Engine_PRIMUS]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, cantina, board, player-view]
---

# Cantina Board 0001 PRIMUS

## Funcao

Mostrar o que pode aparecer ao jogador sem revelar a Enciclopedia completa.

## Estado

Prototipo seguro. Ainda nao e Missao 0001.

## Cartoes

| CardID | Origem | Titulo | Visivel | Estado | Acao |
|---|---|---|---|---|---|
| CARD-0001 | CCF-0002 | Quadro de rumores da Cantina | sim | disponivel | usar [[Cantina_Rumores_0001_PRIMUS]] |
| CARD-0002 | CCF-0004 | Ver nao e ter | sim | regra em teste | manter limite Player View |
| CARD-0003 | CCF-0005 | Missao sem DeltaP previsto | nao | bloqueado | preencher Mission Contract |

## Player View Segura

O jogador pode ver:

- rumores;
- ganchos;
- risco aparente;
- recompensa aparente;
- aviso de incerteza.

O jogador nao pode ver:

- CatalogEntries completas;
- fontes internas;
- DeltaP oculto;
- estado real de viloes ocultos;
- conflitos que ainda estao bloqueados.

## Proxima Acao

Quando 5 CatalogEntries forem validadas, escolher um card e preencher [[Mission_Contract_0001_PRIMUS]].
