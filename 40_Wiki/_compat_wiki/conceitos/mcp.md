---
tipo: wiki
area: wiki
projeto: FabioOS
status: ativo
tags: [mcp, protocolo, conceito, anthropic, extensão, ferramenta]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# MCP — Model Context Protocol

## Função

[FATO] Protocolo aberto (Anthropic, 2024) que define como modelos de linguagem se conectam a fontes de dados e ferramentas externas. Permite ao Claude usar ferramentas além do que está na janela de contexto — acesso a arquivos, APIs, browsers, bancos de dados e sistemas externos.

## Como funciona

```
Claude Code ←→ MCP Client ←→ [transporte] ←→ MCP Server ←→ Sistema externo
```

**Transportes:**
- **stdio**: processo filho no mesmo computador (ex: n8n-docs, filesystem)
- **HTTP/SSE**: servidor remoto ou local acessado via HTTP (ex: Obsidian REST API, n8n MCP)

**O MCP Server expõe:**
- **Tools** — funções que Claude pode chamar (ex: `read_file`, `execute_workflow`)
- **Resources** — dados que Claude pode ler (ex: arquivos, páginas wiki)
- **Prompts** — templates de prompt reutilizáveis

## MCPs ativos no FabioOS

| Nome | Tipo | Sistema | Transporte |
|---|---|---|---|
| `filesystem` | Oficial | Acesso a arquivos do vault | stdio |
| `context7` | Oficial | Documentação de libs | stdio |
| `github` | Oficial | Repositório FabioOS | stdio |
| `playwright-mcp` | Microsoft | Controle de browser | stdio |
| `n8n-docs` | Comunitário | Documentação dos nós n8n | stdio |
| `obsidian` | Obsidian REST | Leitura do vault Obsidian | HTTP |
| `n8n-mcp` | n8n HTTP | Execução de workflows | HTTP |
| `plugin:claude-mem:mcp-search` | Plugin interno | Busca de memórias | interno |

## Onde entra no FabioOS

[INTERPRETAÇÃO] O MCP é a "cola" do FabioOS — é o que transforma o Claude Code de um assistente de chat em um agente operacional capaz de ler o vault, executar workflows n8n, controlar browsers e buscar memórias de sessões anteriores.

[DECISÃO] A estratégia de MCPs do FabioOS é: usar oficiais e comunitários maduros para o que já existe, e criar MCPs customizados via [[wiki/sistemas/fastmcp]] para funcionalidades específicas do sistema (Trader, busca avançada no vault).

## Criar MCP customizado

Via [[wiki/sistemas/fastmcp]] (Python) ou [[wiki/sistemas/mcp-servers]] (TypeScript):

```python
# Mínimo com fastmcp
from fastmcp import FastMCP
mcp = FastMCP("fabios-vault-search")

@mcp.tool()
def buscar(query: str) -> str:
    """Busca no vault do FabioOS"""
    ...
```

## Relações

- [[wiki/sistemas/fastmcp]]
- [[wiki/sistemas/mcp-servers]]
- [[wiki/sistemas/n8n-mcp]]
- [[wiki/sistemas/playwright-mcp]]
- [[wiki/sistemas/tradingview-mcp]]
- [[wiki/sistemas/claude-mem]]

## Próximas ações

- [ ] Criar primeiro MCP customizado do FabioOS (candidato: busca no vault)
- [ ] Documentar todos os MCPs ativos em `60_Sistemas/MCP/`
