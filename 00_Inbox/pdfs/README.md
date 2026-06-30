---
tipo: inbox
area: 00_Inbox
projeto: FabioOS
status: ativo
fase: 18.2
classe_dado: entrada-nao-classificada
permissao: drop-folder
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [fabios, pdf, inbox, drop-folder, codex, documentalista]
---

# Drop Folder de PDFs

Esta pasta e a porta de entrada local do pipeline:

```text
PDF novo -> watcher Codex -> evento -> Claude/documentalista -> Arquivista -> curadoria -> RAG com lock
```

## Como Usar

1. Coloque aqui um PDF.
2. Rode o watcher:

```powershell
python 60_Sistemas/FabioOS/scripts/watch_pdf_drop.py --once
```

3. O watcher cria um evento em `_events/` e registra a fila em:

```text
60_Sistemas/FabioOS/logs/pdf_drop_events.jsonl
```

## Regra

- Esta pasta recebe PDFs ainda nao classificados.
- O watcher nao executa OCR e nao reindexa RAG.
- O evento entrega ao Claude apenas o caminho do arquivo e metadados.
- PDFs sensiveis exigem classificacao e curadoria humana antes de qualquer aprendizado.

## Bloqueio Atual

O Stirling PDF esta no lado do documentalista/Claude. Enquanto o Stirling exigir autenticacao, a porta de entrada apenas registra o gatilho.
