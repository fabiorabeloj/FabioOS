---
tipo: wiki
area: wiki
projeto: FabioOS
status: ativo
fonte: [[sources/repositorios/playwright-mcp]]
tags: [mcp, browser, automação, microsoft, playwright, design]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Playwright MCP

## Função

[FATO] Servidor MCP oficial da Microsoft que permite ao Claude controlar um browser em tempo real via snapshots de acessibilidade. Habilita navegação, cliques, formulários e captura de screenshots durante sessões do Claude Code.

## Contexto

[FATO] Repo `microsoft/playwright-mcp`, versão v0.0.76+, 34k+ estrelas. Executa via `npx @playwright/mcp@latest` — não requer instalação permanente.

[FATO] Diferença importante: ao contrário do Playwright CLI (que roda scripts de teste automatizados), o playwright-mcp permite interação *interativa* — Claude navega e responde ao que vê em tempo real.

[DECISÃO] Configurado globalmente em `~/.claude/settings.json` como `playwright-mcp`. Disponível em qualquer projeto, não apenas no FabioOS.

## Como usar

O MCP ativa automaticamente quando Claude precisa abrir um browser. Exemplos de uso:

```
"Abra linear.app e descreva o layout"
"Navegue até minha instância n8n em localhost:5678 e liste os workflows ativos"
"Capture o design deste site e extraia os tokens visuais"
```

## Onde entra no FabioOS

- **Skill Taste**: dependência obrigatória — sem playwright-mcp a skill não funciona
- **Skill Huashu Design**: pode usar browser para capturar referências de design
- **Pesquisa web**: Claude pode navegar e extrair dados durante sessões
- **n8n**: inspecionar a interface do n8n sem sair do Claude Code

## Relações

- [[wiki/sistemas/taste-skill]]
- [[wiki/sistemas/huashu-design]]
- [[wiki/conceitos/mcp]]

## Próximas ações

- [ ] Testar em sessão: pedir ao Claude para abrir localhost:5678 e descrever workflows
- [ ] Usar com taste-skill para análise de design de referência
