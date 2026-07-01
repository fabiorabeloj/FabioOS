---
tipo: registro-operacional
area: 60_Sistemas
projeto: FabioOS
status: concluido
tags: [cursor, frente, openclaw, megatron, agentes]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Frente Cursor — Configuracao agentes OpenClaw + MEGATRON

## Funcao

Configurar e validar todos os agentes necessarios (OpenClaw nativos + MEGATRON Python + Workboard) sem colidir com Codex/Claude.

## Frente

| Campo | Valor |
|---|---|
| ID | `CURSOR_OPENCLAW_AGENTES` |
| Dono | Cursor |
| Estado | concluida |
| Entrega | [[60_Sistemas/OpenClaw/CONFIGURACAO_AGENTES_2026-06-29]] |

## Artefatos

- `60_Sistemas/OpenClaw/scripts/configure_agentes_fabioos.ps1` (novo)
- `60_Sistemas/OpenClaw/CONFIGURACAO_AGENTES_2026-06-29.md` (novo)
- Correcao `sync_workboard_megatron.ps1` (`--board fabioos`)
- `60_Sistemas/MEGATRON/agentes/STATUS_Agentes.md` (regenerado via dashboard)

## Anti-colisao

- Nao editar `STATUS.md`, `NEXT_ACTIONS.md`, `Registro_Frentes_Ativas.md`, `~/.openclaw`
- Nao reindexar RAG
- Commit/push aguardam Fabio

## Criterio de concluido

- Gateway operacional
- `main` + `fabioos-ponte` listados com OpenRouter
- Smoke test dos 5 MEGATRON
- Workboard com cards MEGATRON
- Script unificado de validacao
