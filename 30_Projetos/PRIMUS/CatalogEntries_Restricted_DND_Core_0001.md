---
tipo: catalogentries
area: 30_Projetos
projeto: PRIMUS
status: restrito-catalogado
fonte: [[05_Raw_Sources/PRIMUS/2026-06-30_pdf-dnd-core-restricted-lote-0001]]
spec: [[80_Specs/PRIMUS/Spec_CatalogEntry_PRIMUS]]
classe_dado: Restricted
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, dnd, catalogentry, restricted, fonte]
---

# CatalogEntries Restricted - D&D Core 0001

## Objetivo

Transformar os PDFs D&D Core em entradas operacionais seguras, sem copiar o conteudo integral.

Estas entradas sao **CatalogEntries de fonte**. Elas nao sao regras jogaveis completas.

## CatalogEntries de Fonte

| EntryID | Type | Name | SourceID | Box | Subbox | Affects | NeverAffects | Instancing Hint | LicenseStatus | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CE-DND-SRC-PHB-2014 | source_book | Player-facing Core Rules | SRC-DND-PHB-2014 | Fonte Restrita | D&D Core | CatalogPool, Validacao VE, Character Options | public_export, raw_rag, worldstate_without_delta_p | usar apenas para validar entradas de personagem com pagina/referencia | Restricted | Medium | restricted-source |
| CE-DND-SRC-DMG-2014 | source_book | Referee Core Rules | SRC-DND-DMG-2014 | Fonte Restrita | D&D Core | CatalogPool, Validacao VE, Encounter/Treasure | public_export, raw_rag, worldstate_without_delta_p | usar apenas para validar encontro, tesouro e estruturas de aventura | Restricted | Medium | restricted-source |
| CE-DND-SRC-MM-2014 | source_book | Bestiary Core Rules | SRC-DND-MM-2014 | Fonte Restrita | D&D Core | CatalogPool, Validacao VE, Creature Roles | public_export, raw_rag, worldstate_without_delta_p | usar apenas para validar criatura, ameaca e papel de combate | Restricted | Medium | restricted-source |

## Mapeamento para o Lote 0001

| CatalogEntry existente | Fonte preferencial | Acao segura |
|---|---|---|
| CE-DND-0001 Player Character | SRC-DND-PHB-2014 | validar conceito e fonte; nao copiar regra |
| CE-DND-0002 Class | SRC-DND-PHB-2014 | ja tem VE-local-index-pass; manter fonte restrita |
| CE-DND-0003 Species/Race | SRC-DND-PHB-2014 | resolver parcial com ancora generica ou aceitar evidencia por especie |
| CE-DND-0004 Background | SRC-DND-PHB-2014 | ja tem VE-local-index-pass |
| CE-DND-0005 Spell | SRC-DND-PHB-2014 | ja tem VE-local-index-pass |
| CE-DND-0006 Equipment | SRC-DND-PHB-2014 | validado como quinta entrada estavel via PRIMUS Index |
| CE-DND-0007 Creature | SRC-DND-MM-2014 | validar pelo PRIMUS Index ou documentalista |
| CE-DND-0008 Condition | SRC-DND-PHB-2014 | ja tem VE-local-index-pass |
| CE-DND-0009 Encounter | SRC-DND-DMG-2014 | validar quando DMG estiver processavel |
| CE-DND-0010 Treasure | SRC-DND-DMG-2014 | validar quando DMG estiver processavel |

## Regras de Promocao

Uma entrada derivada destas fontes so pode virar `pool-ready` se:

- tiver `source_id`;
- tiver pagina ou referencia rastreavel;
- tiver resumo proprio, nao copia longa;
- mantiver `LicenseStatus: Restricted`;
- tiver `NeverAffects` preenchido;
- nao for enviada ao RAG bruto.

## Recomendacao Operacional

`CE-DND-0006 Equipment` ja foi validada como quinta entrada estavel. O proximo ganho de confianca e validar `CE-DND-0007 Creature` com `SRC-DND-MM-2014`.
