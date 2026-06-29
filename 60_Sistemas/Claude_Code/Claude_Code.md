---
tipo: sistema
area: tecnologia
status: ativo
tags: [tecnico, Claude, CLI]
criado_em: 2026-06-25
atualizado_em: 2026-06-25
---

# Claude Code

## O que é?

Claude Code é uma CLI (Command Line Interface) que permite executar agentes Claude diretamente do terminal para automações, desenvolvimento e gerenciamento de código.

## Para que serve?

- Automatizar tarefas complexas via CLI
- Executar Claude como agente autônomo
- Integrar com [[n8n]] e workflows
- Processar arquivos e dados em lote
- Gerar código baseado em contexto

## Onde entra no FabioOS?

[[60_Sistemas|Sistemas]] > [[Claude_Code]] → automações:
- Processamento de notas via [[integracao-n8n-github]]
- Geração de documentação automática
- Análise de repositório
- Integração com [[n8n]]

## Como usar?

1. **Instalar Claude Code CLI**
2. **Autenticar com API key**
3. **Rodar agente**: `claude run [task]`
4. **Integrar com n8n**: Disparar via webhook

## Documentação

- [Claude Code Docs](https://docs.anthropic.com/claude-code)
- [[MCP]] — protocolo subjacente
- [[OpenRouter]] — roteamento de modelos

## Relações

- ↔ [[n8n]] — execução de automações
- ↔ [[GitHub]] — versionamento de scripts
- ↔ [[MCP]] — protocolo de contexto
- ↔ [[OpenRouter]] — escolha de modelo

## Próximas ações

- [ ] Documentar scripts existentes
- [ ] Criar templates de automação
- [ ] Integrar com [[n8n]] workflows
- [ ] Testar agentes autônomos
