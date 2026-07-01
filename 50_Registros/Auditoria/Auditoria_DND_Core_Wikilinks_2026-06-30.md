---
tipo: auditoria
area: 50_Registros
projeto: PRIMUS
status: ativo
classe_dado: Restricted
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, dnd, auditoria, wikilinks, restricted]
---

# Auditoria - DND Core Wikilinks Seguros

## Pedido

Extrair wikilinks e markdowns dos livros oficiais enviados como PDFs.

## Decisao de Seguranca

Os livros D&D Core foram tratados como `Restricted`.

Portanto, a extracao nao copia texto integral, regras, tabelas ou secoes completas. A entrega usa apenas:

- livro;
- pagina;
- categoria;
- ancora curta;
- wikilink de destino PRIMUS.

## Fontes Processadas

| SourceID | Livro | Arquivo gerado | Ancoras categorizadas |
|---|---|---|---:|
| SRC-DND-PHB-2014 | Livro do Jogador | [[40_Wiki/PRIMUS/Fontes_Oficiais_DND/DND_Core_PHB_2014_Index_Seguro]] | 1527 |
| SRC-DND-DMG-2014 | Guia do Mestre | [[40_Wiki/PRIMUS/Fontes_Oficiais_DND/DND_Core_DMG_2014_Index_Seguro]] | 1197 |
| SRC-DND-MM-2014 | Manual dos Monstros | [[40_Wiki/PRIMUS/Fontes_Oficiais_DND/DND_Core_MM_2014_Index_Seguro]] | 994 |

## Origem Tecnica

- PDFs em `00_Inbox/pdfs/`.
- PyMuPDF confirmou que os PDFs nao possuem outline interno.
- A extracao operacional usou o PRIMUS Index local em `C:\Users\user\Desktop\Projeto\primus-site\primus.sqlite`.
- A coluna `text` nao foi exportada.

## Resultado

- Criada pasta [[40_Wiki/PRIMUS/Fontes_Oficiais_DND/README]].
- Criado mapa [[40_Wiki/PRIMUS/Fontes_Oficiais_DND/Wikilinks_DND_Core_PRIMUS]].
- Indices linkados ao [[40_Wiki/_MOCs/MOC_PRIMUS]] e as familias da Enciclopedia PRIMUS.

## Limites

- Sem dump integral.
- Sem RAG/reindex.
- Sem exportacao publica.
- Sem criacao massiva de notas individuais para cada ancora.

## Proxima Acao

Transformar apenas as entradas priorizadas em notas proprias, usando [[40_Wiki/PRIMUS/Templates/Template_Entrada_Enciclopedia_PRIMUS]].
