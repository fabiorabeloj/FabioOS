---
tipo: spec
area: 80_Specs
projeto: PRIMUS
status: rascunho
fonte: [[40_Wiki/PRIMUS/Falhas_Ontologicas_PRIMUS]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, spec, ontologia, entidades, eventos, estados]
---

# SPEC - Ontologia Formal PRIMUS

## Objetivo

Separar o que existe, o que acontece e o que muda no PRIMUS.

## Classes Base

| Classe | Definicao | Exemplos |
|---|---|---|
| Entity | algo com identidade estavel | criatura, item, local, faccao, deidade |
| Event | algo que ocorre e transforma estado | missao, encounter, operacao, morte |
| State | condicao derivada | reputacao, flag, acesso, divida |
| Agent | entidade com intencao e capacidade de acao | jogador, NPC, faccao, criatura inteligente |
| Relation | ligacao tipada entre objetos | pertence, afeta, depende, ocorre_em |
| Boundary | fronteira formal de uma instancia | missao, dungeon, cena |
| Value | medida de risco/recompensa/custo | recompensa, risco, prioridade |

## Hierarquia Inicial

```text
Entity
-> Agent
   -> PlayerCharacter
   -> NPC
   -> Creature
   -> Faction
   -> Deity
-> Object
   -> Item
   -> Artifact
   -> Currency
-> Place
   -> Region
   -> Settlement
   -> Site
   -> Dungeon
   -> Plane

Event
-> Mission
-> Encounter
-> FactionProject
-> WorldUpdate

State
-> WorldState
-> InstanceState
-> ActorState
-> DeltaP
```

## Relacoes Tipadas Minimas

| Relacao | Uso |
|---|---|
| `requires` | uma coisa exige outra |
| `belongs_to` | pertence a livro, setting, faccao ou familia |
| `affects` | pode alterar algo |
| `never_affects` | limite explicito |
| `inhabits` | entidade habita local |
| `controls` | faccao controla local/recurso |
| `occurs_in` | evento ocorre em local/instancia |
| `produces_delta` | evento gera DeltaP |
| `updates_state` | DeltaP altera estado |

## Criterios de Aceite

- Nenhum objeto novo entra sem classe base.
- Nenhum evento executavel entra sem pre-condicao e pos-condicao.
- Nenhum estado muda sem DeltaP.
- Nenhuma relacao importante fica apenas em texto livre.

## Proxima Entrega

Converter CatalogEntries reais para esta ontologia minima.
