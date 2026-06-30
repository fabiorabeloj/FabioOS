---
tipo: relatorio-operacional
area: 60_Sistemas
projeto: FabioOS
status: operacional-v0
fase: 18.2
classe_dado: interno
permissao: execucao-local
fonte: [[60_Sistemas/FabioOS/specs/2026-06-30_pipeline-pdf-aprende]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [fabios, pdf, codex, n8n, drop-folder, watcher]
---

# Pipeline Drop PDF - Porta de Entrada Codex v0

## Missao

Entregar ao Claude/documentalista o gatilho seguro:

```text
PDF novo -> caminho do arquivo + metadados + evento auditavel
```

## O Que Foi Implementado

- Drop folder oficial: `00_Inbox/pdfs/`.
- Pasta de eventos: `00_Inbox/pdfs/_events/`.
- Watcher local: `60_Sistemas/FabioOS/scripts/watch_pdf_drop.py`.
- Workflow n8n importavel: `60_Sistemas/n8n/Workflows/FabioOS_DropPDF_Aprende.json`.
- Log JSONL local: `60_Sistemas/FabioOS/logs/pdf_drop_events.jsonl`.

## Limites

- Nao faz OCR.
- Nao copia conteudo do PDF.
- Nao chama API externa.
- Nao reindexa RAG.
- Nao altera `documentalista.py`.

## Como Rodar

```powershell
python 60_Sistemas/FabioOS/scripts/watch_pdf_drop.py --once
```

Para monitor continuo:

```powershell
python 60_Sistemas/FabioOS/scripts/watch_pdf_drop.py
```

## Contrato com Claude

Cada PDF detectado gera um Markdown em `00_Inbox/pdfs/_events/` com comando sugerido:

```powershell
python 60_Sistemas/MEGATRON/agentes/implementacao/claude/documentalista.py info --pdf "<caminho>"
```

O Claude decide o proximo passo quando o Stirling estiver autenticado.

## Estado Atual

Operacional como gatilho. OCR real segue bloqueado pela autenticacao do Stirling, conforme a SPEC do Claude.
