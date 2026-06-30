---
tipo: plano
area: 30_Projetos
projeto: PRIMUS
status: ativo
classe_dado: Restricted
fonte: [[05_Raw_Sources/PRIMUS/2026-06-30_pdf-dnd-core-restricted-lote-0001]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, dnd, restricted, copyright, catalogo]
---

# Plano - Transformacao Restricted D&D Core

## Missao

Usar PDFs D&D Core como fonte privada de validacao do PRIMUS sem transformar o FabioOS em repositorio de texto protegido.

## Camadas

```text
PDF local ignorado pelo Git
  -> evento drop-folder
  -> documentalista extrai localmente em area ignorada
  -> Codex/PRIMUS gera CatalogEntries e resumos seguros
  -> curadoria humana
  -> CatalogPool
```

## Responsabilidades

| Camada | Dono | Regra |
|---|---|---|
| Extracao de texto/OCR | Claude/documentalista | zona exclusiva do Claude |
| Porta de entrada PDF | Codex | concluida |
| CatalogEntries/metadados PRIMUS | Codex | permitido |
| RAG/reindex | Claude | somente com lock e curadoria |
| Interface | Cursor | apenas visualizacao do status |

## Saida Permitida no Git

- metadados;
- SourceIDs;
- hashes/event IDs;
- resumos funcionais de alto nivel;
- CatalogEntries;
- decisoes de governanca.

## Saida Proibida no Git

- texto integral;
- capitulos;
- tabelas copiadas longas;
- listas completas protegidas;
- stat blocks integrais;
- PDFs.

## Sequencia Recomendada

1. Usar `CE-DND-SRC-PHB-2014`, `CE-DND-SRC-DMG-2014`, `CE-DND-SRC-MM-2014` como fontes restritas.
2. Validar `CE-DND-0006 Equipment` como quinta entrada estavel.
3. Adiar `CE-DND-0003 Species/Race` se a ancora generica continuar parcial.
4. Promover apenas CatalogEntries com pagina/referencia, resumo proprio e `NeverAffects`.
5. Gerar Missao 0001 somente depois de contrato e DeltaP previsto.

## Criterio de Aceite

- As tres fontes D&D Core existem como `SourceID`.
- O lote Restricted esta ligado ao CatalogEntries Lote 0001.
- Nenhum conteudo integral foi copiado.
- O Claude/documentalista pode usar os eventos para extrair localmente quando pronto.
