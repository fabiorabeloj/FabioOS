---
tipo: changelog
area: 50_Registros
projeto: PRIMUS
status: registrado
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, digestor, pdf, catalogentry, markdown]
---

# 2026-06-30 - PRIMUS Digestor v0

## Entrega

Criada a primeira maquina local do PRIMUS para converter fontes grandes em CatalogEntries e Markdown Obsidian.

## Arquivos

- [[05_Raw_Sources/PRIMUS/2026-06-30_google-drive-rpg-docx]]
- [[80_Specs/PRIMUS/Spec_Digestor_PDF_PRIMUS]]
- [[30_Projetos/PRIMUS/Plano_Digestor_PRIMUS]]
- [[60_Sistemas/PRIMUS_Digestor/README]]

## Scripts

- `01_extract_text.py`
- `02_segment_pdf.py`
- `03_classify_entries.py`
- `04_validate_entries.py`
- `05_export_markdown.py`
- `06_import_primus_index.py`

## Resultado

O PRIMUS agora possui pipeline minimo:

```text
PDF/DOCX/TXT/SQLite -> texto -> blocos -> CatalogEntry -> validacao -> Markdown
```

## Limite

O digestor nao copia capitulos inteiros, nao publica conteudo protegido e nao executa Missao 0001.
