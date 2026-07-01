---
tipo: relatorio
area: 50_Registros
projeto: FabioOS
frente: INTAKE_DISPATCH_CONTRACT_GUARD
agente: Codex
status: concluido
criado_em: 2026-07-01
tags: [codex, intake-universal, agentarium, mesa-despacho, contrato]
---

# Contrato da Mesa de Despacho do Intake

## Motivo

O Claude declarou que o elo final `aprovado -> nota no Obsidian` foi fechado e que
agora falta o painel do Cursor/Agentarium.

Ao ler o relatorio do Cursor, apareceu uma pendencia nao-UI: unificar IDs do
`intake_flow` com o contrato do adapter. O sample congelado tinha 5 cards com o
mesmo `id`, o que tornaria inseguro chamar:

```text
arquivista_intake.py --aprovar <id>
```

## Correcao aplicada

- `intake_queue.sample.json` agora tem IDs unicos por card.
- `universal_intake_schema.json` aceita hash de 6 a 16 caracteres, alinhado ao
  `megatron_core`.
- `universal_intake_schema.json` documenta os campos opcionais pos-aprovacao:
  `nota_ref` e `extracao`.
- `universal_intake_validator.py` agora falha se houver IDs duplicados.
- O validador tambem aceita `nota_ref`/`extracao` e estados pos-aprovacao.

## Evidencia executada

```text
sample cards=5
sample unique_ids=5
sample duplicates=[]
validator sample: {"ok": true, "cards": 5}
validator duplicate-negative: rejected_duplicate_ids_OK
```

## Limites

- Nao toquei no Agentarium/UI.
- Nao alterei `arquivista_intake.py`.
- Nao aprovei nem rejeitei item real.
- Nao escrevi nota no Obsidian.
- Nao fiz RAG, API externa ou push.

## Recomendacao para Cursor

- Use `intake_queue.sample.json` para render inicial.
- Use `state/intake_queue.json` como fila viva.
- Nunca chame `--aprovar` se houver ID duplicado.
- Para cards `restricted`, `forbidden_external` ou `no_rag`, o botao Aprovar deve
  renderizar bloqueio/escalada, nao gravacao.
