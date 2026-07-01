---
tipo: changelog
area: MEGATRON
frente: INTAKE_COMMAND_EXTRACTOR
data: 2026-07-01
status: concluido
tags: [fabios, megatron, intake, changelog]
---

# Changelog - Comando Natural no Intake

## Adicionado

- `intake_command_extract.py`, extrator deterministico de comando natural para produto, serie, tema e prazo.
- Suporte a texto direto, stdin e payload JSON simples.
- Auto-teste interno do extrator.

## Alterado

- `universal_intake_adapter.py` passa a anexar `extracao` opcional nos cards quando encontra sinais estruturados suficientes.
- Resumo do card pode receber cabeca estruturada de alta legibilidade.

## Protecoes

- Item `forbidden_external` nao recebe `extracao`.
- Nenhuma acao externa.
- Nenhum envio.
- Nenhuma aprovacao real.
- Sem RAG/reindex.
- Sem push.
