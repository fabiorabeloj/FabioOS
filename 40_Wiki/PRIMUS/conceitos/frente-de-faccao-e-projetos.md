---
tipo: conceito
area: 40_Wiki
projeto: PRIMUS
classe_dado: interno
autoria: derivado (conceito de design abstrato; sem texto integral)
fonte_conceitual: Stars Without Number / Worlds Without Number free editions
criado_em: 2026-07-01
tags: [primus, design, faccoes, projetos, sandbox, conceito]
---

# Frente de Faccao e Projetos

## O conceito

Uma faccao nao deve ser apenas um nome no cenario. Ela precisa ter uma frente de
acao: objetivo, plano atual, recurso disponivel, obstaculo e proximo movimento.
O projeto da faccao transforma uma ideia politica ou social em pressao ativa no
mundo.

## Por que e forte

E uma ideia reutilizavel: qualquer grupo do mundo pode ser modelado como uma
forca que tenta mudar o estado atual. Ela tambem evita que o mundo fique parado
esperando o jogador, porque cada projeto cria tensao mesmo fora da cena.

## Relacoes no grafo

- Expande [[faccoes-e-turnos-de-faccao]] com um nivel operacional.
- Alimenta [[Spec_Tension_Engine_PRIMUS]] com objetivos em conflito.
- Gera mudancas para [[Spec_DeltaP_PRIMUS]] e atualiza [[WorldState_0001_PRIMUS]].
- Pode virar conflito jogavel na [[Spec_Cantina_Conflict_Engine_PRIMUS]].

## Onde o DADO vive

Listas de faccoes, assets, tabelas e estatisticas vivem no PRIMUS Index/SQLite.
O grafo registra apenas o principio: faccao como projeto ativo.

## Uso no PRIMUS

Para cada faccao importante, registrar um projeto atual em uma frase: "quer X,
usando Y, antes que Z aconteca". Isso vira materia-prima para rumores, missoes e
DeltaP.
