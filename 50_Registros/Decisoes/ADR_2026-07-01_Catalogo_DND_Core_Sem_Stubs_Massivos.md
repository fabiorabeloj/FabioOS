---
tipo: adr
area: 50_Registros
projeto: PRIMUS
status: aceito
classe_dado: interno
criado_em: 2026-07-01
tags: [primus, adr, obsidian, dnd, catalogo, grafo]
---

# ADR - DND Core como Catalogo, nao Stubs Massivos

## Contexto

Foi gerado um lote de `10603` stubs Markdown para PHB, DMG e MM.

A execucao provou que a abordagem e tecnicamente possivel, mas arquiteturalmente ruim para o Obsidian.

## Problema

Criar uma nota para cada registro bruto:

- polui o grafo com milhares de bolinhas fracas;
- reduz o valor dos wikilinks;
- torna a navegacao humana pior;
- mistura catalogo tecnico com conhecimento processado;
- confunde "ter referencia" com "ter conhecimento".

## Decisao

O FabioOS nao deve criar stubs massivos em Markdown para livros oficiais.

Livros oficiais devem entrar como:

1. fonte restrita;
2. indice seguro;
3. catalogo consolidado;
4. dados consultaveis em SQLite/JSONL;
5. notas promovidas manual ou semi-automaticamente apos V(E).

## Consequencias

- O grafo do Obsidian permanece semantico.
- O PRIMUS continua podendo consultar o acervo.
- Notas individuais passam a representar conhecimento util, nao registros brutos.
- Stubs podem existir como artefato tecnico temporario fora do grafo, mas nao em `40_Wiki`.

## Regra

```text
Uma nota no Obsidian precisa ter valor semantico proprio.
Um registro bruto pertence ao catalogo/dado, nao ao grafo.
```

## Aplicacao

Substituir `40_Wiki/PRIMUS/Fontes_Oficiais_DND/Stubs/` por:

- [[40_Wiki/PRIMUS/Fontes_Oficiais_DND/Catalogo_DND_Core_Consolidado]]
- indices seguros existentes;
- promocao seletiva de notas fortes.
