---
tipo: registro
area: 30_Projetos
projeto: PRIMUS
status: rascunho-operacional
fonte: [[30_Projetos/PRIMUS/WorldState_0001_PRIMUS]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, tensoes, tension-engine, worldstate]
---

# Tensoes Iniciais PRIMUS

## Funcao

Registrar as primeiras tensoes estruturais derivadas do [[WorldState_0001_PRIMUS]]. Elas ainda nao sao missoes: sao pressao causal que pode virar conflito.

## Schema de Tensao

```yaml
tension_id:
nome:
tipo:
origem:
atores:
alvo:
recursos:
restricoes:
peso_inicial:
possiveis_conflitos:
status:
```

## TNS-0001 - Mundo sem tensoes canonicas escolhidas

```yaml
tension_id: TNS-0001
nome: Mundo sem tensoes canonicas escolhidas
tipo: estrutural
origem: WorldState inicial sem faccoes e sem conflitos
atores: []
alvo: WorldState
recursos: [catalogo_e, fontes_primus]
restricoes: [nao_inventar_canon, respeitar_precedencia]
peso_inicial: 3
possiveis_conflitos:
  - escolher uma regiao/tema canonicamente seguro
  - selecionar faccoes candidatas com fonte
  - bloquear missao ate haver atores
status: aberta
```

## TNS-0002 - Hub existe antes do entorno jogavel

```yaml
tension_id: TNS-0002
nome: Hub existe antes do entorno jogavel
tipo: interface
origem: Cantina Conflict Engine
atores: [HUB-0001-Cantina]
alvo: Player View
recursos: [cantina, roteiro_principio_superabundancia]
restricoes: [ver_nao_e_ter, sem_vazamento_de_enciclopedia_total]
peso_inicial: 4
possiveis_conflitos:
  - painel de rumores da Cantina
  - conflitos visiveis mas nao adquiridos
  - escolhas limitadas por acesso
status: aberta
```

## TNS-0003 - Catalogo E ainda nao gera conflitos automaticamente

```yaml
tension_id: TNS-0003
nome: Catalogo E ainda nao gera conflitos automaticamente
tipo: motor
origem: Pipeline EIP
atores: [Enciclopedia_Funcional]
alvo: Instancia_Controlada
recursos: [tipagem_universal, templates_por_familia]
restricoes: [cada_entrada_precisa_type, cada_conflito_precisa_fonte]
peso_inicial: 5
possiveis_conflitos:
  - entrada sem instancing hint
  - conflito sem ator
  - missao sem DeltaP previsto
status: aberta
```

## Proximo Passo

Converter estas tensoes em conflitos candidatos usando [[80_Specs/PRIMUS/Spec_Tension_Engine_PRIMUS]].
