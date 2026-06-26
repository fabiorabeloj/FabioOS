---
tipo: wiki
area: sistemas
projeto: FabioOS
status: pendente
camada: camada-1
tags: [cursor, desenvolvimento, ide, software, mcp, camada-1]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Cursor

## Função no FabioOS

[DECISÃO] O Cursor é a **oficina de desenvolvimento de software** do FabioOS — entra quando o projeto deixa de ser apenas vault e passa a exigir componentes de código: MCPs customizados, parsers, crawlers, dashboards, APIs locais e scripts robustos.

## O que essa ferramenta faz

[FATO] IDE com assistente de IA integrado (suporte a múltiplos modelos). Especializado em edição de código com contexto de projeto, refatoração guiada por IA, geração de testes e navegação por grandes codebases.

No FabioOS, o Cursor deve cumprir:

- Desenvolver o MCP customizado do FabioOS (Fase 15)
- Criar parsers para ingestão de PDFs, DOCX e Google Docs
- Construir crawlers para captura de páginas web
- Desenvolver dashboards e APIs locais
- Trabalhar em projetos de código maior que o escopo do Claude Code

Diferença entre Claude Code e Cursor:

```
Claude Code = operador do vault e repositório
Cursor      = oficina de desenvolvimento de software
```

[FATO] Status atual: **não integrado**. Mencionado no Plano Mestre como ferramenta futura para desenvolvimento de componentes de software do FabioOS.

## O que essa ferramenta não deve fazer

- Substituir o Claude Code na operação do vault e repositório
- Ser usado para editar notas Obsidian (Claude Code faz isso melhor)
- Manter o vault — apenas desenvolver componentes de software que o vault usa

## Relação com outras ferramentas

| Ferramenta | Relação |
|---|---|
| [[wiki/sistemas/claude-code]] | Claude Code opera o vault; Cursor desenvolve software que o suporta |
| [[wiki/sistemas/fastmcp]] | Cursor usará fastmcp para criar MCP customizado do FabioOS |
| [[wiki/sistemas/github]] | Código desenvolvido no Cursor é versionado no GitHub |
| [[wiki/sistemas/n8n]] | Componentes desenvolvidos no Cursor podem ser usados por n8n |

## Uso atual

- [ ] Nenhum — **pendente** (Fase 16.5)

## Uso futuro

- [ ] MCP customizado do FabioOS em Python com fastmcp
- [ ] Parser de PDFs para `sources/pdfs/`
- [ ] Crawler de páginas para `sources/web/`
- [ ] Dashboard do FabioOS (Fase 21)
- [ ] API local para integração com n8n e OpenClaw

## Riscos e cuidados

- **Escopo de código vs vault**: componentes de software desenvolvidos no Cursor devem ser versionados separadamente ou em subpastas de código bem delimitadas — não misturar com notas Markdown
- **Dependências**: projetos Python/Node criados no Cursor não devem ser commitados com `node_modules/`, `.venv/` ou outros diretórios de dependência — configurar `.gitignore` adequado
- **Segredos em código**: nunca hardcodar tokens ou chaves em código desenvolvido no Cursor

## Próximas ações

- [ ] Definir qual será o primeiro componente de software do FabioOS (candidato: MCP de busca no vault)
- [ ] Avaliar quando o FabioOS cruzará o limiar de complexidade que justifica usar o Cursor
- [ ] Preparar estrutura de projeto Python para o MCP customizado

## Links internos

- [[wiki/indices/mapa-fabios]]
- [[wiki/sistemas/claude-code]]
- [[wiki/sistemas/fastmcp]]
- [[wiki/sistemas/github]]
- [[wiki/sistemas/n8n]]
- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]
