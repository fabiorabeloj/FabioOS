---
tipo: changelog
area: 50_Registros
projeto: PRIMUS
status: registrado
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, validacao, sqlite, catalogentries]
---

# 2026-06-30 - Validacao V(E) de 5 Entradas via PRIMUS Index

## Entrega

Usado o runtime local [[30_Projetos/PRIMUS/Runtime_PRIMUS_Index_Local]] para validar 5 CatalogEntries por livro, pagina e `record_id`.

## Resultado

- 4 entradas receberam `VE-local-index-pass`;
- 1 entrada recebeu `VE-local-index-partial`;
- nenhuma missao foi executada;
- nenhum trecho longo de fonte foi copiado.

## Arquivos

- [[30_Projetos/PRIMUS/Validacao_VE_5_Entradas_PRIMUS_Index]]
- [[30_Projetos/PRIMUS/CatalogEntries_Lote_0001_PRIMUS]]
- [[30_Projetos/PRIMUS/Validacao_VE_Lote_0001_PRIMUS]]

## Proxima Acao

Revisar `CE-DND-0003` para obter ancora generica melhor de `species/race` ou substituir a quinta entrada por `equipment`, que o indice encontra com mais estabilidade.
