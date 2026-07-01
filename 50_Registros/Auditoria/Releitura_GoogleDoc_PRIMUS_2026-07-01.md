---
tipo: auditoria
area: 50_Registros
projeto: PRIMUS
status: ativo
classe_dado: interno
fonte: [[05_Raw_Sources/PRIMUS/2026-06-30_google-doc_primus_contexto_completo_final]]
documento_google: https://docs.google.com/document/d/1x1DLPglzkbnRXTAz7i2PTus8uh5pJ9fQdO7NErgnbhw/edit?usp=sharing
criado_em: 2026-07-01
atualizado_em: 2026-07-01
tags: [primus, auditoria, google-docs, releitura, arquitetura]
---

# Releitura do Google Doc PRIMUS - 2026-07-01

## Contexto

O Google Doc foi relido apos a criacao da malha Obsidian do PRIMUS, dos indices seguros D&D Core e do MOC central.

O documento no Drive nao parece ter sido alterado desde a ultima absorcao relevante. A mudanca desta rodada e de **otica arquitetural**, nao de conteudo bruto novo.

## Diagnostico Atual

A leitura anterior capturou corretamente:

- circuito E -> I -> P;
- tipagem universal;
- precedencia Canon > Setting > Homebrew > Framework;
- WorldState como prioridade antes da Missao 0001;
- Tension Engine como candidato a nucleo causal;
- Cantina como interface de escolhas;
- DeltaP como persistencia formal.

A leitura atual mostra que isso ainda estava incompleto. O documento tambem exige uma camada de operadores que ainda nao estava bem separada no vault.

## Mudanca de Enquadramento

Antes:

```text
PRIMUS = sistema persistente de missoes
```

Agora:

```text
PRIMUS = simulador persistente de mundos orientado por tensoes
```

Consequencia: mais CatalogEntries nao bastam. O sistema precisa decidir o que merece processamento.

## Operadores que Precisam Virar Sistema

| Operador | Papel | Status antes | Acao agora |
|---|---|---|---|
| Arquivo Consultavel | produto de consulta do jogador | citado, mas subdimensionado | formalizar como camada de produto |
| Conhecimento Progressivo | estados do que o jogador sabe | disperso | formalizar estados e escopo |
| Campo de Relevancia `R(X)` | decide o que processar | lacuna | criar criterio de processamento |
| WorldModifier | alteracao global do WorldState | citado em WorldCycle | formalizar tipo |
| ActivityModule | atividade estruturada fora de combate | ausente | formalizar tipo |
| JourneyEngine | deslocamento significativo | ausente | formalizar motor |
| PersistentProgressionObject | entidade persistente que evolui | ausente | formalizar tipo |
| PersistentModifier | transformacao persistente | ausente | formalizar tipo |
| ProblemGenerator | transforma tensao em problema | citado, sem spec | priorizar antes de novas missoes |

## Ajuste de Prioridade

O proximo gargalo nao e ingerir mais livro.

O gargalo e:

```text
WorldState -> R(X) -> Tensao -> Problema -> Conflito -> Cantina -> Missao -> DeltaP
```

Sem `R(X)`, o sistema tenta processar tudo. Com `R(X)`, ele processa somente o que pode alterar o estado do mundo, a escolha dos jogadores ou o conhecimento progressivo.

## Decisao

- Manter Missao 0001 bloqueada.
- Nao promover ingestao massiva como proxima prioridade.
- Formalizar os operadores de mundo antes de executar Engrenagem 6.
- Tratar Arquivo Consultavel como parte do produto final, nao como README auxiliar.

## Artefatos Criados Nesta Rodada

- [[40_Wiki/PRIMUS/Arquivo_Consultavel_PRIMUS]]
- [[80_Specs/PRIMUS/Spec_Operadores_Mundo_PRIMUS]]

## Proxima Acao Recomendada

Criar `ProblemGenerator v0` a partir de `WorldState_0001`, `Tensoes_Iniciais` e `Campo de Relevancia R(X)`, antes de qualquer Missao 0001.
