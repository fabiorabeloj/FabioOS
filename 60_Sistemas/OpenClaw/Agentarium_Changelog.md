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

## v0.3 — Agent Catalog

**Status:** estavel local.

### Implementado

- `fabioAgents.ts` — 27 agentes FabioOS com layer, policy, responsabilidades;
- `status: active | planned | inactive` — 5 ativos, 22 planejados;
- `GET /catalog` — catalogo completo;
- aba **Agent Catalog** com filtro por camada;
- Security Matrix expandida para todos os agentes;
- Inspector com responsibilities, inputs/outputs, requiresApprovalFor.

### Limite atual

- agentes planejados nao simulam movimento;
- policy ainda simulada (nao le openclaw.json);
- WhatsApp nao conectado ao runtime real.

## v0.2.1 — Pixel Ops Animation Layer

**Status:** estável local.

### Implementado

- sprites 8-bit originais (matriz ASCII → CSS grid) para 5 agentes;
- animações: idle, walk, thinking, executing, approval, done, error, danger;
- efeitos de status (pontos, scanline, `!`, check, X);
- movimento entre zonas com walk1/walk2 por 800ms;
- zonas táticas com grid, contador e acento por tipo;
- HUD pixelado (scanlines, bordas, sombras, badges);
- `prefers-reduced-motion` respeitado.

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
