---
tipo: changelog
area: 50_Registros
projeto: FabioOS
frente: INTAKE_CLASSIFIER_CONVERGENCE
agente: Codex
data: 2026-07-01
tags: [changelog, intake-universal, megatron-core]
---

# 2026-07-01 - Convergencia dos classificadores do Intake

## Corrigido

- `email_intake_dry_run.py` deixou de usar sua propria decisao de dominio/urgencia
  no relatorio Markdown legado.
- O e-mail fake da prova agora aparece no relatorio como
  `escolaos/high/criar_tarefa`, alinhado ao MEGATRON Core.

## Validado

- Email fake em Markdown.
- Email fake em fila universal.
- WhatsApp fake em fila universal.
- PDF fake em fila universal.

## Limites

- Sem acao externa.
- Sem RAG.
- Sem alterar o core.
