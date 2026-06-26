---
tipo: changelog
area: 50_Registros
projeto: FabioOS
status: concluído
tags: [changelog, workstation, setup, claude-code, mcps, skills]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Changelog — Workstation Claude Code (2026-06-26)

## O que foi feito

Configuração completa da workstation do Claude Code para o FabioOS em duas sessões de trabalho.

## Instalado

### Ferramentas-base
- Git, GitHub CLI (autenticado como `fabiorabeloj`), Node.js, npm, Python, uv, ripgrep, fd, jq, Playwright CLI

### MCPs configurados
- `filesystem` — acesso ao vault e sistema de arquivos
- `context7` — documentação de libs em tempo real
- `github` — API GitHub
- `obsidian` — vault Obsidian via REST API (porta 27124)
- `n8n-mcp` — execução de workflows n8n (porta 5678)
- `n8n-docs` — documentação dos nós n8n (czlonkowski, npm global)
- `playwright-mcp` — controle de browser em tempo real

### Plugins instalados
- `claude-mem@thedotmack` v13.8.1 — memória persistente
- `superpowers@superpowers-dev` v6.0.3 — skills fundamentais
- `ui-ux-pro-max@ui-ux-pro-max-skill` v2.6.2 — design UI/UX
- `obsidian@obsidian-skills` v1.0.1 — skills Obsidian
- `gsd-core@skills-dir` v1.6.0 — meta-prompting e spec-driven dev

### Skills SKILL.md (invocação manual)
- `taste` (senlindesign) — extração de design taste de sites; requer Playwright MCP
- `huashu-design` (alchaincyf) — protótipos HTML de alta fidelidade

## Clonado como referência

| Repo | Local | Função |
|------|-------|--------|
| `modelcontextprotocol/servers` | `claude-extensions/mcp-servers` | Referência de implementações MCP |
| `PrefectHQ/fastmcp` | `claude-extensions/fastmcp` | Framework Python para criar MCPs |
| `leonxlnx/taste-skill` | `claude-extensions/taste-skill-A` | Variante alternativa do Taste |
| `atilaahmettaner/tradingview-mcp` | `claude-extensions/tradingview-mcp` | MCP financeiro (sem credenciais) |

## Rejeitado / Não instalado

| Item | Motivo |
|------|--------|
| `modelcontextprotocol/registry` | Serviço externo (API em registry.modelcontextprotocol.io) — não requer clone local |

## Já disponível (via gsd-core)

| Item | Como acessar |
|------|--------------|
| Graphify | CLI: `gsd graphify` dentro do gsd-core |
| Impeccable | Capability no sistema de capacidades do gsd-core |

## Vault atualizado

- `60_Sistemas/Claude_Code/Workstation_FabioOS.md` — visão geral da workstation
- `60_Sistemas/MCP/Inventario_MCP.md` — inventário de MCPs
- `60_Sistemas/Skills/Inventario_Skills.md` — inventário de skills e plugins
- `50_Registros/Changelog/2026-06-26_workstation-setup.md` — este arquivo

## Pendente / Próximas ações

- [ ] Testar Taste com Playwright MCP em site real
- [ ] Criar primeiro MCP customizado com fastmcp
- [ ] Configurar credenciais do tradingview-mcp quando pronto para uso
- [ ] Avaliar expansão da workstation com skills adicionais do awesome-claude-skills
