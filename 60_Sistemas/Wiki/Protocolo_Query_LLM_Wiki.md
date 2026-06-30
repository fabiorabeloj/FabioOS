---
tipo: protocolo
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [llm-wiki, query, rag, obsidian, recuperacao]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Protocolo de Query - LLM Wiki FabioOS

## Funcao

Definir como responder perguntas usando a memoria persistente do FabioOS.

## Regra central

Pergunta importante deve consultar memoria antes de virar resposta definitiva.

## Fluxo

```text
pergunta
-> classificar dominio
-> consultar 10_Dashboard/_entrada/index.md
-> consultar paginas relevantes
-> usar RAG se busca textual nao bastar
-> sintetizar resposta
-> citar fontes internas
-> registrar conhecimento novo quando aplicavel
```

## Quando ler index

Ler `10_Dashboard/_entrada/index.md` antes de:

- criar pagina nova;
- responder pergunta arquitetural;
- escolher protocolo;
- mexer em governanca;
- acionar RAG/MCP;
- retomar contexto apos pausa.

## Quando usar RAG

Usar RAG quando:

- a pergunta exigir busca semantica;
- houver muitos documentos possiveis;
- a resposta depender de historico;
- houver risco de esquecer decisoes antigas;
- a busca textual nao localizar a pagina correta.

## Quando registrar resposta

Registrar resposta como nota, decisao, comparacao, tarefa, Skill ou Spec quando:

- a resposta muda arquitetura;
- define criterio;
- cria regra;
- compara ferramentas;
- revela lacuna;
- sera reutilizada;
- precisa ser citada no futuro.

## Fontes internas

Respostas devem apontar para:

- paginas wiki;
- decisoes;
- specs;
- skills;
- protocolos;
- STATUS/NEXT_ACTIONS;
- changelog quando relevante.

## Lacunas

Se a memoria nao contem resposta suficiente, registrar:

- pergunta;
- area;
- documento esperado;
- fonte possivel;
- prioridade;
- proxima acao.

## Limites

- Nao inventar estado operacional.
- Nao assumir ferramenta ativa sem verificar.
- Nao chamar API externa sem aprovacao ou regra definida.
- Nao confundir plano futuro com componente ativo.
