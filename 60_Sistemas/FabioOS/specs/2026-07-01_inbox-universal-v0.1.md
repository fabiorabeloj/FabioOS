---
tipo: spec
area: 60_Sistemas
projeto: FabioOS
status: implementado
classe_dado: interno
criado_em: 2026-07-01
tags: [fabios, megatron, intake-universal, codex, cursor]
---

# SPEC - Inbox Universal v0.1

## Objetivo

Implementar a parte Codex da ordem do Claude: schema, adaptador, payloads fake,
validador local, logs seguros e saida consumivel pelo Cursor.

## Contrato

Fonte de verdade: [[60_Sistemas/FabioOS/specs/2026-07-01_MEGATRON_Core_Spec_v0.1]].

Saida principal: fila JSON no shape de
`60_Sistemas/MEGATRON/v1/examples/intake_queue.sample.json`.

## Entregas

- `60_Sistemas/FabioOS/schemas/universal_intake_schema.json`
- `60_Sistemas/FabioOS/scripts/universal_intake_adapter.py`
- `60_Sistemas/FabioOS/scripts/universal_intake_validator.py`
- `60_Sistemas/FabioOS/examples/universal_intake_payloads_fake.json`
- `60_Sistemas/FabioOS/examples/intake_gmail_fake.json`
- `60_Sistemas/FabioOS/examples/intake_whatsapp_fake.json`
- `60_Sistemas/FabioOS/examples/intake_pdf_fake.json`
- adaptacao de `email_intake_dry_run.py` para emitir fila universal

## Criterios de aceite

- [x] Email fake vira payload valido.
- [x] WhatsApp fake de saude vira `restricted`, `rag_permitido=false`.
- [x] Payload com token vira `forbidden_external` com `summary` redigido.
- [x] PDF fake vira card valido.
- [x] Spam/promocao vira `archived`.
- [x] IDs usam timestamp + hash/fingerprint.
- [x] Validador aceita o sample congelado do Claude e o sample novo do Codex.
- [x] Validador rejeita summary com segredo.
- [x] Nenhum teste envia, arquiva, deleta, marca como lido ou chama API externa.

## Comandos

```powershell
python 60_Sistemas/FabioOS/scripts/universal_intake_adapter.py `
  --input 60_Sistemas/FabioOS/examples/universal_intake_payloads_fake.json `
  --generated-at 2026-07-01T09:30:00 `
  --stdout
```

```powershell
python 60_Sistemas/FabioOS/scripts/universal_intake_adapter.py `
  --input 60_Sistemas/FabioOS/examples/universal_intake_payloads_fake.json `
| python 60_Sistemas/FabioOS/scripts/universal_intake_validator.py
```

## Limites

- Sem RAG/reindex.
- Sem envio externo.
- Sem alterar mensagens reais.
- Sem credenciais.
- Sem alterar `intake_flow.py`, `megatron_core.py`, sample do Cursor ou Agentarium.
