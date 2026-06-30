---
project: PRIMUS
object: constitution
type: rule
status: stable
face: EIP
tags: [primus, constituicao, eip]
---

# PRIMUS — Mapa do Sistema

## 1. Geometria

PRIMUS possui três faces:

```mermaid
flowchart LR
  E[Enciclopédia Funcional] --> I[Instância Controlada]
  I --> P[Persistência]
  P --> E
```

## 2. Definição das faces

### E — Enciclopédia Funcional

Conteúdo catalogado, tipado, rastreável e consultável.

Exemplos:

- raça
- classe
- magia
- item
- criatura
- plano
- facção
- local

### I — Instância Controlada

Unidade fechada de jogo.

Exemplos:

- missão
- dungeon
- encontro
- evento
- desafio
- recompensa

### P — Persistência

Diferença de estado registrada.

Exemplos:

- WorldFlag
- AccessKey
- Reputation
- Debt
- Scar
- DeathRecord
- ItemTransfer

## 3. Pipeline editorial

```mermaid
flowchart LR
  T1[T1 Captura] --> T2[T2 Materialização]
  T2 --> T3[T3 Integração]
  T3 --> T4[T4 Instanciamento]
```

## 4. Regra-matriz

Nada entra no PRIMUS sem:

1. Tipo.
2. Fonte.
3. Encaixe.
4. Limites.
5. Instanciamento.
6. Possível ΔP.
