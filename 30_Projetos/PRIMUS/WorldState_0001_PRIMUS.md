---
tipo: worldstate
area: 30_Projetos
projeto: PRIMUS
status: rascunho-operacional
fonte: [[05_Raw_Sources/PRIMUS/2026-06-30_google-doc_primus_contexto_completo_final]]
spec: [[80_Specs/PRIMUS/Spec_WorldState_PRIMUS]]
world_state_id: PRIMUS-WS-0001
escopo: WorldLine
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, worldstate, linha-de-mundo, tension-engine, delta-p]
---

# WorldState 0001 - PRIMUS

## Funcao

Criar o primeiro estado de mundo do PRIMUS sem executar missao e sem inventar canon definitivo. Este arquivo e um bootstrap operacional: permite testar o Tension Engine e preparar conflitos antes da Missao 0001.

## Estado

```yaml
world_state_id: PRIMUS-WS-0001
nome: Linha de Mundo Alfa
versao: 0.1
escopo: WorldLine
canon_base: D&D 5e
status: rascunho-operacional
data_interna: indefinida
regioes_ativas:
  - HUB-0001-Cantina
factions_ativas: []
tensoes_ativas:
  - TNS-0001
  - TNS-0002
  - TNS-0003
conflitos_disponiveis: []
delta_p_aplicado: []
fontes:
  - Google Doc PRIMUS contexto completo final
  - Roteiro de Execucao PRIMUS
notas: "Estado inicial sem missao executada; usado para derivar tensoes e conflitos."
```

## Entidades Ativas

| ID | Tipo | Nome | Estado | Observacao |
|---|---|---|---|---|
| HUB-0001-Cantina | hub | Cantina | ativo | Interface de retorno e escolha de conflitos. |
| WS-ALFA | worldline | Linha de Mundo Alfa | ativo | Linha inicial de teste, sem canon derivado ainda. |

## Tensoes Ativas

| ID | Nome | Origem | Estado |
|---|---|---|---|
| TNS-0001 | Mundo sem tensoes canonicas escolhidas | WorldState inicial | aberta |
| TNS-0002 | Hub existe antes do entorno jogavel | Cantina Conflict Engine | aberta |
| TNS-0003 | Catalogo E ainda nao gera conflitos automaticamente | Pipeline EIP | aberta |

Detalhes em [[Tensoes_Iniciais_PRIMUS]].

## Regras de Uso

- Nao executar Missao 0001 a partir deste arquivo sem antes gerar conflitos candidatos.
- Nao criar faccoes definitivas sem fonte, template ou justificativa.
- Nao aplicar DeltaP sem registrar origem e escopo.
- Nao simular tempo continuo; atualizacoes ocorrem por procedimento explicito.

## Proxima Transicao

```text
WorldState_0001
-> Tension Engine
-> conflitos candidatos
-> Cantina Conflict Engine
-> escolha de missao
```

## Relacoes

- [[40_Wiki/PRIMUS/Motor_Causal_PRIMUS]]
- [[Tensoes_Iniciais_PRIMUS]]
- [[80_Specs/PRIMUS/Spec_Tension_Engine_PRIMUS]]
