---
tipo: adr
area: 50_Registros
projeto: FabioOS
status: aceito
autor: Claude (arquiteto-chefe)
criado_em: 2026-07-01
atualizado_em: 2026-07-01
tags: [adr, obsidian, ingestao, grafo, wikilinks, governanca, nota-vs-dado, apostilas, primus]
---

# ADR 2026-07-01 — Nota vs Dado: como qualquer fonte entra no Obsidian (LEI)

## Contexto

O Fabio esperava, ao ingerir livros, "MDs de todas as armas, itens e ideias". A
execução literal gerou **10.603 stubs** (PHB/DMG/MM) — provando que é possível,
mas que **destrói o Obsidian**: milhares de "bolinhas soltas" sem wikilinks, grafo
virando hairball, dado bruto confundido com conhecimento. O Codex corrigiu a rota
([[50_Registros/Decisoes/ADR_2026-07-01_Catalogo_DND_Core_Sem_Stubs_Massivos]]) e
está **certo**. Esta ADR **ratifica** aquela e a **eleva a regra universal do
FabioOS** — vale para qualquer fonte, não só D&D — e define o modo das apostilas.

## Decisão (a LEI)

### 1. Princípio "Nota vs Dado"

> **Uma nota no Obsidian existe para ser PENSADA e LIGADA (wikilinks). Dado em
> massa vai para índice/catálogo consultável, NUNCA para o grafo.**

Ter referência ≠ ter conhecimento. Um catálogo em Markdown de milhares de linhas
não é um "segundo cérebro" — é um banco de dados pior que um banco de dados.

### 2. Dois modos de ingestão (decididos pela FONTE)

| Fonte | Modo | O que vira |
|---|---|---|
| **Livro oficial / restrito / referência em massa** (D&D, WWN…) | **CATÁLOGO** | fonte restrita + **índice seguro** (âncora/página, sem texto integral) + **1 catálogo consolidado** + dados em SQLite/JSONL. **Só vira nota** o nó com valor semântico: conceito, facção, lugar, procedimento, missão, ou item/criatura **efetivamente usado** (CatalogPool/missão). Promoção seletiva após V(E). |
| **Apostila autoral do Fabio / material docente** (Geo, Fil) | **CONHECIMENTO** | **nota completa por tópico + mapa de conceitos + aula + revisão + banco de questões + gabarito**, wikilinkado no MOC da matéria. **É AQUI que o Obsidian cresce de verdade.** |

### 3. O teste (gate antes de criar qualquer nota)

> "Isso vai ser **pensado e ligado** a outras ideias — ou é **uma linha de dado**?"
> Ideia → nota (com wikilinks). Dado → índice/catálogo. Na dúvida, não cria nó.

## Resposta direta ao Fabio

- **Livro oficial cresce o Obsidian pouco e seletivamente** (catálogo + poucos nós
  fortes) — e por copyright nem poderia virar dump. Os dois limites (grafo saudável
  + direito autoral) apontam para o mesmo lugar.
- **Sua apostila cresce o Obsidian MUITO.** Ela é sua IP, de alto valor e do seu
  domínio: vira conhecimento completo, conectado, reutilizável em aula/prova/revisão.
  **Mande uma apostila e o vault ganha de verdade.**

## Consequências

- Grafo permanece semântico e navegável; wikilinks mantêm valor.
- Copyright respeitado (o Modo Catálogo já é copyright-safe).
- PRIMUS continua consultando o acervo inteiro pelo índice/SQLite.
- O crescimento real do vault vem das **apostilas autorais**, não de dumps.
- Stubs massivos ficam **banidos de `40_Wiki`** (podem existir como artefato técnico
  temporário fora do grafo, se preciso).

## Aplicação

- Ratifica a remoção de `40_Wiki/PRIMUS/Fontes_Oficiais_DND/Stubs/` e o
  `Catalogo_DND_Core_Consolidado` como padrão.
- Apostilas seguem o **Modo Conhecimento** (Spec_Ingestao_Apostilas_EscolaOS).
- Vale para toda ingestão futura (PDF pipeline, Crawl4AI, Drive): aplicar o teste.

## Relações
- [[50_Registros/Decisoes/ADR_2026-07-01_Catalogo_DND_Core_Sem_Stubs_Massivos]]
- [[80_Specs/EscolaOS/Spec_Ingestao_Apostilas_EscolaOS]]
- [[80_Specs/PRIMUS/Spec_Markdownizacao_Segura_Livros_PRIMUS]]
- [[60_Sistemas/FabioOS/specs/2026-06-30_pipeline-pdf-aprende]]
