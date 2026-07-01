---
tipo: auditoria
area: 50_Registros
projeto: PRIMUS
status: substituido
classe_dado: Restricted
criado_em: 2026-07-01
tags: [primus, dnd, stubs, auditoria, restricted, official-core]
---

# Auditoria - DND Core Stubs Oficiais

## Pedido

Gerar todos os stubs dos livros oficiais.

## Decisao Posterior

Esta abordagem foi substituida pela ADR:

- [[50_Registros/Decisoes/ADR_2026-07-01_Catalogo_DND_Core_Sem_Stubs_Massivos]]

Motivo: stubs massivos sao tecnicamente possiveis, mas ruins para o grafo do Obsidian.

## Resultado

Foram gerados stubs seguros para todos os registros dos livros oficiais core presentes no PRIMUS Index local:

| Livro | Book key | Stubs |
|---|---|---:|
| Livro do Jogador 2014 | `phb` | 3880 |
| Guia do Mestre 2014 | `dmg` | 3629 |
| Manual dos Monstros 2014 | `mm` | 3094 |
| **Total** |  | **10603** |

Catalogo substituto:

- [[40_Wiki/PRIMUS/Fontes_Oficiais_DND/Catalogo_DND_Core_Consolidado]]

## Metodo

Foi criado o exportador:

- `60_Sistemas/PRIMUS_Digestor/scripts/07_export_official_stubs.py`

O script consulta apenas:

- `id`;
- `book_key`;
- `category`;
- `subtype`;
- `name`;
- `page`;
- `heading`;
- `kind`.

A coluna `text` nao e exportada nem usada nos stubs.

## Politica de Seguranca

Cada stub:

- e `Restricted`;
- nao contem texto integral;
- nao contem tabela completa;
- nao contem statblock;
- nao substitui o livro;
- aponta para fonte, pagina, categoria e destino de revisao;
- exige V(E) antes de promocao.

## Escopo Excluido

`classes_compendio` ficou fora deste lote porque nao e livro oficial core. Ele pode virar lote separado depois, como compendio derivado.

## Validacao

- Lote massivo gerado: `10603` stubs.
- Lote massivo recolhido da wiki ativa.
- `py_compile` do exportador: OK.
- Sem RAG/reindex.
- Sem push.

## Proxima Acao

Escolher uma categoria pequena para promocao controlada:

1. `objetos` do PHB;
2. `entidades` do MM;
3. `funcoes` do PHB;
4. `locais` do DMG.

Promocao significa gerar resumo transformativo ou versao autoral PRIMUS, nao copiar texto oficial.
