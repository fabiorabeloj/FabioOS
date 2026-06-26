---
tipo: documentação
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [claude-code, workstation, ferramentas, mcps, skills, plugins]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Workstation Claude Code — FabioOS

## Função

Visão geral completa da workstation do Claude Code no FabioOS: ferramentas-base, MCPs, plugins, skills e repositórios de referência instalados.

## Contexto

A workstation do Claude Code é o conjunto de ferramentas, extensões e configurações que ampliam as capacidades do Claude neste ambiente. Foi montada em sessões de setup em junho de 2026.

## Ferramentas-base instaladas

| Ferramenta | Função |
|------------|--------|
| Git | Controle de versão |
| GitHub CLI (`gh`) | Autenticado como `fabiorabeloj` |
| Node.js + npm | Runtime JS e gerenciador de pacotes |
| Python + uv | Runtime Python e gerenciador de ambientes |
| ripgrep | Busca ultrarrápida em arquivos |
| fd | Busca de arquivos (alternativa ao find) |
| jq | Processamento de JSON no terminal |
| Playwright CLI | Automação de browser para testes |

## MCPs configurados

Ver detalhes em [[60_Sistemas/MCP/Inventario_MCP]].

**Resumo:**
- `filesystem`, `context7`, `github`, `playwright-mcp` → global
- `obsidian`, `n8n-mcp`, `n8n-docs` → projeto FabioOS
- `plugin:claude-mem:mcp-search` → via plugin

## Plugins instalados

Ver detalhes em [[60_Sistemas/Skills/Inventario_Skills]].

| Plugin | Versão | Função-chave |
|--------|--------|--------------|
| claude-mem | 13.8.1 | Memória persistente entre sessões |
| superpowers | 6.0.3 | TDD, debugging, colaboração |
| ui-ux-pro-max | 2.6.2 | Design UI/UX com banco de dados de estilos |
| obsidian | 1.0.1 | Skills para Obsidian CLI e formatos |
| gsd-core | 1.6.0 | Meta-prompting e spec-driven development |

## Repositórios em `claude-extensions/`

| Repo | Tipo | Função |
|------|------|--------|
| `awesome-claude-skills` | Referência | Catálogo comunitário de skills |
| `awesome-claude-code` | Referência | Catálogo de recursos Claude Code |
| `superpowers` | Plugin | Base do plugin superpowers |
| `gsd-core` | Plugin (skills-dir) | Base do plugin gsd-core |
| `get-shit-done` | Arquivado | Substituído por gsd-core |
| `n8n-mcp` | MCP npm | Base do n8n-docs MCP |
| `ui-ux-pro-max-skill` | Plugin | Base do plugin ui-ux-pro-max |
| `claude-mem` | Plugin | Base do plugin claude-mem |
| `obsidian-skills` | Plugin | Base do plugin obsidian |
| `huashu-design` | Skill SKILL.md | Design HTML-native (invocação manual) |
| `taste-skill-B` | Skill SKILL.md | Design taste / extração de tokens visuais |
| `taste-skill-A` | Referência | Variante alternativa do Taste |
| `mcp-servers` | Referência | Implementações de referência MCP oficiais |
| `fastmcp` | Referência | Framework Python para criar MCPs |
| `tradingview-mcp` | Estudo | MCP de mercado financeiro (sem credenciais) |

## Locais de configuração

| Arquivo/Diretório | Conteúdo |
|-------------------|----------|
| `~/.claude/settings.json` | MCPs globais, plugins ativos, tema |
| `~/.claude.json` | MCPs de projeto, configurações por projeto |
| `~/.claude/skills/` | Skills-dir: gsd-core, huashu-design, taste-skill |
| `~/.claude/plugins/` | Cache e marketplaces de plugins |
| `C:\Users\user\claude-extensions\` | Todos os repos clonados |

## Relações

- [[60_Sistemas/MCP/Inventario_MCP]]
- [[60_Sistemas/Skills/Inventario_Skills]]
- [[60_Sistemas/n8n]]
- [[Atendimento_Pietra]]
- [[Trader]]

## Próximas ações
- [ ] Testar todos os MCPs em sessão ativa com `claude mcp list`
- [ ] Criar primeiro workflow n8n via MCP
- [ ] Usar Taste + Playwright MCP para analisar um site de referência
- [ ] Criar MCP customizado para FabioOS usando fastmcp como base
- [ ] Documentar uso dos nós mais importantes do n8n via n8n-docs
