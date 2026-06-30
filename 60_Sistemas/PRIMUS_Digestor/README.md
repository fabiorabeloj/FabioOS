---
tipo: sistema
area: 60_Sistemas
projeto: PRIMUS
status: operacional-v0
fonte: [[80_Specs/PRIMUS/Spec_Digestor_PDF_PRIMUS]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, digestor, python, pdf, markdown]
---

# PRIMUS Digestor

## Funcao

Pipeline local para transformar fontes grandes em CatalogEntries rastreaveis.

## Fluxo

```text
PDF/DOCX/TXT/SQLite
  -> extracted_raw.jsonl
  -> blocks.jsonl
  -> catalog_entries.jsonl
  -> validacao
  -> Markdown Obsidian
```

## Scripts

| Script | Funcao |
|---|---|
| `01_extract_text.py` | extrai texto por pagina de TXT/MD/PDF/DOCX quando bibliotecas existem |
| `02_segment_pdf.py` | segmenta paginas em blocos candidatos |
| `03_classify_entries.py` | gera CatalogEntries heuristicas |
| `04_validate_entries.py` | valida campos obrigatorios |
| `05_export_markdown.py` | exporta Markdown Obsidian |
| `06_import_primus_index.py` | importa registros do `primus.sqlite` existente |

## Fonte de Verdade

Markdown nao e fonte de verdade.

Fonte operacional:

- JSONL;
- SQLite;
- XLSX futuro.

## Uso Rapido com PRIMUS Index

```powershell
python 60_Sistemas/PRIMUS_Digestor/scripts/06_import_primus_index.py --db "C:\Users\user\Desktop\Projeto\primus-site\primus.sqlite" --book phb --query Juramento --limit 5 --out 60_Sistemas/PRIMUS_Digestor/data/catalog_entries_demo.jsonl
python 60_Sistemas/PRIMUS_Digestor/scripts/04_validate_entries.py --input 60_Sistemas/PRIMUS_Digestor/data/catalog_entries_demo.jsonl
python 60_Sistemas/PRIMUS_Digestor/scripts/05_export_markdown.py --input 60_Sistemas/PRIMUS_Digestor/data/catalog_entries_demo.jsonl --out 60_Sistemas/PRIMUS_Digestor/out/markdown_demo
```

## Smoke Test

```powershell
python 60_Sistemas/PRIMUS_Digestor/tests/smoke_test.py
```

## Restricoes

- nao copiar capitulos inteiros;
- nao publicar conteudo protegido;
- snippets curtos apenas para rastreio;
- entradas duvidosas ficam `Confidence: Low`;
- fontes privadas ficam `LicenseStatus: Restricted`.
