---
tipo: relatorio
area: 50_Registros
projeto: FabioOS
status: concluido
agente: Cursor
classe_dado: interno
criado_em: 2026-07-01
tags: [fabios, bugbot, onda1, intake, cursor]
---

# Bugbot Onda 1 — Entradas Sensoriais (2026-07-01)

## Resumo

| Canal | Script/modulo | Smoke | Veredito |
|-------|---------------|-------|----------|
| E-mail | `email_intake_dry_run.py` | OK | Script OK; **pipeline Gmail ausente** |
| Intake universal | `intake_flow.py` + `megatron_core.py` | OK | Fila + redacao token OK |
| PDF drop | `watch_pdf_drop.py` | OK | 5 PDFs ja indexados (skipped) |
| PietraOS | `pietra_inbox.py` + `pietra_state.py` | OK | Sensivel bloqueado; state manual |
| n8n | 6 workflows JSON | auditado | **Sem Gmail Trigger** |
| WhatsApp | Agentarium `personalHandler.ts` | build OK | `canSend: false` sempre |
| Mobile | `mobile_gateway_fabioos.py` | nao rodado | Servidor nao iniciado nesta sessao |
| Dashboard | `dashboard_fabioos.py` | OK | Gera `10_Mapas/Dashboard_Operacional_FabioOS.md` |

**Reteste:** `.\60_Sistemas\FabioOS\scripts\smoke_intake_onda1.ps1`

---

## Achados por severidade

### Alta — fluxo morto (handoff Codex/Fabio)

| ID | Achado | Evidencia |
|----|--------|-----------|
| A1 | Gmail nao alimenta FabioOS automaticamente | Nenhum workflow `FabioOS_Gmail_*`; export Codex manual |
| A2 | Dois classificadores divergentes | Mesmo e-mail escola: `email_intake` → `pietraos`; `megatron_core` → `escolaos` |
| A3 | `email_intake` e `intake_queue.json` desconectados | Saida Markdown vs JSON; ordem Codex Inbox Universal v0.1 aberta |

### Media

| ID | Achado | Evidencia |
|----|--------|-----------|
| M1 | `pietra_state.json` nao e regenerado sozinho | `colegio-pietra` so tinha `atendimentos.jsonl` ate rodar `pietra_state.py` |
| M2 | n8n ativo depende de Docker :5678 | Workflows existem no repo; runtime nao validado nesta sessao |
| M3 | `megatron_core.classificar_intake` retorna `summary` cru | `intake_flow` redige na fila; CLI direto pode vazar segredo |

### Baixa — OK ou corrigido

| ID | Achado | Status |
|----|--------|--------|
| B1 | Payload e-mail vazio gerava relatorio vazio | **Corrigido** (sessao anterior) |
| B2 | `watch_pdf_drop` path escape | Rejeita saida fora do vault (email script) |
| B3 | WhatsApp envio automatico | `canSend: false` em todos os retornos de `personalHandler` |
| B4 | Agentarium build | `tsc` + `vite build` OK |

---

## Detalhe por canal

### E-mail

- Sample: escola urgente → bucket `Escola / Pietra`; newsletter → `FYI / ruido`.
- Empty payload: exit 1 (pos-patch).
- **Causa do “nao funciona”:** sensor upstream, nao classificador.

### MEGATRON intake

- 5 payloads fake → 4 `waiting_approval`, 1 spam `archived`.
- Token `sk-TEST...` redigido na fila.
- Fila: `60_Sistemas/MEGATRON/v1/state/intake_queue.json`

### PDF

- `--once --dry-run`: `created: 0, skipped: 5` — PDFs ja vistos pelo watcher state.
- n8n `FabioOS_DropPDF_Aprende.json`: webhook consultivo; gravacao local via watcher.

### PietraOS

- Mensagem saude → `Risco: ALTO`, `bloquear_humano`, sem sugestao automatica.
- `demo-pro`: state com 2 atendimentos apos smoke.
- Tenants gitignored (`60_Sistemas/Pietra/tenants/`).

### n8n

- `FabioOS_Webhook_Inbox`: aceita `tipo=email` mas **nao le Gmail**.
- `FabioOS_Intake_Orquestrador_Seguro`: flags PII/segredo — OK.
- Gmail: so mencionado em gates/planos, **zero trigger**.

### Agentarium WhatsApp

- Default: `WHATSAPP_PERSONAL_MODE=draft_only`.
- Grupos: bloqueados salvo `WHATSAPP_GROUPS_ENABLED=true`.
- Escola: `WHATSAPP_SCHOOL_ENABLED` default false.

---

## Patches aplicados (Cursor)

1. `email_intake_dry_run.py` — empty payload + acentos (sessao anterior).
2. `smoke_intake_onda1.ps1` — reteste automatizado Onda 1.
3. Regenerado `colegio-pietra/pietra_state.json` local (operacional, gitignored).

---

## Handoff

| Para | Acao |
|------|------|
| **Codex** | Gmail export → JSON → adapter universal; n8n dry-run; unificar classificadores |
| **Claude** | Fechar `universal_intake_schema`; redacao em `megatron_core` summary |
| **Fabio** | Autorizar Gmail trabalho; decidir tenant Pietra prod (`colegio-pietra`) |

---

## Proxima onda

**Onda 2 — Seguranca:** scan `_restrito/`, logs, changelogs, `.gitignore`, redacao intake.

Comando: pedir ao Cursor **"executa bugbot onda 2"**.
