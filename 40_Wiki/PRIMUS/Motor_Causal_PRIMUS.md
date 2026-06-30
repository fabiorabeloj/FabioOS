---
tipo: wiki
area: 40_Wiki
projeto: PRIMUS
status: ativo
fonte: [[05_Raw_Sources/PRIMUS/2026-06-30_google-doc_primus_contexto_completo_final]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, worldstate, tension-engine, causalidade, delta-p]
---

# Motor Causal PRIMUS

## Tese

O nucleo operacional do PRIMUS nao deve comecar pela primeira missao. A missao e uma consequencia. A fundacao deve ser:

```text
WorldState
-> Tensoes
-> Conflitos
-> Faccoes
-> Missoes
-> DeltaP
-> WorldState
```

## Descoberta Central

A pergunta "como uma faccao chega a um ataque bem-sucedido?" revelou que `tensao -> missao` e insuficiente. Antes da missao, precisam existir:

- estado inicial do mundo;
- atores;
- objetivos;
- recursos;
- restricoes;
- doutrina/alinhamento;
- autorizacao ou oportunidade;
- projeto/operacao;
- resultado verificavel.

## Modelo de Causalidade

Modelos rejeitados:

- aleatoriedade pura;
- determinismo absoluto;
- Geist como operador computavel.

Modelo aceito:

```text
necessidade estrutural + contingencia ponderada
```

A estrutura define o espaco de possibilidades. Os dados escolhem qual possibilidade estrutural se manifesta.

## Cantina Conflict Engine

A Cantina deixa de ser apenas hub narrativo e vira interface de escolha:

```text
Cantina
-> conflitos disponiveis
-> escolha do jogador
-> missao
-> DeltaP
-> retorno
```

Regra de superabundancia: os jogadores devem receber mais conflitos do que conseguem resolver. Isso permite que o mundo continue mudando sem depender de execucao continua.

## Scheduler

PRIMUS nao pressupoe simulacao continua. O mundo avanca por procedimentos explicitos de atualizacao quando necessario.

## Ordem de Implementacao Recomendada

1. WorldState.
2. Tension Engine.
3. Cantina Conflict Engine formal.
4. Faction Engine.
5. Problem Generator.
6. Economy Engine usando canon como fonte.
7. Encounter Engine.
8. Dungeon Engine.
9. Mission Engine.
10. DeltaP completo.

## Impacto Imediato

A [[30_Projetos/PRIMUS/Missao_0001_Preparacao]] deve ficar congelada como preparacao, nao como proxima execucao. O proximo passo real e formalizar WorldState minimo.

## Artefatos Iniciais

- [[30_Projetos/PRIMUS/WorldState_0001_PRIMUS]]
- [[30_Projetos/PRIMUS/Tensoes_Iniciais_PRIMUS]]
- [[80_Specs/PRIMUS/Spec_WorldState_PRIMUS]]
- [[80_Specs/PRIMUS/Spec_Tension_Engine_PRIMUS]]

## Relacoes

- [[PrimusOS]]
- [[Leis_do_PRIMUS]]
- [[Pipeline_PRIMUS]]
- [[Livros_do_PRIMUS]]
