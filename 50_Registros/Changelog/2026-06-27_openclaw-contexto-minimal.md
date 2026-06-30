---
tipo: changelog
area: 50_Registros
projeto: FabioOS
status: concluido
tags: [changelog, openclaw, custo, contexto, interinato]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Changelog - OpenClaw Contexto Minimal

## O que foi feito

- Investigado o custo alto do agente `fabioos-ponte`.
- Confirmado que a pasta da ponte e pequena; o custo vinha principalmente do prompt de sistema e das ferramentas injetadas pelo OpenClaw.
- Aplicada configuracao local do OpenClaw: `tools.byProvider.openrouter.profile = minimal`.
- Reiniciado o gateway com `openclaw gateway restart`.
- Testado novamente o agente `fabioos-ponte` em `openrouter/free`.

## Resultado medido

- Antes: aproximadamente `21121` tokens de entrada.
- Depois: aproximadamente `7340` tokens de entrada.
- Reducao aproximada: 65%.
- Custo monetario do teste: `0`, usando `openrouter/free`.

## Observacoes

- A configuracao global `tools.profile = coding` foi preservada.
- A reducao foi aplicada somente por provider OpenRouter.
- A ponte deve continuar manual por padrao; sem heartbeat automatico.
- O teste de mensagem teve comportamento de onboarding do OpenClaw, mas a metrica de contexto confirmou a reducao.

## Pendente

- Claude revisar a configuracao quando retornar.
- Se necessario, criar um agente OpenClaw ainda mais restrito apenas para status/ponte.
