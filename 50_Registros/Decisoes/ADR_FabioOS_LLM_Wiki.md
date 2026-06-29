---
tipo: adr
area: FabioOS
projeto: FabioOS
status: aprovado
tags: [adr, llm-wiki, obsidian, rag, mcp, governanca]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# ADR - FabioOS como LLM Wiki Operacional

## Contexto

O FabioOS cresceu como vault Obsidian, repositorio Git, sistema de agentes, scripts, RAG, MCP, OpenClaw, n8n e multiplos modelos de IA.

Apenas armazenar notas ou recuperar chunks nao basta para sustentar o sistema. O conhecimento precisa acumular, conectar, revisar contradicoes e orientar acao.

## Problema

Sem uma camada LLM Wiki, o FabioOS corre risco de:

- redescobrir conhecimento a cada pergunta;
- criar notas duplicadas;
- deixar respostas importantes morrerem no chat;
- misturar fonte bruta com conhecimento consolidado;
- usar RAG sobre material pouco processado;
- permitir que agentes escrevam sem schema.

## Alternativas consideradas

| Alternativa | Avaliacao |
|---|---|
| Obsidian apenas como cofre de notas | Simples, mas fraco para agentes e acumulacao de conhecimento. |
| RAG diretamente sobre fontes brutas | Util, mas pode recuperar fragmentos sem sintese e sem contexto institucional. |
| Wiki manual mantida pelo usuario | Alta qualidade, mas manutencao cara e pouco escalavel. |
| LLM Wiki mantida por agentes | Melhor equilibrio, desde que tenha governanca, schema, index, log e revisao humana. |

## Decisao

O FabioOS adotara o padrao LLM Wiki como camada central de memoria.

Fontes brutas serao preservadas como evidencia imutavel. A wiki em Markdown sera o conhecimento compilado e mantido por LLMs. Index e log serao usados para navegacao e auditoria. RAG consultara preferencialmente a wiki processada. MCP sera usado para manutencao controlada. MEGATRON coordenara os cerebros especializados. Codex e Claude Code atuarao como mantenedores da codebase cognitiva.

## Consequencias positivas

- conhecimento passa a acumular em vez de ser redescoberto;
- agentes ganham schema de escrita;
- RAG melhora por consultar conhecimento processado;
- Obsidian continua legivel por humanos;
- Git registra a evolucao;
- contradicoes e lacunas podem ser auditadas;
- futuras automacoes ganham trilho seguro.

## Consequencias negativas

- exige disciplina de index/log;
- aumenta a necessidade de revisao periodica;
- pode gerar documentos demais se nao houver piloto;
- exige decisao clara entre atualizar pagina existente ou criar nova;
- pode demandar manutencao de links e frontmatter.

## Riscos

- automatizar ingest antes de validar qualidade;
- criar wiki paralela sem integrar com `wiki/` existente;
- nao diferenciar fonte bruta de sintese;
- deixar MCP sem matriz de permissao;
- usar RAG sem testes de recuperacao.

## Proximos passos

1. Criar schema operacional da wiki.
2. Criar protocolos de ingest, query e lint.
3. Criar `index.md` e `log.md` centrais.
4. Criar RAG/MCP Control Plane.
5. Executar piloto pequeno apenas com autorizacao humana.
6. Revisar governanca operacional antes de automatizar escala.
