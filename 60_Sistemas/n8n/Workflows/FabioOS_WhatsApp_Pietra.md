---
tipo: sistema
area: 60_Sistemas
projeto: FabioOS
sistema: n8n
workflow: FabioOS_WhatsApp_Pietra
status: pronto-para-importar
tags: [n8n, workflow, whatsapp, pietra, openclaw, automação]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Workflow: FabioOS — WhatsApp → Pietra

## Nome do workflow

`FabioOS - WhatsApp para Pietra`

## Objetivo

Receber mensagens do WhatsApp via Evolution API, classificar pelo Pietra, salvar log anonimizado no vault e notificar o professor com a sugestão de resposta. O professor sempre aprova antes de responder.

**Critério de sucesso da Fase 11:**
> Uma mensagem externa aciona uma ação controlada no FabioOS.

## Gatilho

- **Tipo:** Webhook (HTTP POST da Evolution API)
- **Endpoint:** `http://localhost:5678/webhook/whatsapp-pietra`
- **Método:** POST
- **Content-Type:** `application/json`

## Entrada esperada (payload Evolution API)

```json
{
  "event": "messages.upsert",
  "instance": "escola",
  "data": {
    "key": { "remoteJid": "5511999999999@s.whatsapp.net" },
    "message": { "conversation": "Boa tarde, quando é a prova de geo?" },
    "pushName": "Nome do Remetente",
    "messageTimestamp": 1719396000
  }
}
```

## Processamento (nós)

```
[Webhook] → [Extrair Dados] → [Classificar Intent] → [Verificar Escalonamento]
    → [Salvar Log no Vault] → [Montar Notificação] → [Responder webhook]
```

### Nó 1: Webhook
Recebe o POST da Evolution API.

### Nó 2: Extrair Dados (Code)
- Extrai: número (4 últimos dígitos para anonimizar), mensagem, nome, timestamp
- Gera filename de log: `PIETRA_YYYY-MM_LOG.md`
- Prepara estrutura para classificação

### Nó 3: Classificar Intent (Code)
Compara a mensagem com as palavras-gatilho de cada uma das 11 categorias do Pietra:

| Categoria | Gatilhos principais |
|---|---|
| financeiro | mensalidade, boleto, pagamento, atraso |
| secretaria | declaração, histórico, documento, horário |
| coordenação | coordenação, reunião, reclamação |
| professor | professor, prof, disciplina |
| material | lista, livro, apostila, uniforme |
| horário | horário, entrada, saída, feriado |
| prova | prova, avaliação, nota, gabarito |
| matrícula | matrícula, rematrícula, vaga |
| segunda_chamada | segunda chamada, faltou, atestado |
| ocorrência | ocorrência, briga, bullying, agressão |
| duvida_pedagogica | dificuldade, reforço, laudo |

Retorna: `{categoria, nivel, escalonar, resposta_modelo_key}`

### Nó 4: Verificar Escalonamento (If)
Se `escalonar === true` → rota de escalamento direto (notifica coordenação).
Se não → rota normal (prepara sugestão para professor).

### Nó 5: Salvar Log no Vault (HTTP Request)
- Appenda linha ao arquivo `sources/_inbox/PIETRA_YYYY-MM_LOG.md` via Obsidian API
- Formato: `| data | hora | canal | categoria | nível | ação | status |`
- Número anonimizado: apenas 4 últimos dígitos

### Nó 6: Montar Notificação (Code)
Prepara mensagem de notificação para o professor:
```
[PIETRA] Nova mensagem recebida
Canal: WhatsApp | Número: ****9999
Categoria: prova | Nível: médio

Mensagem: "Boa tarde, quando é a prova de geo?"

Resposta sugerida:
"Olá! A avaliação de Geografia para a turma [TURMA] está prevista para [DATA]..."

Para responder: acesse o WhatsApp da escola.
```

### Nó 7: Responder webhook
Retorna JSON de confirmação para a Evolution API.

## Saída

**HTTP 200 — Sucesso:**
```json
{
  "status": "ok",
  "categoria": "prova",
  "nivel": "médio",
  "acao": "sugestao_preparada"
}
```

**HTTP 200 — Escalonamento:**
```json
{
  "status": "escalado",
  "categoria": "ocorrência",
  "nivel": "alto",
  "acao": "coordenacao_notificada"
}
```

## Integrações

| Sistema | Como |
|---|---|
| **Evolution API** | Dispara webhook ao receber mensagem WhatsApp |
| **n8n** | Processa e classifica |
| **Obsidian REST API** | Salva log anonimizado |
| **WhatsApp (Evolution)** | Professor recebe notificação (opcional, via nó adicional) |

## Como configurar e ativar

### Pré-requisitos
1. Evolution API rodando (ver `60_Sistemas/OpenClaw/setup/EVOLUTION_API_SETUP.md`)
2. Instância WhatsApp conectada e webhook apontando para n8n
3. Workflow `FabioOS_Webhook_Inbox.json` já importado (Fase 10)
4. Credencial `Obsidian API Token` configurada no n8n

### Importar o workflow
1. n8n → Workflows → Import
2. Selecionar: `60_Sistemas/n8n/Workflows/FabioOS_WhatsApp_Pietra.json`
3. Ativar o workflow

## Teste mínimo

```powershell
# Simular webhook da Evolution API
curl -X POST http://localhost:5678/webhook/whatsapp-pietra `
  -H "Content-Type: application/json" `
  -d '{
    "event": "messages.upsert",
    "instance": "escola",
    "data": {
      "key": {"remoteJid": "5511999999999@s.whatsapp.net"},
      "message": {"conversation": "Boa tarde, quando e a prova de geografia do 9A?"},
      "pushName": "Responsavel Teste",
      "messageTimestamp": 1719396000
    }
  }'
```

**Resultado esperado:**
- Resposta JSON: `{status: "ok", categoria: "prova", nivel: "médio"}`
- Log criado em `sources/_inbox/PIETRA_2026-06_LOG.md`

Ou use `/simular-mensagem-pietra "Quando é a prova de geo?"` para testar sem precisar do n8n.

## Riscos

| Risco | Mitigação |
|---|---|
| Evolution API offline | Verificar `docker ps` antes de usar |
| Webhook duplicado | Filtrar event `messages.upsert` e ignorar mensagens enviadas pelo próprio número |
| Mensagem de outro idioma | Classificar como `não-classificada`, triagem manual |
| Volume alto de mensagens | Adicionar rate limiting no n8n |
| Dados sensíveis no log | Anonimizar sempre — nunca logar nome completo ou número inteiro |

## Próxima melhoria

- Adicionar nó de resposta automática ao remetente: "Olá! Sua mensagem foi recebida. Em breve retornaremos."
- Integrar RAG (Fase 12): buscar respostas anteriores similares antes de sugerir
- Dashboard de atendimentos (Fase 21)
- Suporte a áudio transcrito (Fase futura)

## Relações

- [[60_Sistemas/OpenClaw/Sistema_OpenClaw]]
- [[60_Sistemas/Pietra/intents/INTENTS_CATALOGO]]
- [[60_Sistemas/Pietra/respostas-modelo/RESPOSTAS_MODELO]]
- [[60_Sistemas/n8n/Workflows/FabioOS_Webhook_Inbox]]
- [[wiki/sistemas/n8n]]
- [[wiki/sistemas/openclaw]]
