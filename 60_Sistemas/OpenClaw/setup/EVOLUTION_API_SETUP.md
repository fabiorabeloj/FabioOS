---
tipo: sistema
area: 60_Sistemas
projeto: FabioOS
sistema: OpenClaw
status: pendente-execucao
tags: [openclaw, evolution-api, docker, whatsapp, setup]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Evolution API — Guia de Setup para FabioOS

## O que é

Evolution API é uma plataforma open-source que conecta números WhatsApp a sistemas externos via REST API e webhooks. No FabioOS, ela é a camada de recepção do OpenClaw.

## Pré-requisitos

- Docker instalado e ativo
- Número WhatsApp disponível para escanear QR Code (pode ser número pessoal em modo teste)
- Porto 8080 livre

## Instalação via Docker

```powershell
# Criar volume de dados
docker volume create evolution_data

# Iniciar o contêiner
docker run -d `
  --name evolution-api `
  -p 8080:8080 `
  -e AUTHENTICATION_TYPE=apikey `
  -e AUTHENTICATION_API_KEY=CHANGE_ME_EVOLUTION_API_KEY `
  -e WEBHOOK_GLOBAL_URL=http://host.docker.internal:5678/webhook/whatsapp-pietra-v2 `
  -e WEBHOOK_GLOBAL_ENABLED=true `
  -e WEBHOOK_GLOBAL_WEBHOOK_BY_EVENTS=false `
  -v evolution_data:/evolution/Instances `
  atendai/evolution-api:latest
```

**Variáveis importantes:**
- `AUTHENTICATION_API_KEY` — troque `CHANGE_ME_EVOLUTION_API_KEY` por uma chave segura local, sem salvar no repositório
- `WEBHOOK_GLOBAL_URL` — aponta para o workflow n8n que processará as mensagens

## Verificar se está rodando

```powershell
# Status do contêiner
docker ps --filter "name=evolution"

# Logs em tempo real
docker logs evolution-api -f

# Testar a API
curl http://localhost:8080/manager
```

## Criar instância e conectar WhatsApp

```powershell
# 1. Criar instância
curl -X POST http://localhost:8080/instance/create `
  -H "apikey: CHANGE_ME_EVOLUTION_API_KEY" `
  -H "Content-Type: application/json" `
  -d '{"instanceName":"escola","qrcode":true}'

# 2. Buscar QR Code (escanear com o WhatsApp)
curl http://localhost:8080/instance/connect/escola `
  -H "apikey: CHANGE_ME_EVOLUTION_API_KEY"

# Copie o qrcode.base64 e abra em:
# https://base64.guru/converter/decode/image
# Escaneie com o WhatsApp
```

## Verificar conexão

```powershell
curl http://localhost:8080/instance/connectionState/escola `
  -H "apikey: CHANGE_ME_EVOLUTION_API_KEY"
```

Resposta esperada: `{"state": "open"}` = conectado.

## Configurar webhook para o n8n

```powershell
curl -X POST http://localhost:8080/webhook/set/escola `
  -H "apikey: CHANGE_ME_EVOLUTION_API_KEY" `
  -H "Content-Type: application/json" `
  -d '{
    "url": "http://host.docker.internal:5678/webhook/whatsapp-pietra-v2",
    "webhook_by_events": false,
    "webhook_base64": false,
    "events": ["MESSAGES_UPSERT"]
  }'
```

## Testar envio (sem automação ainda)

```powershell
# Enviar mensagem de teste para um número
curl -X POST http://localhost:8080/message/sendText/escola `
  -H "apikey: CHANGE_ME_EVOLUTION_API_KEY" `
  -H "Content-Type: application/json" `
  -d '{
    "number": "5511999999999",
    "text": "Mensagem de teste FabioOS"
  }'
```

## Segurança

- A chave `AUTHENTICATION_API_KEY` deve ficar apenas em variáveis de ambiente e no n8n como credencial
- Nunca commitar a chave no repositório
- O n8n deve validar que o webhook vem da Evolution API (header `apikey`)
- Usar firewall para que a porta 8080 não fique exposta à rede externa

## Status no FabioOS

| Item | Status |
|---|---|
| Docker instalado | ✅ |
| Evolution API instalada | ⬜ pendente |
| Instância conectada ao WhatsApp | ⬜ pendente |
| Webhook configurado para n8n | ⬜ pendente |
| Workflow FabioOS_WhatsApp_Pietra ativo | ⬜ pendente |
| Primeiro atendimento classificado | ⬜ pendente |

## Relações

- [[60_Sistemas/OpenClaw/Sistema_OpenClaw]]
- [[wiki/sistemas/openclaw]]
- [[60_Sistemas/n8n/Workflows/FabioOS_WhatsApp_Pietra]]
