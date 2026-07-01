---
tipo: conceito
area: 40_Wiki
projeto: PRIMUS
classe_dado: interno
autoria: derivado (conceito de design abstrato; sem texto integral)
fonte_conceitual: Stars Without Number / Worlds Without Number free editions
criado_em: 2026-07-01
tags: [primus, design, missao, agencia, sandbox, conceito]
---

# Missao com Situacao, nao Trilho

## O conceito

Uma missao deve apresentar uma situacao instavel, nao uma sequencia obrigatoria
de cenas. Ha um problema, partes interessadas, riscos e oportunidades; o jogador
decide como entrar, negociar, evitar, atacar ou transformar a situacao.

## Por que e forte

Esse conceito preserva agencia e torna a preparacao mais robusta. Se o jogador
desvia do plano, a situacao ainda funciona porque as forcas internas continuam
claras.

## Relacoes no grafo

- Expande [[aventura-como-situacao]].
- Nasce de [[Spec_Cantina_Conflict_Engine_PRIMUS]] e [[Cantina_Board_0001_PRIMUS]].
- Deve alterar [[WorldState_0001_PRIMUS]] por meio de [[Spec_DeltaP_PRIMUS]].
- Pode ser alimentada por [[rumor-com-fonte-e-incerteza]].

## Onde o DADO vive

Contratos, recompensas, mapa, NPCs e detalhes de encontro vivem em Mission
Contract, PRIMUS Index ou notas de instancia. O grafo guarda o criterio.

## Uso no PRIMUS

Ao gerar missao, validar: existe situacao? existem atores? existem consequencias
para sucesso, falha e omissao? Se nao, e trilho disfarcado.
