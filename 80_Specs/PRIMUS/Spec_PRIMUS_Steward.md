---
tipo: spec
area: 80_Specs
projeto: PRIMUS
status: rascunho
fonte: [[40_Wiki/PRIMUS/Arquitetura_MultiIA_PRIMUS]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, spec, steward, agente, governanca]
---

# SPEC - PRIMUS Steward

## Objetivo

Criar a camada de continuidade operacional do PRIMUS.

## Definicao

PRIMUS Steward e o agente gerente-executor que:

1. percebe o estado atual;
2. decide a proxima acao valida;
3. executa a menor unidade util;
4. registra o resultado;
5. atualiza a fila;
6. aponta a proxima tarefa.

## Arquivos Vivos

| Arquivo | Funcao |
|---|---|
| `PRIMUS_MASTER.md` | norma consolidada |
| `Fila_Operacional_PRIMUS.md` | tarefas pendentes/em andamento/concluidas |
| `PRIMUS_DONE_LOG.md` | memoria factual do que foi feito |
| `Changelog` | mudancas estruturais |
| `WorldState_0001_PRIMUS.md` | estado inicial do mundo/projeto |

## Formato de Resposta do Steward

```text
1. Estado atual
2. Pendencia detectada
3. Acao executada agora
4. Registro do que foi feito
5. Proxima acao
```

## Limites

- Nao apagar log.
- Nao sobrescrever Stable sem changelog.
- Nao executar missao sem contrato e DeltaP.
- Nao adicionar fonte sem matriz de uso.
- Nao promover lore sem rastreabilidade.

## Implementacao Minima

Usar Obsidian + Git:

- fila em Markdown;
- done log em `50_Registros/Logs_Agentes/`;
- changelog por lote;
- barramento para handoff ao Claude;
- commit tematico por entrega.
