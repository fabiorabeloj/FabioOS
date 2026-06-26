---
tipo: wiki
area: wiki
projeto: FabioOS
status: ativo
fonte: [[sources/repositorios/n8n-mcp]]
tags: [mcp, n8n, documentação, automação, workflow, stdio]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# n8n MCP (Documentação de Nós)

## Função

[FATO] Servidor MCP que fornece documentação dos nós do n8n diretamente ao Claude Code. Permite ao Claude entender, construir e depurar workflows n8n sem precisar consultar a interface web ou documentação externa.

## Contexto

[FATO] Pacote npm `n8n-mcp` (czlonkowski). Instalado globalmente via `npm install -g n8n-mcp`. Configurado como MCP `n8n-docs` (transporte stdio) no arquivo `.claude.json` do projeto FabioOS.

[FATO] Distinto do MCP HTTP do n8n (que executa workflows em `localhost:5678`). O n8n-mcp provê *documentação* dos nós — o que cada nó faz, seus parâmetros e como configurá-lo.

## Como usar

O MCP é consultado automaticamente pelo Claude quando trabalhando com n8n. Para consulta explícita:

```
"Quais parâmetros o nó HTTP Request aceita?"
"Como configurar o nó Webhook para receber POST com JSON?"
"Mostre a documentação do nó Code (JavaScript)"
```

[DECISÃO] No FabioOS, `n8n-docs` + MCP HTTP do n8n (execução) formam o par completo para desenvolvimento de automações: Claude *entende* os nós via n8n-docs e *executa* os workflows via MCP HTTP.

## Onde entra no FabioOS

- **Desenvolvimento de workflows**: Claude constrói automações com conhecimento real dos nós
- **Debugging**: Claude entende erros de configuração ao consultar a documentação
- **Aprendizado do n8n**: explorar nós disponíveis sem abrir a interface web

## Relações

- [[wiki/conceitos/mcp]]
- [[wiki/sistemas/fastmcp]]

## Próximas ações

- [ ] Criar primeiro workflow n8n assistido pelo Claude usando n8n-docs
- [ ] Testar consulta: "Liste os nós disponíveis para integração com Telegram"
