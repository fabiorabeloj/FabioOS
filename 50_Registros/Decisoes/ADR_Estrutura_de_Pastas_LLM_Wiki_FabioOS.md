---
tipo: adr
area: 50_Registros/Decisoes
projeto: FabioOS
status: aceito
tags: [fabios, adr, llm-wiki, obsidian, estrutura]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# ADR - Estrutura de Pastas LLM Wiki do FabioOS

## Contexto

O FabioOS cresceu rapidamente com Obsidian, GitHub, RAG, MCP, MEGATRON, agentes, Cursor, OpenClaw, n8n, fontes, wiki, registros e protocolos.

Com isso, surgiram pastas com funcoes sobrepostas:

- `10_Mapas/` e `10_Dashboard/`;
- `20_Projetos/` e `30_Projetos/`;
- `30_Conhecimento/`, `40_Repertorio/`, `wiki/` e `40_Wiki/`;
- `40_Decisoes/` e `50_Registros/Decisoes/`;
- `50_Fontes/`, `sources/` e `05_Raw_Sources/`.

## Problema

Sem estrutura fisica clara, cada agente pode criar arquivos em lugares diferentes, duplicar conhecimento e quebrar a continuidade.

## Alternativas consideradas

### 1. Manter estrutura atual sem alteracao

Vantagem: menor risco imediato.

Desvantagem: perpetua duplicacao e confusao visual no Obsidian.

### 2. Organizar por IA ou ferramenta

Exemplo: `ChatGPT/`, `Claude/`, `Codex/`, `Cursor/`.

Vantagem: facil saber quem produziu.

Desvantagem: errado para LLM Wiki. IAs sao operadores, nao categorias de conhecimento.

### 3. Organizar apenas por area

Exemplo: Escola, Trader, Vida, IA.

Vantagem: intuitivo para uso humano.

Desvantagem: mistura fonte, wiki, decisao, spec, log e sistema no mesmo lugar.

### 4. Organizar pela mentalidade LLM Wiki

Separar fonte bruta, conhecimento processado, operacao do sistema, skills, specs, registros e arquivo.

Vantagem: melhor para Obsidian, Git, RAG, MCP, MEGATRON e agentes.

Desvantagem: exige periodo de transicao e compatibilidade com `sources/` e `wiki/`.

## Decisao

Adotar a estrutura fisica baseada em LLM Wiki:

```text
00_Inbox/
05_Raw_Sources/
10_Dashboard/
20_Areas/
30_Projetos/
40_Wiki/
50_Registros/
60_Sistemas/
70_Skills/
80_Specs/
90_Arquivo/
```

Manter `sources/` e `wiki/` como caminhos operacionais de compatibilidade ate migracao planejada.

## Consequencias positivas

- estrutura aparece visualmente no Obsidian;
- reduz ambiguidade de destino;
- melhora governanca de agentes;
- prepara MEGATRON para classificar entradas;
- prepara migracao futura de RAG/MCP;
- facilita commits tematicos.

## Consequencias negativas

- coexistirao `sources/` e `05_Raw_Sources/` por um periodo;
- coexistirao `wiki/` e `40_Wiki/` por um periodo;
- agentes precisam consultar o mapa antes de escrever;
- migracao completa exigira revisao de backlinks.

## Riscos

- duplicacao se novos arquivos forem salvos no alias errado;
- quebra de scripts se caminhos antigos forem removidos;
- reindexacao RAG prematura;
- commit acidental de fontes sensiveis.

## Proximos passos

1. Commitar estrutura fisica v1.
2. Revisar com Claude/Fabio.
3. Migrar um lote piloto pequeno.
4. Atualizar scripts para aceitar aliases.
5. Decidir se `sources/` e `wiki/` ficam como aliases permanentes.
