---
project: PRIMUS
object: dashboard
type: dashboard
status: active
face: EIP
tags: [primus, dashboard]
---

# Dashboard PRIMUS

## Visão E/I/P

```dataview
TABLE object, type, status, face
FROM "30_Projetos/PRIMUS"
WHERE project = "PRIMUS"
SORT face ASC, type ASC
```

## Entradas sem fonte

```dataview
TABLE type, name, source_pdf, page, confidence
FROM "30_Projetos/PRIMUS"
WHERE project = "PRIMUS" AND object = "CatalogEntry" AND (source_pdf = "" OR !source_pdf)
SORT type ASC
```

## Entradas sem instanciamento

```dataview
TABLE type, name, instancing_hints
FROM "30_Projetos/PRIMUS"
WHERE project = "PRIMUS" AND object = "CatalogEntry" AND length(instancing_hints) = 0
SORT type ASC
```

## Missões planejadas

```dataview
TABLE mission_id, letters, objective, risk_level, returns_deltaP
FROM "30_Projetos/PRIMUS"
WHERE project = "PRIMUS" AND object = "InstanceMission" AND status = "planned"
SORT mission_id DESC
```

## ΔP recentes

```dataview
TABLE delta_type, target_id, value_after, mission_id, timestamp
FROM "30_Projetos/PRIMUS"
WHERE project = "PRIMUS" AND object = "PersistenceDelta"
SORT timestamp DESC
LIMIT 20
```

## Changelog

```dataview
TABLE version, date, scope, status
FROM "30_Projetos/PRIMUS"
WHERE project = "PRIMUS" AND object = "changelog"
SORT date DESC
```
