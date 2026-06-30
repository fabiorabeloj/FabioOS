---
tipo: spec
area: 80_Specs
projeto: PRIMUS
status: rascunho
fonte: [[05_Raw_Sources/PRIMUS/2026-06-30_chatgpt_project_primus_inventario_logs]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, spec, deltap, persistencia, worldstate]
---

# SPEC - DeltaP PRIMUS

## Definicao

DeltaP e diferenca de estado validada.

```text
DeltaP: Estado(t0) -> Estado(t1)
```

Nao e resumo narrativo. Nao e memoria vaga. E uma alteracao rastreavel causada por evento valido.

## Schema Minimo

```yaml
delta_p_id:
delta_type:
scope:
target_id:
value_before:
value_after:
justification:
mission_id:
timestamp:
status:
source:
```

## Tipos Oficiais

| Tipo | Funcao |
|---|---|
| WorldFlag | altera estado global, regional, planar ou social |
| AccessKey | libera acesso a lugar, faccao, missao, rota, plano ou recurso |
| Reputation | altera relacao com faccao, NPC, assentamento ou deidade |
| Debt | cria obrigacao, favor, contrato ou divida |
| Curse | adiciona restricao persistente |
| Boon | adiciona beneficio persistente |
| DeathRecord | registra morte ou remocao critica |
| Scar | registra marca fisica, social, magica, planar ou politica |
| ItemTransfer | transfere item ou posse |
| Ownership | registra propriedade |
| TimerState | registra contador, prazo ou relogio |

## Regras

- Todo DeltaP deve apontar para evento/missao ou procedimento de update.
- DeltaP sem `value_before` e `value_after` fica incompleto.
- DeltaP sem `scope` nao atualiza WorldState.
- DeltaP pode substituir, neutralizar ou encerrar DeltaP anterior.
- WorldState e leitura acumulada dos DeltaP validos.

## Criterios de Aceite

- Um DeltaP permite explicar exatamente o que mudou.
- Um agente consegue recalcular WorldState a partir dos DeltaP ativos.
- DeltaP nao depende de lembranca do mestre ou do chat.
