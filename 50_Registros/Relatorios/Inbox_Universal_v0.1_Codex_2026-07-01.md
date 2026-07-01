---
tipo: relatorio
area: 50_Registros
projeto: FabioOS
status: concluido
classe_dado: interno
criado_em: 2026-07-01
tags: [fabios, megatron, intake-universal, codex, cursor]
---

# Inbox Universal v0.1 - Codex

## Contexto

Claude definiu que o nucleo do FabioOS nao e "Gmail", e sim o Intake Universal:

```text
entrada -> normaliza -> classifica -> sensibilidade -> dominio -> agente
-> proposta -> aprovacao humana -> log -> memoria
```

A tarefa do Codex era alinhar a frente de e-mail ao contrato universal, gerar
payloads fake para canais diferentes, validar seguranca e produzir saida
consumivel pelo Cursor.

## Entregas

- Schema: `60_Sistemas/FabioOS/schemas/universal_intake_schema.json`
- Adaptador: `60_Sistemas/FabioOS/scripts/universal_intake_adapter.py`
- Validador: `60_Sistemas/FabioOS/scripts/universal_intake_validator.py`
- Payloads fake:
  - `60_Sistemas/FabioOS/examples/intake_gmail_fake.json`
  - `60_Sistemas/FabioOS/examples/intake_whatsapp_fake.json`
  - `60_Sistemas/FabioOS/examples/intake_pdf_fake.json`
  - `60_Sistemas/FabioOS/examples/universal_intake_payloads_fake.json`
- Sample para Cursor: `60_Sistemas/FabioOS/examples/universal_intake_queue.codex_sample.json`
- SPEC: [[60_Sistemas/FabioOS/specs/2026-07-01_inbox-universal-v0.1]]

## Resultado da prova minima

O sample gerado contem 5 cards:

| Canal | Resultado esperado | Estado |
|---|---|---|
| Gmail escola | `escolaos`, tarefa, aguarda Fabio | OK |
| WhatsApp saude/atestado | `restricted`, sem RAG, escala humano | OK |
| WhatsApp com token fake | `forbidden_external`, summary redigido | OK |
| PDF edital | card valido, aguarda aprovacao | OK |
| Gmail promocional | `spam`, arquivado | OK |

## Garantias

- IDs usam timestamp + hash.
- O validador aceita o sample legado do Claude e o sample novo do Codex.
- `summary` nao copia segredo quando `sensitivity=forbidden_external`.
- Corpo bruto fica apenas em `raw_content_ref` gitignored.
- `private`, `restricted`, `no_rag` e `forbidden_external` nao entram no RAG automaticamente.
- Nenhum teste envia, arquiva, deleta, marca como lido ou chama API externa.
- O validador rejeita cards com campos extras de corpo bruto e summary com segredo.

## Testes executados

```powershell
python -m py_compile `
  60_Sistemas/FabioOS/scripts/universal_intake_adapter.py `
  60_Sistemas/FabioOS/scripts/universal_intake_validator.py `
  60_Sistemas/FabioOS/scripts/email_intake_dry_run.py
```

```powershell
python 60_Sistemas/FabioOS/scripts/universal_intake_adapter.py `
  --input 60_Sistemas/FabioOS/examples/universal_intake_payloads_fake.json `
  --stdout `
| python 60_Sistemas/FabioOS/scripts/universal_intake_validator.py
```

```powershell
python 60_Sistemas/FabioOS/scripts/email_intake_dry_run.py `
  --input 60_Sistemas/FabioOS/examples/intake_gmail_fake.json `
  --queue-json `
| python 60_Sistemas/FabioOS/scripts/universal_intake_validator.py
```

```powershell
python 60_Sistemas/FabioOS/scripts/universal_intake_validator.py `
  --input 60_Sistemas/MEGATRON/v1/examples/intake_queue.sample.json
```

Teste negativo executado: um card adulterado com `summary` contendo padrao de
segredo foi rejeitado pelo validador.

## Limites

- Nao alterei `intake_flow.py`, `megatron_core.py`, sample do Claude ou Agentarium.
- Nao toquei em RAG, n8n ativo, OpenClaw runtime ou credenciais.
- A fila viva continua gitignored em `60_Sistemas/MEGATRON/v1/state/intake_queue.json`.

## Proxima acao

Cursor pode consumir `60_Sistemas/FabioOS/examples/universal_intake_queue.codex_sample.json`
enquanto a fila viva ainda nao for ligada a canal real.
