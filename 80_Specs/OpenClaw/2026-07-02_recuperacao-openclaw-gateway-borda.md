---
tipo: spec
area: 80_Specs
projeto: FabioOS
sistema: OpenClaw
status: especificado
tags: [openclaw, spec, gateway, intake, agentarium]
criado_em: 2026-07-02
atualizado_em: 2026-07-02
---

# SPEC - Recuperacao OpenClaw como Gateway de Borda

## Objetivo

Transformar OpenClaw de frente ambigua em gateway de borda testavel para o MEGATRON.

## Fora de escopo

- Reinstalar OpenClaw.
- Comprar hardware.
- Abrir firewall/LAN.
- Gerar QR Code mobile.
- Enviar mensagens WhatsApp.
- Alterar tokens.
- Reindexar RAG.
- Substituir Agentarium.

## Entrada

Um comando inofensivo de teste:

```text
FabioOS teste: registrar lembrete ficticio no intake universal, sem enviar nada.
```

## Saida esperada

Um item estruturado no contrato de `Universal Intake`, com origem `openclaw`, canal `edge_gateway`, estado `detected`, agente sugerido `inbox` ou `roteador`, `approval_required: true` e sem envio externo.

## Fluxo alvo

```text
Usuario
  -> OpenClaw / fabioos-ponte
  -> adaptador OpenClaw -> Universal Intake
  -> MEGATRON classifica
  -> Agentarium mostra card
  -> Fabio aprova/rejeita
  -> log no vault
```

## Ferramentas

- OpenClaw Gateway `127.0.0.1:18789`.
- Agente OpenClaw `fabioos-ponte`.
- `60_Sistemas/FabioOS/scripts/universal_intake_adapter.py`.
- Agentarium `POST /events` ou `/integrations/whatsapp/message` quando aplicavel.
- n8n apenas se houver workflow dry-run.

## Permissoes

| Acao | Permissao |
|---|---|
| Ler mensagem de teste | permitido |
| Criar payload local | permitido |
| Criar card visual | permitido |
| Enviar mensagem externa | proibido |
| Executar comando de sistema recebido do chat | proibido |
| Ler arquivos pessoais sem escopo | proibido |
| Usar modelo pago | proibido sem decisao explicita |

## Criterios de aceite

- [ ] Gateway responde HTTP `200`.
- [ ] `openclaw agents list` mostra `fabioos-ponte`.
- [ ] Um comando de teste cria payload de intake.
- [ ] Payload valida contra schema.
- [ ] Card aparece no Agentarium ou Workboard.
- [ ] Nao ha envio externo.
- [ ] Reinicio do gateway nao perde configuracao essencial.
- [ ] Relatorio salvo em `50_Registros/Auditoria/`.

## Implementacao minima

1. Criar adaptador seco `openclaw_to_universal_intake.py` se nao existir rota nativa.
2. Aceitar somente payload local/manual no primeiro teste.
3. Validar contra o schema do FabioOS.
4. Escrever em fila dedicada de teste, nunca na fila viva por padrao.
5. Publicar evento visual opcional.

## Evolucao futura

- Pareamento mobile quando o fluxo local passar.
- Canal Telegram/WhatsApp somente depois do dry-run.
- MCP OpenClaw apenas com sandbox e escopo.
- Roteamento via LLM Orchestrator quando custo/privacidade estiverem medidos.

## Relacoes

- [[50_Registros/Auditoria/Diagnostico_OpenClaw_Recuperacao_2026-07-02]]
- [[50_Registros/Decisoes/ADR_2026-07-02_OpenClaw_Gateway_De_Borda]]
- [[60_Sistemas/OpenClaw/Plano_Recuperacao_OpenClaw_FabioOS_2026-07-02]]
- [[60_Sistemas/FabioOS/schemas/universal_intake_schema]]
- [[60_Sistemas/OpenClaw/Agentarium]]
