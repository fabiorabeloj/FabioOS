---
tipo: fonte
area: sources
projeto: FabioOS
status: ativo
tags: [repositório, mcp, registry, descoberta, api-externa]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# modelcontextprotocol/registry

## Função

Registro/catálogo centralizado de servidores MCP disponíveis. Funciona como uma "loja de apps" para MCPs, com API de descoberta e publicação.

## Contexto

Serviço externo hospedado em `https://registry.modelcontextprotocol.io`. Em preview (API frozen desde out/2025). **Não requer instalação local** — é consumido como API externa.

## Onde acessar

```
https://registry.modelcontextprotocol.io
```

Não clonado localmente — sem necessidade.

## Comandos úteis

```bash
# Buscar MCPs disponíveis via API
curl https://registry.modelcontextprotocol.io/v0/servers

# Buscar por categoria
curl "https://registry.modelcontextprotocol.io/v0/servers?search=obsidian"
```

## Como ajuda o FabioOS

- Descoberta de novos MCPs disponíveis para o FabioOS
- Publicação futura de MCPs customizados do FabioOS
- Referência de MCPs ativos e bem mantidos

## Relação com sistemas

- **MCP**: catálogo central de servidores disponíveis

## Próximas ações
- [ ] Consultar para descobrir MCPs relevantes para n8n, Obsidian e Trader
- [ ] Avaliar publicação de MCPs customizados do FabioOS futuramente
