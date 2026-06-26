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

## Status atual

A wiki está sendo inicializada. O conteúdo virá da camada `sources/` à medida que o conhecimento for sendo processado e organizado.

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

## Relações

- [[schema/README]] — regras e convenções da LLM-Wiki
- [[sources/repositorios/]] — fontes que alimentam esta wiki
