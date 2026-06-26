---
tipo: wiki
area: wiki
projeto: FabioOS
status: ativo
fonte: [[sources/repositorios/huashu-design]]
tags: [skill, design, html, protótipo, animação, interativo]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Huashu Design

## Função

[FATO] Skill de design HTML-native para Claude Code. Produz protótipos de alta fidelidade, demos interativos, animações, slideshows e exploração de variantes de design diretamente em HTML puro.

## Contexto

[FATO] Repo `alchaincyf/huashu-design`, versão 2.0 (abril 2026). Criado por alchaincyf (花叔/Huashu). Formato SKILL.md — invocação manual. O Claude age como *designer*, não como programador: o foco é na expressão visual, não na arquitetura do código.

[FATO] 20 filosofias de design, revisão em 5 dimensões de qualidade, suporte a export para MP4/GIF. HTML nativo — sem frameworks ou dependências externas.

[INTERPRETAÇÃO] A abordagem HTML-native tem vantagem no FabioOS: os protótipos podem ser salvos no vault e visualizados no Obsidian diretamente, sem servidor.

## Como usar

```
@~/.claude/skills/huashu-design/SKILL.md
"Crie um protótipo HTML para o dashboard do sistema Trader"
"Faça um demo interativo do fluxo de onboarding do Pietra"
"Explore 3 variantes de design para o menu de navegação do FabioOS"
```

## Onde entra no FabioOS

- **Prototipagem rápida**: validar ideias de interface antes de implementar
- **Demos**: apresentar funcionalidades do FabioOS visualmente
- **Exploração de variantes**: comparar estilos antes de decidir

[DECISÃO] Complementa o [[wiki/sistemas/taste-skill]]: Taste extrai DNA visual de referências externas; Huashu implementa esse DNA em protótipos.

## Relações

- [[wiki/sistemas/taste-skill]]
- [[wiki/sistemas/playwright-mcp]]

## Próximas ações

- [ ] Criar protótipo do dashboard do FabioOS como primeiro teste
- [ ] Testar export para GIF de animação de onboarding
