---
tipo: wiki
area: wiki
projeto: FabioOS
status: ativo
fonte: [[sources/repositorios/taste-skill]]
tags: [skill, design, tokens, análise, ui, playwright]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Taste Skill

## Função

[FATO] Skill de design para Claude Code que executa reverse-engineering do "design taste" de qualquer site. Dado uma URL, captura DOM e screenshot via browser real, executa análise em 4 etapas e extrai tokens de design concretos e DNA visual.

## Contexto

[FATO] Repo `senlindesign/taste-skill`. Formato SKILL.md. Escolhida como opção principal (Opção B) no FabioOS por focar em trade-offs concretos e tokens reutilizáveis. Requer Playwright MCP para captura de browser.

[FATO] Opção alternativa `leonxlnx/taste-skill` (Opção A) clonada em `claude-extensions/taste-skill-A/` como referência secundária, sem ativação.

[INTERPRETAÇÃO] A distinção entre "DNA visual" (por que o design funciona) e tokens (o que existe) é o diferencial desta skill — produz insumos acionáveis, não apenas descrições.

## Como usar

Dependência: [[wiki/sistemas/playwright-mcp]] deve estar ativo.

```
@~/.claude/skills/taste-skill/SKILL.md
"Analise o design de linear.app e extraia os tokens visuais"
```

Saída da análise inclui:
- Paleta de cores com uso semântico
- Tipografia (fontes, tamanhos, pesos, espaçamento)
- Grid e espaçamento
- Sombras e bordas
- DNA visual: o "porquê" das decisões de design

## Onde entra no FabioOS

- **Projetos com interface**: extrair referências visuais para Pietra, Trader ou qualquer UI
- **Consistência visual**: criar tokens reutilizáveis antes de implementar interfaces
- **Análise competitiva**: entender padrões de design de ferramentas que o FabioOS usa

## Relações

- [[wiki/sistemas/playwright-mcp]]
- [[wiki/sistemas/huashu-design]]

## Próximas ações

- [ ] Primeiro teste: analisar design de obsidian.md ou n8n.io
- [ ] Salvar resultado da análise em `sources/design/` do vault
