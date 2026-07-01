---
tipo: configuracao
area: 60_Sistemas
sistema: OpenClaw
projeto: FabioOS
status: operacional
tags: [openclaw, megatron, agentes, configuracao, cursor]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Configuracao — Agentes OpenClaw + MEGATRON

## Funcao

Registro unico de quais agentes existem, como estao configurados e como validar.

## OpenClaw (nativos)

| ID | Papel | Modelo | Workspace | Auth |
|---|---|---|---|---|
| `main` | chat default / dashboard | `openrouter/free` | `~/.openclaw/workspace` | OpenRouter manual |
| `fabioos-ponte` | ponte visual FabioOS (read-only) | `openrouter/free` | `60_Sistemas/OpenClaw/ponte/` | OpenRouter manual |

Gateway: `127.0.0.1:18789`, bind `loopback`, distro WSL `OpenClawGateway`.

## MEGATRON (Python — nao nativos OpenClaw)

| ID | Script | Execucao |
|---|---|---|
| `agent.safecommit` | `safecommit.py` | `run_megatron_agent.ps1 -Agente safecommit` |
| `agent.arquivista` | `arquivista.py` | requer `--titulo` e `--texto` ou `--arquivo` |
| `agent.inbox` | `inbox.py` | `run_megatron_agent.ps1 -Agente inbox` |
| `agent.rag` | `rag_agent.py` | venv RAG; pergunta como argumento |
| `agent.dashboard` | `dashboard.py` | gera `STATUS_Agentes.md` |

Workboard `fabioos`: cards MEGATRON para visibilidade (sem execucao automatica).

## Validacao unificada

```powershell
60_Sistemas\OpenClaw\scripts\configure_agentes_fabioos.ps1
60_Sistemas\OpenClaw\scripts\configure_agentes_fabioos.ps1 -SkipOpenClawChat
```

## URLs chat

| Sessao | URL |
|---|---|
| default | http://127.0.0.1:18789/chat?session=main |
| ponte | http://127.0.0.1:18789/chat?session=fabioos-ponte |

## Relacoes

- [[60_Sistemas/OpenClaw/ponte/MAPA_Agentes_MEGATRON_OpenClaw]]
- [[60_Sistemas/OpenClaw/ponte/AGENTS]]
- [[60_Sistemas/MEGATRON/agentes/STATUS_Agentes]]
- [[60_Sistemas/OpenClaw/Troubleshooting_Chat_Web_2026-06-29]]

## Proximas acoes

- [ ] Revisar cards obsoletos no Workboard (interinato) manualmente no UI
- [ ] Promover MEGATRON de `especificado` para `piloto` apos revisao humana (Codex/Claude)
