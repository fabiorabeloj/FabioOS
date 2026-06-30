---
tipo: referencia
area: 60_Sistemas
sistema: OpenClaw
projeto: FabioOS
status: ativo
tags: [agentarium, agentes, catalogo, megatron]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
---

# Agentarium — Catálogo de Agentes FabioOS

Referencia humana alinhada a arquitetura multiagente hierarquica.

Fonte tecnica: `apps/agentarium/backend/src/agents/fabioAgents.ts`

## Status de implantacao

| Status | Significado |
|---|---|
| **active** | No mapa operacional + simulador |
| **planned** | Catalogo apenas — sem movimento |
| **inactive** | Reservado para desativacao futura |

## Ativos (v0.3)

| ID | Nome | Camada | Zona |
|---|---|---|---|
| pietra | Pietra | school | WhatsApp / Escola |
| arquivista | Arquivista | knowledge | Obsidian |
| codex | Codex | technical | GitHub / Codigo |
| pesquisador | Pesquisador | knowledge | RAG / Pesquisa |
| supervisor | Supervisor | security | Aprovacao Humana |

## Nucleo essencial (planejado)

MEGATRON, Guardiao, Roteador, Memoria, Integrador, Tecnico de Sistema, Observador

## Escola (planejado)

Secretaria Escolar, Avaliador, Planejador Pedagogico, Comunicador Institucional, Professor-Autor, Curador

## Operacao pessoal (planejado)

Financeiro, Risco Trader, Relator, CRM, Email Inbox, Calendario, Saude / Bem-estar

## Interface (planejado)

Cartografo, Designer de Sistema

## Camadas

```txt
command    — orquestracao e classificacao
security   — auditoria e permissoes
technical  — codigo, automacao, infra
knowledge  — Obsidian, RAG, curadoria
school     — escola e pedagogia
finance    — financas e trader
interface  — HUD e visual
personal   — CRM, email, calendario, bem-estar
```

## Regra central

Agente que pensa nao executa sozinho; agente que executa nao decide sozinho; agente que decide deixa rastro; agente sensivel e supervisionado.

## API

| Endpoint | Descricao |
|---|---|
| GET /catalog | 27 agentes com metadata completa |
| GET /agents | Somente ativos (mapa) |
| GET /security/matrix | Todos os agentes do catalogo |

## Proxima fase (v0.4)

Leitura read-only de `openclaw.json` real.

## Proxima fase (v0.5)

Eventos reais n8n/OpenClaw — **inclui WhatsApp/Evolution → Pietra + Supervisor**.

## Relacoes

- [[60_Sistemas/OpenClaw/Agentarium]]
- [[60_Sistemas/OpenClaw/Agentarium_Policies]]
- [[60_Sistemas/OpenClaw/ponte/MAPA_Agentes_MEGATRON_OpenClaw]]
