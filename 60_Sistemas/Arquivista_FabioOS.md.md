---
type: sistema
area: FabioOS
source: ChatGPT
status: ativo
tags: [fabioos, arquivista, n8n, openrouter, obsidian, github]
created: 2026-06-23
---

# Arquivista FabioOS

## Função

Classificar conteúdo bruto e transformá-lo em nota Markdown para Obsidian.

## Entrada

Textos vindos de ChatGPT, Claude, Hermes Agent, OpenClaw, WhatsApp, e-mail, PDF, áudio ou formulário.

## Saída

JSON estruturado com:

- title
- folder
- filename
- type
- area
- tags
- markdown

## Fluxo

```text
Entrada → n8n → OpenRouter → Code → GitHub → Obsidian