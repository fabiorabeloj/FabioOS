---
tipo: changelog
area: 50_Registros
projeto: FabioOS
frente: INTAKE_DISPATCH_CONTRACT_GUARD
agente: Codex
data: 2026-07-01
tags: [changelog, intake-universal, agentarium]
---

# 2026-07-01 - Contrato da Mesa de Despacho Intake

## Corrigido

- Sample `intake_queue.sample.json` deixou de ter IDs duplicados.
- Schema do Intake Universal passou a aceitar IDs com hash de 6 a 16 caracteres.
- Schema passou a aceitar `nota_ref` e `extracao` como campos opcionais de cards.
- Validador passou a rejeitar filas com IDs duplicados.

## Validado

- Sample congelado validado.
- Teste negativo de ID duplicado rejeitado.

## Limites

- Sem tocar na UI do Cursor.
- Sem aprovar item real.
- Sem push.
