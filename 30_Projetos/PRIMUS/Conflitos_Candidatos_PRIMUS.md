---
tipo: registro
area: 30_Projetos
projeto: PRIMUS
status: rascunho-operacional
fonte: [[30_Projetos/PRIMUS/Tensoes_Iniciais_PRIMUS]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, conflitos, cantina, tension-engine, player-view]
---

# Conflitos Candidatos PRIMUS

## Funcao

Converter tensoes em conflitos candidatos para a Cantina Conflict Engine. Estes conflitos ainda nao sao missoes; sao opcoes visiveis, bloqueadas ou pendentes de fonte.

## Tabela Operacional

| ID | Origem | Titulo | Status | Visivel na Cantina | Bloqueio |
|---|---|---|---|---|---|
| CCF-0001 | TNS-0001 | Escolher primeira regiao segura | bloqueado | nao | falta fonte/regiao canonica selecionada |
| CCF-0002 | TNS-0002 | Quadro de rumores da Cantina | pronto-para-prototipo | sim | nenhum bloqueio tecnico; exige Player View minima |
| CCF-0003 | TNS-0003 | Entradas sem instancing hint | pronto-para-triagem | sim | precisa selecionar entradas E reais |
| CCF-0004 | TNS-0002 | Ver nao e ter | pronto-para-regra | sim | precisa marcar estados V/A/Oculto |
| CCF-0005 | TNS-0003 | Missao sem DeltaP previsto | bloqueado | nao | precisa schema DeltaP completo |

## CCF-0001 - Escolher primeira regiao segura

```yaml
conflict_candidate_id: CCF-0001
origem_tension_id: TNS-0001
titulo: Escolher primeira regiao segura
atores: []
local: indefinido
gatilho: WorldState inicial nao possui regiao canonica jogavel
risco: inventar lore sem fonte
recompensa_possivel: primeira base espacial/geografica para conflitos reais
delta_p_possivel: nenhum
peso: 3
visivel_em_player_view: false
status: bloqueado
bloqueios:
  - falta regiao
  - falta fonte
  - falta ator
fontes:
  - [[WorldState_0001_PRIMUS]]
```

## CCF-0002 - Quadro de rumores da Cantina

```yaml
conflict_candidate_id: CCF-0002
origem_tension_id: TNS-0002
titulo: Quadro de rumores da Cantina
atores: [HUB-0001-Cantina]
local: Cantina
gatilho: jogadores precisam ver opcoes sem receber conhecimento total
risco: vazar Enciclopedia total
recompensa_possivel: primeira interface de escolha
delta_p_possivel: nenhum ate haver missao
peso: 4
visivel_em_player_view: true
status: pronto-para-prototipo
bloqueios: []
fontes:
  - [[Motor_Causal_PRIMUS]]
  - [[Spec_Cantina_Conflict_Engine_PRIMUS]]
```

## CCF-0003 - Entradas sem instancing hint

```yaml
conflict_candidate_id: CCF-0003
origem_tension_id: TNS-0003
titulo: Entradas sem instancing hint
atores: [Enciclopedia_Funcional]
local: Catalogo PRIMUS
gatilho: entradas E precisam declarar como viram jogo
risco: conteudo permanecer texto solto
recompensa_possivel: converter catalogo em motor
delta_p_possivel: nenhum
peso: 5
visivel_em_player_view: false
status: pronto-para-triagem
bloqueios:
  - precisa selecionar entries reais
fontes:
  - [[Tipagem_Universal_PRIMUS]]
  - [[Pipeline_PRIMUS]]
```

## CCF-0004 - Ver nao e ter

```yaml
conflict_candidate_id: CCF-0004
origem_tension_id: TNS-0002
titulo: Ver nao e ter
atores: [Player_View, HUB-0001-Cantina]
local: Cantina
gatilho: jogador pode visualizar catalogos sem adquirir poder
risco: quebrar progressao
recompensa_possivel: primeira regra de acesso mobile/interface
delta_p_possivel: item_transfer ou access_key, somente apos evento de jogo
peso: 4
visivel_em_player_view: true
status: pronto-para-regra
bloqueios:
  - falta schema V/A/Oculto
fontes:
  - [[Leis_do_PRIMUS]]
```

## CCF-0005 - Missao sem DeltaP previsto

```yaml
conflict_candidate_id: CCF-0005
origem_tension_id: TNS-0003
titulo: Missao sem DeltaP previsto
atores: [Mission_Engine]
local: Motor do Jogo
gatilho: Missao 0001 existe como preparacao, mas nao pode executar sem DeltaP
risco: mundo resetar ou gerar consequencia nao rastreavel
recompensa_possivel: contrato de missao confiavel
delta_p_possivel: a definir
peso: 5
visivel_em_player_view: false
status: bloqueado
bloqueios:
  - DeltaP incompleto
  - WorldState ainda nao recebe atualizacao real
fontes:
  - [[Missao_0001_Preparacao]]
  - [[Spec_WorldState_PRIMUS]]
```

## Proximo Passo

Construir a primeira Player View da Cantina usando apenas conflitos com `visivel_em_player_view: true`.
