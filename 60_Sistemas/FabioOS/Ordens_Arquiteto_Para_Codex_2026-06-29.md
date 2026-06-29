---
tipo: ordens-coordenacao
area: 60_Sistemas
projeto: FabioOS
status: ativo
de: Claude (arquiteto-chefe)
para: Codex
criado_em: 2026-06-29
atualizado_em: 2026-06-29
tags: [fabios, multiagente, ordens, coordenacao, arquitetura, anti-colisao]
---

# Ordens do Arquiteto-Chefe para o Codex — 2026-06-29

## Contexto

Claude reassumiu a **liderança técnica/arquitetural**. Foi feita auditoria de arquitetura (plano em `50_Registros/` / conversa). O Codex já adiantou MUITO e **alinhado** ao plano — abaixo, o reconhecimento, a divisão de zonas (anti-colisão) e as ordens.

## Trabalho do Codex que JÁ resolveu itens do plano (não refazer)

- ✅ **Migração estrutural:** `wiki/`→`40_Wiki/_compat_wiki/`, `sources/`→`05_Raw_Sources/_compat_sources/`; estrutura canônica v2 aplicada. (resolve "fonte-de-verdade ambígua")
- ✅ **Mapa canônico v2** + Plano Mestre apontando para o v2.
- ✅ Camada de **Governança** iniciada (`60_Sistemas/Governanca/`, `Protocolos/`, `Wiki/schema/`).
- ✅ RAG reindexado pós-limpeza (1206 chunks) e validado 10/10.

## Divisão de zonas (regra anti-colisão)

| Zona | Dono | Observação |
|---|---|---|
| `60_Sistemas/MEGATRON/` (v0, v1, agentes), `60_Sistemas/MCP_FabioOS/` | **Claude** | NÃO editar sem handoff |
| `60_Sistemas/RAG/fabioos_db`, scripts RAG, política de chunk/reindex | **Claude** | NÃO reindexar/editar scripts sem lock + handoff |
| Estrutura do vault, migração, links, governança documental, roadmap, Obsidian | **Codex** | zona principal do Codex |
| Runtime (n8n, OpenClaw, WhatsApp, Google) | **bloqueado** | só com aprovação humana |

## ORDENS ao Codex (na sua zona, sem runtime, sem push)

1. **Corrigir links pós-migração (P1).** Varrer o vault por wikilinks `[[wiki/...]]` e `[[sources/...]]` e atualizar para `[[40_Wiki/_compat_wiki/...]]` / `[[05_Raw_Sources/_compat_sources/...]]`. Fazer em **lotes pequenos**, com changelog e contagem de links corrigidos. Não quebrar âncoras.
2. **Consolidar a governança numa hierarquia única (P2).** Produzir **1 índice de governança** (`60_Sistemas/Governanca/INDEX.md`) que organize: Constituição (Modelo Formal) → protocolos operacionais. **Marcar como `superado`** os protocolos redundantes/sobrepostos em vez de criar novos. Meta: parar o *sprawl*, não aumentá-lo.
3. **Reconciliar roadmaps.** Finalizar: Roadmap v2 = autoritativo; Plano Mestre v1 = histórico. Atualizar a leitura obrigatória do `CLAUDE.md` e o Painel de Pendências para refletir isso.
4. **Auditoria de links/órfãos read-only** do vault inteiro pós-reorg: relatório de links quebrados restantes (não corrigir os fora da sua zona; listar).
5. **NÃO tocar** em: `MEGATRON/`, `MCP_FabioOS/`, `fabioos_db`, scripts RAG. Se algo dessas zonas precisar mudar, **registrar pedido de handoff** no `Registro_Frentes_Ativas.md` e aguardar o Claude.
6. **RAG hardening = zona do Claude.** Você pode preparar, como **documento** (sem tocar o db/scripts), uma proposta de "golden questions por domínio" para o Claude revisar. Decisão de chunk-size e de parar de indexar o Legado é do Claude.
7. **Sem push e sem runtime.** Push para `origin/main`/PR e ativação de n8n/OpenClaw/WhatsApp/Google **dependem de aprovação humana**. Você pode preparar proposta de baseline Git, não executá-la.
8. **Protocolo:** registrar lock no `Registro_Frentes_Ativas.md` antes de qualquer artefato compartilhado; scan de segredos antes de commit; changelog em cada entrega.

## O que o Claude (arquiteto-chefe) fará em paralelo

- RAG hardening (chunk-size, parar de indexar Legado, ficha técnica, golden questions versionadas).
- MEGATRON (v1 canônico, v0 rollback) + caminho para coordenador real.
- MCP FabioOS (reteste nativo, manter read-only).
- Decisões de arquitetura + ADRs.

## Regras invioláveis (ambos)
- Não apagar conhecimento; preservar histórico.
- Não colidir: respeitar zonas + locks.
- Sem push/runtime sem aprovação humana.
- Registrar toda decisão relevante (changelog/ADR).

## Próxima sincronização
Ao concluir os itens 1–4, o Codex atualiza `STATUS.md`/`NEXT_ACTIONS.md` + changelog e aguarda revisão do Claude antes de qualquer push.
