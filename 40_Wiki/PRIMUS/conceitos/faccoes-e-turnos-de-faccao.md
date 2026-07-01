---
tipo: conceito
area: 40_Wiki
projeto: PRIMUS
classe_dado: interno
autoria: derivado (conceito de design abstrato; sem texto integral de livro)
fonte_conceitual: sandbox toolkits (Worlds/Stars Without Number — edições free)
criado_em: 2026-07-01
tags: [primus, design, faccoes, sandbox, worldstate, conceito]
---

# Facções e Turnos de Facção

> **Exemplo do Modo Catálogo aplicado a livro (ADR Nota vs Dado):** o livro NÃO
> vira mil notas. Só o **conceito forte, reutilizável e ligável** vira nó. Aqui está
> uma IDEIA de design (abstrata), não conteúdo protegido copiado.

## O conceito

Uma **facção** é um agente coletivo do mundo (guilda, culto, reino, cartel) com
**objetivos, recursos e influência**. Num **turno de facção**, cada facção **age
para avançar seus objetivos** — mesmo sem o jogador presente. O mundo, assim, **se
move sozinho**: alianças, conflitos e mudanças emergem da interação das facções ao
longo do tempo.

## Por que é forte (e não um stub)

- **É pensável e ligável:** conecta-se ao motor que o Codex já construiu.
- **É abstrato/autoral-adaptável:** a mecânica-ideia (agentes que agem por turno),
  não a tabela específica de um livro protegido.
- **É reutilizável:** vale para qualquer mundo, não só D&D.

## Relações no grafo (PRIMUS)

- Alimenta o **[[WorldState_0001_PRIMUS]]** — as facções são parte do estado do mundo.
- É um motor de **[[Spec_Tension_Engine_PRIMUS|tensões]]**: objetivos de facção que
  se chocam geram as tensões que viram conflitos.
- Liga-se ao **[[Spec_DeltaP|ΔP]]**: cada turno de facção é uma variação válida do mundo.
- Fornece **conflitos candidatos** para a **[[Spec_Cantina_Conflict_Engine_PRIMUS|Cantina]]**.

## Onde o DADO vive (não vira nota)

Estatísticas, listas de facções de um livro específico, tabelas → **catálogo/índice
consultável (PRIMUS Index)**, não o grafo. O grafo fica só com o **conceito**.

## Uso no PRIMUS
Definir 3-5 facções iniciais com objetivo + recurso; rodar 1 turno de facção por
ciclo de mundo; registrar as variações no DeltaPLog.
