---
tipo: spec
area: 80_Specs
projeto: PRIMUS
status: rascunho-operacional
fonte: [[40_Wiki/PRIMUS/Changelog_PRIMUS_5_6]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, spec, viloes, villain-engine, worldstate]
---

# Spec - Villain Engine PRIMUS

## Missao

Tratar viloes como vetores historicos persistentes.

## Entrada

- CatalogEntries validadas;
- arquetipo funcional;
- fonte canonica ou homebrew validado;
- vetor associado;
- funcao de mundo;
- relacao com faccoes, regioes e jogadores.

## Saida

- registro em [[30_Projetos/PRIMUS/Villains_0001_PRIMUS]];
- vetor associado;
- conflito candidato;
- possivel DeltaP.

## Modelo de Criacao

```text
Arquetipo Universal
+ Referencia Canonica
+ Mito/Historia
+ Raca
+ Classe
+ Funcao de Mundo
+ Estetica
+ Contradicao Interna
```

## Estados de Vilao

- ativo;
- latente;
- oculto;
- selado;
- derrotado;
- morto;
- ressurgente;
- transformado;
- sucessorio;
- mitico.

## Campos Minimos

```yaml
villain_id:
nome:
estado:
arquetipo:
referencia_canonica:
raca:
classe:
funcao_de_mundo:
vetor_associado:
faccao_associada:
relacao_com_jogadores:
forma_de_retorno:
delta_p_possivel:
fonte:
canon_status:
```

## Regras

- Vilao nao nasce canonico sem fonte.
- Vilao precisa ter funcao de mundo.
- Derrota nao remove automaticamente o vilao.
- Todo vilao precisa responder: o que permanece depois dele?
- Liga de Viloes deve ser funcionalmente assimetrica.

## Criterios de Aceite

- vilao possui estado operacional;
- vilao possui vetor associado;
- vilao possui funcao de mundo;
- vilao tem pelo menos uma consequencia possivel;
- vilao nao viola precedencia Canon > Setting > Homebrew > Framework.
