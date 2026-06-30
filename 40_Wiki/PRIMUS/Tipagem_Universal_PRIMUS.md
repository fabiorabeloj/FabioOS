---
tipo: wiki
area: 40_Wiki
projeto: PRIMUS
status: ativo
fonte: [[05_Raw_Sources/PRIMUS/2026-06-30_google-doc_primus_contexto_completo_final]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, tipos, schema, catalogo, eip]
---

# Tipagem Universal PRIMUS

## Funcao

Formalizar a regra: nada entra no PRIMUS sem Type.

## Registro Minimo

```yaml
id:
type:
name:
source:
page:
snippet:
box:
subbox:
affects:
never_affects:
portability:
tags:
confidence:
```

## Familias de Tipos

| Familia | Exemplos de tipos |
|---|---|
| Player | `race`, `subrace`, `species_trait`, `class`, `subclass`, `background`, `feat`, `proficiency`, `language` |
| Spell/Power | `spell`, `cantrip`, `ritual`, `condition`, `damage_type`, `effect` |
| Item/Loot | `item`, `magic_item`, `artifact`, `consumable`, `currency`, `loot_table`, `recipe` |
| NPC/Creature/Deity | `creature`, `npc`, `deity`, `spirit`, `demon`, `angel`, `undead`, `construct`, `boss` |
| World/Atlas | `plane`, `domain`, `region`, `biome`, `route`, `settlement`, `district`, `landmark`, `site`, `dungeon`, `room`, `trap`, `puzzle`, `secret` |
| Faction/Law/Culture | `faction`, `organization`, `guild`, `religion`, `culture`, `custom`, `law`, `taboo`, `festival`, `trade_network` |
| Rule/Engine | `rule`, `procedure`, `generator`, `table`, `formula`, `constraint`, `template` |
| Instance/Mission | `mission`, `objective`, `gate`, `encounter`, `event`, `questline`, `reward`, `consequence` |
| Persistence/DeltaP | `world_flag`, `access_key`, `reputation`, `debt`, `curse`, `boon`, `scar`, `death_record`, `item_transfer`, `ownership`, `timer_state` |

## Campos de Controle

- `Affects`: o que a entrada pode afetar.
- `NeverAffects`: o que ela nunca pode afetar.
- `Portability`: portable, persistent ou local.
- `Confidence`: nivel de confianca da extracao.
- `Subbox`: canon, setting, homebrew ou framework.

## Relacao com EIP

| Tipo de conteudo | Face dominante |
|---|---|
| Catalogo, regra, local, entidade | E |
| Missao, encontro, evento, contrato | I |
| Consequencia, reputacao, divida, item transferido | P |

## Relacoes

- [[Taxonomia_PRIMUS]]
- [[Leis_do_PRIMUS]]
- [[Pipeline_PRIMUS]]
- [[Livros_do_PRIMUS]]
