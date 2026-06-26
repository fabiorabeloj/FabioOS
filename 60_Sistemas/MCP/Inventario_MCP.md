---
tipo: inventário
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [mcp, model-context-protocol, claude-code, workstation]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Inventário de MCPs — FabioOS

## Função

Registro centralizado de todos os servidores MCP configurados no Claude Code do FabioOS, com status de conexão e propósito.

## Contexto

MCP (Model Context Protocol) conecta o Claude Code a ferramentas externas, dados e serviços. Cada servidor MCP expõe ferramentas e recursos que o Claude pode usar durante uma sessão.

## MCPs operacionais

### Configuração global (`~/.claude/settings.json`)

| MCP | Tipo | Função | Status |
|-----|------|--------|--------|
| `filesystem` | stdio (npx) | Acesso a arquivos do vault e sistema de arquivos | ✅ configurado |
| `context7` | stdio (npx) | Documentação de bibliotecas em tempo real | ✅ configurado |
| `github` | stdio (npx) | Acesso à API do GitHub (repos, PRs, issues) | ✅ configurado |
| `playwright-mcp` | stdio (npx) | Controle de browser em tempo real pelo Claude | ✅ configurado |

### Configuração de projeto (`.claude.json` — projeto FabioOS)

| MCP | Tipo | Endpoint | Função | Status |
|-----|------|----------|--------|--------|
| `obsidian` | HTTP | `https://127.0.0.1:27124/mcp/` | Leitura/escrita no vault Obsidian via REST API | ✅ Connected (SSL self-signed) |
| `n8n-mcp` | HTTP | `http://localhost:5678/mcp-server/http` | Execução de workflows n8n | ✅ Connected |
| `n8n-docs` | stdio | `n8n-mcp` (global npm) | Documentação dos nós n8n para construção de workflows | ✅ Connected |

### MCPs via plugins

| MCP | Plugin | Função | Status |
|-----|--------|--------|--------|
| `plugin:claude-mem:mcp-search` | claude-mem | Busca na memória persistente | ✅ Connected |

## Referência — MCP Registry

O registro oficial de MCPs disponíveis está em: `https://registry.modelcontextprotocol.io`

Não requer instalação local — consultar diretamente como API ou via browser para descobrir novos servidores.

## Repos de referência MCP clonados

| Repo | Caminho | Função |
|------|---------|--------|
| `modelcontextprotocol/servers` | `claude-extensions/mcp-servers` | Implementações de referência oficiais (Filesystem, Git, Memory, etc.) |
| `PrefectHQ/fastmcp` | `claude-extensions/fastmcp` | Framework Python para criar servidores MCP customizados |
| `tradingview-mcp` | `claude-extensions/tradingview-mcp` | MCP de dados de mercado (estudo; sem credenciais configuradas) |

## Nota de segurança

- `obsidian`: token Bearer em `.claude.json` (não commitado no vault)
- `n8n-mcp`: JWT em `.claude.json` (não commitado no vault)
- `github`: GITHUB_TOKEN em `settings.json` local (não versionado)
- `tradingview-mcp`: **sem credenciais configuradas** — apenas clonado para estudo

## Relações

- [[60_Sistemas/Skills/Inventario_Skills]] — Taste skill requer playwright-mcp
- [[60_Sistemas/Claude_Code/Workstation_FabioOS]] — visão geral da workstation
- [[60_Sistemas/n8n]] — workflows conectados via n8n-mcp

## Próximas ações
- [ ] Testar playwright-mcp em sessão ativa (`claude mcp list`)
- [ ] Criar primeiro MCP customizado usando fastmcp como referência
- [ ] Avaliar tradingview-mcp para uso futuro no sistema Trader
- [ ] Documentar os nós n8n mais usados via n8n-docs
