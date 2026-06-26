---
tipo: wiki
area: wiki
projeto: FabioOS
status: ativo
fonte: [[sources/repositorios/gsd-core]]
tags: [claude-code, gsd, meta-prompting, spec-driven, skill, agente]
criado_em: 2026-06-25
atualizado_em: 2026-06-25
---

# GSD Core

## Função

[FATO] Sistema de meta-prompting e desenvolvimento spec-driven para agentes de código IA, com 70+ skills nomeadas, agentes especializados, hooks, templates e workflows.

## Contexto

[FATO] Mantido pela organização `open-gsd`, é o sucessor do repositório arquivado `gsd-build/get-shit-done`. Versão 1.6.0 com suporte a Claude Code, Cursor e Gemini CLI.

[DECISÃO] O FabioOS adotou o GSD Core como framework principal de planejamento e execução de projetos dentro do Claude Code. Instalado em `C:\Users\user\claude-extensions\gsd-core\` e linkado via junction em `.claude/skills/` (project-level) e `~/.claude/skills/` (global).

## Como usar

Os comandos GSD são acessíveis via `/gsd:*` no Claude Code:

- `/gsd:plan-phase` — planejar uma fase de projeto
- `/gsd:execute-phase` — executar um plano
- `/gsd:debug` — debugar problemas com ciclos de checkpoint
- `/gsd:code-review` — revisar código com agentes especializados

[INTERPRETAÇÃO] O padrão GSD de `spec-phase → plan-phase → execute-phase` é particularmente útil para projetos do FabioOS que envolvem múltiplos sistemas (n8n, Obsidian, MCP) onde a especificação prévia reduz retrabalho.

## Componentes principais

| Componente | Descrição |
|---|---|
| Skills (70+) | Instruções nomeadas para tarefas específicas |
| Agents | Subagentes especializados (planner, executor, debugger...) |
| Hooks | Scripts de automação (SessionStart, PreCommit) |
| MemPalace | Sistema de memória persistente entre sessões |
| Graphify | CLI para grafos de conhecimento do projeto |

## Onde entra no FabioOS

- **Claude Code**: skills e agentes disponíveis em toda sessão
- **LLM-Wiki**: pode usar GSD para organizar o fluxo de curadoria
- **n8n**: metodologia GSD aplicável ao desenvolvimento de workflows
- **Escola/Pietra**: framework para planejar materiais e projetos pedagógicos

## Relações

- [[wiki/sistemas/claude-mem]]
- [[wiki/sistemas/claude-code]]
- [[60_Sistemas/Claude_Code/Workstation_FabioOS]]
- [[60_Sistemas/Claude_Code/Claude_Project_Config]]
- [[schema/fluxo-wiki]]

## Próximas ações

- [ ] Explorar skills GSD mais relevantes para o FabioOS (Prioridade: MemPalace, Graphify)
- [ ] Testar `gsd-graphify` no vault para gerar grafo de conhecimento
- [ ] Avaliar hooks GSD para integração com fluxo LLM-Wiki
