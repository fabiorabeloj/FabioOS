# n8n: ligar WhatsApp pessoal ao Hermes Canal

Quando `instance === fabioos-pessoal`, o workflow deve chamar o Agentarium **antes** do fluxo Pietra.

## No no "Extrair Dados"

Remova a regra que exige prefixo `FabioOS` em mensagens pessoais `fromMe`. No modo pessoal, aceite qualquer texto seu.

## Adicionar ramo (apos "Ignorar?" saida false)

1. **IF** `Modo Pessoal?` — condicao: `{{ $json.modo === 'pessoal' }}`

2. **HTTP Request** `Hermes -> Agentarium`
   - POST `http://host.docker.internal:3847/integrations/whatsapp/personal/message`
   - Body JSON:

```json
{
  "messageId": "={{ 'wa-' + $json.dataHora + '-' + $json.numeroAnon }}",
  "conversationId": "={{ $json.numeroAnon }}",
  "contactName": "={{ $json.nome }}",
  "from": "5511000000000",
  "direction": "incoming",
  "text": "={{ $json.texto }}",
  "timestamp": "={{ new Date().toISOString() }}",
  "source": "whatsapp",
  "provider": "evolution_api"
}
```

3. **Respond to Webhook** — `{ "status": "hermes", "jobId": "{{ $json.jobId }}" }`

4. Saida **false** do IF continua para `Classificar Intent` (Pietra/escola).

## Resultado

- Mensagem WhatsApp -> `00_Inbox/Processar/Hermes_Canal_Fabio.md`
- Agentarium mostra Hermes em movimento
- Cursor le a inbox quando voce pedir

## Importar / atualizar workflow

```powershell
.\sync_n8n_whatsapp_workflow.ps1
```

## Teste ponta a ponta (sem WhatsApp real)

```powershell
.\test_n8n_webhook_personal.ps1
.\test_n8n_webhook_personal.ps1 -Text "/help"
```

## Teste local (direto no Agentarium, sem n8n)

```powershell
.\test_whatsapp_personal_message.ps1
```
