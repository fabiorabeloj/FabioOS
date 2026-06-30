# MEGATRON Tactical Agentarium

Painel de **presença + governança + segurança operacional** dos agentes FabioOS (OpenClaw multi-agent sandbox).

## Inicio rapido

```powershell
# Na raiz do repo
.\start_agentarium.ps1
```

| Recurso | URL |
|---|---|
| **Painel** | http://127.0.0.1:5174 |
| API | http://127.0.0.1:3847 |
| Security Matrix | http://127.0.0.1:3847/security/matrix |

## Manual (dois terminais)

```bash
# Terminal 1 — backend (3847)
cd apps/agentarium/backend && npm install && npm run dev

# Terminal 2 — frontend (5174)
cd apps/agentarium/frontend && npm install && npm run dev
```

## Funcionalidades v0.3

- **Agent Catalog** — 27 agentes FabioOS (5 ativos, 22 planejados)
- Filtro por camada (command, security, technical, knowledge, school, finance, interface, personal)
- **Pixel Ops Animation Layer** — sprites 8-bit originais
- **Security Matrix** — todos os agentes do catalogo
- `GET /catalog` — metadata completa

## Funcionalidades v0.2.1

- Mapa tático 16-bit com agentes em movimento
- **Pixel Ops Animation Layer** — sprites 8-bit originais + HUD 16-bit
- **Security Matrix** — sandbox, access, exec, write, elevated, risk
- **Agent Inspector** — policy, agentDir, auth, risk notes
- `POST /agents/:id/policy` — altera policy simulada e recalcula risco

### Testar animações por estado (Codex)

```powershell
$utf = { param($j) [System.Text.Encoding]::UTF8.GetBytes($j) }

# Thinking
Invoke-RestMethod -Uri "http://127.0.0.1:3847/agents/codex/state" -Method POST `
  -ContentType "application/json; charset=utf-8" `
  -Body (& $utf '{"state":"thinking","task":"Analisando tarefa","zone":"Classificação"}')

# Executing
Invoke-RestMethod -Uri "http://127.0.0.1:3847/agents/codex/state" -Method POST `
  -ContentType "application/json; charset=utf-8" `
  -Body (& $utf '{"state":"executing","task":"Aplicando patch","zone":"GitHub"}')

# Waiting approval / Done / Error — idem com state correspondente
```

## Testes

```powershell
.\test_agentarium_event.ps1          # evento de estado
.\test_agentarium_policy_danger.ps1  # demo danger (Codex)
```

## Documentacao

- `60_Sistemas/OpenClaw/Agentarium.md` — arquitetura e API
- `60_Sistemas/OpenClaw/Agentarium_Policies.md` — politicas dos 5 agentes
- `backend/src/policies/defaultPolicies.ts` — fonte das policies
