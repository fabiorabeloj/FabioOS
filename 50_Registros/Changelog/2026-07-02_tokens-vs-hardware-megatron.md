---
tipo: changelog
area: MEGATRON
projeto: FabioOS
status: registrado
tags: [fabios, megatron, orcamento, tokens, hardware, changelog]
criado_em: 2026-07-02
---

# Changelog - Tokens vs Hardware MEGATRON

## Adicionado

- ADR `Tokens/API vs Hardware Local no MEGATRON`.
- Addendum no plano de orcamento com a regra: Core 24/7 + tokens controlados antes de GPU.
- Gate de compra de GPU local.
- Gate de aumento de teto de API.

## Decisao

O FabioOS deve investir primeiro em infraestrutura permanente e API controlada:

```text
Core 24/7 -> tokens com teto -> RAM/SSD/backup -> GPU quando metricas justificarem
```

## Limites

- Nenhuma compra executada.
- Nenhuma chave criada.
- Nenhuma API chamada.
- Nenhum push.
