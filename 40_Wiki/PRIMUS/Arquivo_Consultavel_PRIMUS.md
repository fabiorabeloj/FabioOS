---
tipo: wiki
area: 40_Wiki
projeto: PRIMUS
status: ativo
classe_dado: interno
fonte: [[50_Registros/Auditoria/Releitura_GoogleDoc_PRIMUS_2026-07-01]]
criado_em: 2026-07-01
atualizado_em: 2026-07-01
tags: [primus, arquivo-consultavel, conhecimento-progressivo, produto]
---

# Arquivo Consultavel PRIMUS

## Definicao

O Arquivo Consultavel e a camada de produto que permite aos jogadores descobrir, consultar, comparar e recordar conhecimento adquirido durante a operacao do PRIMUS.

Ele nao e um novo vertice do prisma EIP. Ele e um operador de acesso.

```text
E -> I -> P
      |
      v
Arquivo Consultavel
```

## Papel

| Funcao | Regra |
|---|---|
| Descobrir | mostrar apenas conhecimento liberado |
| Consultar | permitir busca por entidades, lugares, itens, criaturas e faccoes |
| Comparar | revelar diferencas entre estados de conhecimento |
| Recordar | manter cronica de missoes, DeltaP e descobertas |

## Conhecimento Progressivo

O jogador nao recebe conhecimento total automaticamente.

| Estado | Definicao |
|---|---|
| oculto | existe no sistema, mas nao foi descoberto |
| avistado | foi percebido, mas sem compreensao |
| catalogado | possui registro confiavel |
| compreendido | possui contexto, uso e relacoes |

## Aplicavel a

- criaturas;
- itens;
- magias;
- faccoes;
- locais;
- artefatos;
- WorldModifiers;
- PersistentModifiers;
- PersistentProgressionObjects.

## Relacao com a Enciclopedia

A Enciclopedia PRIMUS guarda o que pode existir. O Arquivo Consultavel mostra o que o jogador pode saber.

```text
Enciclopedia E = conhecimento possivel
Arquivo Consultavel = conhecimento disponivel ao jogador
```

## Relacao com Persistencia

Conhecimento tambem e recurso persistente.

Uma descoberta pode gerar DeltaP:

```yaml
delta_type: KnowledgeState
target_id: entidade_ou_local
value_before: oculto
value_after: catalogado
source: missao/evento/procedimento
```

## Relacoes

- [[40_Wiki/_MOCs/MOC_PRIMUS]]
- [[40_Wiki/PRIMUS/Enciclopedia/README]]
- [[40_Wiki/PRIMUS/Persistencia/README]]
- [[80_Specs/PRIMUS/Spec_Operadores_Mundo_PRIMUS]]
- [[80_Specs/PRIMUS/Spec_DeltaP_PRIMUS]]
