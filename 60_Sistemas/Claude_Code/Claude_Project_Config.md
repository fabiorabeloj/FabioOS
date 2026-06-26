---
tipo: documentação
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [claude-code, skills, commands, agents, configuração]
criado_em: 2026-06-25
atualizado_em: 2026-06-25
---

# Configuração Project-Level `.claude/` — FabioOS

## Função

Documenta a estrutura `.claude/` project-level criada no vault FabioOS, o que foi copiado, de onde veio, por que e como manter.

## Contexto

O Claude Code suporta configurações em dois níveis:
- **Global** (`~/.claude/`) — válido em todos os projetos
- **Project-level** (`.claude/` na raiz do repo) — válido apenas neste vault

Esta configuração project-level foi criada na Fase 4 do FabioOS para tornar o vault autossuficiente e portable.

## Estrutura criada

```
.claude/
├── skills/               ← junctions para skills em claude-extensions/
│   ├── gsd-core/         → C:\Users\user\claude-extensions\gsd-core
│   ├── huashu-design/    → C:\Users\user\claude-extensions\huashu-design
│   └── taste-skill/      → C:\Users\user\claude-extensions\taste-skill-B
├── commands/             ← comandos slash personalizados do FabioOS
│   ├── archive-source.md
│   ├── source-to-wiki.md
│   ├── update-index.md
│   ├── check-secrets.md
│   ├── session-changelog.md
│   └── safe-commit.md
├── agents/               ← agentes especializados do FabioOS
│   ├── vault-architect.md
│   ├── wiki-curator.md
│   ├── security-reviewer.md
│   └── school-assistant.md
├── hooks/                ← pasta reservada (sem hooks ativos ainda)
└── settings.local.json   ← permissões locais (gitignored)
```

## Skills copiadas

As skills são **junctions** (não cópias), apontando para os repositórios em `C:\Users\user\claude-extensions\`. As globais em `~/.claude/skills/` foram mantidas e não removidas.

| Skill | Repositório original | Tipo | Invocação |
|---|---|---|---|
| gsd-core | open-gsd/gsd-core | Plugin formal (plugin.json) | `/gsd:*` |
| huashu-design | huashu/huashu-design | SKILL.md manual | `@.claude/skills/huashu-design/SKILL.md` |
| taste-skill | senlindesign/taste-skill-B | SKILL.md manual | `@.claude/skills/taste-skill/SKILL.md` |

## Comandos disponíveis

Invocados com `/nome-do-comando` no Claude Code:

| Comando | Função |
|---|---|
| `/archive-source` | Arquiva fonte bruta em sources/ |
| `/source-to-wiki` | Transforma fonte em página wiki/ |
| `/update-index` | Atualiza índices sources/README.md e wiki/README.md |
| `/check-secrets` | Escaneia arquivos por credenciais antes do commit |
| `/session-changelog` | Gera changelog da sessão em 50_Registros/Changelog/ |
| `/safe-commit` | Fluxo completo de commit com verificação de segurança |

## Agentes disponíveis

Acessados pelo Claude Code via subagentes:

| Agente | Função |
|---|---|
| `vault-architect` | Audita e organiza estrutura do vault |
| `wiki-curator` | Transforma sources/ em wiki/ com revisão humana |
| `security-reviewer` | Detecta tokens e credenciais antes de commits |
| `school-assistant` | Suporte a materiais escolares (esqueleto) |

## Diagnóstico de Bun

Auditoria realizada em 2026-06-25:
- `gsd-ensure-canonical-path.js`: menção a "bundled" (não Bun runtime) — seguro
- `bun-runner.js` (claude-mem): usa `#!/usr/bin/env node` — não requer Bun
- **Conclusão: sem dependência real de Bun. Nenhuma ação necessária.**

## Como manter

### Adicionar nova skill
1. Clonar repo em `C:\Users\user\claude-extensions\<nome>`
2. Criar junction: `cmd /c mklink /J ".claude\skills\<nome>" "C:\Users\user\claude-extensions\<nome>"`
3. Atualizar esta nota

### Adicionar novo comando
1. Criar `.claude/commands/<nome>.md` com frontmatter e prompt
2. Comando disponível como `/<nome>` automaticamente no próximo restart

### Adicionar novo agente
1. Criar `.claude/agents/<nome>.md` com frontmatter obrigatório (name, description, model, tools)
2. Agente disponível como subagente no próximo restart

## Segurança

- `.claude/settings.local.json` — gitignored (permissões locais, sem tokens)
- As junctions em `.claude/skills/` apontam para dirs fora do repo — não commitam conteúdo dos repos
- Nenhum token, senha ou credencial está nos arquivos deste diretório

## Relações

- [[60_Sistemas/Claude_Code/Workstation_FabioOS]]
- [[60_Sistemas/Skills/Inventario_Skills]]
- [[60_Sistemas/MCP/Inventario_MCP]]
- [[schema/fluxo-wiki]]

## Próximas ações

- [ ] Testar cada comando com caso real
- [ ] Expandir `school-assistant` quando Escola/Pietra for iniciado
- [ ] Avaliar hooks GSD para automação de SessionStart
- [ ] Documentar vault na wiki quando fluxo LLM-Wiki estiver validado
