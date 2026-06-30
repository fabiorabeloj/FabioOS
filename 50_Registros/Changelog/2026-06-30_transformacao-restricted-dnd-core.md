---
tipo: changelog
area: 50_Registros
projeto: PRIMUS
status: registrado
classe_dado: interno
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, dnd, restricted, catalogentry]
---

# 2026-06-30 - Transformacao Restricted D&D Core

## Contexto

Claude definiu que extracao/documentalista e sua zona. Codex ficou responsavel pela transformacao Restricted dos D&D no PRIMUS.

## Entrega

- Nota-fonte segura: [[05_Raw_Sources/PRIMUS/2026-06-30_pdf-dnd-core-restricted-lote-0001]].
- CatalogEntries de fonte: [[30_Projetos/PRIMUS/CatalogEntries_Restricted_DND_Core_0001]].
- Plano de uso seguro: [[30_Projetos/PRIMUS/Plano_Transformacao_Restricted_DND_Core]].

## Limites Preservados

- sem extracao de texto;
- sem OCR;
- sem RAG;
- sem dump integral no Git/Obsidian;
- sem alterar `documentalista.py`.

## Resultado

Os PDFs D&D Core agora existem no PRIMUS como fontes restritas rastreaveis:

- `SRC-DND-PHB-2014`;
- `SRC-DND-DMG-2014`;
- `SRC-DND-MM-2014`.

## Validacao Adicional

`CE-DND-0006 Equipment` foi validada via PRIMUS Index:

- livro: `phb`;
- pagina: `153`;
- record id: `bed90f56-fd8f-48cd-af0f-b3e0e0bfc7e0`;
- ancora: `EQUIPAMENTO`;
- resultado: `VE-local-index-pass`.

Isso completa uma alternativa estavel de 5 entradas `pass`, mantendo `CE-DND-0003` como parcial.

## Validacao CE-DND-0007

`CE-DND-0007 Creature` foi validada via PRIMUS Index:

- livro: `mm`;
- pagina: `4`;
- record id: `35c6d241-b738-4c62-9dd6-ff591dfcf90a`;
- ancora: `O QUE E UM MONSTRO`;
- resultado: `VE-local-index-pass`.

Isso inicia o grupo Desafio com uma entrada `pass`, sem extrair texto do PDF MM.

## Rodada de Ancoras

Foram aplicadas ancoras adicionais via PRIMUS Index:

| CatalogEntry | Resultado | Livro | Pagina | Record ID | Ancora |
|---|---|---|---:|---|---|
| CE-DND-0003 | VE-local-index-pass | phb | 18 | `868a79ee-22cc-4ca8-b30b-ec35f5652e54` | ESCOLHENDO UMA RAÇA |
| CE-DND-0009 | VE-local-index-pass | dmg | 81 | `d73f90d8-bf4b-4b49-8392-e71f3ddfe186` | CRIANDO ENCONTROS |
| CE-DND-0010 | VE-local-index-pass | dmg | 133 | `b267d38d-749c-4710-adaa-b7aeb1792e0d` | USANDO AS TABELAS DE TESOURO INDIVIDUAL |

Nenhum texto integral foi copiado.
