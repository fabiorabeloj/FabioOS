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

## Funcionalidades v0.2

- Mapa tático 16-bit com agentes em movimento
- **Security Matrix** — sandbox, access, exec, write, elevated, risk
- **Agent Inspector** — policy, agentDir, auth, risk notes
- Badges pixelados `[SBX]`, `[FS]`, `[EXEC]`, `[ELEV]`, `[RISK]`
- `POST /agents/:id/policy` — altera policy simulada e recalcula risco

## Testes

```powershell
.\test_agentarium_event.ps1          # evento de estado
.\test_agentarium_policy_danger.ps1  # demo danger (Codex)
```

## Documentacao

- `60_Sistemas/OpenClaw/Agentarium.md` — arquitetura e API
- `60_Sistemas/OpenClaw/Agentarium_Policies.md` — politicas dos 5 agentes
- `backend/src/policies/defaultPolicies.ts` — fonte das policies
