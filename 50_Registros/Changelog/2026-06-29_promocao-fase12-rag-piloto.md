---
tipo: changelog
area: 50_Registros
projeto: FabioOS
status: concluído
agente: Claude (arquiteto-chefe)
tags: [changelog, sessão, rag, fase-12, piloto, promocao]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Changelog — Promoção da Fase 12 RAG a piloto

## O que foi feito

Claude retomou o contexto a partir do último changelog (validação RAG pós-ranking
do Cursor) e exerceu a decisão que o handoff atribuiu ao arquiteto-chefe:
**promover ou não a Fase 12 RAG a piloto**.

- Revisada a evidência bruta `60_Sistemas/RAG/validacao_pos_ranking_2026-06-29.json`
  (gerada 2026-06-29T18:51Z, top-k=5, modo recuperação): **10/10 bom**, 0 parcial,
  0 fraco; **5/5 segurança ok**, 0 vazamentos.
- Verificado diretamente o índice real: coleção `fabioos` com **1206 chunks**.
- Resolvida a discrepância do relatório do Cursor (cita "1795 chunks" — número
  legado da restauração de 27/06; a validação real rodou contra 1206).
- **Decisão: Fase 12 RAG promovida a piloto** (modo recuperação, read-only).
- Hardening de precisão (`MAX_CHARS`, ficha técnica, política de reindex) avaliado
  e **diferido para Fase 12.1** — não bloqueia o piloto, pois a validação em modo
  recuperação já passou 10/10.

## Instalado/configurado

- Nada instalado. Nenhuma API externa chamada. Nenhum reindex do `fabioos_db`.

## Criado/modificado no vault

Criado:
- `50_Registros/Decisoes/ADR_2026-06-29_Promocao_Fase12_RAG_Piloto.md` — ADR da decisão.
- `50_Registros/Changelog/2026-06-29_promocao-fase12-rag-piloto.md` — este changelog.

Modificado:
- `60_Sistemas/FabioOS/Registro_Frentes_Ativas.md` — frente `PROMOCAO_FASE12_PILOTO`
  (Claude) registrada como concluída + entrada no histórico.
- `60_Sistemas/FabioOS/STATUS.md` — seção Fase 12 atualizada para "PROMOVIDA A PILOTO".
- `60_Sistemas/FabioOS/NEXT_ACTIONS.md` — item de decisão marcado `[x]`; bloco
  "Fase 12.1 - hardening RAG" adicionado.

## Commits realizados

Nenhum. Por protocolo, commit + push permanecem Fabio-gated (exigem scan de segredos).

## Pendente

- **Autorização do Fabio** para commitar o working tree (scan de segredos antes).
  Árvore inclui também trabalho não commitado de outras frentes (Cursor: `.cursor/`,
  validação RAG; encoding audit; OpenClaw `ponte/`). Cada frente é de seu dono.
- **Fase 12.1 (zona Claude):** `MAX_CHARS` 6000→~1000–1500 + reindex com lock;
  ficha técnica canônica; política de reindex.
- **Handoff Cursor:** corrigir citação "1795"→"1206" no relatório de validação.

## Próximas ações

1. Fabio autoriza commit (após scan) ou orienta o que entra no commit temático.
2. Claude executa Fase 12.1 (hardening RAG) quando priorizado.
3. Roadmap v2: próxima frente técnica é a evolução do MEGATRON v1 (CLI → coordenador).
