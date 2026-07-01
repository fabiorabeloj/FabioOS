# Testes WhatsApp — FabioOS Agentarium v0.5.3

## Prompts e tarefas (uso principal)

Envie no chat **Voce** do WhatsApp:

```text
tarefa: revisar prova 9A geografia
prompt: organizar inbox do FabioOS
fabioos: implementar envio automatico Pietra
preciso que o Codex corrija o Agentarium amanha
```

Ou comando:

```text
/tarefa revisar estrutura do vault LLM-Wiki
/tarefas
```

**O que acontece:**
1. MEGATRON confirma no WPP com ID do job
2. Cria arquivo `00_Inbox/Processar/Tarefas_WPP/wa-job-xxx.md`
3. Atualiza indice e `Megatron_Canal_Fabio.md`
4. Sugere agente (Codex, Pietra, Arquivista, Cursor)

**No Cursor:**

```text
Leia 00_Inbox/Processar/Tarefas_WPP/wa-job-xxx.md e execute.
```

Teste local:

```powershell
.\test_wpp_task.ps1
.\test_wpp_task.ps1 -Prompt "tarefa: testar captura MEGATRON"
```

---

Apos ligar o PC ou se o MEGATRON nao responder:

```powershell
.\start_megatron_whatsapp.ps1
```

Diagnostico:

```powershell
.\check_megatron_whatsapp.ps1
```

**Causa #1 de silencio:** Agentarium backend offline (porta 3847).

No WhatsApp (chat **Voce**), mande: `ola` ou `/status`

---

Por padrao `WHATSAPP_REPLY_TO_FABIO=true` — o Hermes **envia de volta** para seu numero via Evolution:

| Voce manda | MEGATRON responde |
|---|---|
| `/oi` | Saudacao |
| `/status` | Status do sistema |
| `/help` | Lista de comandos |
| Mensagem sua (sem /) | "Recebido. Hermes registrou job ..." |
| Mensagem de terceiro | Aviso no seu WPP (rascunho nao vai ao contato) |

**Terceiros:** continua `draft_only` — nunca envia resposta automatica a outras pessoas.

Desligar respostas para Fabio:
```powershell
$env:WHATSAPP_REPLY_TO_FABIO = "false"
# Reiniciar backend Agentarium
```

## Checklist rapido

```powershell
# 1. Backend vivo
Invoke-RestMethod http://127.0.0.1:3847/health

# 2. Status dos canais
.\test_wpp_status.ps1

# 3. Comando /status (Hermes pessoal)
.\test_wpp_personal_status.ps1

# 4. Mensagem pessoal normal
.\test_wpp_personal_message.ps1

# 5. Mensagem escolar (Pietra) — simulada
.\test_wpp_school_message.ps1

# 6. Painel
# http://127.0.0.1:5174

# 7. Ponta a ponta via n8n (simula Evolution)
.\sync_n8n_whatsapp_workflow.ps1
.\test_n8n_webhook_personal.ps1
.\test_n8n_webhook_personal.ps1 -Text "/status"
```

## O que confirmar no painel

- **PERSONAL WPP: CONNECTED** (apos mensagem ou POST /integrations/whatsapp/connected)
- Hermes se move em mensagem pessoal
- Pietra se move em mensagem escolar (com WHATSAPP_SCHOOL_ENABLED=true)
- Event Log: `[PERSONAL-WPP]`, `[SCHOOL-WPP]`, `[COMMAND]`
- **autoSend: OFF** — nenhuma resposta externa enviada

## Canais

| Canal | Agente | Numero | Estado padrao |
|---|---|---|---|
| Pessoal | Hermes | fabioos-pessoal (seu) | enabled |
| Escola | Pietra | instancia escola (futuro) | disabled |

## Habilitar escola (quando tiver celular)

```powershell
$env:WHATSAPP_SCHOOL_ENABLED = "true"
# Reiniciar Agentarium backend
```

## Habilitar envio real (futuro — nao usar agora)

```powershell
$env:WHATSAPP_AUTO_SEND = "true"
# Ainda requer approvalState=approved + canSend
```
