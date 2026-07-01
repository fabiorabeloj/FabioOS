---
tipo: spec
area: 80_Specs
projeto: PRIMUS
status: rascunho-operacional
classe_dado: interno
fonte: [[50_Registros/Auditoria/Releitura_GoogleDoc_PRIMUS_2026-07-01]]
criado_em: 2026-07-01
atualizado_em: 2026-07-01
tags: [primus, spec, operadores, worldstate, tension-engine]
---

# SPEC - Operadores de Mundo PRIMUS

## Missao

Formalizar operadores que o Google Doc ja exigia, mas que ainda estavam dispersos no vault.

Estes operadores existem para impedir dois erros:

- simular tudo;
- ingerir conteudo sem saber se ele altera o mundo.

## Cadeia Atual

```text
WorldState
-> Campo de Relevancia R(X)
-> Tensao
-> Problema
-> Conflito
-> Cantina
-> Missao
-> DeltaP
-> WorldState
```

## Campo de Relevancia R(X)

`R(X)` mede a capacidade atual de um elemento alterar o estado do sistema.

| Nivel | Criterio |
|---|---|
| R0 | existe, mas nao afeta nada agora |
| R1 | pode ser consultado no Arquivo |
| R2 | pode alterar uma entrada de Enciclopedia |
| R3 | pode gerar tensao ou conflito |
| R4 | pode alterar WorldState via DeltaP |
| R5 | ameaca ou oportunidade estrutural central |

Regra:

```text
Somente R3+ entra no ciclo causal.
R0-R2 ficam em Enciclopedia/Arquivo.
```

## WorldModifier

Alteracao global, regional, planar ou cosmica do WorldState.

Exemplos:

- Lua Vermelha;
- conjuncao planar;
- inverno eterno;
- tempestade arcana;
- segunda lua.

Campos minimos:

```yaml
world_modifier_id:
escopo:
gatilho:
efeito:
duracao:
reversibilidade:
delta_p_relacionado:
relevancia:
```

## ActivityModule

Atividade estruturada fora de combate.

Exemplos:

- caca;
- pesquisa;
- mineracao;
- comercio;
- torneio;
- navegacao.

Regra:

```text
Sem tensao, nao simular.
Com tensao, instanciar.
```

## JourneyEngine

Motor de deslocamentos significativos.

Uma jornada so vira instancia se tiver:

- risco;
- custo;
- descoberta;
- perseguicao;
- prazo;
- conflito territorial;
- consequencia persistente.

## PersistentProgressionObject

Entidade persistente que evolui.

Exemplos:

- artefato;
- guilda;
- castelo;
- companheiro;
- montaria;
- nave;
- base.

Campos minimos:

```yaml
ppo_id:
tipo:
estado_atual:
nivel_ou_estagio:
gatilhos_de_evolucao:
efeitos:
delta_p_historico:
```

## PersistentModifier

Transformacao persistente aplicada a ator, regiao, item ou faccao.

Exemplos:

- vampirismo;
- licantropia;
- corrupcao;
- mutacao;
- ascensao;
- maldicao.

Campos minimos:

```yaml
persistent_modifier_id:
alvo:
origem:
efeito_mecanico:
efeito_social:
condicao_de_remocao:
delta_p_origem:
```

## ProblemGenerator

Transforma tensao em problema jogavel.

Entrada:

- WorldState;
- tensoes ativas;
- vetores;
- Campo de Relevancia R(X);
- conhecimento disponivel no Arquivo Consultavel.

Saida:

- problema;
- atores;
- opcao de conflito;
- possivel missao;
- DeltaP previsto.

## Relacao com Specs Existentes

- [[80_Specs/PRIMUS/Spec_WorldState_PRIMUS]]
- [[80_Specs/PRIMUS/Spec_Tension_Engine_PRIMUS]]
- [[80_Specs/PRIMUS/Spec_Vector_Engine_PRIMUS]]
- [[80_Specs/PRIMUS/Spec_WorldCycle_PRIMUS]]
- [[80_Specs/PRIMUS/Spec_DeltaP_PRIMUS]]
- [[80_Specs/PRIMUS/Spec_Mission_Contract_PRIMUS]]

## Criterios de Aceite

- cada operador possui entrada e saida;
- nenhum operador altera WorldState sem DeltaP;
- R(X) decide o que entra no ciclo causal;
- Arquivo Consultavel controla conhecimento do jogador;
- Missao 0001 permanece bloqueada ate ProblemGenerator v0 existir.
