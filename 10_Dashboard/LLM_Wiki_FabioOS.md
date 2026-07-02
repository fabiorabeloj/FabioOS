---
tipo: dashboard
area: FabioOS
projeto: FabioOS
status: ativo
tags: [llm-wiki, dashboard, obsidian, rag, mcp]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Dashboard LLM Wiki FabioOS

## Documentos centrais

- [[30_Projetos/FabioOS/LLM_Wiki_FabioOS]]
- [[50_Registros/Decisoes/ADR_FabioOS_LLM_Wiki]]
- [[60_Sistemas/Wiki/Schema_Wiki_FabioOS]]
- [[60_Sistemas/Wiki/Protocolo_Ingest_LLM_Wiki]]
- [[60_Sistemas/Wiki/Protocolo_Query_LLM_Wiki]]
- [[60_Sistemas/Wiki/Protocolo_Lint_LLM_Wiki]]
- [[10_Dashboard/RAG_MCP_Control_Plane]]

## Entradas existentes reaproveitadas

- [[40_Wiki/LLM_Wiki/LLM_Wiki_Pattern]]
- [[60_Sistemas/Claude_Code/project_llmwiki_architecture]]
- [[60_Sistemas/Wiki/schema/fluxo-wiki]]
- [[60_Sistemas/Wiki/schema/qualidade-wiki]]
- [[40_Wiki/_compat_wiki/README]]
- [[40_Wiki/_compat_wiki/indices/mapa-fabios]]

## Arquivos operacionais

- [[10_Dashboard/_entrada/index]]
- [[50_Registros/Logs_Agentes/log]]
- [[60_Sistemas/FabioOS/STATUS]]
- [[60_Sistemas/FabioOS/NEXT_ACTIONS]]
- [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]]

## Relacoes

- MEGATRON: [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]], [[60_Sistemas/MEGATRON/v0/README_MEGATRON_v0]]
- RAG: [[60_Sistemas/RAG/Arquitetura_RAG_FabioOS]], [[40_Wiki/_compat_wiki/conceitos/rag]]
- MCP: [[60_Sistemas/MCP/Inventario_MCP]], [[40_Wiki/_compat_wiki/conceitos/mcp]]
- Skills: [[60_Sistemas/Skills/Inventario_Skills]]
- Agentes: [[60_Sistemas/MEGATRON/agentes/README_Agentes]]
- Aptidao de IAs: [[40_Wiki/Modelos_e_IAs/Matriz_de_Aptidao_das_IAs_FabioOS]]

## Status

| Item | Estado |
|---|---|
| Decisao LLM Wiki | formalizada |
| Schema | criado |
| Ingest | protocolo criado |
| Query | protocolo criado |
| Lint | protocolo criado |
| Index/log | criados |
| RAG/MCP Control Plane | criado |
| Piloto | executado em FabioOS/Governanca |

## Piloto recomendado

Area: FabioOS / Governanca.

Motivo:

- baixo risco operacional;
- fontes ja estao no vault;
- testa atualizacao de pagina existente;
- conecta LLM Wiki, RAG/MCP e matriz de aptidao;
- nao exige API externa, n8n, OpenClaw ou reindexacao.

## Criterio de sucesso do piloto

- uma fonte preservada;
- uma pagina existente atualizada;
- no maximo uma pagina nova criada;
- `10_Dashboard/_entrada/index.md` atualizado;
- `50_Registros/Logs_Agentes/log.md` atualizado;
- lacuna ou contradicao registrada;
- changelog atualizado;
- sem commit sem aprovacao.

## Piloto executado

| Item | Resultado |
|---|---|
| Fonte | [[05_Raw_Sources/_compat_sources/fabios/2026-06-29_governanca-operacional-pontos-cegos]] |
| Pagina criada | [[40_Wiki/_compat_wiki/conceitos/governanca-operacional-fabios]] |
| Pagina existente atualizada | [[30_Projetos/FabioOS/LLM_Wiki_FabioOS]] |
| Index/log | atualizados |
| API externa | nao usada |
| RAG reindex | nao executado |
| Commit/push | nao executado |
