---
tipo: sistema
area: 60_Sistemas
sistema: OpenClaw
projeto: FabioOS
status: piloto
tags: [agentarium, observabilidade, agentes, openclaw, dashboard]
criado_em: 2026-06-29
atualizado_em: 2026-06-30
---

# Agentarium

## Função

**MEGATRON Tactical Agentarium** — camada externa de observabilidade do FabioOS. Painel de **presença + governança + segurança operacional**: agentes 2D em movimento entre zonas, com políticas OpenClaw (sandbox, ferramentas, elevated, agentDir) e matriz de risco.

O Agentarium **não modifica** o core do OpenClaw. É um serviço independente em `apps/agentarium/`.

## Contexto

| Camada | Papel |
|---|---|
| OpenClaw / MEGATRON | execução e runtime dos agentes |
| n8n / scripts / GitHub | origem de eventos reais |
| **Agentarium** | visualização e presença operacional |

## Estado operacional vs animação visual

| Conceito | Onde vive | Responsabilidade |
|---|---|---|
| **Estado operacional** | Backend (`store.ts`, memória v0.1) | `state`, `task`, `zone`, `updatedAt` — fonte da verdade |
| **Animação visual** | Frontend (`AgentAvatar`, CSS `transition`) | Move o avatar quando `zone` muda; não inventa estado |

O frontend **nunca** altera estado localmente sem evento do backend (WebSocket ou HTTP).

## Estrutura

```text
apps/agentarium/
├── backend/          # Fastify + WebSocket + simulador
├── frontend/         # Vite + React + TypeScript
└── README.md
```

## Modelo de agente (v0.2)

```ts
type AgentPolicy = {
  sandboxMode: "off" | "all" | "non-main" | "unknown";
  sandboxScope: string;
  workspaceRoot: string;
  workspaceAccess: "rw" | "ro" | "none" | "unknown";
  allowedTools: string[];
  deniedTools: string[];
  toolProfile?: string;
  elevated: "disabled" | "enabled" | "restricted" | "unknown";
  agentDir: string;
  authProfile: "local" | "default-fallback" | "unknown";
  riskLevel: "safe" | "warning" | "danger";
  riskNotes: string[];
};

type Agent = {
  id: string;
  name: string;
  role: string;
  state: "idle" | "thinking" | "executing" | "waiting_approval" | "done" | "error";
  task: string;
  zone: string;
  updatedAt: string;
  policy: AgentPolicy;
};
```

Políticas padrão: `backend/src/policies/defaultPolicies.ts` e [[60_Sistemas/OpenClaw/Agentarium_Policies]].

## Governança multiagente OpenClaw

1. **Sandbox por agente** — cada entrada em `agents.list[]` pode sobrescrever a config global (`sandbox.mode`, `scope`, `workspaceRoot`, `workspaceAccess`, `docker.*`, `browser.*`, `prune.*`).
2. **Precedência** — config específica do agente vence a global.
3. **Ferramentas** — passam por cadeia de filtros (tool profile → provider → global → agent → sandbox → subagent). Ver `GET /security/matrix` (`toolFilterChain`).
4. **`exec` é perigoso** — pode escrever no filesystem mesmo com `write`/`edit` negados.
5. **Agente read-only de verdade** — negar `exec` e `process`; usar `workspaceAccess: ro` ou `none`.
6. **`agentDir` único** — nunca compartilhar entre agentes; alerta vermelho se detectado.
7. **OAuth** — copiar manualmente apenas `api_key`/`token` portátil; nunca refresh token OAuth.
8. **`non-main`** — depende de `session.mainKey`, não do id do agente.
9. **Sandbox off explícito** — para agentes que nunca devem ser sandboxados, usar `sandbox.mode: off` de forma consciente (Supervisor auditor).

## Security Matrix e Inspector

| UI | Função |
|---|---|
| **Security Matrix** | Tabela Agent / Sandbox / Access / Exec / Write / Elevated / Risk |
| **Agent Inspector** | Clique no agente → policy completa + risk notes |
| **Badges pixelados** | `[SBX: ALL]`, `[FS: RO]`, `[EXEC: NO]`, `[ELEV: OFF]`, `[RISK: SAFE]` |

Cores: safe = verde, warning = amarelo, danger = vermelho (avatar com tremor leve).

## Pixel Ops Animation Layer

Camada visual **8/16-bit** do Agentarium — sprites originais em matriz de pixels, sem assets externos.

### Estrutura

```text
apps/agentarium/frontend/src/pixel/
  pixelTypes.ts       # tipos e mapeamento estado → animação
  pixelPalettes.ts    # paleta de cores por caractere
  agentSprites.ts     # matrizes por agente (idle, walk, thinking…)
  animations.css      # keyframes CSS

apps/agentarium/frontend/src/components/pixel/
  PixelSprite.tsx     # renderiza matriz em CSS grid
  PixelAgentAvatar.tsx
  PixelShadow.tsx
  PixelStatusEffect.tsx
```

### Como os sprites são definidos

Cada linha de uma `PixelFrame` é uma string; cada caractere vira um quadrado colorido pela paleta (`.` = transparente). Exemplo: `K` = contorno escuro, `C` = ciano.

### Como criar novo sprite

1. Adicionar entrada em `agentSprites.ts` com frames `idle`, `walk1`, `walk2`, etc.
2. Definir paleta com `mergePalette({ ... })`.
3. Registrar emoji/ID no backend se for agente ativo.

### Como adicionar nova animação

1. Incluir frames em `PixelSpriteFrames` em `pixelTypes.ts`.
2. Adicionar keyframe em `animations.css` e classe `.pixel-anim--*`.
3. Mapear em `resolvePixelAnim()` e `resolveAnimClass()`.

### Mapeamento estado → animação

| Estado | Animação | Efeito extra |
|---|---|---|
| idle | `pixel-idle` | respiração 1px |
| thinking | `pixel-thinking` | 3 pontos pulsantes |
| executing | `pixel-executing` | scanline + bits |
| waiting_approval | `pixel-approval` | `!` pixelado |
| done | `pixel-done` | check verde |
| error | `pixel-error` | tremor + X |
| danger (policy) | `pixel-danger` | tremor vermelho |
| walking (800ms após mudança de zona) | `pixel-walk` | alterna walk1/walk2 |

### Reduzir/desativar animações

- Respeita `prefers-reduced-motion: reduce` (animações quase desligadas).
- Simulador pode ser desligado com `AGENTARIUM_AUTO_SIM=false`.

Sprites são **originais** (matriz ASCII → CSS grid); nenhum pacote ou imagem externa.

## Agentes iniciais (v0.2)

| ID | Nome | Função | Zona inicial |
|---|---|---|---|
| `pietra` | Pietra | Atendimento escolar e mensagens | WhatsApp |
| `arquivista` | Arquivista | Captura e arquivamento Obsidian | Inbox |
| `codex` | Codex | GitHub e manutenção técnica | GitHub |
| `pesquisador` | Pesquisador | RAG e organização conceitual | RAG |
| `supervisor` | Supervisor | Aprovação humana e segurança | Aprovação Humana |

## Zonas do mapa

WhatsApp · Inbox · Classificação · Obsidian · GitHub · n8n · RAG · Aprovação Humana · Concluído · Erro

Layout fixo em `frontend/src/types.ts` (`ZONE_LAYOUT`).

## Inicio rapido (Windows)

Na raiz do repositorio:

```powershell
.\start_agentarium.ps1
```

Com reinstalacao de dependencias:

```powershell
.\start_agentarium.ps1 -Install
```

O script abre **duas janelas** PowerShell (backend + frontend) e exibe os links abaixo.

| Recurso | URL |
|---|---|
| Painel (frontend) | http://127.0.0.1:5174 (**obrigatorio: `npm run dev` no frontend**) |
| API (backend) | http://127.0.0.1:3847 |
| Health | http://127.0.0.1:3847/health |
| Security Matrix | http://127.0.0.1:3847/security/matrix |
| WebSocket | ws://127.0.0.1:3847/ws |

## Teste manual de policy (elevar risco)

```powershell
.\test_agentarium_policy_danger.ps1
```

Ou manualmente (Codex com exec sem sandbox → danger):

```powershell
$body = '{"sandboxMode":"off"}'
Invoke-RestMethod -Uri "http://127.0.0.1:3847/agents/codex/policy" -Method POST `
  -ContentType "application/json; charset=utf-8" `
  -Body ([System.Text.Encoding]::UTF8.GetBytes($body))
```

## Teste manual de evento

Com o backend rodando:

```powershell
.\test_agentarium_event.ps1
```

O script envia `POST /agents/codex/state` com body UTF-8 explicito (evita mojibake no PowerShell).

Para zonas com acento (`Classificacao`, `Aprovacao Humana`), use sempre:

```powershell
-ContentType "application/json; charset=utf-8"
-Body ([System.Text.Encoding]::UTF8.GetBytes($json))
```

Ou envie via `POST /events` com o mesmo padrao.

## Simulacao vs evento real

| Origem | Como identificar | Efeito |
|---|---|---|
| **Simulacao** | Ativa por padrao (`AGENTARIUM_AUTO_SIM` != `false`); rotas `/simulation/*` | Backend altera agentes a cada ~4,5 s em fluxos predefinidos |
| **Evento real / manual** | `POST /agents/:id/state`, `POST /events`, ou `test_agentarium_event.ps1` | Atualizacao pontual; WebSocket notifica o frontend na hora |

Para **desligar a simulacao** (ver apenas eventos reais):

```powershell
# Antes de iniciar o backend
$env:AGENTARIUM_AUTO_SIM = "false"
cd apps\agentarium\backend
npm run dev
```

Ou com backend ja rodando:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:3847/simulation/stop" -Method POST
```

Para religar:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:3847/simulation/start" -Method POST
```

## Encoding (UTF-8)

- Arquivos-fonte em `apps/agentarium/` devem estar em **UTF-8** (`.editorconfig` + `.gitattributes`).
- Respostas JSON do backend incluem `charset=utf-8`.
- Mojibake (`Programa��o`) no terminal e problema de **exibicao** do PowerShell — use os scripts da raiz ou UTF-8 explicito nos POSTs.

## Painel vazio / agentes nao aparecem

1. Backend deve responder em http://127.0.0.1:3847/health
2. Frontend deve estar **rodando** (`npm run dev`) — abrir http://127.0.0.1:5174 (nao 5173, salvo se Vite mudar a porta)
3. Se a porta 5174 estiver ocupada, o Vite usa a proxima — veja a linha `Local:` no terminal
4. Em dev, o frontend usa `.env.development` com conexao direta a `http://127.0.0.1:3847` (CORS habilitado)
5. Use `.\start_agentarium.ps1` para subir backend + frontend juntos

## Como rodar (manual)

### Backend

```bash
cd apps/agentarium/backend
npm install
npm run dev
```

- HTTP: `http://127.0.0.1:3847`
- WebSocket: `ws://127.0.0.1:3847/ws`
- Simulação automática: `AGENTARIUM_AUTO_SIM=true` (padrão)

### Frontend

```bash
cd apps/agentarium/frontend
npm install
npm run dev
```

- UI: `http://127.0.0.1:5174`
- Proxy Vite: `/api` → backend, `/ws` → WebSocket

## API (v0.2)

| Método | Rota | Descrição |
|---|---|---|
| GET | `/health` | Saúde (`product: MEGATRON Tactical Agentarium`) |
| GET | `/agents` | Lista agentes com policy |
| GET | `/agents/:id` | Um agente |
| GET | `/security/matrix` | Matriz de segurança + alertas globais |
| POST | `/agents/:id/state` | Atualiza estado operacional |
| POST | `/agents/:id/policy` | Atualiza policy simulada; recalcula risco; WS |
| POST | `/events` | Evento genérico (`agentId`, `source`) |
| POST | `/simulation/start` | Inicia simulador |
| POST | `/simulation/stop` | Para simulador |
| GET | `/simulation/status` | Status do simulador |
| POST | `/simulation/error/:id` | Demo de estado erro |

### Exemplo — atualizar policy

```bash
curl -X POST http://127.0.0.1:3847/agents/codex/policy \
  -H "Content-Type: application/json" \
  -d '{"sandboxMode":"all","workspaceAccess":"rw","allowedTools":["read","write","edit"],"deniedTools":["exec"],"elevated":"disabled"}'
```

### Exemplo — evento real (futuro n8n)

```bash
curl -X POST http://127.0.0.1:3847/events \
  -H "Content-Type: application/json" \
  -d '{"agentId":"codex","state":"executing","task":"CI workflow","zone":"n8n","source":"n8n"}'
```

## Como adicionar agente

1. Backend: incluir em `backend/src/policies/defaultPolicies.ts`.
2. Backend: opcional fluxo em `backend/src/simulator.ts`.
3. Frontend: emoji em `frontend/src/types.ts` (`AGENT_EMOJI`).
4. Reiniciar backend.

## Como adicionar zona

1. Backend: validar em `isValidZone()` em `store.ts`.
2. Frontend: incluir em `ZONES` e `ZONE_LAYOUT` em `types.ts`.
3. Ajustar posições no mapa (percentuais `x`, `y`, `w`, `h`).

## Integrações futuras (preparado, não implementado)

| Origem | Mecanismo sugerido |
|---|---|
| **n8n** | HTTP Request → `POST /events` |
| **OpenClaw** | webhook ou script ponte → `/events` |
| **GitHub** | n8n Actions / webhook → mapear para `codex` |
| **Obsidian** | script pós-arquivamento → `arquivista` |
| **WhatsApp/Evolution** | evento Evolution → `pietra` |

Endpoint unificado: `POST /events` com campo `source` para auditoria.

## Limitações v0.2

- Estado e policy em memória (reinício perde histórico).
- Simulação ativa por padrão.
- Policy é **simulada** (espelho conceitual OpenClaw, não lê `openclaw.json` ao vivo).
- Sem autenticação nos endpoints.
- Sem persistência nem histórico temporal.
- Layout 2D fixo (não geográfico).
- Não substitui Workboard OpenClaw nem `STATUS_Agentes.md`.

## Relações

- [[60_Sistemas/OpenClaw/Agentarium_Policies]]
- [[60_Sistemas/OpenClaw/ponte/MAPA_Agentes_MEGATRON_OpenClaw]]
- [[60_Sistemas/OpenClaw/CONFIGURACAO_AGENTES_2026-06-29]]
- [[60_Sistemas/MEGATRON/agentes/README_Agentes]]

## Próximas ações

- [ ] Workflow n8n mínimo postando em `/events`
- [ ] Desligar simulação em produção (`AGENTARIUM_AUTO_SIM=false`)
- [ ] Mapear IDs MEGATRON → Agentarium
- [ ] Histórico de transições (v0.2)
