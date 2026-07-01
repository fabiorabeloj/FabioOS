---
tipo: handoff
area: 60_Sistemas
projeto: FabioOS
status: ativo
autor: Cursor (Interface / Agentarium)
destinatario: Claude (Maestro)
criado_em: 2026-06-30
tags: [fabios, cursor, agentarium, pdf-pipeline, barramento, interface]
---

# Handoff Cursor → Claude — PDF Pipeline (Interface)

> **Relay para o barramento** (Fabio cola ou Maestro registra):

```text
de: cursor
para: claude
tipo: handoff
status: aberto
mensagem: |
  ACK da SPEC pipeline-pdf-aprende. Concordo com a divisao Codex (porta) / Claude (cognicao) / Fabio (Stirling auth).
  Minha parte (zona Interface) ENTREGUE no Agentarium v0.7.2:
  - Aba "PDF Pipeline" espelha 00_Inbox/pdfs/_events/*.json + contagem de PDFs pendentes
  - Probe Stirling :8081 (online / auth_required / offline) — mostra bloqueio 401 honestamente
  - Watcher reativo em _events/ e drop folder; WebSocket pdf_pipeline_snapshot + GET /integrations/pdf-pipeline/status
  - NAO toquei megatron.py, registry.py, barramento.py, reasoningbank.py, maestro_state.py, documentalista, RAG
  Quando documentalista processar um PDF, peço: atualizar safety.ocr_executed no evento JSON ou escrever status em _events/ para o painel avancar de DETECTADO -> OCR OK -> INDEXADO.
  Stirling auth continua bloqueio #1 — aguardo Fabio. Reindex RAG: nao testo da minha zona; aviso quando validar 10/10.
```

## O que foi feito (Cursor)

| Item | Detalhe |
|------|---------|
| Painel | Aba **PDF Pipeline** no Agentarium |
| Fonte | `00_Inbox/pdfs/_events/*.json` (zona Codex) |
| Stirling | Probe HTTP local — exibe AUTH 401 sem mentir |
| Tempo real | File watcher + WebSocket |
| API | `GET /integrations/pdf-pipeline/status` |

## Pedido ao Maestro

1. Quando OCR rodar, marcar `safety.ocr_executed: true` no evento (ou convenção equivalente).
2. Após curadoria + reindex, marcar `safety.rag_reindexed: true`.
3. O painel já interpreta esses flags para stages visuais.

## Relações

- [[60_Sistemas/FabioOS/specs/2026-06-30_pipeline-pdf-aprende]]
- [[60_Sistemas/FabioOS/Pipeline_DropPDF_Codex_v0]]
- [[60_Sistemas/FabioOS/Orquestracao_Cursor_2026-06-29]]
