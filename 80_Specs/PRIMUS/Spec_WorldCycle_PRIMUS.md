---
tipo: spec
area: 80_Specs
projeto: PRIMUS
status: rascunho-operacional
fonte: [[40_Wiki/PRIMUS/Changelog_PRIMUS_5_6]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, spec, worldcycle, worldstate, deltap]
---

# Spec - WorldCycle PRIMUS

## Missao

Definir o procedimento de atualizacao do mundo entre instancias.

## Gatilhos

- fim de missao;
- retorno a Cantina;
- passagem de tempo;
- derrota, fuga, morte ou retorno de vilao;
- conflito ignorado;
- mudanca de regiao;
- evento cosmico;
- atualizacao de faccao.

## Entrada

- WorldState atual;
- vetores ativos/latentes/ocultos/selados;
- conflitos disponiveis e ignorados;
- DeltaP pendente;
- estado das faccoes e viloes.

## Saida

- WorldState atualizado;
- DeltaP registrado;
- novos conflitos candidatos;
- Cantina Board atualizada;
- lista de riscos escalados.

## Procedimento v0

1. Congelar snapshot do WorldState atual.
2. Listar vetores relevantes.
3. Aplicar DeltaP validos.
4. Atualizar estado dos vetores.
5. Atualizar tensoes.
6. Mover atores relevantes.
7. Processar conflitos ignorados.
8. Gerar novas opcoes de Cantina.
9. Registrar changelog e log operacional.

## Regras

- WorldCycle nao roda continuamente.
- WorldCycle nao inventa evento sem causa.
- Conflito ignorado deve deslocar, escalar, recuar ou ser resolvido por outro ator.
- Toda alteracao persistente exige DeltaP.
- Se nao houver fonte, a saida fica como rascunho ou prototipo.

## Criterios de Aceite

- o ciclo tem entrada e saida rastreaveis;
- toda mudanca aponta para causa;
- todo DeltaP tem antes/depois;
- nenhuma missao e executada sem contrato;
- a Cantina recebe apenas opcoes seguras para jogador.
