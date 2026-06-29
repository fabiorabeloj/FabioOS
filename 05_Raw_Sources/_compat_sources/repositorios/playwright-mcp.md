---
tipo: fonte
area: sources
projeto: FabioOS
status: ativo
tags: [repositório, mcp, playwright, browser, automação]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# playwright-mcp (microsoft)

## Função

Servidor MCP oficial da Microsoft que permite ao Claude controlar um browser em tempo real via snapshots de acessibilidade. Diferente do Playwright CLI (que roda scripts de teste): este permite interação interativa durante sessões do Claude.

## Contexto

Repo: `microsoft/playwright-mcp`. Versão v0.0.76+. 34k+ estrelas. Configurado como MCP `playwright-mcp` global (`~/.claude/settings.json`).

## Onde foi configurado

Não clonado localmente — executado via npx.

MCP configurado em: `~/.claude/settings.json` como `playwright-mcp`

```json
"playwright-mcp": {
  "command": "npx",
  "args": ["@playwright/mcp@latest"]
}
```

## Comandos úteis

```bash
# Verificar status
claude mcp list  # verifica playwright-mcp

# Testar: pedir ao Claude para abrir uma URL
# "Abra https://example.com e descreva o que vê"
```

## Como ajuda o FabioOS

- Permite ao Claude navegar em sites para extrair informações
- Necessário para a skill **Taste** (análise de design de sites)
- Automação de testes de interfaces do FabioOS
- Pesquisa e extração de dados da web em sessões ativas

## Relação com sistemas

- **MCP**: configurado como `playwright-mcp` (global)
- **Skills**: dependência obrigatória da skill `taste` (senlindesign)
- **Claude Code**: Claude usa este MCP para controlar browser

## Próximas ações
- [ ] Testar em sessão ativa: pedir ao Claude para navegar em um site
- [ ] Usar com a skill Taste para análise de design
