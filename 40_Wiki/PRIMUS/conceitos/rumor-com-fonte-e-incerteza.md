---
tipo: conceito
area: 40_Wiki
projeto: PRIMUS
classe_dado: interno
autoria: derivado (conceito de design abstrato; sem texto integral)
fonte_conceitual: Stars Without Number / Worlds Without Number free editions
criado_em: 2026-07-01
tags: [primus, design, rumores, informacao, cantina, conceito]
---

# Rumor com Fonte e Incerteza

## O conceito

Um rumor bom nao e apenas uma pista. Ele tem fonte, interesse e incerteza. Quem
contou? O que essa pessoa ganha? O que pode estar errado? Assim, informacao vira
decisao e nao so entrega de contexto.

## Por que e forte

Rumores conectam mundo, NPCs, faccoes e missoes sem forcar o jogador por uma
trilha. Eles tambem tornam a Cantina uma interface viva do mundo.

## Relacoes no grafo

- Especializa [[Cantina_Rumores_0001_PRIMUS]].
- Usa [[npc-com-agenda-e-alavancas]] como fonte interessada.
- Aponta para conflitos da [[Spec_Cantina_Conflict_Engine_PRIMUS]].
- Pode revelar ou distorcer tensoes de [[Spec_Tension_Engine_PRIMUS]].

## Onde o DADO vive

Listas de rumores prontos, nomes e resultados de rolagem ficam em indice ou em
instancias de sessao. A nota registra o padrao de construcao.

## Uso no PRIMUS

Todo rumor de Cantina deve ter tres campos: fonte, interesse e grau de incerteza.
Isso impede que rumor vire apenas exposition dump.
