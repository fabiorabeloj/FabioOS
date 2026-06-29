---
tipo: arquitetura
area: FabioOS
projeto: FabioOS
status: aprovado
tags: [llm-wiki, obsidian, rag, mcp, megatron, governanca]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# LLM Wiki FabioOS

## Tese central

O FabioOS adota a mentalidade **LLM Wiki Operacional**.

Isso significa que o sistema nao deve apenas guardar notas, nem apenas recuperar chunks por RAG. O conhecimento relevante deve ser progressivamente compilado, sintetizado, conectado, revisado e mantido em Markdown por agentes, sob governanca do MEGATRON.

Formula operacional:

```text
raw sources imutaveis
-> wiki markdown compilada
-> schema de manutencao
-> index e log
-> RAG sobre conhecimento organizado
-> MCP para acao controlada
-> MEGATRON como orquestrador
```

## Diferenca entre RAG tradicional e LLM Wiki

RAG tradicional busca fragmentos de documentos no momento da pergunta. Ele e util, mas redescobre o conhecimento a cada consulta.

LLM Wiki compila conhecimento antes da consulta. Ela cria paginas, atualiza paginas existentes, registra contradicoes, conecta conceitos e mantem uma sintese acumulada.

No FabioOS:

- RAG responde: "o que o sistema recupera agora?"
- LLM Wiki responde: "o que o sistema ja estruturou e manteve ao longo do tempo?"

## Camadas

### Raw sources

Fontes brutas sao evidencias. Devem ser preservadas em `sources/`, `50_Fontes/`, `00_Inbox/` ou pasta equivalente, sem edicao destrutiva.

Exemplos:

- PDFs;
- prints;
- emails;
- transcricoes;
- cursos;
- repositorios;
- documentos;
- conversas;
- demonstracoes;
- materiais escolares;
- materiais do TraderOS;
- materiais do PRIMUS.

Regra: fonte bruta e evidencia, nao conhecimento final.

### Wiki

A wiki e a camada processada. No FabioOS, a pasta `wiki/` ja existe e deve ser fortalecida como base de conhecimento compilado.

Ela contem:

- conceitos;
- entidades;
- sistemas;
- projetos;
- sinteses;
- indices;
- decisoes importantes;
- relacoes entre ferramentas;
- aplicacoes no FabioOS.

Regra: a wiki nao copia fonte; ela transforma fonte em conhecimento operacional.

### Schema

O schema define como agentes mantem a wiki.

Documentos existentes reaproveitados:

- [[schema/fluxo-wiki]]
- [[schema/qualidade-wiki]]
- [[60_Sistemas/Claude_Code/project_llmwiki_architecture]]

Documento operacional novo:

- [[60_Sistemas/Wiki/Schema_Wiki_FabioOS]]

## Operacoes oficiais

### Ingest

Ingest incorpora uma fonte nova ao sistema.

Fluxo:

```text
fonte bruta
-> leitura
-> resumo
-> conceitos
-> entidades
-> comparacao com wiki existente
-> atualizacao de paginas existentes
-> criacao de pagina nova somente se necessario
-> index
-> log
-> proxima acao
```

Protocolo: [[60_Sistemas/Wiki/Protocolo_Ingest_LLM_Wiki]]

### Query

Query responde uma pergunta usando a wiki, o index e, quando necessario, RAG.

Fluxo:

```text
pergunta
-> leitura do index
-> busca de paginas relevantes
-> consulta da wiki
-> RAG se necessario
-> resposta com fontes internas
-> registro se gerar conhecimento novo
```

Protocolo: [[60_Sistemas/Wiki/Protocolo_Query_LLM_Wiki]]

### Lint

Lint revisa a saude da wiki.

Procura:

- notas orfas;
- duplicatas;
- contradicoes;
- paginas obsoletas;
- links quebrados;
- conceitos sem pagina;
- fontes nao processadas;
- decisoes sem consequencia.

Protocolo: [[60_Sistemas/Wiki/Protocolo_Lint_LLM_Wiki]]

## Papel de index.md

O `index.md` na raiz e o mapa semantico minimo para agentes. Ele aponta para os documentos centrais e evita que agentes criem paginas sem procurar equivalentes.

Ele nao substitui `wiki/README.md` nem `wiki/indices/mapa-fabios.md`; ele funciona como entrada compacta para LLMs.

## Papel de log.md

O `log.md` na raiz e cronologico e append-only. Ele registra ingests, queries importantes, lint passes, decisoes de manutencao e reorganizacoes.

Ele nao substitui changelog de engenharia; ele registra a evolucao da wiki.

## Relacao com Obsidian

Obsidian e a IDE cognitiva do FabioOS.

Equivalencia:

```text
Obsidian = IDE
Markdown = codigo do conhecimento
wiki/ = codebase cognitiva
GitHub -> historico
LLM = mantenedor
MEGATRON = orquestrador
RAG = busca inteligente
MCP = acao controlada
```

## Relacao com MEGATRON

MEGATRON decide:

- qual cerebro consultar;
- quando usar RAG;
- quando usar MCP;
- quando uma resposta deve virar nota;
- quando uma fonte deve virar ingest;
- quando acionar lint;
- quando pedir aprovacao humana;
- quando registrar decisao ou tarefa.

MEGATRON nao deve fazer tudo. Ele deve coordenar.

## Relacao com multiplos cerebros

Cada cerebro especializado consome e produz conhecimento na wiki:

| Cerebro | Uso da LLM Wiki |
|---|---|
| Estrategico | decisoes, roadmaps, trade-offs, STATUS e NEXT_ACTIONS |
| Tecnico | specs, skills, scripts, RAG, MCP e protocolos |
| Escolar | aulas, provas, revisoes, comunicados e criterios pedagogicos |
| TraderOS | regras, diario, risco e metricas |
| PRIMUS | lore, personagens, regras e continuidade |
| Aprendizagem | cursos, PDFs, videos, fontes e repertorio |
| Governanca | permissoes, seguranca, auditoria e definicao de concluido |
| Meta | lacunas, duplicacoes, obsolescencia e melhoria do proprio sistema |

## Relacao com RAG

RAG deve consultar preferencialmente conhecimento processado:

```text
raw sources = evidencia
wiki = conhecimento compilado
RAG = recuperacao sobre conhecimento organizado
LLM = sintese e raciocinio
```

RAG sobre fonte bruta pode existir, mas nao deve ser o unico modo.

## Relacao com MCP

MCP e a camada de ferramentas acionaveis. Ele pode ler, criar, editar, consultar sistemas e acionar automacoes.

Por isso, MCP exige:

- escopo;
- permissao;
- risco;
- log;
- teste;
- aprovacao humana em acoes externas ou sensiveis.

Painel: [[10_Dashboard/RAG_MCP_Control_Plane]]

## Relacao com Codex e Claude Code

Codex e Claude Code devem operar como mantenedores da codebase cognitiva.

Antes de criar ou alterar notas, devem:

1. ler `CLAUDE.md`;
2. ler `index.md`;
3. ler `log.md`;
4. consultar `wiki/README.md`;
5. consultar o schema aplicavel;
6. procurar pagina existente;
7. atualizar pagina existente quando possivel;
8. criar pagina nova somente quando necessario;
9. atualizar index/log;
10. registrar changelog quando relevante.

## Riscos

| Risco | Mitigacao |
|---|---|
| notas soltas | index, log, schema e lint |
| duplicacao | procurar pagina existente antes de criar |
| contradicao | registrar diferenca e decisao |
| RAG fraco | priorizar wiki compilada |
| MCP perigoso | permissoes, logs e aprovacao |
| excesso de documentos | piloto pequeno antes de escala |

## Criterios de validacao

A LLM Wiki estara validada quando um piloto demonstrar:

- fonte bruta preservada;
- pagina existente atualizada quando houver equivalente;
- pagina nova criada somente quando necessario;
- links internos criados;
- `index.md` atualizado;
- `log.md` atualizado;
- lacuna ou contradicao registrada;
- changelog produzido;
- resultado recuperavel em query posterior.

## Piloto 2026-06-29 - Governanca operacional

O primeiro piloto controlado da LLM Wiki foi executado no dominio FabioOS/Governanca.

Fonte preservada:

- [[sources/fabios/2026-06-29_governanca-operacional-pontos-cegos]]

Pagina wiki criada:

- [[wiki/conceitos/governanca-operacional-fabios]]

Paginas existentes atualizadas:

- [[30_Projetos/FabioOS/LLM_Wiki_FabioOS]]
- [[index]]
- [[log]]
- [[50_Registros/Changelog/CHANGELOG_FabioOS]]

Resultado:

- a fonte foi preservada;
- a pagina wiki distingue fato, interpretacao e decisao;
- o conceito foi conectado a MEGATRON, RAG/MCP, matriz de aptidao, schema e agentes;
- o piloto nao usou API externa, nao reindexou RAG, nao chamou MCP runtime, nao executou automacao e nao fez commit.

Conclusao: o fluxo minimo da LLM Wiki foi validado em escala pequena. A proxima frente deve criar a camada completa de governanca operacional antes de automatizar ingestao em massa.

## Decisao final

O FabioOS adotara LLM Wiki como camada central de memoria operacional, mantida por agentes e governada pelo MEGATRON.

A migracao sera incremental. Nao havera reorganizacao em massa do vault sem piloto, revisao humana e changelog.
