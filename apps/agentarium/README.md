# MEGATRON Tactical Agentarium

Painel de **presença + governança + segurança operacional** dos agentes FabioOS (OpenClaw multi-agent sandbox).

**Versão atual: v0.5** — Character Identity + Personal WhatsApp Governance

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
| WhatsApp intake | http://127.0.0.1:3847/integrations/whatsapp/jobs |

## Funcionalidades v0.5

- **10 agentes ativos** com identidade visual (Agent Class no Inspector)
- **Hermes** — WhatsApp pessoal (draft_only, sem envio automatico)
- **Pietra** — escola/institucional (separada de Hermes)
- Sprites 8-bit originais por classe tactica
- **Event Log** + **Personal WhatsApp Intake** panel
- `POST /integrations/whatsapp/message` — governanca WhatsApp pessoal
- Movimento por evento real (sim off por padrao)
- Telefones mascarados no frontend (`5511****9999`)

## Personal WhatsApp Governance

1. **Hermes** = WhatsApp pessoal (triagem, rascunhos, encaminhamento).
2. **Pietra** = escola/institucional — nunca canal pessoal.
3. Nenhuma mensagem enviada automaticamente.
4. Modo padrao: `draft_only` (`WHATSAPP_PERSONAL_MODE=draft_only`).
5. Grupos desligados: `WHATSAPP_GROUPS_ENABLED=false`.
6. Allowlist opcional: `WHATSAPP_ALLOWED_CONTACTS=5511...,5512...`.
7. Bloqueio: `WHATSAPP_BLOCKED_CONTACTS=...`.
8. Jobs visiveis no painel **Personal WhatsApp Intake**.
9. Aprovacao manual futura via Supervisor + `Awaiting Fabio`.

### Testar mensagem pessoal

```powershell
.\test_whatsapp_personal_message.ps1
```

Resultado esperado: Hermes move Personal WhatsApp → Message Intake; Event Log `[WHATSAPP] [MANUAL_TEST]`; `approvalState: draft_only`.

### Conectar Evolution API / n8n

Instancia `fabioos-pessoal` (Evolution) → webhook n8n `whatsapp-pietra-v2`. Para presenca no Agentarium, encaminhar payload para `POST /integrations/whatsapp/message`.

### Ligar/desligar grupos

```powershell
$env:WHATSAPP_GROUPS_ENABLED = "true"   # desligado por padrao
# Reiniciar backend Agentarium
```

### Configurar allowlist

```powershell
$env:WHATSAPP_ALLOWED_CONTACTS = "5511982123896,5511999999999"
# Reiniciar backend — contatos fora da lista sao registrados sem acao
```

## Simulacao demo (opcional)

```powershell
$env:AGENTARIUM_AUTO_SIM = "true"
.\start_agentarium.ps1
```

## Testes

```powershell
.\test_whatsapp_personal_message.ps1   # Hermes + draft_only
.\test_agentarium_event.ps1           # evento generico
.\test_whatsapp_pessoal.ps1           # Evolution conectado
```

## Documentacao

- `60_Sistemas/OpenClaw/Agentarium.md` — arquitetura completa v0.5
- `60_Sistemas/OpenClaw/Agentarium_Agents.md` — catalogo de agentes
- `backend/src/agents/agentVisualClasses.ts` — classes visuais
