---
tipo: plano
area: 50_Registros
projeto: FabioOS
status: ativo
agente: Cursor
classe_dado: interno
criado_em: 2026-07-01
tags: [fabios, bugbot, cursor, auditoria, revisao]
---

# Plano Bugbot — Revisao do Projeto FabioOS (Cursor)

## Funcao

Definir como o Cursor audita o repositorio inteiro **como bugbot** — nao como frontend, nao como arquiteto, nao como governanca documental.

## Principios

1. **Evidencia antes de patch** — rodar, reproduzir, registrar.
2. **Patch minimo** — so conserta o que quebra com prova; resto vira handoff.
3. **Respeitar zonas** — nao tocar MEGATRON core, RAG db, MCP runtime, push sem OK.
4. **Severidade** — critico (segredo/vazamento) > alto (fluxo morto) > medio (inconsistencia) > baixo (UX).
5. **Entrega** — relatorio em `50_Registros/Relatorios/` + itens no barramento se bloquear outro agente.

## Escopo da revisao (7 ondas)

### Onda 1 — Entradas sensoriais (prioridade maxima)

| Alvo | O que verificar | Dono do fix se nao for bug local |
|------|-----------------|----------------------------------|
| `email_intake_dry_run.py` | payload, classificacao, saida restrita | Codex (pipeline Gmail) |
| `intake_flow.py` / `megatron_core.py` | redacao segredos, fila JSON | Claude (contrato) |
| `watch_pdf_drop.py` | drop → evento JSON | Codex |
| `pietra_inbox.py` / `pietra_state.py` | state gerado, bloqueios | Claude |
| n8n workflows (`60_Sistemas/n8n/Workflows/`) | webhooks, PII flags, Gmail ausente | Codex |
| Agentarium WhatsApp intake | draft_only, allowlist | Cursor so se bug na zona apps/ |

**Criterio de done:** cada canal tem teste minimo documentado e resultado pass/fail.

### Onda 2 — Seguranca e segredos

| Alvo | Verificacao |
|------|-------------|
| `.gitignore` vs pastas `_restrito/` | nada sensivel versionado |
| Scan staged (`check-secrets` / grep padroes) | tokens, sk-, bearer |
| Logs (`50_Registros/Logs_Agentes/`, changelogs) | remetentes/snippets reais |
| Env vars referenciadas vs expostas | inventario sem valores |
| `intake_flow` / email triagem | snippet omitido, remetente mascarado |

**Ferramenta:** `/review-security` ou bugbot em diff recente.

### Onda 3 — Contratos e duplicacao cognitiva

Problema conhecido: **dois classificadores** (FabioOS script vs MEGATRON core) com taxonomias diferentes.

| Acao bugbot |
|-------------|
| Matriz diff: dominio, sensibilidade, urgencia, acao sugerida |
| Listar payloads que classificam diferente |
| Handoff unico para Codex alinhar `universal_intake_schema` |

### Onda 4 — Scripts operacionais FabioOS

Rodar smoke em:

- `dashboard_fabioos.py`
- `classificar_dado_fabioos.py`
- `mobile_gateway_fabioos.py` (porta 8787)
- `gerar_spec_fabioos.py`
- `start_fabioos.ps1` / `start_agentarium.ps1`

Registrar: exit code, dependencias ausentes, paths quebrados pos-migracao Obsidian.

### Onda 5 — RAG e MCP (read-only)

| Acao | Limite |
|------|--------|
| `query_rag.py` 3 perguntas golden | nao reindexar |
| `batch_validate_rag.py` se existir | comparar com ultimo relatorio Cursor |
| MCP `server.py` import/start | nao alterar db |

Bugbot reporta regressao; **nao promove fase**.

### Onda 6 — Agentarium (apps/agentarium)

Revisao de **bugs**, nao features:

- build backend (`tsc`) + frontend (`vite build`)
- endpoints Maestro/PDF/Pietra sync paths corretos pos-migracao
- WebSocket reconnect
- env vars documentadas vs runtime

Usar bugbot em diff `apps/agentarium/**` vs main.

### Onda 7 — Coerencia documental vs runtime

| Check | Metodo |
|-------|--------|
| STATUS/NEXT_ACTIONS vs frentes concluidas | diff manual |
| SPEC marcada implementada vs codigo existe | grep + run |
| Agentes `planned` vs codigo | fabioAgents.ts vs scripts |
| README Agentarium versao vs package real | versao declarada |

Nao reescrever docs — **listar divergencias** para Codex/Claude.

## Ordem de execucao recomendada

```text
Semana A (Fabio pede "bugbot email+intake")
  → Onda 1 (entradas) + Onda 2 (seguranca intake)

Semana B
  → Onda 3 (contratos) + Onda 4 (scripts)

Semana C
  → Onda 5 (RAG read-only) + Onda 6 (Agentarium build)

Semana D
  → Onda 7 (doc vs runtime) + relatorio consolidado
```

## Entregaveis por onda

1. `50_Registros/Relatorios/Bugbot_OndaN_YYYY-MM-DD_Cursor.md`
2. Tabela severidade | arquivo | achado | patch? | dono
3. Testes minimos copy-paste
4. Entrada no barramento se bloquear Codex/Claude

## Relatorio consolidado final

Arquivo alvo: `50_Registros/Relatorios/Bugbot_Auditoria_Completa_FabioOS_YYYY-MM-DD_Cursor.md`

Secoes:

- Resumo executivo (5 linhas)
- Top 10 achados por severidade
- Fluxos mortos (email, n8n Gmail, etc.)
- Duplicacoes perigosas
- Patches aplicados pelo Cursor
- Backlog handoff por agente (Claude / Codex / Fabio)
- Checklist reteste

## O que Cursor NAO faz nesta revisao

- Reindex RAG / editar `fabioos_db`
- OAuth / credenciais / push
- Migracao vault / wikilinks em massa
- Decisoes de arquitetura ou promocao de fase
- Construir frontend novo (so bugfix em apps existentes)

## Proxima acao imediata

Fabio autoriza: **executar Onda 1 completa** (intake sensorial) na proxima sessao Cursor.
