---
project: PRIMUS
object: WorldState
type: world_state
status: active
face: P
tags: [primus, worldstate, persistencia]
---

# WorldState PRIMUS

O WorldState é o estado acumulado do mundo.  
Nada persiste narrativamente sem registro operacional.

## Estado global

```dataview
TABLE delta_type, scope, target_id, value_after, mission_id, timestamp
FROM "30_Projetos/PRIMUS"
WHERE project = "PRIMUS" AND object = "PersistenceDelta"
SORT timestamp DESC
```

## WorldFlags ativos

```dataview
TABLE target_id, value_after, mission_id, justification
FROM "30_Projetos/PRIMUS"
WHERE project = "PRIMUS" AND object = "PersistenceDelta" AND delta_type = "world_flag"
SORT timestamp DESC
```

## AccessKeys liberadas

```dataview
TABLE target_id, value_after, mission_id, justification
FROM "30_Projetos/PRIMUS"
WHERE project = "PRIMUS" AND object = "PersistenceDelta" AND delta_type = "access_key"
SORT timestamp DESC
```

## Reputações

```dataview
TABLE target_id, value_after, mission_id, justification
FROM "30_Projetos/PRIMUS"
WHERE project = "PRIMUS" AND object = "PersistenceDelta" AND delta_type = "reputation"
SORT timestamp DESC
```
