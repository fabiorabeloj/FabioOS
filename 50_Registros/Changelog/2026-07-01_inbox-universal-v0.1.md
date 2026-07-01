---
tipo: changelog
area: 50_Registros
projeto: FabioOS
data: 2026-07-01
tags: [fabios, megatron, intake-universal, changelog]
---

# 2026-07-01 - Inbox Universal v0.1

## Mudancas

- Criado schema JSON do contrato Universal Intake.
- Criado adaptador local para gerar fila consumivel pelo Cursor/Agentarium.
- Criado validador local de contrato e seguranca.
- Criados payloads fake para Gmail, WhatsApp e PDF.
- Adaptado `email_intake_dry_run.py` para emitir fila universal com `--queue-json`
  e `--write-queue`.
- Criado sample versionavel da fila: `universal_intake_queue.codex_sample.json`.

## Validacoes

- `py_compile` dos scripts OK.
- Adapter universal -> validador OK (`5` cards).
- Sample congelado do Claude -> validador OK (`5` cards).
- Email fake -> fila universal -> validador OK (`2` cards).
- Payload vazio rejeitado com exit 1.
- Segredo fake redigido no summary.
- IDs unicos com timestamp + hash.

## Limites preservados

- Sem envio externo.
- Sem apagar, arquivar ou marcar mensagem como lida.
- Sem RAG/reindex.
- Sem credenciais.
- Sem alterar codigo MEGATRON Core ou Agentarium.
