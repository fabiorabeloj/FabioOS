---
tipo: wiki
area: wiki
projeto: FabioOS
status: ativo
fonte: [[sources/repositorios/claude-mem]]
tags: [claude-code, memória, plugin, contexto, mcp-interno]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Claude Mem

## Função

[FATO] Plugin de compressão e persistência de memória para o Claude Code. Mantém contexto de sessões anteriores acessível em sessões futuras via busca semântica.

## Contexto

[FATO] Plugin formal `claude-mem@thedotmack`, versão 13.8.1. Instalado via marketplace `thedotmack`. Expõe um servidor MCP interno (`plugin:claude-mem:mcp-search`) que indexa e consulta memórias de sessões passadas.

[FATO] Requer Bun como runtime para o worker daemon. Na Fase 4.5 do FabioOS o erro "Bun not found" foi resolvido com instalação do Bun 1.3.14 — o worker agora inicia automaticamente no SessionStart.

## Como usar

O plugin opera de forma automática via hooks:

| Evento | Ação |
|---|---|
| SessionStart | Inicia worker daemon + carrega contexto |
| UserPromptSubmit | Inicializa rastreamento da sessão |
| PreToolUse (Read) | Indexa arquivos lidos |
| PostToolUse | Registra observações |
| Stop | Persiste memória ao encerrar |

[DECISÃO] O FabioOS usa o claude-mem como sistema de memória principal entre sessões. As memórias manuais em `~/.claude/projects/.../memory/` complementam o sistema automático.

## Onde entra no FabioOS

- **Continuidade entre sessões**: Claude "lembra" de arquitetura, decisões e preferências do FabioOS
- **Contexto de arquivos**: indexa notas lidas durante o trabalho no vault
- **Observações**: registra o que foi feito em cada sessão

## Relações

- [[wiki/sistemas/gsd-core]]
- [[wiki/sistemas/superpowers]]
- [[wiki/conceitos/mcp]]

## Próximas ações

- [ ] Testar busca de memórias antigas via MCP `plugin:claude-mem:mcp-search`
- [ ] Verificar onde as memórias são armazenadas: `~/.claude-mem/`
