---
tipo: relatorio
area: 60_Sistemas
projeto: FabioOS
sistema: OpenClaw
status: aguardando-scan-qr
tags: [openclaw, evolution-api, whatsapp, n8n, pietra, fase-11]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Relatório de Ativação do WhatsApp Pessoal

## Função

Registrar a ativação controlada da comunicação entre WhatsApp pessoal, Evolution API, n8n e FabioOS.

## Contexto

O objetivo operacional é permitir que o usuário se comunique com o FabioOS pelo WhatsApp pessoal, em modo seguro: recebimento e classificação primeiro, sem envio automático externo.

## Estado atual

| Camada | Estado |
|---|---|
| Docker | Ativo |
| n8n | Ativo em `localhost:5678` |
| Evolution API | Ativa em `localhost:8080` |
| PostgreSQL Evolution | Ativo em container interno |
| Redis Evolution | Ativo em container interno |
| Workflow n8n | `FabioOS - WhatsApp para Pietra` ativo como `fabioosWhatsappPietraV2` |
| Endpoint n8n | `http://localhost:5678/webhook/whatsapp-pietra-v2` |
| Instância WhatsApp | `fabioos-pessoal` |
| Estado da instância | `connecting` |
| QR Code | Gerado em arquivo temporário local |

## Decisões de segurança

- Chave da Evolution API foi salva fora do repositório, em pasta local do usuário.
- Token da instância foi salvo fora do repositório.
- O QR Code não foi salvo no vault.
- Webhook global da Evolution API foi desativado.
- A instância usa webhook específico para `whatsapp-pietra-v2`.
- `groupsIgnore` está ativo para evitar ingestão de grupos.
- `readMessages` e `readStatus` estão desativados.
- Chamadas são rejeitadas com mensagem operacional.
- Não há envio automático de resposta para contatos externos.

## Ajustes executados

- Atualizada a Evolution API para imagem `evoapicloud/evolution-api:latest`, identificada em runtime como `v2.3.7`.
- Criada a instância nova `fabioos-pessoal`, pois a instância anterior `pessoal` ficou presa em estado fechado.
- Corrigido o workflow n8n para ler payloads vindos do Webhook Node em `body`.
- Atualizado endpoint operacional para `whatsapp-pietra-v2`.

## Próxima ação humana

- [ ] Escanear o QR Code no WhatsApp pessoal.
- [ ] Confirmar que a instância `fabioos-pessoal` muda para estado `open`.
- [ ] Enviar uma mensagem de teste para o próprio WhatsApp conectado.
- [ ] Validar se o n8n classifica e registra a entrada.

## Mensagem de teste sugerida

```text
FabioOS, registre na inbox: testar comunicação pelo WhatsApp pessoal.
```

## Relações

- [[60_Sistemas/OpenClaw/Sistema_OpenClaw]]
- [[60_Sistemas/OpenClaw/Roteiro_Ativacao_OpenClaw_Evolution_2026-06-27]]
- [[60_Sistemas/OpenClaw/setup/EVOLUTION_API_SETUP]]
- [[60_Sistemas/n8n/Workflows/FabioOS_WhatsApp_Pietra]]
- [[60_Sistemas/Pietra/Sistema_Pietra]]
