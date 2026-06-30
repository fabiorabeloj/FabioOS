---
tipo: spec
area: 80_Specs
projeto: PRIMUS
status: rascunho-operacional
fonte: [[40_Wiki/PRIMUS/Changelog_PRIMUS_5_6]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, spec, mission-contract, deltap]
---

# Spec - Mission Contract PRIMUS

## Missao

Garantir que toda missao seja um contrato causal, nao uma aventura solta.

## Entrada

- WorldState;
- vetor;
- tensao;
- conflito candidato;
- atores;
- fontes;
- DeltaP previsto.

## Saida

- contrato de missao;
- criterios de sucesso/falha;
- consequencias previstas;
- player view segura;
- registro DeltaP pos-execucao.

## Campos Minimos

```yaml
mission_id:
titulo:
status:
origem_worldstate:
vector_id:
tension_id:
conflict_id:
atores:
local:
gancho_cantina:
classe_de_missao:
objetivo_jogador:
sucesso:
falha:
ignorado:
delta_p_previsto:
fontes:
canon_status:
```

## Regras

- Missao sem DeltaP previsto fica bloqueada.
- Missao sem fonte fica como prototipo, nao canon.
- Missao nao pode alterar WorldState diretamente.
- Missao so altera WorldState via DeltaP validado.
- Player View nao deve revelar Enciclopedia total.

## Criterios de Aceite

- ha origem no WorldState;
- ha vetor e tensao;
- ha conflito candidato;
- ha sucesso, falha e ignorado;
- ha DeltaP previsto;
- ha limite claro entre informacao do jogador e informacao do sistema.
