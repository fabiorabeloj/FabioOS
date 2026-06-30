---
tipo: plano
area: 30_Projetos
projeto: PRIMUS
status: ativo
fonte: [[80_Specs/PRIMUS/Spec_Digestor_PDF_PRIMUS]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, digestor, pdf, markdown, catalogo]
---

# Plano Digestor PRIMUS

## Funcao

Transformar PDFs, DOCX e indices existentes em CatalogEntries utilizaveis pelo PRIMUS.

## Ordem Correta

1. Extrair texto por pagina.
2. Segmentar em blocos.
3. Classificar blocos em tipos PRIMUS.
4. Validar campos obrigatorios.
5. Exportar Markdown.
6. Usar entradas validadas no CatalogPool.
7. Gerar Missao 0001 apenas com contrato e DeltaP previsto.

## Onde Esta a Maquina

```text
60_Sistemas/PRIMUS_Digestor/
```

## Primeiro Uso Recomendado

Usar o SQLite ja existente do PRIMUS Index:

```powershell
python 60_Sistemas/PRIMUS_Digestor/scripts/06_import_primus_index.py `
  --db "C:\Users\user\Desktop\Projeto\primus-site\primus.sqlite" `
  --book phb `
  --query Juramento `
  --limit 5 `
  --out 60_Sistemas/PRIMUS_Digestor/data/catalog_entries_primus_index.jsonl
```

Depois:

```powershell
python 60_Sistemas/PRIMUS_Digestor/scripts/04_validate_entries.py `
  --input 60_Sistemas/PRIMUS_Digestor/data/catalog_entries_primus_index.jsonl

python 60_Sistemas/PRIMUS_Digestor/scripts/05_export_markdown.py `
  --input 60_Sistemas/PRIMUS_Digestor/data/catalog_entries_primus_index.jsonl `
  --out 30_Projetos/PRIMUS/Catalogo_Gerado
```

## Nao Fazer

- Nao exportar todos os livros de uma vez.
- Nao gerar milhares de Markdown sem validacao.
- Nao copiar texto integral.
- Nao promover entradas `Restricted` para material publico.
- Nao executar Missao 0001 antes de contrato.
