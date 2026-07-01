---
tipo: changelog
area: MEGATRON
frente: INTAKE_ADAPTER_OUTPUT_GUARD
data: 2026-07-01
status: concluido
tags: [fabios, megatron, intake, changelog]
---

# Changelog - Adapter Output Guard

## Alterado

- Corrigido `universal_intake_adapter.py` para retornar caminho resolvido ao gravar JSON.
- Eliminado crash no `print` final quando `--output` e relativo.
- Alterado destino padrao do adaptador para `state/intake_queue.codex_adapter.json`, deixando a fila viva `state/intake_queue.json` para o fluxo operacional.

## Validado

- `py_compile` do adaptador.
- Adapter em `--stdout` validado pelo `universal_intake_validator.py`.
- Adapter com `--output` relativo validado com saida `ok`.
- Sample versionado do contrato validado.

## Seguranca

- Sem API externa.
- Sem RAG/reindex.
- Sem envio de mensagem.
- Sem aprovacao real.
- Sem push.
