---
tipo: wiki
area: 40_Wiki
projeto: PRIMUS
status: ativo
fonte: [[90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/PRIMUS/02_TIPOS_PRIMUS]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, taxonomia, tipos, wiki]
---

# Taxonomia PRIMUS

## Funcao

Definir quais tipos podem entrar na Enciclopedia do PRIMUS.

## Regra

Sem tipo, nao entra em E.

## Familias

| Familia | Tipos |
|---|---|
| Personagens | `race`, `subrace`, `class`, `subclass`, `background`, `npc` |
| Habilidades e equipamento | `feat`, `spell`, `item`, `magic_item` |
| Mundo | `plane`, `region`, `settlement`, `site`, `dungeon` |
| Entidades | `creature`, `deity` |
| Social | `faction`, `organization` |
| Gameplay | `mission`, `encounter`, `hazard`, `trap`, `puzzle` |
| Consequencias | `reward`, `consequence` |
| Sistema | `rule`, `procedure`, `generator` |

## Uso no FabioOS

Esta taxonomia deve orientar:

- ingestao de fontes PRIMUS;
- criacao de templates;
- indexacao futura no RAG/Grafo;
- agente `primus-lorekeeper`;
- validacao de missoes e Delta P.

## Lacunas

- Falta separar `canon`, `rascunho`, `inspiracao` e `externo` no frontmatter.
- Falta definir IDs estaveis para entidades.
- Falta mapear equivalencia entre categorias do PRIMUS-TAXON (`ENTIDADES`, `LOCAIS`, `GRUPOS`, `FUNCOES`, `OBJETOS`, `EVENTOS`) e os tipos canonicos.

## Relacoes

- [[PrimusOS]]
- [[Circuito_EIP]]
- [[80_Specs/PRIMUS/Spec_Ingestao_PRIMUS_ChatGPT]]
