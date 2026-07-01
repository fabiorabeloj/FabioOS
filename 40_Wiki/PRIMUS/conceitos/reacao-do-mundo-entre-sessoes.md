---
tipo: conceito
area: 40_Wiki
projeto: PRIMUS
classe_dado: interno
autoria: derivado (conceito de design abstrato; sem texto integral)
fonte_conceitual: Stars Without Number / Worlds Without Number free editions
criado_em: 2026-07-01
tags: [primus, design, worldstate, downtime, consequencia, conceito]
---

# Reacao do Mundo Entre Sessoes

## O conceito

Entre uma sessao e outra, o mundo deve reagir: faccoes avancam, boatos mudam,
problemas pioram, oportunidades expiram e consequencias aparecem. O intervalo
nao e pausa; e parte do motor.

## Por que e forte

Esse conceito torna a campanha viva sem exigir roteiro linear. Ele cria
continuidade, custo de oportunidade e memoria operacional: o que o jogador faz ou
ignora altera o estado futuro.

## Relacoes no grafo

- Depende de [[WorldState_0001_PRIMUS]] como fotografia atual do mundo.
- Usa [[Spec_DeltaP_PRIMUS]] para registrar mudancas entre estados.
- Recebe sinais de [[faccoes-e-turnos-de-faccao]] e [[frente-de-faccao-e-projetos]].
- Atualiza tensoes em [[Spec_Tension_Engine_PRIMUS]].

## Onde o DADO vive

Calendarios, tabelas de evento, nomes e resultados detalhados vivem no indice ou
em logs operacionais. A nota guarda o principio de design.

## Uso no PRIMUS

Ao encerrar uma cena, rodar uma rotina curta: o que avancou, o que piorou, quem
perdeu tempo, que rumor novo surgiu e qual DeltaP precisa ser registrado.
