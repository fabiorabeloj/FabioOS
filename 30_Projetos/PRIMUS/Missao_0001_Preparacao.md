---
tipo: missao
area: 30_Projetos
projeto: PRIMUS
status: rascunho
fonte: [[90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/PRIMUS/06_MISSAO_0001]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, missao-0001, eip, delta-p]
---

# Missao 0001 - Preparacao Viva

## Funcao

Preparar a primeira execucao real do circuito PRIMUS.

## Objetivo

Provar que PRIMUS nao e apenas filosofia: o sistema deve pegar entradas da Enciclopedia, materializar uma instancia jogavel e registrar consequencias persistentes.

## E - Entradas da Enciclopedia

| Familia | Entradas previstas |
|---|---|
| Racas | Humano, Elfo, Anao |
| Classes | Mago, Guerreiro |
| Criaturas | Goblin, Orc, Troll, Dragao pequeno |
| NPCs | Taverneiro, Rei, Sacerdotisa |
| Itens | Espada comum, Escudo, Pocao de cura, Tesouro |
| Magias | Fireball, Cure Wounds |
| Faccao | Coroa Real |

## I - Instancia

Nome de trabalho: Caverna do Dragao Verde.

Estrutura resumida:

1. Entrada da caverna com guardas.
2. Camara principal com combate e armadilha.
3. Camara do tesouro com perigo ambiental.
4. Camara da princesa com interacao.
5. Camara final com mini-boss.

## P - Delta P Previsto

```yaml
delta_p_previsto:
  flags:
    dragon_killed: true
    princess_rescued: true
    artifact_recovered: true
    dungeon_cleared: true
  reputation:
    coroa_real: +10
  knowledge:
    dragon_weakness_discovered: true
    secret_passage_found: true
  new_threats:
    dragon_siblings_appear: true
```

## Validacao

- V(E): todas as entradas possuem tipo?
- V(I): a instancia e jogavel em uma sessao?
- V(P): as consequencias mudam a proxima Enciclopedia?

## Lacunas Antes de Jogar

- [ ] Definir fichas minimas das criaturas.
- [ ] Definir mapa simples da dungeon.
- [ ] Definir contrato de missao em YAML final.
- [ ] Definir como registrar Delta P real apos a sessao.
- [ ] Separar o que e canon PRIMUS e o que e placeholder de teste.

## Relacoes

- [[Roteiro_Execucao_PRIMUS_6_Blocos]]
- [[80_Specs/PRIMUS/Templates_PRIMUS_Blocos]]
- [[40_Wiki/PRIMUS/Circuito_EIP]]
- [[40_Wiki/PRIMUS/Taxonomia_PRIMUS]]
