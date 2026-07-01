---
tipo: conceito
area: 40_Wiki
projeto: PRIMUS
classe_dado: interno
autoria: derivado (conceito abstrato; sem texto integral protegido)
fonte_conceitual: D&D Core 2014 (abstrato; modo catalogo restrito)
criado_em: 2026-07-01
tags: [primus, design, personagem, identidade, restrito, conceito]
---

# Classe como Fantasia Operacional

## O conceito

Uma classe de personagem funciona como fantasia operacional: ela define que tipo
de problema o jogador espera resolver, que promessa de identidade ele assume e
qual papel tende a ocupar diante de risco, socializacao e exploracao.

## Por que e forte

E uma abstracao de design, nao uma lista de classes ou regras. Ajuda o PRIMUS a
entender personagem como vetor de decisao e expectativa, sem copiar conteudo de
livro protegido.

## Relacoes no grafo

- Afeta [[Mission_Contract_0001_PRIMUS]] porque contratos devem oferecer escolhas
  para fantasias operacionais diferentes.
- Interage com [[Spec_Cantina_Conflict_Engine_PRIMUS]] na selecao de conflitos.
- Mudancas de papel e reputacao entram em [[Spec_DeltaP_PRIMUS]].
- Dialoga com [[WorldState_0001_PRIMUS]] quando grupos sociais reagem ao personagem.

## Onde o DADO vive

Nomes de classes, tabelas, progressao e habilidades ficam no PRIMUS Index/SQLite
e no catalogo restrito. Nada disso vira nota solta.

## Uso no PRIMUS

Ao criar uma missao, perguntar quais fantasias operacionais ela convoca:
protecao, descoberta, dominio, cura, negociacao, subterfugio ou ruptura.
