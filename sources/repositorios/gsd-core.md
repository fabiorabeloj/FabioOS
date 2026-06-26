---
tipo: fonte
area: sources
projeto: FabioOS
status: ativo
tags: [repositório, claude-code, skill, gsd, meta-prompting, spec-driven]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# gsd-core (open-gsd)

## Função

Sistema de meta-prompting, context engineering e desenvolvimento spec-driven para agentes de código IA. Contém 70+ skills nomeadas, agentes, hooks, templates e workflows.

## Contexto

Sucessor ativo do repo arquivado `gsd-build/get-shit-done`. Mantido pela organização `open-gsd`. Versão 1.6.0 com suporte a Claude Code, Cursor e Gemini CLI.

## Onde foi clonado

```
C:\Users\user\claude-extensions\gsd-core\
```

Instalado também em: `~/.claude/skills/gsd-core` (junction → claude-extensions/gsd-core)

## Comandos úteis

```bash
# Verificar skills disponíveis
ls C:\Users\user\claude-extensions\gsd-core\skills\

# Verificar hooks disponíveis
ls C:\Users\user\claude-extensions\gsd-core\hooks\

# Verificar agents disponíveis
ls C:\Users\user\claude-extensions\gsd-core\agents\
```

## Como ajuda o FabioOS

- Fornece estrutura de planejamento (spec-phase, plan-phase, execute-phase) para projetos
- Skills de debug, revisão de código, exploração de codebase
- Sistema de memória (mempalace) para persistência de contexto
- Graphify: ferramenta CLI para grafos de conhecimento do projeto

## Relação com sistemas

- **Claude Code**: instalado como plugin via skills-dir
- **Obsidian**: skills de captura e organização de conhecimento
- **n8n**: fluxos de trabalho podem usar GSD como metodologia de desenvolvimento

## Próximas ações
- [ ] Explorar skills do gsd-core mais relevantes para o FabioOS
- [ ] Testar gsd-graphify para gerar grafos do vault
- [ ] Configurar hooks do gsd-core no projeto
