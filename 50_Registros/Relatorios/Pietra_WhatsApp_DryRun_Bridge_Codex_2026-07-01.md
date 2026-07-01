---
tipo: relatorio
area: 50_Registros
projeto: FabioOS
frente: N8N_PIETRA_DRY_RUN_BRIDGE
agente: Codex
status: concluido
criado_em: 2026-07-01
tags: [codex, n8n, whatsapp, pietraos, dry-run]
---

# Relatorio - Pietra WhatsApp Dry Run Bridge

## Entrega

Foi criada uma ponte local segura entre payloads WhatsApp/Evolution e o motor
[[60_Sistemas/Pietra/pietra_conversa|pietra_conversa]].

## Escopo executado

- Bridge local em Python com modo CLI e HTTP.
- Workflow n8n importavel que chama o bridge local.
- Payload fake Evolution para teste.
- Documentacao de operacao do workflow.

## Contrato de seguranca

- `dry_run: true`
- `send_allowed: false`
- `external_effects: false`
- `rag_used: false`
- remetente redigido na resposta;
- segredos bloqueados antes de chamar o motor;
- nenhuma mensagem enviada ao WhatsApp;
- nenhum uso de API externa.

## Como visualizar

No n8n, importar:

```text
60_Sistemas/n8n/Workflows/FabioOS_WhatsApp_Pietra_DryRun.json
```

No Obsidian, abrir:

```text
60_Sistemas/n8n/Workflows/FabioOS_WhatsApp_Pietra_DryRun.md
```

## Proxima acao

Quando Claude liberar piloto, trocar o dry-run por aprovacao humana explicita antes de qualquer envio real.

## Validacao executada

```text
py_compile: OK
workflow JSON: OK
payload fake JSON: OK
CLI fake: status=proposed, send_allowed=false
CLI segredo fake: status=blocked
HTTP /health: ok=true
HTTP POST fake: status=proposed, send_allowed=false, sender=****8888, approval=true
```
