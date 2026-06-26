---
tipo: wiki
area: wiki
projeto: FabioOS
status: ativo
fonte: [[sources/repositorios/fastmcp]]
tags: [mcp, python, framework, criação, extensão, custom]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# FastMCP

## Função

[FATO] Framework Python para criar servidores MCP rapidamente. Funções Python decoradas com `@mcp.tool()` geram automaticamente schemas, validação e documentação MCP — sem código boilerplate.

## Contexto

[FATO] Repo `PrefectHQ/fastmcp` (originalmente `jlowin/fastmcp`, adquirido pela Prefect). Base de ~70% dos servidores MCP existentes. ~1 milhão de downloads diários. Ativo e amplamente adotado.

[FATO] Clonado em `C:\Users\user\claude-extensions\fastmcp\` apenas como referência — sem MCP customizado criado ainda.

[INTERPRETAÇÃO] Dada a adoção massiva (~70% dos MCPs existentes), fastmcp é o caminho padrão para criação de MCPs customizados. A curva de entrada é baixa para quem já tem Python.

## Como usar (exemplo mínimo)

```python
from fastmcp import FastMCP

mcp = FastMCP("meu-mcp")

@mcp.tool()
def buscar_vault(query: str) -> str:
    """Busca no vault do FabioOS"""
    # implementação aqui
    return resultado

if __name__ == "__main__":
    mcp.run()
```

Executar: `fastmcp run servidor.py`

## Onde entra no FabioOS

[DECISÃO] O FabioOS tem três candidatos prioritários para MCPs customizados com fastmcp:

1. **MCP do Vault** — busca semântica nas notas Obsidian (alternativa/complemento ao Obsidian REST API)
2. **MCP do Trader** — dados de posição, alertas, histórico (quando o sistema Trader for implementado)
3. **MCP do n8n customizado** — disparar workflows específicos do FabioOS com parâmetros estruturados

## Relações

- [[wiki/conceitos/mcp]]
- [[wiki/sistemas/mcp-servers]]
- [[wiki/sistemas/n8n-mcp]]

## Próximas ações

- [ ] Criar primeiro MCP customizado: busca simples no vault (`sources/` e `wiki/`)
- [ ] Definir qual funcionalidade tem maior retorno como MCP próprio
