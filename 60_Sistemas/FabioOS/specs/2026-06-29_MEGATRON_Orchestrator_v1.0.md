---
tipo: spec
area: 60_Sistemas
projeto: MEGATRON
status: ativo
tags: [fabios, megatron, orquestrador, boot, agentarium]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
contrato: MEGATRON Orchestrator v1.0
---

# MEGATRON Orchestrator v1.0

## Funcao

Definir como o MEGATRON sobe, integra e expoe **todos os servicos** do FabioOS por **uma unica entrada** (`MEGATRON.cmd`) e **uma unica interface** (Agentarium / aba Cockpit).

## Principio

> Executar MEGATRON = ligar o sistema. A interface e o Agentarium. O launcher e o pre-MEGATRON.exe.

## Entrada canonica

```powershell
.\MEGATRON.cmd
# equivalente
.\start_megatron.ps1
```

Atalho: `MEGATRON.lnk` na Area de Trabalho.

## Fases de boot (ordem fixa)

| Fase | Componente | Script / acao | Health |
|------|------------|---------------|--------|
| 0 | Preflight | megatron_launcher.ps1 | vault, python, node |
| 1 | Docker Desktop | auto | docker ps |
| 2 | Containers | evolution-* + n8n | HTTP 8080, 5678 |
| 3 | OpenClaw | ensure_openclaw_gateway.ps1 | HTTP 18789 |
| 4 | n8n sync | sync_n8n_whatsapp_workflow.ps1 | webhook registrado |
| 5 | Agentarium | start_agentarium.ps1 | HTTP 3847, 5174 |
| 6 | WhatsApp | Evolution webhook + state | connectionState=open |
| 7 | Intake warm | intake_flow.py se fila ausente | intake_queue.json |
| 8 | Maestro watch | watch_maestro_state.ps1 background | maestro_state.json |
| 9 | Maestro sync | POST /integrations/maestro/sync | roster Agentarium |
| 10 | Cockpit | Obsidian, Cursor, terminal | manual |
| 11 | Interface | abre Agentarium UI | tab Cockpit |

## Interface unificada (Agentarium)

URL: `http://127.0.0.1:5174` — aba **MEGATRON** (default).

API orquestrador: `GET /integrations/megatron/status`

Estado persistido: `60_Sistemas/MEGATRON/v1/state/megatron_runtime.json`

Log: `60_Sistemas/MEGATRON/v1/state/megatron_launcher.log`

## Configuracao

Arquivo: `megatron.local.env` (copiar de `megatron.env.example`)

Flags de orquestracao:

- `MEGATRON_WITH_OPENCLAW` — gateway WSL
- `MEGATRON_WITH_WHATSAPP` — Evolution + webhook
- `MEGATRON_WITH_N8N_SYNC` — sync workflow WhatsApp
- `MEGATRON_WITH_MAESTRO_WATCH` — watcher background
- `MEGATRON_WITH_INTAKE_WARM` — gera fila se ausente

## O que NAO sobe automaticamente

- PRIMUS Index (projeto externo)
- RAG ingestao batch
- Canais externos sem credenciais locais
- OpenClaw se distro WSL `OpenClawGateway` ausente (warn, nao bloqueia)

## Criterio de sucesso

1. Duplo-clique em MEGATRON.lnk
2. Agentarium abre na aba Cockpit
3. Servicos essenciais verdes ou com aviso explicado
4. Intake, Pietra, Barramento acessiveis pela mesma UI

## Roadmap MEGATRON.exe

`MEGATRON.cmd` -> compilado -> tray icon -> um processo, mesma maquina de fases.

## Relacoes

- [[60_Sistemas/FabioOS/Protocolo_Retomada_Ambiente_FabioOS]]
- [[10_Dashboard/MEGATRON]]
- [[60_Sistemas/FabioOS/specs/2026-07-01_MEGATRON_Core_Spec_v0.1]]

## Proximas acoes

- [ ] Validar boot completo apos reinicio real do PC
- [ ] Empacotar MEGATRON.exe quando .NET SDK disponivel
- [ ] Botao "Re-orquestrar" na UI (POST boot seguro)
