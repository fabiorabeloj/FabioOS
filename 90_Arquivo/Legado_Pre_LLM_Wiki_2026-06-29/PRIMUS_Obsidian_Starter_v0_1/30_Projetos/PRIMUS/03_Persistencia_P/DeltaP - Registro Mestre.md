---
project: PRIMUS
object: register
type: index
status: active
face: P
tags: [primus, deltap, registro]
---

# ΔP — Registro Mestre

## Tipos aceitos

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

## Entradas ΔP

```dataview
TABLE delta_id, delta_type, scope, target_id, value_before, value_after, mission_id, timestamp
FROM "30_Projetos/PRIMUS"
WHERE project = "PRIMUS" AND object = "PersistenceDelta"
SORT timestamp DESC
```
