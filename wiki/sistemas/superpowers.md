---
tipo: wiki
area: wiki
projeto: FabioOS
status: ativo
fonte: [[sources/repositorios/superpowers]]
tags: [claude-code, skill, plugin, tdd, debugging, desenvolvimento]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Superpowers

## Função

[FATO] Biblioteca de 13 skills fundamentais para Claude Code: TDD, debugging sistemático, padrões de colaboração humano-IA e técnicas comprovadas de desenvolvimento.

## Contexto

[FATO] Criado por Jesse Vincent (`obra`), versão 6.0.3. Plugin formal instalado via marketplace `superpowers-dev`. Taxa de rejeição de PRs de 94% — padrão de qualidade muito criterioso para novas skills.

[INTERPRETAÇÃO] O alto critério de rejeição é um indicativo de que as 13 skills existentes são altamente refinadas — cada uma cobre um padrão de desenvolvimento que passou por validação rigorosa.

## Como usar

Instalado como plugin ativo `superpowers@superpowers-dev`. As skills são invocadas automaticamente pelo Claude Code quando relevantes para a tarefa. O hook SessionStart registra contexto de superpowers.

[DECISÃO] No FabioOS, superpowers é especialmente útil para: desenvolvimento de automações n8n (TDD para workflows) e debugging de integrações MCP.

## Onde entra no FabioOS

- **Desenvolvimento de n8n**: skills de TDD para criar e testar workflows
- **Debugging de MCPs**: debugging sistemático de integrações com Obsidian, n8n, GitHub
- **Qualidade geral**: padrões de colaboração aplicáveis em qualquer projeto do FabioOS

## Relações

- [[wiki/sistemas/gsd-core]]
- [[wiki/sistemas/claude-mem]]
- [[wiki/conceitos/mcp]]

## Próximas ações

- [ ] Identificar quais das 13 skills são mais relevantes para automação n8n
- [ ] Aplicar skill de debugging em próxima integração com problema
