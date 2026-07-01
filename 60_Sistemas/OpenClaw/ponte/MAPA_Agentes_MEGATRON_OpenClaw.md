---
tipo: mapa
area: 60_Sistemas
sistema: OpenClaw
projeto: FabioOS
status: ativo
tags: [openclaw, megatron, agentes, workboard, ponte]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Mapa — Agentes MEGATRON no OpenClaw

## Funcao

Explicar como os **cinco agentes MEGATRON** (specs Python) se relacionam com o **OpenClaw** (runtime visual + `fabioos-ponte`).

OpenClaw **nao registra** SafeCommit/Arquivista/Inbox/RAG/Dashboard como agentes nativos. Eles aparecem no Workboard como **cards de departamento** e sao executados via scripts locais.

## Arquitetura

```text
Fabio / Companion OpenClaw
    │
    ├── fabioos-ponte (agente OpenClaw, read-only, openrouter/free)
    │       └── resume frentes Claude/Codex/Cursor
    │
    ├── Workboard fabioos (visual, sem LLM)
    │       └── cards por frente + cards MEGATRON
    │
    └── MEGATRON agentes (Python, implementacao minima)
            ├── agent.safecommit   → safecommit.py
            ├── agent.arquivista   → arquivista.py
            ├── agent.inbox        → inbox.py
            ├── agent.rag          → rag_agent.py
            └── agent.dashboard    → dashboard.py
```

## Tabela operacional

| Agente MEGATRON | ID | Script | Workboard label | Estado |
|---|---|---|---|---|
| SafeCommit | `agent.safecommit` | `60_Sistemas/MEGATRON/agentes/implementacao/claude/safecommit.py` | `megatron` | piloto minimo |
| Arquivista | `agent.arquivista` | `.../arquivista.py` | `megatron` | piloto minimo |
| Inbox | `agent.inbox` | `.../inbox.py` | `megatron` | piloto minimo |
| RAG | `agent.rag` | `.../rag_agent.py` | `megatron` | piloto minimo (venv RAG) |
| Dashboard | `agent.dashboard` | `.../dashboard.py` | `megatron` | piloto minimo |

## Validacao unificada

```powershell
60_Sistemas\OpenClaw\scripts\configure_agentes_fabioos.ps1
```

Ver registro completo: [[60_Sistemas/OpenClaw/CONFIGURACAO_AGENTES_2026-06-29]].

## Como executar (Windows)

Helper unificado:

```powershell
60_Sistemas\OpenClaw\scripts\run_megatron_agent.ps1 -Agente safecommit
60_Sistemas\OpenClaw\scripts\run_megatron_agent.ps1 -Agente rag -Args '"O que e o FabioOS?"'
```

Python direto (RAG usa venv):

```powershell
python 60_Sistemas\MEGATRON\agentes\implementacao\claude\safecommit.py
60_Sistemas\RAG\.venv\Scripts\python.exe 60_Sistemas\MEGATRON\agentes\implementacao\claude\rag_agent.py "pergunta"
```

## OpenClaw (WSL)

```powershell
wsl -d OpenClawGateway -- openclaw agents list
wsl -d OpenClawGateway -- openclaw workboard list
wsl -d OpenClawGateway -- openclaw agent --agent fabioos-ponte --thinking off --message "Resuma frentes ativas"
```

Sincronizar cards MEGATRON:

```powershell
60_Sistemas\OpenClaw\scripts\sync_workboard_megatron.ps1
```

## Limites

- `fabioos-ponte` nao executa scripts MEGATRON automaticamente (read-only).
- WhatsApp/Evolution e canal externo — trilha separada (Fase 11).
- Agente OpenClaw `main` usa `openrouter/free`; nao substituir MEGATRON.

## Relacoes

- [[60_Sistemas/MEGATRON/agentes/README_Agentes]]
- [[60_Sistemas/MEGATRON/agentes/Registro_Agentes]]
- [[60_Sistemas/OpenClaw/ponte/STATUS_PONTE]]
- [[60_Sistemas/OpenClaw/ponte/AGENTS]]

## Proximas acoes

- [x] Script unificado `configure_agentes_fabioos.ps1`
- [ ] Atualizar cards obsoletos no Workboard (interinato) — manual no UI
- [ ] Conectar Agente Dashboard ao painel OpenClaw quando aprovado
