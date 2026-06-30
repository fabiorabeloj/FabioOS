---
project: PRIMUS
object: book
type: index
status: draft
face: I
book: Motor
tags: [primus, missoes, instancia]
---

# Missões PRIMUS

## Definição

Missão não é narrativa aberta. Missão é contrato executável.

## Campos mínimos

- MissionID
- Letras A–F
- Objetivo
- Gate
- Condição de sucesso
- Condição de falha
- Risco
- Recompensa
- ΔP
- Elementos consumidos de E
- Retorno à Cantina

## Missões

```dataview
TABLE mission_id, letters, objective, risk_level, status, returns_deltaP
FROM "30_Projetos/PRIMUS"
WHERE project = "PRIMUS" AND object = "InstanceMission"
SORT mission_id DESC
```
