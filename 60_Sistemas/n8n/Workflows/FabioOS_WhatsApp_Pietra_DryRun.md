---
tipo: workflow-n8n
area: 60_Sistemas
sistema: n8n
projeto: FabioOS
status: pronto-para-importar
tags: [n8n, whatsapp, pietraos, dry-run, aprovacao-humana]
criado_em: 2026-07-01
---

# FabioOS - WhatsApp Pietra Dry Run

## Objetivo

Receber um payload WhatsApp/Evolution, chamar localmente o motor
[[60_Sistemas/Pietra/pietra_conversa|pietra_conversa]] e devolver apenas uma proposta
segura para aprovacao humana.

Este workflow nao envia mensagem ao responsavel.

## Fluxo

```mermaid
flowchart LR
  A["Evolution webhook"] --> B["n8n webhook"]
  B --> C["Pietra Dry Run Bridge :8791"]
  C --> D["pietra_conversa.conversar"]
  D --> E["Resposta sugerida + cartao"]
  E --> F["Responder sem enviar WhatsApp"]
```

## Arquivos

- Workflow importavel: [[60_Sistemas/n8n/Workflows/FabioOS_WhatsApp_Pietra_DryRun.json]]
- Bridge local: [[60_Sistemas/n8n/scripts/pietra_whatsapp_dry_run_bridge.py]]
- Payload fake: [[60_Sistemas/n8n/examples/evolution_pietra_message.fake.json]]

## Como executar o bridge local

```powershell
python 60_Sistemas/n8n/scripts/pietra_whatsapp_dry_run_bridge.py --serve --port 8791
```

O n8n em Docker deve chamar:

```text
http://host.docker.internal:8791/pietra/whatsapp/dry-run?tenant=colegio-pietra
```

## Teste local sem n8n

```powershell
python 60_Sistemas/n8n/scripts/pietra_whatsapp_dry_run_bridge.py --input 60_Sistemas/n8n/examples/evolution_pietra_message.fake.json --tenant codex-dry-run
```

## Saida esperada

- `dry_run: true`
- `send_allowed: false`
- `external_effects: false`
- `requires_human_approval: true`
- numero do remetente redigido;
- resposta sugerida e/ou cartao de atendimento.

## Limites

- Nao envia WhatsApp.
- Nao chama OpenRouter, Claude, GPT ou RAG.
- Nao grava conhecimento no Obsidian.
- O estado de conversa gerado pelo Pietra fica em `60_Sistemas/Pietra/tenants/`, que e gitignored por regra LGPD.

## Relacoes

- [[60_Sistemas/Pietra/PietraOS_Padrao_Profissional_Chatbot]]
- [[60_Sistemas/Pietra/PietraOS_Arquitetura_Multitenant]]
- [[60_Sistemas/OpenClaw/Sistema_OpenClaw]]
- [[60_Sistemas/FabioOS/schemas/universal_intake_schema]]
