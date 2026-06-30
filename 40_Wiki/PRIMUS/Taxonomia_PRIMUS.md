---
tipo: wiki
area: 40_Wiki
projeto: PRIMUS
status: ativo
fonte: [[90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/PRIMUS/02_TIPOS_PRIMUS]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, taxonomia, tipos, wiki]
---

# Taxonomia PRIMUS

## Funcao

Definir quais tipos podem entrar na Enciclopedia do PRIMUS.

## Regra

Sem tipo, nao entra em E.

## Familias

| Familia | Tipos |
|---|---|
| Player | `race`, `subrace`, `species_trait`, `class`, `subclass`, `background`, `feat`, `proficiency`, `equipment`, `language` |
| Spell/Power | `spell`, `cantrip`, `ritual`, `condition`, `damage_type`, `effect` |
| Item/Loot | `item`, `magic_item`, `artifact`, `consumable`, `currency`, `loot_table`, `recipe` |
| NPC/Creature/Deity | `creature`, `npc`, `deity`, `spirit`, `undead`, `construct`, `boss` |
| World/Atlas | `plane`, `domain`, `region`, `biome`, `settlement`, `landmark`, `site`, `dungeon`, `room`, `hazard`, `trap`, `puzzle`, `secret` |
| Faction/Law/Culture | `faction`, `organization`, `guild`, `religion`, `culture`, `law`, `taboo`, `festival`, `trade_network` |
| Rule/Engine | `rule`, `procedure`, `generator`, `table`, `formula`, `constraint`, `template` |
| Instance/Mission | `mission`, `objective`, `gate`, `encounter`, `event`, `questline`, `reward`, `consequence` |
| Persistence/DeltaP | `world_flag`, `access_key`, `reputation`, `debt`, `curse`, `boon`, `scar`, `death_record`, `item_transfer`, `ownership`, `timer_state` |

## Uso no FabioOS

Esta taxonomia deve orientar:

- ingestao de fontes PRIMUS;
- criacao de templates;
- indexacao futura no RAG/Grafo;
- agente `primus-lorekeeper`;
- validacao de missoes e Delta P.

## Lacunas

- Falta separar `canon`, `rascunho`, `inspiracao` e `externo` no frontmatter.
- Falta definir IDs estaveis para entidades.
- Falta mapear equivalencia entre categorias do PRIMUS-TAXON (`ENTIDADES`, `LOCAIS`, `GRUPOS`, `FUNCOES`, `OBJETOS`, `EVENTOS`) e os tipos canonicos.
- Falta converter esta pagina para schema executavel quando WorldState e Tension Engine estiverem definidos.

## Relacoes

- [[PrimusOS]]
- [[Circuito_EIP]]
- [[Tipagem_Universal_PRIMUS]]
- [[80_Specs/PRIMUS/Spec_Ingestao_PRIMUS_ChatGPT]]
