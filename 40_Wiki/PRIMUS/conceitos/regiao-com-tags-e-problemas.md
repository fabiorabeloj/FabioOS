---
tipo: conceito
area: 40_Wiki
projeto: PRIMUS
classe_dado: interno
autoria: derivado (conceito de design abstrato; sem texto integral)
fonte_conceitual: Stars Without Number / Worlds Without Number free editions
criado_em: 2026-07-01
tags: [primus, design, regioes, tags, problemas, conceito]
---

# Regiao com Tags e Problemas

## O conceito

Uma regiao fica jogavel quando combina identidade, problemas e tags geradoras.
A tag da cor; o problema cria urgencia; a regiao oferece escolhas. Assim, o mapa
deixa de ser decoracao e passa a ser uma maquina de situacoes.

## Por que e forte

E um no de conhecimento, nao um dado, porque ensina como estruturar lugares. A
mesma tecnica serve para cidade, planeta, vila, reino, dungeon ou distrito.

## Relacoes no grafo

- Especializa [[sandbox-e-jogo-por-regioes]].
- Usa [[tags-de-aventura]] como gerador de conflitos.
- Alimenta [[Spec_Tension_Engine_PRIMUS]] com problemas regionais.
- Registra efeitos em [[WorldState_0001_PRIMUS]] e [[Spec_DeltaP_PRIMUS]].

## Onde o DADO vive

Mapas, nomes de localidades, listas de regioes e tabelas de tags ficam no PRIMUS
Index/SQLite ou em notas autorais especificas, se forem realmente usadas em jogo.

## Uso no PRIMUS

Criar cada regiao com tres linhas: "identidade", "problema ativo" e "tag de
pressao". Se nao gerar escolha, ainda e dado cru e nao deve virar nota central.
