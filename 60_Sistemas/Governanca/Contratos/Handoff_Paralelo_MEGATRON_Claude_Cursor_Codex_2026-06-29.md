---
tipo: handoff
area: 60_Sistemas
projeto: FabioOS
status: ativo
criado_em: 2026-06-29
atualizado_em: 2026-06-29
tags: [fabios, megatron, handoff, claude, cursor, codex, multiagente]
---

# Handoff Paralelo - MEGATRON Coordenador

## Tese

O trabalho paralelo so funciona se todos consumirem o mesmo contrato e ninguem editar a zona do outro.

## Donos

| Frente | Dono | Edita | Nao edita |
|---|---|---|---|
| Orquestrador | Claude | `MEGATRON/v1/megatron.py`, `registry.py`, agentes, testes | UI, dashboards, roadmap |
| Apresentacao | Cursor | `MEGATRON/v1/apresentacao.py`, mockups em `60_Sistemas/Cursor/` | nucleo do orquestrador |
| Governanca | Codex | contratos, INDEX de governanca, docs de handoff | codigo MEGATRON/RAG/MCP |

## Costura

Contrato unico:

[[60_Sistemas/Governanca/Contratos/Contrato_Resultado_MEGATRON]]

## Fluxo esperado

```text
Claude implementa Resultado
  -> Cursor renderiza Resultado
  -> Codex audita/documenta Resultado
  -> Fabio decide ativacao externa
```

## Regras

- Sem push.
- Sem API externa.
- Sem WhatsApp/email/trade.
- Sem reindex RAG.
- Sem alterar `fabioos_db`.
- Sem editar arquivo de outra frente.
- Conflito de zona sobe para Claude.

## Pendencias da zona Codex

- Manter contratos documentados.
- Auditar se os artefatos novos seguem o contrato.
- Atualizar governanca sem duplicar protocolos.
- Listar divergencias para Claude, sem corrigir codigo dele.
