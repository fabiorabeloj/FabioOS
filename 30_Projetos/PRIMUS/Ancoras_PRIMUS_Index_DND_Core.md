---
tipo: auditoria-validacao
area: 30_Projetos
projeto: PRIMUS
status: aplicado-local-index
classe_dado: Restricted
fonte: [[30_Projetos/PRIMUS/Runtime_PRIMUS_Index_Local]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, ancoras, dnd, validacao, catalogentry]
---

# Ancoras PRIMUS Index - D&D Core

## Funcao

Registrar ancoras de validacao sem copiar texto protegido.

Cada ancora e apenas:

```text
CatalogEntry -> livro -> pagina -> record_id -> titulo/ancora
```

## Ancoras Aplicadas

| CatalogEntry | Resultado | Livro | Pagina | Record ID | Ancora | Motivo |
|---|---|---|---:|---|---|---|
| CE-DND-0003 | VE-local-index-pass | phb | 18 | `868a79ee-22cc-4ca8-b30b-ec35f5652e54` | ESCOLHENDO UMA RAÇA | ancora generica melhor para species/race |
| CE-DND-0009 | VE-local-index-pass | dmg | 81 | `d73f90d8-bf4b-4b49-8392-e71f3ddfe186` | CRIANDO ENCONTROS | ancora geral para encounter |
| CE-DND-0010 | VE-local-index-pass | dmg | 133 | `b267d38d-749c-4710-adaa-b7aeb1792e0d` | USANDO AS TABELAS DE TESOURO INDIVIDUAL | ancora objeto/recompensa para treasure |

## Ancoras Secundarias

| Uso | Livro | Pagina | Record ID | Ancora |
|---|---|---:|---|---|
| Encounter difficulty | dmg | 82 | `787cf937-b184-4280-98b4-74f7e32b6943` | DIFICULDADE DO ENCONTRO DE COMBATE |
| Treasure tables | dmg | 136 | `5910b59f-c797-4032-8b02-6643e76e293d` | TESOURO INDIVIDUAL: DESAFIO 0-4 |

## Limites

- Nenhum texto integral foi copiado.
- Nenhum PDF foi extraido nesta frente.
- Nenhum conteudo foi enviado ao RAG.
- A validacao e metadado local, nao publicacao de conteudo.
