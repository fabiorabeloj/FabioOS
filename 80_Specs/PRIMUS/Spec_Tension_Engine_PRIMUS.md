---
tipo: spec
area: 80_Specs
projeto: PRIMUS
status: rascunho
fonte: [[05_Raw_Sources/PRIMUS/2026-06-30_google-doc_primus_contexto_completo_final]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, spec, tension-engine, worldstate, conflitos]
---

# SPEC - Tension Engine PRIMUS

## Objetivo

Converter WorldState em tensoes ponderadas e conflitos candidatos sem pular direto para missao.

## Entradas

- [[30_Projetos/PRIMUS/WorldState_0001_PRIMUS]]
- entradas tipadas em E;
- DeltaP aplicado;
- limites de canon/setting/homebrew/framework;
- Player View e permissoes de acesso.

## Saidas

- lista de tensoes validadas;
- conflitos candidatos;
- pesos iniciais;
- bloqueios explicitos quando faltarem atores, recursos ou fonte.

## Fluxo

```text
WorldState
-> coletar sinais
-> normalizar tensoes
-> validar dependencias
-> ponderar possibilidades
-> propor conflitos
-> enviar para Cantina Conflict Engine
```

## Schema de Saida

```yaml
conflict_candidate_id:
origem_tension_id:
titulo:
atores:
local:
gatilho:
risco:
recompensa_possivel:
delta_p_possivel:
peso:
visivel_em_player_view:
status:
bloqueios:
fontes:
```

## Regras

- Nao gerar missao diretamente.
- Nao criar ator definitivo sem fonte ou justificativa manual.
- Nao usar dado antes de existir lista de possibilidades estruturais.
- Nao atualizar WorldState sem DeltaP ou procedimento explicito.
- Se faltar ator, local, motivo, recurso ou autorizacao, a saida deve ser bloqueio, nao invencao.

## Criterios de Aceite

- Dado um WorldState, o motor produz pelo menos uma tensao ou explica por que nao consegue.
- Cada tensao tem origem rastreavel.
- Cada conflito candidato aponta para uma tensao.
- Conflito sem ator/local/motivo fica bloqueado.
- A Cantina recebe conflitos visiveis, mas nao entrega propriedade ao jogador automaticamente.

## Implementacao Minima

Inicialmente, implementar como procedimento manual em Markdown:

1. Ler WorldState.
2. Listar tensoes ativas.
3. Validar dependencias.
4. Gerar candidatos em tabela.
5. Marcar bloqueios.

So depois transformar em script/agente.
