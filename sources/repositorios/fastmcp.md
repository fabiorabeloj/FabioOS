---
tipo: fonte
area: sources
projeto: FabioOS
status: ativo
tags: [repositório, mcp, python, framework, criação]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# fastmcp (PrefectHQ)

## Função

Framework Python para criar servidores MCP rapidamente. Funções Python decoradas geram automaticamente schemas, validação e documentação MCP. Base de ~70% dos servidores MCP existentes, com ~1M downloads diários.

## Contexto

Repo: `PrefectHQ/fastmcp`. Originalmente `jlowin/fastmcp`, adquirido e mantido pela Prefect. Ativo e altamente popular. Referência para criar MCPs customizados do FabioOS em Python.

## Onde foi clonado

```
C:\Users\user\claude-extensions\fastmcp\
```

Clonado apenas como referência — não instalado como MCP ativo.

## Comandos úteis

```bash
# Instalar para desenvolvimento de MCP
pip install fastmcp
# ou
uv add fastmcp

# Exemplo mínimo de servidor MCP
# (ver C:\Users\user\claude-extensions\fastmcp\examples\)
```

## Como ajuda o FabioOS

- Criar MCPs customizados para o FabioOS (ex: MCP de busca no vault, MCP do sistema Trader)
- Integrar o n8n com Claude via MCP customizado
- Base para automações que precisem de ferramentas especializadas

## Relação com sistemas

- **MCP**: framework para criação de servidores MCP
- **Python**: usa o ambiente Python já instalado (uv disponível)
- **n8n**: pode criar MCP que chame workflows n8n
- **Obsidian**: pode criar MCP de acesso avançado ao vault

## Próximas ações
- [ ] Criar primeiro MCP customizado do FabioOS usando fastmcp
- [ ] Definir qual funcionalidade merece um MCP próprio (ex: busca no vault, dados Trader)
