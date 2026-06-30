---
tipo: spec
area: 80_Specs
projeto: PRIMUS
status: rascunho
fonte: [[40_Wiki/PRIMUS/Motor_Causal_PRIMUS]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, spec, cantina, player-view, conflitos]
---

# SPEC - Cantina Conflict Engine PRIMUS

## Objetivo

Transformar conflitos candidatos em opcoes visiveis para o jogador sem revelar a Enciclopedia total e sem conceder propriedade/poder automaticamente.

## Entrada

- [[30_Projetos/PRIMUS/Conflitos_Candidatos_PRIMUS]]
- Player View disponivel;
- regras V/A/Oculto;
- WorldState ativo;
- bloqueios do Tension Engine.

## Saida

Uma lista de opcoes de Cantina:

```yaml
cantina_option_id:
conflict_candidate_id:
titulo_visivel:
descricao_curta:
estado_acesso: V | A | Oculto
requisitos:
risco_visivel:
recompensa_visivel:
bloqueios:
status:
```

## Regras

- `V` significa visivel, nao adquirido.
- `A` significa adquirido por evento de jogo.
- `Oculto` nao aparece para o jogador.
- A Cantina mostra escolhas, nao executa missao sozinha.
- Opcao bloqueada pode aparecer como rumor incompleto se isso nao revelar segredo estrutural.
- Nenhuma opcao pode conceder item, classe, magia, mapa ou vantagem sem evento de jogo.

## Fluxo

```text
Conflitos Candidatos
-> filtrar visibilidade
-> aplicar V/A/Oculto
-> gerar quadro da Cantina
-> jogador escolhe
-> Mission Engine monta instancia
```

## Criterios de Aceite

- Conflitos bloqueados nao viram missao.
- Conflitos visiveis aparecem com linguagem de jogador.
- O jogador nunca acessa a Enciclopedia total.
- Toda escolha aponta para um `conflict_candidate_id`.
- Toda recompensa visivel distingue expectativa de aquisicao real.

## Implementacao Minima

Criar `PlayerView_Cantina_0001_PRIMUS.md` com 2 ou 3 opcoes visiveis, usando somente conflitos candidatos prontos.
