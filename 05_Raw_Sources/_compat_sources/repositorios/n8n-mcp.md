---
tipo: fonte
area: sources
projeto: FabioOS
status: ativo
tags: [repositório, mcp, n8n, documentação, nós]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# n8n-mcp (czlonkowski)

## Função

Servidor MCP que fornece documentação dos nós do n8n diretamente ao Claude Code. Permite ao Claude entender e construir workflows n8n sem precisar acessar a interface web.

## Contexto

Pacote npm `n8n-mcp`. Instalado globalmente via `npm install -g n8n-mcp`. Configurado como MCP `n8n-docs` no projeto FabioOS. Diferente do MCP HTTP do n8n (que executa workflows) — este provê documentação dos nós.

## Onde foi clonado

```
C:\Users\user\claude-extensions\n8n-mcp\
```

Instalado também globalmente: `npm install -g n8n-mcp`

Configurado como MCP: `n8n-docs` (stdio) em `.claude.json`

## Comandos úteis

```bash
# Verificar instalação global
n8n-mcp --version

# Status do MCP
claude mcp list  # verifica n8n-docs: √ Connected
```

## Como ajuda o FabioOS

- Claude pode consultar documentação de qualquer nó n8n durante desenvolvimento
- Facilita criação de workflows sem precisar abrir o n8n manualmente
- Complementa o MCP HTTP do n8n (que executa os workflows em localhost:5678)

## Relação com sistemas

- **n8n**: provê documentação dos nós disponíveis
- **MCP**: configurado como `n8n-docs` (stdio) no projeto
- **Claude Code**: Claude consulta este MCP ao construir automações

## Próximas ações
- [ ] Testar consulta de documentação de nós específicos via n8n-docs
- [ ] Criar primeiro workflow n8n com auxílio do Claude usando este MCP
