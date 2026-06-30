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

## Regra Derivada do Project ChatGPT

WorldState nao deve ser editado manualmente como lore. Ele e leitura acumulada dos DeltaP validos.

```text
Evento valido -> DeltaP -> WorldState recalculado
```

Se algo muda no mundo sem DeltaP, a mudanca ainda nao e estado PRIMUS.

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

## Schema Tecnico Ampliado

```yaml
world_id:
version:
current_cycle:
current_date_mode:
active_flags:
access_keys:
reputations:
debts:
curses:
boons:
deaths:
scars:
item_transfers:
ownerships:
timer_states:
open_threads:
locked_content:
unlocked_content:
last_valid_mission_id:
last_update_timestamp:
```

## Tabelas Recomendadas

| Tabela | Funcao |
|---|---|
| `world_state_index` | indice de versao, ciclo, data e ultima missao valida |
| `world_flags` | flags globais, regionais, planares ou sociais |
| `reputations` | relacoes com faccoes/NPCs/assentamentos |
| `access_keys` | acessos liberados ou consumidos |
| `debts` | obrigacoes e favores pendentes |
| `death_records` | mortes, reversoes e remocoes criticas |
| `scars` | marcas persistentes fisicas, sociais, magicas, planares ou politicas |
| `item_transfers` | transferencias de item/posse |
| `timer_states` | relogios, ciclos e prazos |

## Regras

- `escopo` deve ser Local, Campaign, WorldLine ou DerivedCanon.
- Toda tensao ativa deve apontar para atores, local e fonte/justificativa.
- DeltaP deve ser aplicado de forma rastreavel.
- Estado nao deve reinventar economia, magia ou regras ja resolvidas pelo canon.
- WorldState so muda por DeltaP valido ou procedimento de update registrado.

## Criterios de Aceite

- Um agente consegue listar "o que esta acontecendo no mundo" sem acessar historico de chat.
- Pelo menos uma tensao pode ser derivada de um estado.
- Pelo menos um conflito pode ser derivado de uma tensao.
- A Missao 0001 consegue consumir WorldState em vez de criar contexto do zero.
- Um agente consegue recalcular WorldState lendo DeltaP ativos.

## Proxima Entrega

Selecionar CatalogEntries reais e gerar o primeiro DeltaP de teste sem executar missao completa.
