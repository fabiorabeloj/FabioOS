---
tipo: changelog-projeto
area: 40_Wiki
projeto: PRIMUS
status: formalizado
fonte: [[05_Raw_Sources/PRIMUS/2026-06-30_chatgpt_project_primus_changelog_5_6]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, changelog, worldcycle, vetores, viloes]
---

# PRIMUS - Changelog 5.6

## Titulo

WorldCycle, Vetores de Ameaca e Liga de Viloes Persistente.

## Funcao

Formalizar a versao 5.6 do PRIMUS como passagem de um sistema de missoes para um sistema de mundo persistente operado por vetores, ciclos e consequencias.

## Formula 5.6

```text
WorldState -> Vetores -> Tensoes -> Conflitos -> Atores -> Instancias -> DeltaP -> WorldState
```

## Decisoes Normativas

| ID | Decisao |
|---|---|
| D56-01 | PRIMUS nao gera missoes isoladas; gera missoes a partir de conflitos derivados do WorldState. |
| D56-02 | Vilao nao e encontro; vilao e vetor historico. |
| D56-03 | Liga de Viloes e motor persistente de tensao, nao apenas grupo narrativo. |
| D56-04 | Cantina e interface entre WorldState e escolha dos jogadores. |
| D56-05 | Conflito ignorado nao pausa; ele se desloca. |
| D56-06 | Toda ameaca relevante deve ter estado operacional. |
| D56-07 | PRIMUS nao simula tudo; processa o que tem relevancia, tensao ou consequencia. |
| D56-08 | Todo DeltaP deve poder alterar vetores, faccoes, viloes, regioes, reputacoes, acessos ou cicatrizes. |
| D56-09 | Todo vilao forte deve possuir funcao de mundo, nao apenas estetica. |
| D56-10 | A proxima peca obrigatoria e WorldState v1.0. |

## Vetores

Um vetor e qualquer forca capaz de pressionar o WorldState ao longo do tempo.

Exemplos:

- vilao;
- faccao;
- culto;
- guerra;
- praga;
- divindade;
- artefato;
- plano invasor;
- profecia;
- divida antiga;
- portal instavel;
- catastrofe iminente.

Todo vetor deve responder:

- o que quer;
- o que afeta;
- o que o bloqueia;
- o que acontece se ninguem agir;
- que DeltaP pode produzir.

## Estados de Vetor

| Estado | Definicao |
|---|---|
| ativo | age agora sobre o WorldState |
| latente | existe, mas aguarda gatilho |
| selado | existe, mas esta bloqueado por condicao forte |
| oculto | existe ou age sem conhecimento dos jogadores |
| derrotado | perdeu uma instancia, mas pode deixar efeito |
| transformado | mudou de natureza, escala ou funcao |

## WorldCycle

WorldCycle e o procedimento de atualizacao do mundo.

Ele roda em pontos definidos, nao continuamente:

- fim de missao;
- retorno a Cantina;
- avanco de calendario;
- derrota, fuga ou morte de vilao;
- falha de missao;
- sucesso parcial;
- mudanca de regiao;
- ativacao de WorldModifier;
- escolha de ignorar conflito.

Procedimento:

1. Ler WorldState atual.
2. Identificar vetores relevantes.
3. Atualizar estado dos vetores.
4. Atualizar tensoes.
5. Verificar conflitos emergentes.
6. Mover atores relevantes.
7. Aplicar consequencias de conflitos ignorados.
8. Registrar DeltaP.
9. Atualizar WorldState.
10. Gerar novas opcoes para a Cantina.

## Viloes Persistentes

Regra central:

```text
Derrotar um vilao nao significa remove-lo do PRIMUS.
```

Estados minimos:

- ativo;
- latente;
- oculto;
- selado;
- derrotado;
- morto;
- ressurgente;
- transformado;
- sucessorio;
- mitico.

Pergunta obrigatoria depois de qualquer derrota:

```text
O que permanece depois dele?
```

## Liga de Viloes

A Liga de Viloes e uma estrutura recorrente do WorldState.

Ela pode existir por:

- contrato;
- medo;
- divida;
- profecia;
- inimigo comum;
- submissao;
- pacto planar;
- manipulacao;
- necessidade estrategica;
- controle por artefato;
- prisao compartilhada.

Funcoes:

- espelho sombrio dos jogadores;
- motor de arcos longos;
- fonte de missoes encadeadas;
- mecanismo de retorno de viloes derrotados;
- centro de rivalidade entre viloes;
- ameaca multiversal;
- forca de reorganizacao do WorldState.

## Missao 0001

Status: bloqueada.

Motivo: antes dela, o PRIMUS precisa formalizar:

- WorldState v1.0;
- Vector Engine v1.0;
- Tension Engine v1.0;
- Cantina Conflict Engine v1.0;
- Villain Engine v1.0;
- WorldCycle v1.0;
- DeltaP Schema v1.0;
- Mission Contract v1.0.

## Ordem Oficial Apos 5.6

1. Formalizar WorldState v1.0.
2. Formalizar Vector Engine v1.0.
3. Formalizar Tension Engine v1.0.
4. Formalizar Cantina Conflict Engine v1.0.
5. Formalizar Villain Engine v1.0.
6. Formalizar WorldCycle v1.0.
7. Formalizar DeltaP Schema v1.0.
8. Formalizar Mission Contract v1.0.
9. Criar primeira Liga de Viloes persistente.
10. Criar primeira Cantina Board.
11. Executar Missao 0001.

## Definicao Curta

PRIMUS 5.6 = WorldState + Vetores + Tensoes + Liga de Viloes + WorldCycle + DeltaP.
