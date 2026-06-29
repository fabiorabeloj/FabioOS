---
tipo: sistema
area: tecnologia
status: ativo
tags: [tecnico, protocolo, Claude]
criado_em: 2026-06-25
atualizado_em: 2026-06-25
---

# MCP — Model Context Protocol

## O que é?

Model Context Protocol é um padrão aberto para conectar modelos de IA a fontes de contexto externas (APIs, bancos de dados, sistemas). Define como LLMs acessam ferramentas e dados de forma padronizada.

## Para que serve?

- Integração entre Claude e ferramentas externas
- Padronizar como Claude acessa [[GitHub]], [[n8n]], [[Obsidian]]
- Permitir composição de múltiplas fontes de contexto
- Segurança e auditoria de acessos
- Reutilização de integrações

## Onde entra no FabioOS?

[[60_Sistemas|Sistemas]] > [[MCP]] → core de comunicação:
- Claude ↔ GitHub (commits, PRs, issues)
- Claude ↔ n8n (disparar automações)
- Claude ↔ Obsidian (ler/escrever notas)
- Claude ↔ [[Banco_Vetorial]] (RAG queries)

## Como usar?

1. **Definir servidor MCP**: Expõe recurso (GitHub API, n8n, etc)
2. **Registrar tools**: Quais ações são permitidas
3. **Conectar cliente**: Claude recebe acesso
4. **Invocar**: Claude chama via protocolo padrão

## Integrações MCP no FabioOS

| Integração | Status | Tool | Uso |
|-----------|--------|------|-----|
| GitHub | Ativo | `git` | Versionamento |
| n8n | Planejado | `http` | Automações |
| Obsidian | Planejado | `file` | Leitura/escrita |
| OpenRouter | Ativo | `http` | Roteamento LLM |

## Relações

- ↔ [[Claude Code]] — cliente principal
- ↔ [[GitHub]] — integração crítica
- ↔ [[n8n]] — automações
- ↔ [[Obsidian]] — leitura de vault
- ↔ [[RAG]] — contexto distribuído

## Próximas ações

- [ ] Documentar MCPs em uso no FabioOS
- [ ] Criar servidor MCP para Obsidian
- [ ] Criar servidor MCP para n8n
- [ ] Testar segurança e permissões
- [ ] Implementar auditoria de acessos
