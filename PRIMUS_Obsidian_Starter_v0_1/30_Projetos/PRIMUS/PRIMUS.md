---
project: PRIMUS
type: moc
status: stable
face: EIP
created: 2026-06-25
tags: [primus, moc, rpg, obsidian]
---

# PRIMUS

## Núcleo

PRIMUS é um sistema persistente de RPG baseado em D&D 5e, estruturado pelo circuito:

**E → I → P**

- **E — Enciclopédia Funcional:** conteúdo tipado, rastreável e consultável.
- **I — Instância Controlada:** missões, dungeons e encontros fechados.
- **P — Persistência:** alterações de estado registráveis no mundo.

## Abertura rápida

1. [[00_Constituicao/PRIMUS - Mapa do Sistema]]
2. [[00_Constituicao/Tipagem Universal]]
3. [[00_Constituicao/Regras de Encaixe]]
4. [[01_Enciclopedia_E/Grimorio]]
5. [[02_Instancias_I/Missoes]]
6. [[03_Persistencia_P/WorldState]]
7. [[05_Dashboards/Dashboard PRIMUS]]

## Livros operacionais

| Livro | Função |
|---|---|
| [[01_Enciclopedia_E/Grimorio]] | Conteúdo de ficha e opções do jogador |
| [[01_Enciclopedia_E/Bestiario]] | Criaturas, NPCs, deuses, chefes |
| [[01_Enciclopedia_E/Cosmologia]] | Planos, leis metafísicas e conectividade |
| [[01_Enciclopedia_E/Atlas]] | Regiões, assentamentos, rotas, locais e blueprints |
| [[02_Instancias_I/Missoes]] | Execução fechada do jogo |
| [[03_Persistencia_P/WorldState]] | Estado acumulado do mundo |

## Norma prática

Uma nota PRIMUS válida precisa ter:

- `project: PRIMUS`
- `object`
- `type`
- `face`
- `source_mode`
- `affects`
- `never_affects`
- `instancing_hints`
- `portability`
- `confidence`

Sem isso, é apenas rascunho.
