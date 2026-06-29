---
tipo: changelog
data: 2026-06-27
area: arquitetura
status: registrado
tags: [orcamento, openrouter, megatron, custos, hardware]
---

# Changelog - Plano de Orcamento OpenRouter / FabioOS / MEGATRON

## Resumo

Criado plano de custos para uso da OpenRouter no FabioOS e plano estrategico de orcamento total do FabioOS/MEGATRON.

## Alteracoes

- Criado `60_Sistemas/OpenRouter/Plano_Custos_OpenRouter_FabioOS.md`.
- Criado `00_Arquitetura/Plano_Orcamento_FabioOS_MEGATRON_2026.md`.
- Atualizada a nota `60_Sistemas/OpenRouter/OpenRouter.md` com referencia aos planos.
- Atualizada a wiki `wiki/sistemas/openrouter.md` com links internos.

## Decisoes

- OpenRouter passa a ser tratada como camada de API controlada, nao como substituto de RAG/Grafo local.
- Teto inicial recomendado: US$100, com reavaliacao apos 7 dias de metricas reais.
- Hardware local pesado nao deve ser comprado antes de medir carga real.
- Prioridade operacional: backup, limites de API, medicao de custo, privacidade e roteamento por tarefa.

## Observacao

Nenhuma API key foi criada, solicitada, armazenada ou versionada.
