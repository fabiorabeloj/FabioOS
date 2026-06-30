---
tipo: fonte
area: sources
projeto: FabioOS
status: ativo
tags: [repositório, claude-code, plugin, memória, contexto]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# claude-mem (thedotmack)

## Função

Sistema de compressão e persistência de memória para o Claude Code. Permite que contexto de sessões anteriores seja acessível em sessões futuras via MCP de busca semântica.

## Contexto

Plugin formal instalado via marketplace `thedotmack`. Versão 13.8.1. Usa hooks e um servidor MCP interno (`plugin:claude-mem:mcp-search`) para indexar e buscar memórias anteriores.

## Onde foi clonado

```
C:\Users\user\claude-extensions\claude-mem\
```

Instalado como plugin ativo: `claude-mem@thedotmack` v13.8.1

## Comandos úteis

```bash
# Verificar status do plugin
claude plugins list

# O MCP de busca fica ativo automaticamente quando o plugin está habilitado
claude mcp list  # verifica plugin:claude-mem:mcp-search
```

## Como ajuda o FabioOS

- Mantém contexto entre sessões do Claude Code
- Permite ao Claude "lembrar" de decisões anteriores, arquitetura e preferências
- Fundamental para uso contínuo do FabioOS ao longo do tempo

## Relação com sistemas

- **Claude Code**: plugin ativo (enabled)
- **MCP**: expõe `plugin:claude-mem:mcp-search` como servidor MCP interno

## Próximas ações
- [ ] Testar busca de memórias em nova sessão
- [ ] Verificar onde as memórias são armazenadas localmente
