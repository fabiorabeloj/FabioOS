---
tipo: arquitetura
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [memoria, obsidian, rag, grafo, dados, governanca]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Separacao de Memorias FabioOS

## Funcao

Definir o que deve ir para cada camada de memoria.

## Camadas

| Memoria | Papel | Nao deve conter |
|---|---|---|
| Obsidian/Markdown | conhecimento humano, decisoes, fontes, wiki | credenciais, dumps sensiveis |
| GitHub | versionamento e backup | tokens, `.env`, dados criticos |
| RAG | recuperacao semantica com fontes | logs brutos sensiveis, credenciais |
| Grafo | relacoes entre entidades | detalhes sensiveis sem anonimizar |
| PostgreSQL/Supabase futuro | dados estruturados, tarefas, estados, custos | segredo em texto claro |
| MongoDB/JSONL futuro | logs flexiveis e memoria operacional | decisao importante sem resumo em Markdown |
| Changelog/log | historico auditavel | segredo ou dado restrito bruto |

## Regras

- Decisoes importantes nao ficam apenas em banco.
- Conversas longas devem virar resumo operacional.
- Logs extensos nao precisam virar nota permanente integral.
- Dados restritos devem ser resumidos/anonimizados antes de RAG/Grafo.
- Credenciais ficam fora do vault.

## Relacao com LLM Wiki

Raw sources preservam evidencia.
Wiki compila conhecimento.
RAG recupera.
MCP aciona.
MEGATRON coordena.

## Relacoes

- [[30_Projetos/FabioOS/LLM_Wiki_FabioOS]]
- [[10_Dashboard/RAG_MCP_Control_Plane]]
- [[60_Sistemas/FabioOS/Matriz_Dominios_Dados_Permissoes_2026-06-28]]
