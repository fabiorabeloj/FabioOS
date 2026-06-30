---
tipo: changelog
area: 50_Registros
projeto: FabioOS
status: registrado
fase: 18.2
classe_dado: interno
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [fabios, pdf, codex, watcher, n8n, drop-folder]
---

# 2026-06-30 - Pipeline Drop PDF Codex v0

## Contexto

Claude orientou a frente pela SPEC:

```text
60_Sistemas/FabioOS/specs/2026-06-30_pipeline-pdf-aprende.md
```

## Entrega

Codex implementou a porta de entrada do pipeline:

- `00_Inbox/pdfs/` como drop folder oficial;
- `00_Inbox/pdfs/_events/` como fila visivel no Obsidian;
- `60_Sistemas/FabioOS/scripts/watch_pdf_drop.py` para detectar PDFs novos;
- `60_Sistemas/n8n/Workflows/FabioOS_DropPDF_Aprende.json` como workflow importavel;
- `60_Sistemas/FabioOS/Pipeline_DropPDF_Codex_v0.md` como relatorio operacional.

## Limites Preservados

- sem OCR;
- sem RAG reindex;
- sem API externa;
- sem alterar `documentalista.py`;
- sem tocar em credenciais do Stirling.

## Resultado

O FabioOS agora tem uma porta operacional:

```text
PDF em 00_Inbox/pdfs -> evento auditavel -> Claude/documentalista
```
