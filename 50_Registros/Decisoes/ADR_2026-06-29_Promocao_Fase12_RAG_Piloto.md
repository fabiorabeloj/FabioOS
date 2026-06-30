---
tipo: adr
area: 50_Registros
projeto: FabioOS
status: aceito
autor: Claude (arquiteto-chefe)
fase: 12
criado_em: 2026-06-29
atualizado_em: 2026-06-29
tags: [adr, rag, fase-12, piloto, promocao, validacao]
---

# ADR 2026-06-29 — Promoção da Fase 12 (RAG) a piloto

## Contexto

A Fase 12 (RAG local: Chroma + bge-m3) foi reindexada após a limpeza visual do
Obsidian e revalidada por Cursor em modo recuperação (sem API externa, sem
`--generate`). O handoff atribuiu explicitamente a **Claude (arquiteto-chefe)** a
decisão de promover ou não a fase a piloto. Esta ADR registra essa decisão.

## Evidência revisada

- **Índice real consultado:** `60_Sistemas/RAG/fabioos_db/`, coleção `fabioos`,
  **1206 chunks** (verificado diretamente nesta sessão).
- **Evidência bruta:** `60_Sistemas/RAG/validacao_pos_ranking_2026-06-29.json`,
  gerada em `2026-06-29T18:51Z`, top-k=5, modo recuperação.
- **Aceitação:** 10/10 `bom`, 0 `parcial`, 0 `fraco`.
- **Segurança:** 5/5 consultas adversariais `ok`, **0 vazamentos** (nenhuma
  credencial, log Pietra ou conteúdo de `_inbox`/`.codex` recuperado).
- **Ranking operacional:** "Qual é a fase atual?" recupera Painel_Pendencias +
  STATUS no top-3 (corrigia a regressão de ranking de 27/06).

### Discrepância resolvida
O relatório de Cursor (`Relatorio_Validacao_RAG_2026-06-29_Cursor.md`) cita "1795
chunks" na tabela de critérios — número **legado** da restauração de 27/06. A
validação real rodou contra o índice atual de **1206 chunks**. A citação é
cosmética; não invalida a evidência. **Ação:** corrigir a tabela do relatório.

## Decisão

**Fase 12 RAG é promovida a piloto.** O RAG passa a ser consultável como camada
de recuperação confiável para os demais agentes/MEGATRON, em **modo recuperação**
(retorna trechos + fontes, não gera resposta sintética por padrão).

### Limites do piloto
- Read-only sobre o vault; nenhuma geração com API externa sem autorização.
- Reindex **apenas com lock** em `Registro_Frentes_Ativas.md`.
- Exclusões de segurança permanecem obrigatórias (`_inbox`, `PIETRA*LOG`,
  `.codex`, `.obsidian`, `Descartes_Visuais`, venv).

## Hardening diferido para Fase 12.1 (não bloqueia o piloto)

Itens de D4 da ADR de auditoria, intencionalmente **fora** do critério de piloto
porque a validação em modo recuperação já passou 10/10:

1. **`MAX_CHARS`** — hoje 6000; avaliar ~1000–1500 + overlap para precisão de
   recuperação. Requer reindex com lock + nova rodada de golden questions.
2. **Golden questions versionadas** — parcialmente fechado: o batch reproduzível
   `60_Sistemas/RAG/scripts/batch_validate_rag.py` + a evidência JSON já servem
   como conjunto versionado. Falta documentar como "ficha técnica" canônica.
3. **Política de reindex** — formalizar gatilho (novos docs canônicos) + lock.

## Consequências

- Outros agentes podem confiar no RAG como recuperação de alto sinal.
- Hardening de precisão (chunk menor) fica como melhoria incremental, não como
  bloqueio — evita travar o piloto por otimização prematura.
- Promoção não implica push nem automação externa (continuam Fabio-gated).

## Relações
- [[60_Sistemas/RAG/Relatorio_Validacao_RAG_2026-06-29_Cursor]]
- [[60_Sistemas/RAG/validacao_pos_ranking_2026-06-29]]
- [[50_Registros/Decisoes/ADR_2026-06-29_Auditoria_Arquitetura_Claude]]
- [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]]
- [[60_Sistemas/FabioOS/STATUS]]
