---
tipo: fila
area: 30_Projetos
projeto: PRIMUS
status: ativo
fonte: [[80_Specs/PRIMUS/Spec_PRIMUS_Steward]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, fila, steward, tarefas]
---

# Fila Operacional PRIMUS

## Regra

Toda tarefa deve ter area, status, saida esperada e criterio de conclusao.

## Tarefas

| TaskID | Area | Status | Prioridade | Acao | Saida Esperada |
|---|---|---|---|---|---|
| PRIMUS-TASK-0001 | Fontes | done | alta | Inventariar Project ChatGPT PRIMUS | inventario de logs/fontes |
| PRIMUS-TASK-0002 | Ontologia | done | critica | Criar spec de ontologia formal | [[80_Specs/PRIMUS/Spec_Ontologia_Formal_PRIMUS]] |
| PRIMUS-TASK-0003 | Persistencia | done | critica | Criar spec de DeltaP | [[80_Specs/PRIMUS/Spec_DeltaP_PRIMUS]] |
| PRIMUS-TASK-0004 | Fontes | done | alta | Criar matriz de fontes | [[40_Wiki/PRIMUS/Matriz_Fontes_PRIMUS]] |
| PRIMUS-TASK-0005 | Governanca | done | alta | Criar spec do PRIMUS Steward | [[80_Specs/PRIMUS/Spec_PRIMUS_Steward]] |
| PRIMUS-TASK-0006 | Catalogo | done | critica | Selecionar primeiro lote de CatalogEntries reais | [[CatalogEntries_Lote_0001_PRIMUS]] |
| PRIMUS-TASK-0007 | Validacao | done | critica | Definir V(E), V(I), V(P) operacional | [[80_Specs/PRIMUS/Spec_Validacao_VE_PRIMUS]] |
| PRIMUS-TASK-0008 | Motor | done | alta | Formalizar CatalogPool | [[CatalogPool_0001_PRIMUS]] |
| PRIMUS-TASK-0009 | Motor | pending | alta | Formalizar Engrenagem 6 | spec de geracao de missao |
| PRIMUS-TASK-0010 | Persistencia | pending | alta | Aplicar DeltaP ao WorldState | update manual validado |
| PRIMUS-TASK-0011 | Interface | pending | media | Criar mock da Cantina | tela Obsidian/UI |
| PRIMUS-TASK-0012 | Automacao | pending | media | Desenhar workflow n8n PRIMUS Steward | fluxo sem codigo destrutivo |
| PRIMUS-TASK-0013 | Changelog | done | critica | Formalizar Changelog 5.6 a partir dos logs do Project ChatGPT | [[40_Wiki/PRIMUS/Changelog_PRIMUS_5_6]] |
| PRIMUS-TASK-0014 | Operacao | done | critica | Criar cockpit operacional minimo | [[PRIMUS_Operacao_v1]] |
| PRIMUS-TASK-0015 | Motor | done | alta | Formalizar Vector Engine v0 | [[80_Specs/PRIMUS/Spec_Vector_Engine_PRIMUS]] |
| PRIMUS-TASK-0016 | Motor | done | alta | Formalizar WorldCycle v0 | [[80_Specs/PRIMUS/Spec_WorldCycle_PRIMUS]] |
| PRIMUS-TASK-0017 | Motor | done | alta | Formalizar Villain Engine v0 e Mission Contract v0 | [[80_Specs/PRIMUS/Spec_Villain_Engine_PRIMUS]] |
| PRIMUS-TASK-0018 | Validacao | done-parcial | critica | Validar pagina/trecho de 5 CatalogEntries prioritarias | [[Validacao_VE_5_Entradas_PRIMUS_Index]] |
| PRIMUS-TASK-0019 | Persistencia | pending | critica | Promover WorldState v1.0 | WorldState com vetores e DeltaP |
| PRIMUS-TASK-0020 | Motor | pending | alta | Rodar primeira rodada manual de WorldCycle sem missao canonica | Cantina Board atualizada |
| PRIMUS-TASK-0021 | Validacao | pending | alta | Resolver parcial de CE-DND-0003 ou substituir por Equipment | quinta entrada estavel para pool |
| PRIMUS-TASK-0022 | Fontes | done | alta | Registrar Google Drive `Rpg .docx` como fonte restrita | [[05_Raw_Sources/PRIMUS/2026-06-30_google-drive-rpg-docx]] |
| PRIMUS-TASK-0023 | Digestor | done | critica | Criar PRIMUS Digestor v0 | [[60_Sistemas/PRIMUS_Digestor/README]] |
| PRIMUS-TASK-0024 | Digestor | pending | alta | Rodar digestor em lote pequeno real | `catalog_entries.jsonl` validado |

## Proxima Tarefa

`PRIMUS-TASK-0024`: rodar o digestor em lote pequeno real e validar a saida antes de liberar Engrenagem 6 ou Missao 0001.
