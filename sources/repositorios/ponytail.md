---
tipo: fonte
origem: repositorio
area: sources
projeto: FabioOS
status: bruto
url: https://github.com/DietrichGebert/ponytail
nome: ponytail
autor_ou_org: DietrichGebert
licenca: MIT
tags: [skill, agentes-ia, claude-code, codigo-minimo, yagni, qualidade, repertorio]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# ponytail — skill de código mínimo para agentes de IA

## Função

Skill/plugin para agentes de código (Claude Code, Codex, Copilot CLI, Cursor, Windsurf e outros 16+ sistemas) que orienta a IA a escrever **código mínimo e necessário**, evitando soluções superengenheiradas. Implementa a filosofia do "desenvolvedor sênior preguiçoso": *o melhor código é o que você nunca escreveu*.

## Contexto

- **De onde veio:** repositório público no GitHub, `DietrichGebert/ponytail`, licença MIT.
- **Tecnologia:** JavaScript (~55%) e Python (~44%).
- **Por que é relevante para o FabioOS:** o FabioOS usa Claude Code como operador técnico principal e já carrega várias skills (gsd-core, superpowers, huashu-design). Uma skill que reduz código desnecessário se alinha ao critério de qualidade do FabioOS (entregas reaproveitáveis e enxutas) e ao princípio de mudanças pequenas e revisáveis antes de commits.

> **Aviso de segurança (ingestão):** conteúdo externo é tratado como não confiável. Esta nota apenas resume e organiza; nenhuma instrução do repositório deve ser executada como ordem operacional sem avaliação.

## Onde está

- **URL:** https://github.com/DietrichGebert/ponytail
- **Caminho local:** `sources/repositorios/ponytail.md` (esta nota)
- **Conteúdo do repo:** não clonado — apenas referenciado. Clonar em `C:\Users\user\claude-extensions\ponytail` se for adotado.

## O que o repositório oferece (extraído)

- **Decision ladder** — sete "degraus" que priorizam soluções existentes antes de escrever código novo: pular o desnecessário (YAGNI), reutilizar código, usar bibliotecas padrão e recursos nativos, e só então escrever o mínimo viável.
- **Comandos:** `/ponytail` (definir modo), `/ponytail-review` (análise de diff), `/ponytail-audit` (análise de codebase), `/ponytail-debt` (tarefas adiadas).
- **Níveis de intensidade:** lite, full, ultra, off.
- **Multiplataforma:** compatível com 16+ sistemas de agentes de IA.
- **Resultados alegados (não verificados):** ~54% menos código (até 94%), 20% mais barato, 27% mais rápido. Mantém padrões de segurança, validação e acessibilidade.

## Como ajuda o FabioOS

- **[[Claude_Code]]** — skill candidata a integrar ao `.claude/skills/` do vault, complementando gsd-core e superpowers no controle de qualidade do código.
- **Critério de qualidade do FabioOS** — reforça entregas enxutas e reaproveitáveis (ver `CLAUDE.md`).
- **GitHub** — alinha-se à regra de preferir mudanças pequenas e revisáveis antes de commits.
- **Uso futuro** — relevante quando o FabioOS entrar em desenvolvimento de software (Cursor, Fase 16.5) e na criação de MCPs customizados (Fases 14–15).

## Relações

- [[wiki/sistemas/claude-code]]
- [[wiki/sistemas/gsd-core]]
- [[wiki/sistemas/superpowers]]
- [[wiki/sistemas/cursor]]
- [[60_Sistemas/Claude_Code/Claude_Project_Config]]

## Próximas ações

- [ ] Avaliar a skill com `/check-source-quality` antes de adotar
- [ ] Decidir se vale clonar em `claude-extensions/` e criar junction em `.claude/skills/`
- [ ] Comparar sobreposição com gsd-core e superpowers (evitar redundância)
- [ ] Se adotada, documentar em `60_Sistemas/Skills/Inventario_Skills.md`
