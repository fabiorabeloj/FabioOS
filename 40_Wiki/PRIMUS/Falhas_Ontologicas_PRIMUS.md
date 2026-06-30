---
tipo: wiki
area: 40_Wiki
projeto: PRIMUS
status: ativo
fonte: [[05_Raw_Sources/PRIMUS/2026-06-30_chatgpt_project_primus_inventario_logs]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, ontologia, riscos, validacao]
---

# Falhas Ontologicas PRIMUS

## Tese

O PRIMUS tem engenharia estrutural forte, mas sua ontologia ainda precisa ficar explicita. Sem isso, o sistema pode gerar missoes e documentos, mas nao tera inferencia confiavel.

## Lacunas

| Lacuna | Risco | Correcao |
|---|---|---|
| Entidade e processo no mesmo plano | confundir o que existe com o que acontece | separar Entidade, Evento e Estado |
| DeltaP sem ontologia de estado | persistencia vira log narrativo | definir WorldState, InstanceState e ActorState |
| Tipos sem hierarquia | perda de heranca e inferencia | criar ontologia de classes |
| Precedencia sem semantica de verdade | conflito resolvido so por ordem, nao por significado | separar ontologia base e contextual |
| Causalidade implicita | DeltaP arbitrario | criar pre-condicoes, pos-condicoes e DAG causal |
| Agente indefinido | jogador/NPC/criatura ficam semanticamente soltos | definir agente como entidade + intencao + acao + memoria local |
| Relacoes semanticas ausentes em E | grafo pobre e RAG menos confiavel | tipar relacoes: afeta, pertence, depende, ocorre em |
| Fronteira de instancia indefinida | vazamento entre missao e mundo | definir boundary formal da instancia |
| Tempo nao formalizado | eventos simultaneos e updates confusos | definir ciclo, timestamp e granularidade |
| Valor nao quantificado | risco/recompensa subjetivos | definir peso de risco, custo e valor esperado |

## Decisao

A proxima camada do PRIMUS deve ser uma ontologia formal minima antes de expandir lore ou executar Missao 0001.

## Relacoes

- [[80_Specs/PRIMUS/Spec_Ontologia_Formal_PRIMUS]]
- [[80_Specs/PRIMUS/Spec_DeltaP_PRIMUS]]
- [[80_Specs/PRIMUS/Spec_WorldState_PRIMUS]]
