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
| PRIMUS-TASK-0006 | Catalogo | pending | critica | Selecionar primeiro lote de CatalogEntries reais | 20 entradas tipadas |
| PRIMUS-TASK-0007 | Validacao | pending | critica | Definir V(E), V(I), V(P) operacional | criterios verificaveis |
| PRIMUS-TASK-0008 | Motor | pending | alta | Formalizar CatalogPool | pool consultavel para Engrenagem 6 |
| PRIMUS-TASK-0009 | Motor | pending | alta | Formalizar Engrenagem 6 | spec de geracao de missao |
| PRIMUS-TASK-0010 | Persistencia | pending | alta | Aplicar DeltaP ao WorldState | update manual validado |
| PRIMUS-TASK-0011 | Interface | pending | media | Criar mock da Cantina | tela Obsidian/UI |
| PRIMUS-TASK-0012 | Automacao | pending | media | Desenhar workflow n8n PRIMUS Steward | fluxo sem codigo destrutivo |

## Proxima Tarefa

`PRIMUS-TASK-0006`: selecionar 20 CatalogEntries reais a partir de D&D Core + WWN.
