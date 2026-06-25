---
tipo: sistema
area: tecnologia
status: planejamento
tags: [tecnico, IA, database]
criado_em: 2026-06-25
atualizado_em: 2026-06-25
---

# Banco Vetorial

## O que é?

Um banco de dados especializado em armazenar e buscar vetores (embeddings). Diferente de bancos relacionais, bancos vetoriais otimizam buscas semânticas por similaridade em espaços de alta dimensão.

## Para que serve?

- Armazenar embeddings de documentos do FabioOS
- Buscas semânticas em [[30_Conhecimento|base de conhecimento]]
- Suportar [[RAG]] e consultas contextualizadas
- Integrar com [[Grafos_de_Conhecimento]]
- Alimentar [[Claude Code]] e [[OpenRouter]] com contexto

## Onde entra no FabioOS?

[[60_Sistemas|Sistemas]] > [[Banco_Vetorial]] → usado em:
- Pipeline de ingestão [[integracao-n8n-github-obsidian]]
- Consultas inteligentes sobre repertório
- Automações com n8n e Claude

## Como usar?

1. **Inserção**: Documentos MD são embedados e inseridos
2. **Busca**: Queries são vectorizadas e comparadas
3. **Recuperação**: Top-K resultados mais similares
4. **Contexto**: Enviado para Claude processar

## Opções de banco vetorial

| Sistema | Custo | Escalabilidade | Facilidade |
|---------|-------|-----------------|-----------|
| Pinecone | Pago | Alta | Alta |
| Weaviate | Open-source | Alta | Média |
| Chroma | Open-source | Média | Alta |
| Milvus | Open-source | Alta | Média |
| Qdrant | Open-source/Pago | Alta | Média |

## Relações

- ↔ [[RAG]] — consumidor principal
- ↔ [[Grafos_de_Conhecimento]] — complementar
- ↔ [[n8n]] — pipeline de ingestão
- ↔ [[Claude Code]] — cliente de queries

## Próximas ações

- [ ] Escolher banco vetorial (recomendação: Chroma ou Qdrant)
- [ ] Configurar ingestão automática via n8n
- [ ] Documentar estratégia de embedding
- [ ] Criar scripts de sincronização
- [ ] Testar performance com base atual
