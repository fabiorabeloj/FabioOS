---
tipo: catalogentries
area: 30_Projetos
projeto: PRIMUS
status: bootstrap
fonte: [[40_Wiki/PRIMUS/Matriz_Fontes_PRIMUS]]
spec: [[80_Specs/PRIMUS/Spec_CatalogEntry_PRIMUS]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, catalogentry, lote-0001, enciclopedia]
---

# CatalogEntries - Lote 0001

## Aviso de Precisao

Este lote cria entradas estruturais iniciais a partir das fontes do Project ChatGPT. As paginas/trechos dos PDFs ainda precisam ser validados antes de promocao para `pool-ready`.

## Entradas D&D Core

| ID | Type | Name | Class Base | Source | Instancing Hint | Status |
|---|---|---|---|---|---|---|
| CE-DND-0001 | player_character | Player Character | Agent | D&D Core | ator jogavel de instancia | fonte-pendente |
| CE-DND-0002 | class | Class | Entity | D&D Core | define progressao de personagem | VE-local-index-pass |
| CE-DND-0003 | species | Species/Race | Entity | D&D Core | define origem jogavel | VE-local-index-partial |
| CE-DND-0004 | background | Background | Entity | D&D Core | gera pericias, historia e gancho | VE-local-index-pass |
| CE-DND-0005 | spell | Spell | Entity | D&D Core | efeito mecanico em encontro | VE-local-index-pass |
| CE-DND-0006 | equipment | Equipment | Object | D&D Core | recurso de personagem ou recompensa | fonte-pendente |
| CE-DND-0007 | creature | Creature | Agent | Monster Manual | ator antagonista/neutro | fonte-pendente |
| CE-DND-0008 | condition | Condition | State | D&D Core | estado temporario em instancia | VE-local-index-pass |
| CE-DND-0009 | encounter | Encounter | Event | D&D Core/DMG | unidade de desafio | fonte-pendente |
| CE-DND-0010 | treasure | Treasure | Object | DMG | recompensa e possivel DeltaP | fonte-pendente |

## Entradas Sandbox / WWN

| ID | Type | Name | Class Base | Source | Instancing Hint | Status |
|---|---|---|---|---|---|---|
| CE-WWN-0001 | region | Region | Place | WWN | area para WorldState | fonte-pendente |
| CE-WWN-0002 | site | Site | Place | WWN | local de exploracao | fonte-pendente |
| CE-WWN-0003 | faction | Faction | Agent | WWN/SWN | ator coletivo | fonte-pendente |
| CE-WWN-0004 | tag | Tag | Relation | WWN | modificador semantico de local/ator | fonte-pendente |
| CE-WWN-0005 | ruin | Ruin | Place | WWN | dungeon/site exploravel | fonte-pendente |
| CE-WWN-0006 | settlement | Settlement | Place | WWN | hub/local social | fonte-pendente |
| CE-WWN-0007 | world_event | World Event | Event | WWN | update fora de missao | fonte-pendente |
| CE-WWN-0008 | problem | Problem | Event | WWN | origem de conflito candidato | fonte-pendente |
| CE-WWN-0009 | patron | Patron | Agent | WWN | gerador de contrato de missao | fonte-pendente |
| CE-WWN-0010 | exploration_hook | Exploration Hook | Event | WWN | entrada para Engrenagem 6 | fonte-pendente |

## Campos Padrao do Lote

```yaml
source_layer: bootstrap
box: Enciclopedia Funcional
subbox: canon_or_framework
affects:
  - CatalogPool
  - InstanceSeed
never_affects:
  - regra_base_sem_validacao
  - WorldState_sem_DeltaP
portability: portable
confidence: baixa_ate_validar_pagina
```

## Proxima Acao

Continuar V(E) no lote: revisar `CE-DND-0003` e validar entradas restantes com fonte/pagina via [[Validacao_VE_5_Entradas_PRIMUS_Index]].
