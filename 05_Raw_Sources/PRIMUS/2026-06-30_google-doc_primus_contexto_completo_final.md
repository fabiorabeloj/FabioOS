---
tipo: fonte
area: 05_Raw_Sources
projeto: PRIMUS
status: processado
origem: Google Docs
documento: PRIMUS - CONTEXTO COMPLETO FINAL (NAO PERDER)
url: https://docs.google.com/document/d/1x1DLPglzkbnRXTAz7i2PTus8uh5pJ9fQdO7NErgnbhw/edit?usp=sharing
document_id: 1x1DLPglzkbnRXTAz7i2PTus8uh5pJ9fQdO7NErgnbhw
revision_id: ALtnJHypFqzH1ZNlYn_VeyXRctP9lphPoJ_IgeDXZ9aF1_RF9H7TbNzSFNhJRHxO2wafZ5N6WhfFBJ2j6WHimUXRnlZxZ6cLEevVTzkaAx4
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, google-docs, fonte, rpg, worldstate, tension-engine]
---

# Google Doc - PRIMUS contexto completo final

## Funcao

Registrar a absorcao do Google Doc multiaba do PRIMUS como fonte viva. Este arquivo nao tenta duplicar o documento inteiro: ele preserva o endereco, identifica as abas e extrai as decisoes estruturais que mudam a arquitetura do PRIMUS dentro do FabioOS.

## Abas Identificadas

- Proximo passo (agora) - em blocos operacionais.
- Primus bloco 1.
- Bloco 2.
- Bloco 3.
- SUMARIO-TESTE 2 - PROJETO PRIMUS (VISAO TOTAL).
- Guia 6.
- Guia 7.
- Guia 8.
- PRIMUS v4.
- Guia 10.
- Guia 11.
- Guia 12.
- Guia 13.
- Guia 14.

## Extracao Arquitetural

O documento confirma que PRIMUS nao e uma enciclopedia narrativa. Ele e uma maquina editorial e de jogo persistente:

```text
Enciclopedia Funcional (E)
-> Instancia Controlada (I)
-> Persistencia (P)
-> WorldState atualizado
```

A versao v4 organiza a Constituicao, a tipagem universal, os templates por familia, os livros operacionais, o controle de conflito e os criterios de aceite. A versao v5.1/v5.4 desloca a prioridade da Missao 0001 para a fundacao causal: WorldState, Tension Engine e Cantina Conflict Engine.

## Decisoes Relevantes

| Tema | Decisao extraida |
|---|---|
| Missao 0001 | Nao deve ser prioridade imediata. So deve existir depois da arquitetura essencial. |
| Tempo | Nao e motor primario; deve ser registro canonico derivado do jogo. |
| Economia | Nao reinventar; herdar o canon e apenas registrar/organizar. |
| Recursos magicos | Nao criar mana universal; herdar spell slots, cargas, usos e componentes do canon. |
| Estados | Devem depender do tipo: dungeon, NPC, faccao etc. |
| Relacoes | Devem surgir principalmente de sessoes, DeltaP e persistencia. |
| Causalidade | Modelo aceito: necessidade estrutural + contingencia ponderada. |
| Scheduler | Nao simulacao continua; procedimentos de atualizacao quando necessario. |
| Nucleo causal | Tension Engine passa a ser candidato principal a nucleo causal. |

## Ordem Estrutural Atual

```text
WorldState
-> Tensoes
-> Conflitos
-> Faccoes
-> Missoes
-> DeltaP
-> WorldState
```

## Consequencia Para o FabioOS

O PRIMUS deve ser tratado como um laboratorio de arquitetura operacional do FabioOS:

- LLM Wiki para conhecimento autoportante;
- RAG e Grafo apenas apos governanca e tipagem;
- MCP/automacoes apenas apos contrato de entrada e saida;
- agentes so depois de templates e criterios de aceite;
- jogo e narrativa sempre subordinados a rastreabilidade, tipagem e persistencia.

## Links Gerados

- [[40_Wiki/PRIMUS/Leis_do_PRIMUS]]
- [[40_Wiki/PRIMUS/Pipeline_PRIMUS]]
- [[40_Wiki/PRIMUS/Tipagem_Universal_PRIMUS]]
- [[40_Wiki/PRIMUS/Livros_do_PRIMUS]]
- [[40_Wiki/PRIMUS/Motor_Causal_PRIMUS]]
