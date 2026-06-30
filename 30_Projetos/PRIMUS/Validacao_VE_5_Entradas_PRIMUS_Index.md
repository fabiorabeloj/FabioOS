---
tipo: validacao
area: 30_Projetos
projeto: PRIMUS
status: aplicado-local-index
fonte: [[30_Projetos/PRIMUS/Runtime_PRIMUS_Index_Local]]
spec: [[80_Specs/PRIMUS/Spec_Validacao_VE_PRIMUS]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, validacao, ve, sqlite, catalogentries]
---

# Validacao V(E) - Entradas via PRIMUS Index

## Funcao

Validar CatalogEntries prioritarias usando o runtime local `PRIMUS Index`, sem copiar trechos longos dos livros.

## Criterio

Uma entrada recebe `VE-local-index-pass` quando o banco local possui:

- livro;
- pagina;
- nome ou ancora compativel;
- categoria aproximada;
- registro consultavel por `record_id`.

## Evidencias

| CatalogEntry | Resultado | Livro | Pagina | Record ID | Ancora | Observacao |
|---|---|---|---|---|---|---|
| CE-DND-0002 | VE-local-index-pass | phb | 46 | `68e41d25-b37e-4815-8415-8cdc29c4ac21` | CLASSES | valida `class` como funcao/base de personagem |
| CE-DND-0003 | VE-local-index-pass | phb | 18 | `868a79ee-22cc-4ca8-b30b-ec35f5652e54` | ESCOLHENDO UMA RAÇA | valida `species/race` por ancora generica |
| CE-DND-0004 | VE-local-index-pass | phb | 128 | `314918d2-8dba-4078-bf38-2c7249eb2883` | ANTECEDENTES | valida `background` |
| CE-DND-0005 | VE-local-index-pass | phb | 66 | `add9e812-d4cf-4a54-97fa-f002d6bb8843` | PREPARANDO E CONJURANDO MAGIAS | valida `spell` como regra de magia/conjuracao |
| CE-DND-0006 | VE-local-index-pass | phb | 153 | `bed90f56-fd8f-48cd-af0f-b3e0e0bfc7e0` | EQUIPAMENTO | valida `equipment` como recurso/objeto de personagem |
| CE-DND-0007 | VE-local-index-pass | mm | 4 | `35c6d241-b738-4c62-9dd6-ff591dfcf90a` | O QUE E UM MONSTRO | valida `creature` como ator/ameaca de desafio |
| CE-DND-0008 | VE-local-index-pass | phb | 292 | `249b57c3-89fa-4231-987c-a61d073f34ce` | APENDICE A: CONDICOES | valida `condition` |
| CE-DND-0009 | VE-local-index-pass | dmg | 81 | `d73f90d8-bf4b-4b49-8392-e71f3ddfe186` | CRIANDO ENCONTROS | valida `encounter` como unidade de desafio |
| CE-DND-0010 | VE-local-index-pass | dmg | 133 | `b267d38d-749c-4710-adaa-b7aeb1792e0d` | USANDO AS TABELAS DE TESOURO INDIVIDUAL | valida `treasure` como recompensa/objeto |

## Decisao

As entradas acima deixam de estar apenas em `fonte-pendente`.

Novo estado recomendado:

- `CE-DND-0002`: `VE-local-index-pass`;
- `CE-DND-0003`: `VE-local-index-pass`;
- `CE-DND-0004`: `VE-local-index-pass`;
- `CE-DND-0005`: `VE-local-index-pass`;
- `CE-DND-0006`: `VE-local-index-pass`;
- `CE-DND-0007`: `VE-local-index-pass`;
- `CE-DND-0008`: `VE-local-index-pass`.
- `CE-DND-0009`: `VE-local-index-pass`;
- `CE-DND-0010`: `VE-local-index-pass`.

## Limites

- A validacao usa indice extraido por heuristica.
- A pagina existe no banco, mas ainda nao substitui revisao humana do PDF.
- Nenhum trecho longo foi transcrito para evitar transformar fonte em copia.
- `CE-DND-0003` recebeu ancora generica melhor e deixou de ser parcial.
- `CE-DND-0006` foi validada como alternativa estavel para completar o minimo de 5 entradas pass.
- `CE-DND-0007` foi validada no Monster Manual como primeira entrada pass do grupo Desafio.
- `CE-DND-0009` e `CE-DND-0010` foram validadas contra DMG.

## Impacto

O PRIMUS agora possui evidencias locais suficientes para iniciar a proxima etapa de forma controlada:

```text
CatalogEntry -> V(E) local-index -> CatalogPool parcial -> Mission Contract futuro
```

Missao 0001 continua bloqueada ate:

- vetor narrativo jogavel;
- conflito candidato com ator/local;
- DeltaP previsto;
- WorldState v1.0.
