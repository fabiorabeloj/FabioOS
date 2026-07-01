---
tipo: relatorio
area: 50_Registros
projeto: FabioOS
status: concluido
agente: Cursor
classe_dado: interno
criado_em: 2026-07-01
tags: [fabios, bugbot, intake, agentarium, mesa-despacho, cursor]
---

# Bugbot + Mesa de Despacho — Intake Universal v0.9.0 (Cursor)

## Entrega

Ordem Claude (barramento 16:04) + pedido Fabio (opcao 3: bugbot + melhor possivel).

### Agentarium v0.9.0 — aba **Aguardando Fabio**

| Recurso | Implementacao |
|---------|---------------|
| Fila intake | `GET /integrations/intake-dispatch/status` |
| Aprovar | `POST .../cards/:id/approve` → `arquivista_intake.py --aprovar` |
| Rejeitar | `POST .../cards/:id/reject` → status archived + log |
| Comando natural | `POST .../command` → `universal_intake_adapter.py` |
| Regenerar demo | `POST .../refresh-flow` → `intake_flow.py` |
| Coordenacao | header via `coordenacao.py --json` |
| WebSocket | `intake_dispatch_snapshot` |
| Watcher | `state/intake_queue.json` + sample |

Frontend: `IntakeDispatchPanel.tsx` — cards, badges, trava sensivel, nota_ref quando executed.

### Bugbot — ciclo ponta a ponta

Script: `60_Sistemas/FabioOS/scripts/smoke_intake_ciclo_completo.ps1`

Prova:
1. `intake_flow.py` → fila
2. `arquivista_intake.py --aprovar escolaos` → `.md` em `00_Inbox/Triagem/`
3. `--aprovar saude` → bloqueado (trava §3)
4. validator OK pos-patch
5. adapter comando natural → `escolaos`

### Patches auxiliares

- `universal_intake_validator.py`: aceita `nota_ref`, hash 6+ chars, status pos-aprovacao

## Alinhamento diagnostico Claude

| Item Claude | Status pos-entrega |
|-------------|-------------------|
| Espinha classificacao | OK (provado) |
| Aprovacao interativa | OK (UI + arquivista) |
| Escrita Obsidian | OK (nota em Triagem) |
| Sensivel nao grava | OK (blocked) |
| Fila consumivel | OK (live + sample fallback) |

## Teste minimo Fabio

```powershell
# 1. Ciclo bugbot
.\60_Sistemas\FabioOS\scripts\smoke_intake_ciclo_completo.ps1

# 2. UI
.\start_agentarium.ps1
# Abrir http://127.0.0.1:5174 → aba "Aguardando Fabio"
```

## Arquivos principais

- `apps/agentarium/backend/src/intakeDispatch/*`
- `apps/agentarium/frontend/src/components/IntakeDispatchPanel.tsx`
- `60_Sistemas/FabioOS/scripts/smoke_intake_ciclo_completo.ps1`

## Pendencias (nao Cursor)

- Gmail real → Codex
- Extracao estruturada serie/tema/prazo no comando — Claude/Codex
- Unificar IDs intake_flow (sem hash) vs adapter (com hash) — Codex
