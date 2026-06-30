---
tipo: changelog
area: 60_Sistemas
sistema: OpenClaw
projeto: FabioOS
status: ativo
tags: [agentarium, changelog, megatron]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
---

# Agentarium Changelog

## v0.2 — MEGATRON Tactical Agentarium

**Status:** estável local.

### Implementado

- painel de presença operacional;
- movimento visual dos agentes entre zonas;
- Security Matrix (sandbox, access, exec, write, elevated, risk);
- Agent Inspector (policy, agentDir, auth, risk notes);
- badges de política pixelados (`[SBX]`, `[FS]`, `[EXEC]`, `[ELEV]`, `[RISK]`);
- cálculo de risco (`evaluateAgentRisk`) com alertas OpenClaw;
- endpoints `GET /security/matrix`, `POST /agents/:id/policy`;
- documentação de sandbox, tools, elevated e agentDir;
- estética 16-bit tactical operations dashboard;
- scripts `start_agentarium.ps1`, `test_agentarium_event.ps1`, `test_agentarium_policy_danger.ps1`.

### Limite atual

- políticas ainda simuladas em memória;
- não conectado ao `openclaw.json` real;
- apenas 5 agentes ativos (Pietra, Arquivista, Codex, Pesquisador, Supervisor);
- catálogo completo de agentes FabioOS ainda não implementado.

### Próxima fase (v0.3)

- catálogo completo com `status: active | inactive | planned`;
- filtros por camada (`command`, `security`, `technical`, etc.);
- aba **Agent Catalog** para agentes planejados;
- sem simular movimento de agentes `planned`.

## v0.1 — Painel inicial

- backend Fastify + WebSocket + simulador;
- frontend Vite + React com mapa 2D;
- 5 agentes iniciais com estados operacionais;
- integração via `POST /events` e `POST /agents/:id/state`.
