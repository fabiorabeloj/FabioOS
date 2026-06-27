---
tipo: sistema
area: 60_Sistemas
projeto: FabioOS
fase: 13
status: minimo-funcional
tags: [fabios, grafo, fase-13, ontologia, obsidian]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Grafo de Conhecimento do FabioOS

## Funcao

Implementar a Fase 13 do FabioOS em uma versao minima, local e segura.

O grafo representa relacoes entre notas, sistemas, projetos, conceitos,
tags e dominios do vault. Ele nao substitui o RAG. O RAG recupera por
significado; o grafo mostra relacoes explicitas e navegaveis.

## Contexto

A Fase 12 criou a memoria semantica local. A Fase 13 adiciona uma camada
relacional sobre o proprio Obsidian, usando:

- wikilinks;
- frontmatter;
- estrutura de pastas;
- tags;
- dominio inferido pelo caminho.

Esta fase nao depende de Neo4j para comecar. O primeiro artefato e um JSON
local versionavel, que pode alimentar Neo4j, visualizacoes, MCPs ou dashboards
no futuro.

## Escopo minimo

1. Ler arquivos Markdown curados do vault.
2. Excluir entradas brutas, caches, banco RAG, logs runtime e configuracoes
   sensiveis.
3. Criar nos para notas, sistemas, projetos, tags, dominios e conceitos.
4. Criar arestas para:
   - `referencia`;
   - `pertence_a`;
   - `classifica`;
   - `documenta`;
   - `usa_ferramenta`;
   - `depende_de`.
5. Gerar metricas basicas para validar cobertura.

## Arquivos

- `Ontologia_FabioOS_Grafo.md` - ontologia operacional da Fase 13.
- `scripts/build_graph.py` - construtor local do grafo.
- `scripts/export_graph_csv.py` - exportador CSV para Neo4j/Gephi.
- `scripts/query_graph.py` - consulta local de nos, hubs e vizinhancas.
- `scripts/audit_graph.py` - auditoria de consistencia e cobertura.
- `data/grafo_fabioos.json` - saida gerada pelo construtor.
- `data/neo4j_nodes.csv` - nos em formato de importacao Neo4j.
- `data/neo4j_edges.csv` - relacoes em formato de importacao Neo4j.
- `data/gephi_edges.csv` - relacoes em formato simples para Gephi.

## Como usar

```powershell
python 60_Sistemas/Grafo/scripts/build_graph.py
```

O script nao faz chamadas externas, nao usa API, nao reindexa RAG e nao altera
arquivos fora de `60_Sistemas/Grafo/data/`.

Para exportar o grafo para CSV:

```powershell
python 60_Sistemas/Grafo/scripts/export_graph_csv.py
```

Saidas geradas:

- `data/neo4j_nodes.csv`
- `data/neo4j_edges.csv`
- `data/gephi_edges.csv`

Para consultar o grafo localmente:

```powershell
python 60_Sistemas/Grafo/scripts/query_graph.py --search RAG
python 60_Sistemas/Grafo/scripts/query_graph.py --top 10
python 60_Sistemas/Grafo/scripts/query_graph.py --node "60_Sistemas/RAG/Arquitetura_RAG_FabioOS"
```

Para auditar consistencia e cobertura:

```powershell
python 60_Sistemas/Grafo/scripts/audit_graph.py
```

Saidas:

- `data/auditoria_grafo.md`
- `data/auditoria_grafo.json`

## Politica de versionamento dos dados

Os arquivos gerados em `data/*.json` e `data/*.csv` sao regeneraveis e nao
devem ser versionados por padrao. A pasta `data/` mantem apenas:

- `.gitignore` - regra local dos artefatos gerados;
- `auditoria_grafo.md` - evidencia leve da ultima auditoria.

Para recriar os artefatos locais, rode:

```powershell
python 60_Sistemas/Grafo/scripts/build_graph.py
python 60_Sistemas/Grafo/scripts/export_graph_csv.py
python 60_Sistemas/Grafo/scripts/audit_graph.py
```

## Criterio de aceite

A Fase 13 minima e considerada funcional quando:

- o grafo e gerado sem erro;
- existem nos para projetos, sistemas, conceitos e notas;
- existem arestas `referencia` entre wikilinks;
- existem arestas `pertence_a` ligando notas aos dominios/pastas;
- o arquivo `data/grafo_fabioos.json` pode ser aberto e inspecionado.
- os CSVs de exportacao mantem a mesma contagem de nos e arestas do JSON.

## Limites

- Nao extrai entidades por LLM.
- Nao grava em Neo4j.
- Nao infere relacoes ambiciosas sem fonte explicita.
- Nao usa conteudo bruto de `00_Inbox/` ou `sources/_inbox/`.
- Nao toca no banco vetorial da Fase 12.

## Proximas acoes

- [ ] Validar visualmente as principais conexoes.
- [x] Definir exportacao opcional para CSV/Neo4j.
- [x] Criar consulta local basica do grafo.
- [x] Criar auditoria local de consistencia.
- [ ] Adicionar relacoes extraidas de frontmatter padronizado.
- [ ] Conectar o grafo ao futuro MCP FabioOS.
