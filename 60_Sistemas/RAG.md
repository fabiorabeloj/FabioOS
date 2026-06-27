---
tipo: sistema
area: tecnologia
projeto: FabioOS
status: ativo
tags: [tecnico, IA, retrieval]
criado_em: 2026-06-25
atualizado_em: 2026-06-27
---

# RAG — Retrieval-Augmented Generation

## O que é?

RAG (Retrieval-Augmented Generation) é um padrão de arquitetura que combina recuperação de documentos com geração de linguagem natural. Em vez de confiar apenas no conhecimento treinado do modelo, RAG busca informações relevantes em uma base de conhecimento antes de gerar a resposta.

## Para que serve?

- Respostas baseadas em contexto específico
- Redução de alucinações em LLMs
- Consultas sobre base de conhecimento do FabioOS
- Integração com [[Banco_Vetorial]]
- Automações com [[Claude Code]] e [[OpenRouter]]

## Onde entra no FabioOS?

[[60_Sistemas|Sistemas]] > [[RAG]] → usado em:
- Processamento de novas notas via [[integracao-n8n-github-obsidian]]
- Consultas sobre [[30_Conhecimento|repertório]]
- Respostas contextualizadas via Claude

## Como usar?

1. **Indexação**: Novos arquivos em [[Obsidian]] são capturados via [[n8n]]
2. **Embedding**: Texto é convertido em vetores via [[Banco_Vetorial]]
3. **Recuperação**: Busca semântica retorna documentos relevantes
4. **Geração**: Claude gera resposta com contexto recuperado

## Relações

- ↔ [[Banco_Vetorial]] — armazena embeddings
- ↔ [[Grafos_de_Conhecimento]] — conecta conceitos
- ↔ [[Claude Code]] — executa queries
- ↔ [[n8n]] — automatiza pipeline
- ↔ [[MCP]] — protocolo de contexto

## Próximas ações

- [ ] Documentar pipeline RAG completo
- [ ] Definir estratégia de embedding (OpenAI, local)
- [ ] Implementar busca semântica em Obsidian
- [ ] Integrar com dashboard de conhecimento
- [ ] Testar com questões sobre FabioOS
