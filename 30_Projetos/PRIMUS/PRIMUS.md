---
tipo: projeto
area: 30_Projetos
projeto: PRIMUS
status: ativo
aliases: [PrimusOS, PRIMUS]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, primusos, rpg, narrativa, continuidade, eip]
---

# PRIMUS

## Funcao

PRIMUS e o dominio narrativo do FabioOS: um sistema para criar mundos persistentes, missoes, personagens, regras, eventos e consequencias sem perder continuidade.

## Estado Atual

O projeto estava preservado no legado e em arquivos locais de Downloads/Desktop. Este lote inicia a reentrada do PRIMUS na estrutura viva do Obsidian.

## Nucleo

- [[40_Wiki/PRIMUS/PrimusOS]]
- [[40_Wiki/PRIMUS/Circuito_EIP]]
- [[40_Wiki/PRIMUS/Taxonomia_PRIMUS]]
- [[Plano_Ingestao_PRIMUS]]
- [[80_Specs/PRIMUS/Spec_Ingestao_PRIMUS_ChatGPT]]

## Circuito Operacional

```text
E - Enciclopedia
  -> I - Instancia jogavel
  -> P - Persistencia / Delta P
  -> E atualizado
```

O sistema nao reseta. Cada missao deve modificar o estado do mundo.

## Camadas do Projeto

| Camada | Funcao | Pasta |
|---|---|---|
| Fonte | preservar docs, exports e evidencias | `05_Raw_Sources/PRIMUS/` |
| Projeto | executar roadmap e missoes | `30_Projetos/PRIMUS/` |
| Wiki | consolidar conceitos e regras | `40_Wiki/PRIMUS/` |
| Spec | planejar ingestao e implementacao | `80_Specs/PRIMUS/` |
| Arquivo | preservar legado sem editar | `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/PRIMUS/` |

## Decisoes

- Usar `PrimusOS` como nome canonico do dominio narrativo dentro do FabioOS.
- Manter `PRIMUS` como nome do projeto/campanha/sistema criativo.
- Nao copiar material de D&D em massa para wiki; usar como referencia licenciada e fonte externa.
- Separar quatro estados: `canon`, `rascunho`, `inspiracao`, `externo`.

## Proxima Acao Executavel

Executar o [[Plano_Ingestao_PRIMUS]] em lotes:

1. consolidar sumario e circuito;
2. extrair contexto completo;
3. mapear entidades/tipos;
4. montar primeira missao controlada;
5. registrar Delta P.

## Relacoes

- [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]]
- [[05_Raw_Sources/PRIMUS/Inventario_Fontes_PRIMUS_2026-06-30]]
- [[90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/PRIMUS/INDEX_PRIMUS]]
