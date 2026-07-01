---
tipo: relatorio
area: 50_Registros
projeto: FabioOS
status: concluido
agente: Cursor
classe_dado: interno
criado_em: 2026-07-01
tags: [fabios, bugbot, onda2, seguranca, cursor]
---

# Bugbot Onda 2 — Seguranca e Segredos (2026-07-01)

## Resumo

| Check | Resultado |
|-------|-----------|
| `.gitignore` vs `_restrito/` / tenants / intake state | OK |
| Tokens `sk-` / `ghp_` em arquivos versionados | Nenhum |
| `intake_log.jsonl` | Sem corpo de mensagem — so metadados |
| `intake_queue.json` live + validator | OK (5 cards) |
| `universal_intake_validator.py` | Detecta segredo em summary |
| `email_intake_dry_run.py` | Snippet omitido; remetente mascarado |
| Changelogs com PII real de terceiros | Nao encontrado |
| Smoke Onda 2 | `smoke_seguranca_onda2.ps1` |

**Reteste:** `.\60_Sistemas\FabioOS\scripts\smoke_seguranca_onda2.ps1`

---

## Achados

### Media

| ID | Achado | Onde | Acao |
|----|--------|------|------|
| S1 | E-mails pessoais/profissionais **versionados** no wiki | `40_Wiki/_compat_wiki/memoria/Mapa_Memoria_Fabio.md`, changelogs | Decisao Fabio: aceitar como metadata operacional ou mover para `_restrito` |
| S2 | Telefone WhatsApp **hardcoded** como default | `apps/agentarium/backend/src/whatsapp/config.ts` L49 | Preferir `FABIO_WHATSAPP_NUMBER` sem fallback real |
| S3 | `megatron_core` retorna `summary` cru no dict | `megatron_core.py` | **Claude:** redigir na origem; adapter/flow ja redigem na fila |

### Baixa — OK

| ID | Item |
|----|------|
| B1 | Samples versionados usam `@escola.exemplo`, `+5511999990001` — fake |
| B2 | `.codex/config.toml` gitignored |
| B3 | `intake_flow` redige `forbidden_external` na fila |
| B4 | `universal_intake_adapter` rejeita payload vazio (exit 1) |
| B5 | Validator exige `[REDIGIDO` em `forbidden_external` |
| B6 | `github.md` cita token mas nao expoe valor |

### Positivo pos-Onda 1

Codex entregou **`universal_intake_adapter.py`** + **`universal_intake_validator.py`**: ponte email → `megatron_core` → fila unificada com redacao. Sample email escola classifica como **`escolaos`** (nao mais divergencia se usar adapter).

---

## .gitignore auditado

Cobertura confirmada:

- `05_Raw_Sources/_compat_sources/*/_restrito/*`
- `60_Sistemas/Pietra/tenants/`
- `60_Sistemas/MEGATRON/v1/state/intake_queue.json`
- `60_Sistemas/MEGATRON/v1/state/intake_log.jsonl`
- `60_Sistemas/MEGATRON/v1/state/_raw/`
- `.env`, `.codex/config.toml`, `logs/`

**Git tracked em paths sensiveis:** apenas `.gitkeep` + samples fake.

---

## Redacao por canal

| Canal | Corpo na fila/log | Remetente |
|-------|-------------------|-----------|
| MEGATRON intake | `raw_content_ref` gitignored; summary redigido | Completo na fila (fake ou real local) |
| email dry-run MD | Snippet omitido | Mascarado `co***@domain` |
| intake_log.jsonl | Sem texto de mensagem | N/A |
| Agentarium WhatsApp | `textPreview` truncado; `maskPhone` | Mascarado |

---

## Patches aplicados (Cursor)

1. `smoke_seguranca_onda2.ps1` — reteste automatizado.
2. (Onda 1) `email_intake_dry_run.py` empty payload + acentos.

Nenhum patch em `megatron_core` ou `config.ts` — zona Claude / decisao Fabio.

---

## Handoff

| Para | Acao |
|------|------|
| **Claude** | Redacao em `megatron_core.summary` no CLI |
| **Fabio** | Decidir se e-mails no wiki ficam versionados |
| **Cursor (opcional)** | Remover default telefone real em `config.ts` |

---

## Proxima onda

**Onda 3 — Contratos duplicados:** matriz diff classificadores + alinhar `email_intake` vs adapter vs `megatron_core`.

Comando: **"executa bugbot onda 3"**.
