---
tipo: spec
area: 80_Specs
projeto: PRIMUS
status: operacional-v0
fonte: [[05_Raw_Sources/PRIMUS/2026-06-30_google-drive-rpg-docx]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, spec, digestor, pdf, catalogentry]
---

# Spec - Digestor PDF/DOCX PRIMUS

## Missao

Converter fontes grandes de RPG em CatalogEntries rastreaveis, tipadas e exportaveis para Obsidian.

## Tese

PDF ou DOCX nao entra no PRIMUS como livro copiado.

Ele entra como mina de pecas:

```text
fonte -> pagina -> bloco -> CatalogEntry -> validacao -> markdown -> instancia
```

## Escopo v0

O digestor trabalha apenas na camada E:

```text
E = Enciclopedia Funcional
```

Ele nao executa missao, nao altera WorldState e nao gera DeltaP final.

## Entradas

- PDFs locais;
- TXT/MD exportados;
- DOCX quando bibliotecas locais permitirem;
- SQLite do PRIMUS Index existente.

## Saidas

- `extracted_raw.jsonl`;
- `blocks.jsonl`;
- `catalog_entries.jsonl`;
- relatorio de validacao;
- Markdown Obsidian gerado a partir de entradas validas.

## Campos Obrigatorios

```yaml
EntryID:
Type:
Name:
Box:
Subbox:
Source:
SourcePath:
Page:
Snippet:
Summary:
Affects:
NeverAffects:
InstancingHints:
Confidence:
LicenseStatus:
```

## Tipos Aceitos

- race;
- subrace;
- class;
- subclass;
- background;
- feat;
- spell;
- item;
- magic_item;
- creature;
- npc;
- deity;
- plane;
- region;
- settlement;
- site;
- dungeon;
- faction;
- organization;
- rule;
- procedure;
- generator;
- mission;
- encounter;
- hazard;
- trap;
- puzzle;
- reward;
- consequence.

## Regras de Seguranca

- Nao copiar capitulo inteiro.
- Nao publicar texto protegido.
- Snippet deve ser curto e servir apenas para rastreio.
- Se a fonte for privada ou livro comercial, marcar `LicenseStatus: Restricted`.
- Se houver duvida de classificacao, marcar `Confidence: Low`.
- Markdown e visualizacao; fonte operacional e JSONL/SQLite/XLSX.

## Criterios de Aceite

- script de extracao roda em arquivo pequeno;
- classificador gera CatalogEntries com campos obrigatorios;
- validador rejeita entrada incompleta;
- exportador cria Markdown com YAML frontmatter;
- smoke test passa sem usar conteudo protegido.
