---
tipo: wiki
area: 40_Wiki
projeto: PRIMUS
status: ativo
fonte: [[90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/PRIMUS/00_CIRCUITO_MESTRE]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, eip, persistencia, mundo-vivo]
---

# Circuito EIP

## Funcao

O Circuito EIP e o nucleo operacional do PRIMUS.

```text
E - Enciclopedia
  -> I - Instancia
  -> P - Persistencia / Delta P
  -> E atualizado
```

## E - Enciclopedia

Banco conceitual do mundo. Contem tipos, entidades, locais, regras, criaturas, itens, faccoes e conhecimento canonico.

## I - Instancia

Materializacao jogavel: missao, encontro, dungeon, cena, evento ou sessao. A instancia usa entradas da Enciclopedia para produzir uma experiencia concreta.

## P - Persistencia

Registro das mudancas que ficam. Exemplos:

- flags;
- itens obtidos;
- mortes;
- reputacao;
- conhecimento descoberto;
- danos;
- novos NPCs;
- mudancas politicas ou cosmologicas.

## Regra Principal

O circuito nao termina em P. O Delta P volta para E e altera a proxima instancia.

## Por que importa

Sem persistencia, PRIMUS vira apenas gerador de aventura. Com persistencia, ele vira mundo vivo.

## Relacoes

- [[PrimusOS]]
- [[Taxonomia_PRIMUS]]
- [[30_Projetos/PRIMUS/Plano_Ingestao_PRIMUS]]
