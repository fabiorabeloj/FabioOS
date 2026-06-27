---
tipo: wiki
area: wiki
projeto: FabioOS
status: ativo
tags: [conceito, rag, recuperacao-semantica, memoria, fase-12]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# RAG — Recuperação Aumentada por Geração

## Função

RAG (*Retrieval-Augmented Generation*) é a camada de **memória semântica** do FabioOS: recupera trechos relevantes do vault por **significado** (não por palavra-chave) e os entrega como contexto para uma resposta fundamentada e rastreável.

## Contexto

No [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON|Modelo Formal]], RAG é uma **camada auxiliar da memória**, não um fim. Ele **consulta** o conhecimento organizado no Obsidian — não o substitui. É o primeiro tijolo cognitivo que o MEGATRON consome.

```
pergunta → embedding local → busca top-k no banco vetorial → contexto → resposta com fontes
```

## Como usar

- **Arquitetura e decisões da implementação:** [[60_Sistemas/RAG/Arquitetura_RAG_FabioOS]] (Chroma + `bge-m3` local + Claude).
- **Banco vetorial subjacente:** [[wiki/conceitos/banco-vetorial]].
- **Regra de qualidade:** se não houver fonte suficiente, o sistema declara ignorância (Regra da Ignorância Explícita) em vez de alucinar.
- **Privacidade:** embeddings rodam localmente; dados sensíveis (`sources/_inbox/`, logs Pietra) são excluídos do índice.

## Relações

- [[60_Sistemas/RAG/Arquitetura_RAG_FabioOS]]
- [[wiki/conceitos/banco-vetorial]]
- [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]]
- [[60_Sistemas/MEGATRON/agentes/specs/Agente_RAG]]

## Próximas ações

- [ ] Concluir a validação da Fase 12 (consultas em modo recuperação)
- [ ] Conectar o RAG ao grafo (Fase 13) e ao MEGATRON
