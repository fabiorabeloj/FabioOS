---
tipo: player-view
area: 30_Projetos
projeto: PRIMUS
status: rascunho-operacional
fonte: [[30_Projetos/PRIMUS/Conflitos_Candidatos_PRIMUS]]
spec: [[80_Specs/PRIMUS/Spec_Cantina_Conflict_Engine_PRIMUS]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, player-view, cantina, conflitos, interface]
---

# Player View - Cantina 0001

## Funcao

Primeira tela conceitual da Cantina PRIMUS. Ela mostra opcoes visiveis ao jogador sem revelar a Enciclopedia total e sem conceder propriedade automaticamente.

## Regra de Acesso

| Estado | Significado |
|---|---|
| V | Visivel: o jogador pode ver ou ouvir falar. |
| A | Adquirido: o jogador conquistou por evento de jogo. |
| Oculto | Nao aparece para o jogador. |

## Opcoes Visiveis

| ID | Conflito | Estado | Titulo Visivel | Acao Permitida |
|---|---|---|---|---|
| PV-CAN-0001 | CCF-0002 | V | Quadro de rumores da Cantina | consultar rumores disponiveis |
| PV-CAN-0002 | CCF-0004 | V | Regras de acesso: ver nao e ter | entender limites de posse/acesso |

## PV-CAN-0001 - Quadro de rumores da Cantina

```yaml
cantina_option_id: PV-CAN-0001
conflict_candidate_id: CCF-0002
titulo_visivel: Quadro de rumores da Cantina
descricao_curta: "A Cantina lista possibilidades, mas nem toda possibilidade e uma missao pronta."
estado_acesso: V
requisitos:
  - WorldState ativo
  - conflitos candidatos visiveis
risco_visivel: "rumores podem estar incompletos"
recompensa_visivel: "descobrir opcoes futuras de aventura"
bloqueios: []
status: visivel
```

## PV-CAN-0002 - Regras de acesso: ver nao e ter

```yaml
cantina_option_id: PV-CAN-0002
conflict_candidate_id: CCF-0004
titulo_visivel: "Ver nao e ter"
descricao_curta: "Voce pode conhecer a existencia de algo sem possuir, usar ou desbloquear aquilo."
estado_acesso: V
requisitos:
  - Player View ativa
risco_visivel: "confundir conhecimento com aquisicao"
recompensa_visivel: "clareza sobre progressao e desbloqueios"
bloqueios:
  - falta schema final V/A/Oculto
status: visivel-com-aviso
```

## Opcoes Ocultas ou Bloqueadas

| Conflito | Estado | Motivo |
|---|---|---|
| CCF-0001 | Oculto | Falta fonte/regiao/ator. |
| CCF-0003 | Oculto | E triagem interna do catalogo, nao opcao de jogador. |
| CCF-0005 | Oculto | Missao sem DeltaP previsto nao pode aparecer. |

## O Que Ainda Nao Acontece

- nenhuma missao e executada;
- nenhum item e adquirido;
- nenhuma regiao canonica e criada;
- nenhum DeltaP e aplicado;
- nenhum segredo da Enciclopedia total e revelado.

## Proxima Acao

Definir `Cantina_Rumores_0001_PRIMUS.md` com 2 ou 3 rumores seguros, cada um apontando para conflito candidato ou bloqueio.
