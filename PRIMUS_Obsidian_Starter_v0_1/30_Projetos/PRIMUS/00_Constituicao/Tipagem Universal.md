---
project: PRIMUS
object: constitution
type: rule
status: stable
face: E
tags: [primus, tipagem, catalogo]
---

# Tipagem Universal PRIMUS

## Lei

Nada entra no PRIMUS sem tipo.

## Famílias de tipos

### PLAYER

- race
- subrace
- lineage
- species_trait
- name_list
- class
- subclass
- class_feature
- background
- feat
- proficiency
- equipment
- weapon
- armor
- tool
- language

### SPELL / POWER

- spell
- spell_list
- cantrip
- ritual
- condition
- damage_type
- effect

### ITEM / LOOT

- item
- magic_item
- artifact
- consumable
- container
- currency
- loot_table
- craft_rule
- recipe
- trade_good

### ENTITY

- creature
- npc
- deity
- spirit
- demon
- angel
- undead
- construct
- boss

### WORLD / ATLAS

- cosmology_model
- plane
- domain
- realm
- region
- biome
- route
- settlement
- district
- landmark
- site
- dungeon
- level
- room
- feature
- hazard
- trap
- puzzle
- secret

### SOCIAL / CULTURE

- faction
- organization
- guild
- religion
- culture
- custom
- law
- taboo
- architecture_pattern
- cuisine
- festival
- trade_network

### RULE / ENGINE

- rule
- procedure
- generator
- table
- formula
- constraint
- template

### INSTANCE / MISSION

- mission
- objective
- gate
- encounter
- combat_encounter
- social_encounter
- exploration_encounter
- event
- questline
- reward
- consequence

### PERSISTENCE / ΔP

- world_flag
- access_key
- reputation
- debt
- curse
- boon
- scar
- death_record
- item_transfer
- ownership
- timer_state

## Consulta Dataview

```dataview
TABLE type, face, status, confidence
FROM "30_Projetos/PRIMUS"
WHERE project = "PRIMUS" AND object = "CatalogEntry"
SORT type ASC
```
