---
tipo: spec
area: 80_Specs
projeto: PRIMUS
status: ativo
fonte: [[30_Projetos/PRIMUS/Mapa_Digestao_Rpg_Docx_PRIMUS]]
criado_em: 2026-07-01
atualizado_em: 2026-07-01
tags: [primus, markdown, livros, copyright, catalogentry, obsidian]
---

# SPEC - Markdownizacao Segura de Livros PRIMUS

## Objetivo

Definir quando um livro, PDF, DOCX ou apostila pode virar Markdown no Obsidian.

## Regra Central

Nem toda fonte pode virar nota completa.

```text
Fonte autoral ou livre -> Markdown completo possivel
Fonte restrita -> indice, CatalogEntry, resumo curto, padrao abstrato
Fonte duvidosa -> quarentena ate classificacao
```

## O que Pode Virar MD em Livros Restritos

| Tipo de saida | Permitido | Exemplo |
|---|---|---|
| Indice seguro | sim | nome, categoria, pagina, destino PRIMUS |
| CatalogEntry | sim | type, name, affects, never_affects |
| Resumo curto | sim | funcao operacional sem copiar redacao |
| Padrao abstrato | sim | "item como vetor de campanha" |
| Nota autoral derivada | sim | ideia nova escrita do zero |
| Texto integral | nao | capitulo, tabela completa, statblock |
| Lista completa protegida | nao | copiar conteudo integral de um livro comercial |
| Lista completa de stubs em `40_Wiki` | nao | polui o grafo e enfraquece wikilinks |
| Catalogo consolidado | sim | contagens, indices, fonte e criterios de promocao |

## Armas, Itens, Magias, Racas e Criaturas

Essas familias podem virar muitos MDs, mas com niveis diferentes:

| Familia | Saida segura inicial |
|---|---|
| armas | categorias, papeis taticos, referencia de pagina |
| armaduras | categorias, funcao narrativa, referencia |
| itens comuns | uso operacional, risco, custo abstrato |
| itens magicos | vetor narrativo, tentacao, consequencia |
| magias | tags, escola, funcao de cena, fonte |
| racas/especies | papel narrativo e origem, sem copiar texto |
| classes/subclasses | papel de jogo, funcao, fonte |
| criaturas | tipo, ameaca, habitat, funcao de encontro |
| faccoes | objetivo, recurso, pressao, relacao |
| planos/lugares | funcao cosmologica, risco, acesso |

## Estados de Nota

| Estado | Significado |
|---|---|
| `stub-seguro` | pagina com metadados e links, sem conteudo protegido |
| `resumo-seguro` | resumo curto e transformativo |
| `autoral` | texto criado pelo FabioOS |
| `restrito` | depende de fonte privada; nao publicar |
| `bloqueado` | nao pode entrar no Obsidian ainda |

## Pipeline

```text
Livro/Fonte
  -> classificar licenca
  -> extrair metadados seguros
  -> catalogo consolidado / SQLite / JSONL
  -> selecionar candidatos
  -> validar V(E)
  -> promover poucas notas fortes para Enciclopedia
```

## Criterios de Aceite

- cada MD tem `source_id`;
- cada MD tem `license_status`;
- cada MD aponta para [[40_Wiki/_MOCs/MOC_PRIMUS]];
- nenhum MD contem texto longo protegido;
- cada MD declara `affects` e `never_affects`;
- se for restrito, fica claro que nao e publicavel.

## Aplicacao Imediata

Criar MDs de ideias seguras e abstratas a partir de [[30_Projetos/PRIMUS/CatalogEntries_Candidatas_Rpg_Docx_PRIMUS]].

Para listas completas de armas, itens, magias e criaturas, a etapa correta e manter catalogo consultavel e promover apenas entradas semanticamente fortes.

## Implementacao v0 e Correcao

Implementado em 2026-07-01:

- [[40_Wiki/PRIMUS/Fontes_Oficiais_DND/Catalogo_DND_Core_Consolidado]]
- `60_Sistemas/PRIMUS_Digestor/scripts/07_export_official_stubs.py`
- [[50_Registros/Auditoria/Auditoria_DND_Core_Stubs_2026-07-01]]
- [[50_Registros/Decisoes/ADR_2026-07-01_Catalogo_DND_Core_Sem_Stubs_Massivos]]

O lote massivo de stubs provou o limite da abordagem e foi recolhido da wiki ativa. A regra final e: catalogo bruto fora do grafo; notas individuais so quando promovidas.
