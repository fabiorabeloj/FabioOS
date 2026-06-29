---
tipo: inventário
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [skills, claude-code, plugins, workstation]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Inventário de Skills — FabioOS

## Função

Registro centralizado de todas as skills, plugins e extensões instaladas no Claude Code para o FabioOS.

## Contexto

Skills são extensões que ampliam as capacidades do Claude Code. Existem dois formatos: plugins formais (instalados via marketplace) e skills-dir (carregadas automaticamente de `~/.claude/skills/`). Skills no formato SKILL.md requerem invocação manual.

## Plugins instalados (via marketplace)

| Plugin | Versão | Marketplace | Função | Status |
|--------|--------|-------------|--------|--------|
| `claude-mem` | 13.8.1 | thedotmack | Memória persistente entre sessões, compressão de contexto | ✅ enabled |
| `superpowers` | 6.0.3 | superpowers-dev | Skills fundamentais: TDD, debugging, colaboração | ✅ enabled |
| `ui-ux-pro-max` | 2.6.2 | ui-ux-pro-max-skill | Design UI/UX: 84 estilos, 161 paletas, 73 pares de fontes | ✅ enabled |
| `obsidian` | 1.0.1 | obsidian-skills | Skills para Obsidian CLI, Markdown, Bases e JSON Canvas | ✅ enabled |

## Skills-dir (auto-carregadas de `~/.claude/skills/`)

| Nome | Versão | Caminho local | Função | Status |
|------|--------|---------------|--------|--------|
| `gsd-core` | 1.6.0 | `~/.claude/skills/gsd-core` → `claude-extensions/gsd-core` | GSD: meta-prompting, spec-driven dev, 70+ skills | ✅ loaded |

## Skills formato SKILL.md (invocação manual)

Requerem `@import` no CLAUDE.md ou invocação explícita na sessão.

| Nome | Caminho local | Função | Dependência |
|------|---------------|--------|-------------|
| `taste` (senlindesign) | `~/.claude/skills/taste-skill/SKILL.md` | Extrai design taste de sites: tokens, DNA visual, trade-offs | Playwright MCP ✅ |
| `huashu-design` | `~/.claude/skills/huashu-design/SKILL.md` | Design HTML-native: protótipos de alta fidelidade, 20 filosofias, animações | Nenhuma |

## Repos de referência clonados (não ativados)

| Nome | Caminho | Função |
|------|---------|--------|
| `taste-skill-A` (leonxlnx) | `claude-extensions/taste-skill-A` | Variante alternativa do Taste — anti-slop com variance/motion/density |
| `awesome-claude-skills` | `claude-extensions/awesome-claude-skills` | Catálogo de referência de skills da comunidade |
| `awesome-claude-code` | `claude-extensions/awesome-claude-code` | Catálogo de recursos Claude Code |

## Como usar

**Plugin formal:** já está ativo na próxima sessão do Claude Code automaticamente.

**Skill SKILL.md (Taste):** em qualquer sessão Claude Code, use `/taste <url>` ou diga "analise o design de X" — a skill é carregada pelo gsd-core ou via `@~/.claude/skills/taste-skill/SKILL.md`.

**Skill SKILL.md (Huashu):** invoque pedindo protótipos HTML ou use `@~/.claude/skills/huashu-design/SKILL.md`.

## Regra operacional

Antes de executar uma tarefa manualmente, verificar o protocolo:

`60_Sistemas/FabioOS/Protocolo_Roteamento_Capacidades_IA.md`

Regra prática:

```text
Se já existe capacidade instalada para a tarefa, use-a ou registre por que ela
não serve neste caso.
```

Quando a tarefa envolver escolha entre modelos, IAs, agentes ou ferramentas externas, consultar tambem:

`40_Repertorio/IA/Modelos_e_IAs/Matriz_de_Aptidao_das_IAs_FabioOS.md`

Quando a tarefa envolver criacao, consulta ou manutencao de conhecimento, consultar tambem:

`index.md`, `log.md` e `60_Sistemas/Wiki/Schema_Wiki_FabioOS.md`

## Relações

- [[60_Sistemas/MCP/Inventario_MCP]] — MCPs necessários para algumas skills (ex: Playwright para Taste)
- [[60_Sistemas/Claude_Code/Workstation_FabioOS]] — visão geral da workstation
- [[60_Sistemas/FabioOS/Protocolo_Roteamento_Capacidades_IA]] — regra de uso efetivo das capacidades instaladas
- [[40_Repertorio/IA/Modelos_e_IAs/Matriz_de_Aptidao_das_IAs_FabioOS]] — vocacao, limites e criterios de teste das IAs/ferramentas

## Próximas ações
- [ ] Testar `/taste` em um projeto com Playwright MCP ativo
- [ ] Testar `huashu-design` em protótipo HTML
- [ ] Avaliar skills do `gsd-core` mais usadas e documentar as prioritárias
