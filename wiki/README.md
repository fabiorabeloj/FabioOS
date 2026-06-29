---
tipo: wiki
area: wiki
projeto: FabioOS
status: ativo
tags: [wiki, índice, llm-wiki]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Wiki — FabioOS

## Função

Páginas geradas, organizadas ou mantidas pela IA. Aqui ficam entidades, conceitos, sínteses, índices e páginas conectadas que formam o conhecimento estruturado do FabioOS.

## Status atual (Fase 5 — 2026-06-26)

10 páginas criadas a partir de 10 fontes em `sources/repositorios/`. Mapa navegável disponível em [[wiki/indices/mapa-fabios]].

| Pasta | Páginas | Status |
|---|---|---|
| `sistemas/` | 9 | gsd-core, claude-mem, superpowers, playwright-mcp, n8n-mcp, fastmcp, taste-skill, huashu-design, tradingview-mcp |
| `conceitos/` | 4+ | mcp, rag, banco-vetorial, governanca-operacional-fabios |
| `indices/` | 1 | mapa-fabios |
| `projetos/` | 0 | a criar |
| `entidades/` | 0 | a criar |

## Estrutura planejada

```
wiki/
  sistemas/        ← páginas sobre sistemas do FabioOS (n8n, Claude Code, Obsidian, etc.)
  projetos/        ← páginas síntese de projetos ativos
  conceitos/       ← conceitos técnicos e metodológicos
  entidades/       ← pessoas, ferramentas, serviços
  indices/         ← mapas e índices de navegação
```

## Como alimentar a wiki

1. Adicionar fontes brutas em `sources/`
2. Claude Code processa e gera páginas conectadas em `wiki/`
3. As páginas são linkadas e indexadas automaticamente

## LLM Wiki operacional

A partir de 2026-06-29, a wiki tambem segue:

- [[30_Projetos/FabioOS/LLM_Wiki_FabioOS]]
- [[60_Sistemas/Wiki/Schema_Wiki_FabioOS]]
- [[60_Sistemas/Wiki/Protocolo_Ingest_LLM_Wiki]]
- [[60_Sistemas/Wiki/Protocolo_Query_LLM_Wiki]]
- [[60_Sistemas/Wiki/Protocolo_Lint_LLM_Wiki]]
- [[60_Sistemas/FabioOS/Mapa_Canonico_Pastas_Obsidian_v2_2026-06-29]]
- [[60_Sistemas/FabioOS/Plano_Normalizacao_Pastas_Obsidian_2026-06-29]]
- [[60_Sistemas/Wiki/Estrutura_de_Pastas_LLM_Wiki_FabioOS]]
- [[50_Registros/Auditoria/Proposta_de_Migracao_Estrutural_FabioOS]]
- [[10_Dashboard/Mapa_Estrutural_FabioOS]]
- [[50_Registros/Decisoes/ADR_Estrutura_de_Pastas_LLM_Wiki_FabioOS]]
- [[index]]
- [[log]]

Regra: resposta de IA nao e entrega ate virar persistencia verificavel no sistema.

Compatibilidade: `40_Wiki/` e a camada-alvo de conhecimento processado. `wiki/` permanece preservada enquanto links, RAG, MCP e scripts sao migrados com seguranca.

## Relações

- [[schema/README]] — regras e convenções da LLM-Wiki
- [[sources/repositorios/]] — fontes que alimentam esta wiki
