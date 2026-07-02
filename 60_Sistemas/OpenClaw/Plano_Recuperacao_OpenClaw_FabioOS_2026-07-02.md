---
tipo: plano
area: 60_Sistemas
projeto: FabioOS
sistema: OpenClaw
status: pronto-para-execucao
tags: [openclaw, recuperacao, plano, gateway, borda]
criado_em: 2026-07-02
atualizado_em: 2026-07-02
---

# Plano de Recuperacao OpenClaw no FabioOS

## Principio

OpenClaw so entra onde ele e melhor: uma borda conversacional/operacional local. Ele nao deve governar a memoria, a decisao, a automacao ou o envio externo.

## Estado atual

| Camada | Estado |
|---|---|
| Gateway OpenClaw | ativo em `127.0.0.1:18789` |
| Agente `fabioos-ponte` | existe |
| Modelo | `openrouter/free` |
| n8n | ativo em `127.0.0.1:5678` |
| Evolution API | ativo em `127.0.0.1:8080` |
| Agentarium | documentado; nao validado nesta rodada |
| Mobile/QR | suspenso ate o teste local passar |

## Ordem correta

1. Local primeiro: provar OpenClaw -> Intake sem celular.
2. Visual depois: mostrar o item no Agentarium ou Workboard.
3. n8n depois: conectar com dry-run, sem envio.
4. Mobile depois: QR/LAN so apos fluxo local confiavel.
5. Automacao real por ultimo: qualquer envio externo exige aprovacao humana.

## Teste minimo

```text
FabioOS teste: criar card ficticio de intake para revisar OpenClaw, sem enviar nada.
```

Resultado aceito:

- payload local criado;
- validacao OK;
- card visual criado;
- log salvo;
- nenhum envio externo;
- custo zero ou modelo gratuito.

## Plano tecnico

### Fatia 1 - Contrato

- Mapear saida OpenClaw para `Universal Intake`.
- Usar `source=openclaw`.
- Usar fila dedicada de teste.
- Nao tocar fila viva por padrao.

### Fatia 2 - Visualizacao

- Enviar evento para Agentarium ou criar Workboard card.
- Marcar dono: `MEGATRON`.
- Marcar estado: `detected` ou `waiting_approval`.

### Fatia 3 - Hardening

- Limitar tokens/contexto do `fabioos-ponte`.
- Manter `openrouter/free` para testes.
- Bloquear execucao de shell por mensagens externas.
- Registrar custo estimado por teste.

### Fatia 4 - Mobile

- Reabrir QR somente apos Fatias 1-3.
- Se LAN/firewall falhar, usar canal alternativo antes de comprar hardware.

## O que nao fazer

- Nao comprar Beelink/OpenClaw edition como correcao emocional.
- Nao abrir firewall sem necessidade.
- Nao permitir auto-send.
- Nao transformar Workboard em fonte da verdade.
- Nao deixar OpenClaw decidir sozinho entre agentes.

## Indicador de sucesso

OpenClaw sera considerado recuperado quando o Fabio puder dizer:

```text
Falei por um canal simples, o FabioOS entendeu, apareceu no painel,
pediu aprovacao e registrou no Obsidian, sem eu brigar com token,
QR ou prompt solto.
```

## Relacoes

- [[50_Registros/Auditoria/Diagnostico_OpenClaw_Recuperacao_2026-07-02]]
- [[50_Registros/Decisoes/ADR_2026-07-02_OpenClaw_Gateway_De_Borda]]
- [[80_Specs/OpenClaw/2026-07-02_recuperacao-openclaw-gateway-borda]]
- [[60_Sistemas/OpenClaw/ponte/STATUS_PONTE]]
- [[60_Sistemas/FabioOS/scripts/universal_intake_adapter]]
