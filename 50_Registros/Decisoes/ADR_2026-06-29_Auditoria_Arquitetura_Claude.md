---
tipo: adr
area: 50_Registros
projeto: FabioOS
status: aceito
autor: Claude (arquiteto-chefe)
criado_em: 2026-06-29
atualizado_em: 2026-06-29
tags: [adr, arquitetura, auditoria, multiagente, rag, governanca, estrutura]
---

# ADR 2026-06-29 — Auditoria de Arquitetura e Plano de Consolidação

## Contexto

Claude reassumiu a liderança técnica/arquitetural do FabioOS. Foi conduzida uma auditoria (4 subagentes paralelos falharam por limite de uso; consolidação feita pelo arquiteto a partir da revisão acumulada da sessão). O sistema cresceu com 3 agentes (Claude/Codex/Cursor) e passou por reorganização estrutural.

## Decisões

### D1 — Fonte de verdade estrutural única (canônica v2)
Estrutura canônica governa novos arquivos. Conteúdo legado migrado para camadas de compatibilidade: `40_Wiki/_compat_wiki/`, `05_Raw_Sources/_compat_sources/`. **Status: executado pelo Codex** (`wiki/` e `sources/` migrados). Pendente: corrigir wikilinks em massa (ordem ao Codex).

### D2 — Governança consolidada, não multiplicada
Hierarquia única: **Constituição (Modelo Formal `00_Arquitetura/01...`) → protocolos operacionais**. Protocolos redundantes devem ser marcados `superado`, não recriados. Criar `60_Sistemas/Governanca/INDEX.md` como índice único. (ordem ao Codex)

### D3 — Roadmap v2 é autoritativo
`Roadmap_Fases_FabioOS_v2_2026-06-29` substitui o Plano Mestre v1 (que vira histórico). Atualizar leitura obrigatória do `CLAUDE.md`. Ordem v2: Governança → MEGATRON v1 → hardening RAG/Grafo/MCP → Google dry-run → Observabilidade → n8n/OpenClaw → domínios.

### D4 — RAG é zona do Claude; hardening pendente
Manter Chroma + bge-m3 local. **Decisões pendentes (Claude):** (a) revisar `MAX_CHARS` (hoje 6000 — provavelmente grande demais para precisão; avaliar ~1000–1500 + overlap); (b) **parar de indexar `90_Arquivo/Legado` como ativo** (contraditório — indexar só o vivo); (c) ficha técnica + golden questions **versionadas**; (d) política de reindex com lock. Reindex só com lock no `Registro_Frentes_Ativas`.

### D5 — MEGATRON v1 canônico
v1 (`60_Sistemas/MEGATRON/v1`) é canônico; v0 é rollback explícito. Golden questions devem ser versionadas (hoje em scratchpad). Evoluir de CLI para coordenador real (sistema nervoso).

### D6 — Disciplina Git e multiagente
`origin/main` sem baseline; 72 commits locais num só branch. **Pendente (aprovação humana):** estabelecer baseline em `main` (merge revisado do PR #1) e adotar **branch-por-agente** para reduzir colisão. Locks manuais já falharam 1× (incidente RAG) — manter `Registro_Frentes_Ativas` + zonas.

### D7 — Divisão de zonas (anti-colisão)
- **Codex:** estrutura, migração, links, governança documental, roadmap, Obsidian.
- **Claude:** RAG, MCP, MEGATRON, arquitetura cognitiva, ADRs.
- **Bloqueado (aprovação humana):** push, n8n, OpenClaw, WhatsApp, Google.

## Consequências
- Evita duplicação e colisão entre agentes; preserva conhecimento (nada apagado).
- Mantém ambição (organismo único) com fundação institucional antes de escala/automação.
- Ações de runtime e push permanecem sob controle humano.

## Relações
- [[60_Sistemas/FabioOS/Roadmap_Fases_FabioOS_v2_2026-06-29]]
- [[60_Sistemas/FabioOS/Ordens_Arquiteto_Para_Codex_2026-06-29]]
- [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]]
- [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]]
