---
tipo: spec
area: 80_Specs
projeto: PRIMUS
status: rascunho
fonte: [[05_Raw_Sources/PRIMUS/2026-06-30_google-doc_primus_contexto_completo_final]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, spec, worldstate, tension-engine, delta-p]
---

# SPEC - WorldState PRIMUS

## Objetivo

Definir o estado minimo de mundo necessario antes de executar missoes PRIMUS.

## Problema

Missao sem estado de mundo vira narrativa isolada. O Google Doc v5.1/v5.4 desloca a prioridade: primeiro WorldState, depois Tension Engine, depois conflitos e missoes.

## Entrada

- entradas tipadas em E;
- decisoes de canon/setting/homebrew/framework;
- faccoes ou atores existentes;
- locais relevantes;
- registros DeltaP anteriores, se existirem.

## Saida

Um objeto WorldState consultavel, versionavel e atualizavel por DeltaP.

## Schema Minimo

```yaml
world_state_id:
nome:
versao:
escopo:
canon_base:
data_interna:
regioes_ativas:
factions_ativas:
tensoes_ativas:
conflitos_disponiveis:
delta_p_aplicado:
fontes:
status:
notas:
```

## Regras

- `escopo` deve ser Local, Campaign, WorldLine ou DerivedCanon.
- Toda tensao ativa deve apontar para atores, local e fonte/justificativa.
- DeltaP deve ser aplicado de forma rastreavel.
- Estado nao deve reinventar economia, magia ou regras ja resolvidas pelo canon.

## Criterios de Aceite

- Um agente consegue listar "o que esta acontecendo no mundo" sem acessar historico de chat.
- Pelo menos uma tensao pode ser derivada de um estado.
- Pelo menos um conflito pode ser derivado de uma tensao.
- A Missao 0001 consegue consumir WorldState em vez de criar contexto do zero.

## Proxima Entrega

Criar `WorldState_0001_PRIMUS.md` em projeto ou registros, contendo estado minimo para a primeira linha de mundo.
