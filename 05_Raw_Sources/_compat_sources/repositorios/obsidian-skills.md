---
tipo: fonte
area: sources
projeto: FabioOS
status: ativo
tags: [repositório, claude-code, plugin, obsidian, vault]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# obsidian-skills (kepano)

## Função

Skills para Claude Code trabalhar com o Obsidian usando CLI, formatos abertos (Markdown, Bases, JSON Canvas). Criado por Steph Ango, CEO do Obsidian.

## Contexto

Repo oficial do criador do Obsidian. Versão 1.0.1. Plugin formal instalado via marketplace `obsidian-skills`. Prioridade alta para o FabioOS por ser a fonte mais direta de integração Claude Code ↔ Obsidian.

## Onde foi clonado

```
C:\Users\user\claude-extensions\obsidian-skills\
```

Instalado como plugin ativo: `obsidian@obsidian-skills` v1.0.1

## Comandos úteis

```bash
# Ver skills disponíveis
ls C:\Users\user\claude-extensions\obsidian-skills\skills\

# Ver plugin.json
cat C:\Users\user\claude-extensions\obsidian-skills\.claude-plugin\plugin.json
```

## Como ajuda o FabioOS

- Permite ao Claude Code operar nativamente com o vault Obsidian
- Compatível com a estrutura LLM-Wiki (sources/wiki/schema)
- Facilita criação, edição e organização de notas via CLI
- Suporte a Bases (database queries no Obsidian) e JSON Canvas

## Relação com sistemas

- **Claude Code**: plugin ativo (enabled)
- **Obsidian**: integração direta com vault via CLI e formatos nativos
- **MCP**: complementa o MCP Obsidian REST API (porta 27124)

## Próximas ações
- [ ] Testar skills de criação e edição de notas do vault
- [ ] Verificar suporte a Obsidian Bases para queries no vault
