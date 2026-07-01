---
tipo: conceito
area: 40_Wiki
projeto: PRIMUS
classe_dado: interno
autoria: derivado (conceito abstrato; sem texto integral protegido)
fonte_conceitual: D&D Core 2014 (abstrato; modo catalogo restrito)
criado_em: 2026-07-01
tags: [primus, design, tesouro, recompensa, restrito, conceito]
---

# Tesouro como Vetor de Decisao

## O conceito

Tesouro e um vetor de decisao quando muda comportamento: atrai disputa, compra
alianca, cria alvo, desbloqueia rota ou torna uma faccao interessada. O valor
central nao e a lista do que existe, mas o que aquela recompensa faz acontecer.

## Por que e forte

E abstrato, reutilizavel e seguro. Permite usar a logica de recompensa sem copiar
tabelas protegidas ou gerar centenas de notas de itens.

## Relacoes no grafo

- Complementa [[recompensa-com-consequencia]].
- Pode mover [[frente-de-faccao-e-projetos]] por interesse material.
- Altera [[WorldState_0001_PRIMUS]] via [[Spec_DeltaP_PRIMUS]].
- Pode ser gatilho de [[Spec_Cantina_Conflict_Engine_PRIMUS]].

## Onde o DADO vive

Itens, valores, tabelas e raridades ficam no PRIMUS Index/SQLite. So itens
autorais usados em jogo podem virar notas, se forem pensados e conectados.

## Uso no PRIMUS

Cada tesouro importante deve responder: quem quer, quem teme, que opcao abre e
qual consequencia traz.
