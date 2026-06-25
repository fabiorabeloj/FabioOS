---
project: PRIMUS
object: prompt
type: procedure
status: ready
face: EIP
tags: [primus, claude_code, obsidian]
---

# Prompt — Claude Code integrar PRIMUS ao Obsidian

Use este prompt no Claude Code dentro do repositório local do vault FabioOS.

```text
Você está operando no repositório local do meu vault Obsidian chamado FabioOS.

Objetivo: integrar o projeto PRIMUS ao Obsidian como sistema E → I → P.

Não transforme o PRIMUS em texto solto. Cada nota deve ter YAML frontmatter com:
project, object, type, face, status, source_mode, source_pdf, page, confidence, affects, never_affects, instancing_hints, portability, tags.

Crie ou ajuste a estrutura:

30_Projetos/PRIMUS/
  PRIMUS.md
  00_Constituicao/
  01_Enciclopedia_E/
  02_Instancias_I/
  03_Persistencia_P/
  04_Templates/
  05_Dashboards/
  06_Prompts/

Implemente:
1. MOC central PRIMUS.md.
2. Mapa do sistema E → I → P.
3. Tipagem Universal.
4. Regras de Encaixe.
5. Templates para CatalogEntry, Mission, DeltaP, Species, Class, Spell, Creature/NPC/Deity, Plane e Dungeon.
6. Dashboard com Dataview para entradas, missões, ΔP e inconsistências.
7. README com instruções.

Critério de aceitação:
- Nenhuma nota estrutural sem frontmatter.
- Templates produzem Registro, Exposição e Uso.
- Missões têm sucesso, falha, risco, recompensa e ΔP.
- Persistência aparece no WorldState.
- Não reescreva regras canônicas sem fonte.
```
