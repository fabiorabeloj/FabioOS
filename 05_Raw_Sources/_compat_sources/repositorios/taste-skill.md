---
tipo: fonte
area: sources
projeto: FabioOS
status: ativo
tags: [repositório, skill, design, taste, tokens, ui]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# taste-skill (senlindesign) — Opção Principal

## Função

Skill de design para Claude Code que faz reverse-engineer do "design taste" de qualquer site. Dado uma URL, captura DOM e screenshot via browser real, executa análise de 4 etapas e produz tokens de design concretos (cores, tipografia, espaçamento, sombras, grid) e DNA visual (por que o design funciona, não apenas o que existe).

## Contexto

Repo: `senlindesign/taste-skill`. Formato SKILL.md. Escolhida como opção principal (Opção B) por focar em trade-offs concretos e decisões visuais reutilizáveis. Requer Playwright MCP para captura de browser.

## Onde foi clonado

```
C:\Users\user\claude-extensions\taste-skill-B\
```

Disponível em: `~/.claude/skills/taste-skill/SKILL.md` (junction)

## Referência alternativa (Opção A)

```
C:\Users\user\claude-extensions\taste-skill-A\   (leonxlnx/taste-skill)
```
Não ativada. Foco em variance, motion e density para outputs criativos.

## Como usar (invocação manual)

```
/taste https://linear.app
# ou
"Analise o design de linear.app e extraia os tokens visuais"
# ou
@~/.claude/skills/taste-skill/SKILL.md
```

**Dependência:** Playwright MCP deve estar ativo (`claude mcp list` → playwright-mcp ✅)

## Como ajuda o FabioOS

- Extração de sistemas de design de referência
- Geração de guias de estilo para projetos (Pietra, Trader, etc.)
- Alimenta o workflow de design com decisões concretas, não genéricas

## Relação com sistemas

- **Claude Code**: skill SKILL.md (invocação manual)
- **MCP**: requer `playwright-mcp` ativo
- **Obsidian**: outputs podem ser salvos como notas de design no vault

## Próximas ações
- [ ] Testar: `@~/.claude/skills/taste-skill/SKILL.md` + URL de referência
- [ ] Salvar resultado de análise em sources/ do vault
