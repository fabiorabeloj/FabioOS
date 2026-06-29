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
| `/archive-source` | Arquiva fonte bruta em 05_Raw_Sources/_compat_sources/ |
| `/source-to-wiki` | Transforma fonte em página 40_Wiki/_compat_wiki/ |
| `/update-index` | Atualiza índices 05_Raw_Sources/_compat_sources/README.md e 40_Wiki/_compat_wiki/README.md |
| `/check-secrets` | Escaneia arquivos por credenciais antes do commit |
| `/session-changelog` | Gera changelog da sessão em 50_Registros/Changelog/ |
| `/safe-commit` | Fluxo completo de commit com verificação de segurança |

## Agentes disponíveis

Acessados pelo Claude Code via subagentes:

| Agente | Função |
|---|---|
| `vault-architect` | Audita e organiza estrutura do vault |
| `wiki-curator` | Transforma 05_Raw_Sources/_compat_sources/ em 40_Wiki/_compat_wiki/ com revisão humana |
| `security-reviewer` | Detecta tokens e credenciais antes de commits |
| `school-assistant` | Suporte a materiais escolares (esqueleto) |

## Diagnóstico de Bun (Fase 4.5 — resolvido 2026-06-26)

### Causa do erro `Bun not found`

O plugin **claude-mem** (thedotmack/13.8.1) registra hooks em 5 eventos:
`Setup`, `SessionStart`, `UserPromptSubmit`, `PreToolUse` (Read), `PostToolUse`, `Stop`.

Todos os hooks chamam `node bun-runner.js worker-service.cjs <ação>`. O script
`bun-runner.js` internamente chama `findBun()` que:
1. Tenta `where bun` (PATH do shell)
2. Se falhar, testa diretamente `~/.bun/bin/bun.exe`
3. Se nenhum encontrado → emite "Error: Bun not found. Please install Bun"

Bun não estava instalado → todos os hooks falhavam com esse erro.

### Solução aplicada

Instalação de Bun via PowerShell oficial:
```powershell
irm bun.sh/install.ps1 | iex
# Instalado em: C:\Users\user\.bun\bin\bun.exe (v1.3.14)
```

`findBun()` encontra o executável via `existsSync` — independe do PATH.

### Verificação

```
Worker is running  PID: 10272  Port: 37777  Version: 13.8.1  Uptime: 229s
```

O worker do claude-mem iniciou com sucesso no próximo SessionStart.
Hooks funcionando em: SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop.

### Hooks ativos identificados (claude-mem)

| Evento | Ação | Essencial |
|---|---|---|
| Setup | version-check.js | Sim — valida versão do plugin |
| SessionStart | worker-service start | Sim — inicia daemon de memória |
| SessionStart | hook context | Sim — carrega contexto da sessão |
| UserPromptSubmit | hook session-init | Sim — inicializa rastreamento |
| PreToolUse (Read) | hook file-context | Útil — indexa arquivos lidos |
| PostToolUse | hook observation | Útil — registra observações |
| Stop | hook summarize | Útil — persiste memória ao sair |

Todos os hooks são do plugin claude-mem e são **essenciais** para seu funcionamento.
Nenhum hook redundante ou herdado encontrado.

### Nota: GITHUB_TOKEN em settings.json global

O arquivo `~/.claude/settings.json` (global, fora do git) contém um token GitHub
na configuração do MCP server `github`. Este arquivo NÃO está no repositório.
**Risco:** exposição local se a máquina for comprometida.
**Recomendação futura:** migrar para variável de ambiente `GITHUB_TOKEN` em vez de
hardcoded no JSON. Não é urgente, mas deve ser feito antes de qualquer compartilhamento
da máquina ou configuração de CI.

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
- [[60_Sistemas/Wiki/schema/fluxo-wiki]]

## Próximas ações

- [ ] Testar cada comando com caso real
- [ ] Expandir `school-assistant` quando Escola/Pietra for iniciado
- [ ] Avaliar hooks GSD para automação de SessionStart
- [ ] Documentar vault na wiki quando fluxo LLM-Wiki estiver validado
