---
tipo: relatorio
area: MEGATRON
frente: INTAKE_ADAPTER_OUTPUT_GUARD
responsavel: Codex
data: 2026-07-01
status: concluido
tags: [fabios, megatron, intake, codex, contrato, seguranca]
---

# Adapter Output Guard - Codex

## Contexto

Claude apontou dois riscos na zona Codex do Inbox Universal:

1. `universal_intake_adapter.py` gravava o arquivo, mas podia sair com erro quando `--output` era relativo.
2. O adaptador usava por padrao a fila viva `60_Sistemas/MEGATRON/v1/state/intake_queue.json`, que tambem e escrita pelo `intake_flow` e pelo `arquivista_intake`.

## Correcao aplicada

- `write_json()` agora resolve o caminho antes de criar diretorios, gravar e retornar o destino.
- O `print` final usa o caminho resolvido relativo a raiz do vault, eliminando o crash em `--output` relativo.
- A saida padrao mudou para `60_Sistemas/MEGATRON/v1/state/intake_queue.codex_adapter.json`.
- A fila viva `intake_queue.json` deixa de ser alvo padrao do adaptador Codex, reduzindo risco de corrida entre agentes.

## Testes executados

```powershell
python -m py_compile "60_Sistemas/FabioOS/scripts/universal_intake_adapter.py"
```

Resultado: OK.

```powershell
python "60_Sistemas/FabioOS/scripts/universal_intake_adapter.py" --input "60_Sistemas/FabioOS/examples/universal_intake_payloads_fake.json" --stdout | python "60_Sistemas/FabioOS/scripts/universal_intake_validator.py"
```

Resultado: `{"ok": true, "cards": 5}`.

```powershell
python "60_Sistemas/FabioOS/scripts/universal_intake_adapter.py" --input "60_Sistemas/FabioOS/examples/universal_intake_payloads_fake.json" --output "60_Sistemas/MEGATRON/v1/state/intake_queue.codex_smoke.json"
```

Resultado: `{"ok": true, "cards": 5, "queue": "60_Sistemas/MEGATRON/v1/state/intake_queue.codex_smoke.json"}`.

```powershell
python "60_Sistemas/FabioOS/scripts/universal_intake_validator.py" --input "60_Sistemas/FabioOS/examples/universal_intake_queue.codex_sample.json"
```

Resultado: `{"ok": true, "cards": 5}`.

## Limites

- Nao alterei `arquivista_intake.py`.
- Nao alterei Agentarium/Cursor.
- Nao escrevi na fila viva como alvo padrao.
- Nao houve RAG, API externa, envio, aprovacao real ou push.

## Recomendacao ao Claude

Manter `state/intake_queue.json` como fila viva do fluxo operacional e usar arquivos dedicados para provas, validadores e adaptadores. Se o Cursor precisar ler uma fila de teste Codex, usar `state/intake_queue.codex_adapter.json` ou receber `--output` explicito.
