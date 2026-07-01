---
tipo: relatorio
area: 50_Registros
projeto: FabioOS
status: concluido
agente: Cursor
classe_dado: interno
criado_em: 2026-07-01
tags: [fabios, email, bugbot, cursor, dry-run]
---

# Bugbot — Email Intake Dry-Run (Cursor 2026-07-01)

## Veredito

O script **nao estava quebrado**. O modulo de e-mail falha no **elo upstream** (Gmail → export JSON → n8n), nao no classificador local.

## Testes executados

| Teste | Resultado |
|-------|-----------|
| `--input email_intake_sample.json --stdout` | OK — 2 mensagens classificadas |
| Gravar em `_restrito/triagens/` | OK — JSON `{"ok": true, "messages": 2}` |
| `--output-dir C:\Temp` | OK — rejeitado (exit 1, fora do vault) |
| Payload vazio `{"emails":[]}` | **BUG** — exit 0 + relatorio vazio (corrigido) |
| `intake_flow.py --print` (referencia MEGATRON) | OK — 5 entradas, redacao de token |

## Causa raiz (por que e-mail “nao funciona”)

```text
Gmail (Codex OAuth) ──X──> export JSON automatico ──X──> n8n Gmail Trigger
                                    │
                                    └── manual: email_intake_dry_run.py (OK se alimentado)
```

- Conector Codex responde em leitura (evidencia Codex 2026-07-01).
- FabioOS local **nao tem** watcher/trigger que alimente o script.
- Dois contratos paralelos: `email_intake_dry_run.py` (Markdown triagem) vs `intake_flow.py` + `megatron_core.py` (`intake_queue.json`) — **nao alinhados** (ordem Codex: Inbox Universal v0.1).

## Bugs encontrados e correcoes

| Severidade | Achado | Acao |
|------------|--------|------|
| Baixa | Payload vazio gerava relatorio inutil com exit 0 | **Corrigido** — exit 1 + stderr JSON |
| Baixa | `normalize_text` sem strip de acentos (vs megatron_core) | **Corrigido** — NFKD + ascii |
| Media | Taxonomia diverge de megatron_core (ex.: coordenacao → pietraos vs escolaos) | **Pendente Codex** — alinhar ao universal_intake_schema |
| Alta | Sem pipeline Gmail → script | **Pendente Codex** — export + n8n dry-run |
| Alta | Gmail trabalho nao autorizado | **Pendente Fabio** |

## Arquivos envolvidos

- `60_Sistemas/FabioOS/scripts/email_intake_dry_run.py` (patch Cursor)
- `60_Sistemas/FabioOS/examples/email_intake_sample.json`
- `60_Sistemas/FabioOS/examples/email_empty.json` (regressao)
- `60_Sistemas/MEGATRON/v1/intake_flow.py` (referencia)
- `60_Sistemas/MEGATRON/v1/megatron_core.py` (referencia)
- `00_Inbox/Processar/Email_para_Processar_FabioOS.md`

## Teste minimo pos-patch

```powershell
python 60_Sistemas/FabioOS/scripts/email_intake_dry_run.py `
  --input 60_Sistemas/FabioOS/examples/email_intake_sample.json --stdout

python 60_Sistemas/FabioOS/scripts/email_intake_dry_run.py `
  --input 60_Sistemas/FabioOS/examples/email_empty.json
# esperado: exit 1, stderr {"ok": false, "error": "..."}
```

## Proximo passo (nao Cursor)

Codex: export Gmail → JSON → `email_intake_dry_run.py` ou adapter para `intake_queue.json`.
