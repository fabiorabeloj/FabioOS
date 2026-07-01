---
tipo: conceito
area: 40_Wiki
projeto: PRIMUS
classe_dado: interno
autoria: derivado (conceito de design abstrato; sem texto integral)
fonte_conceitual: sandbox toolkits (Without Number — edições free)
tags: [primus, design, sandbox, regioes, agencia, conceito]
criado_em: 2026-07-01
---

# Sandbox e Jogo por Regiões

## O conceito
Em vez de uma história linear (trilho), o mundo é um **espaço aberto de regiões e
pontos de interesse**. O jogador **escolhe para onde ir**; o mestre prepara **lugares
com potencial**, não uma sequência fixa de cenas. A narrativa **emerge** das escolhas
somadas ao mundo que reage.

## Por que é forte
- **Agência do jogador** no centro: o mundo responde, não conduz.
- **Escalável e reutilizável:** prepara-se por região, não por roteiro.
- **Casa com o motor:** o mundo que "anda sozinho" (facções, turnos) + escolha do jogador.

## Relações no grafo
- Precisa das [[faccoes-e-turnos-de-faccao|facções]] e [[tags-de-aventura|tags]] para
  as regiões terem vida própria.
- Cada visita/escolha gera variacoes -> [[Spec_DeltaP_PRIMUS|DeltaP]] e alimenta o
  [[Spec_Tension_Engine_PRIMUS|Tension Engine]].

## Onde o DADO vive
Mapas e tabelas de geração de hex/local → índice. O grafo fica com o **princípio**
(jogo por regiões × trilho).

## Uso no PRIMUS
Estruturar o [[WorldState_0001_PRIMUS]] como regiões com pontos de interesse; deixar
a Cantina como hub de onde o jogador escolhe o próximo conflito.
