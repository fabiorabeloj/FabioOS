---
tipo: sistema
area: tecnologia
status: planejamento
tags: [tecnico, IA, grafo]
criado_em: 2026-06-25
atualizado_em: 2026-06-25
---

# Grafos de Conhecimento

## O que é?

Grafo de conhecimento é uma estrutura que representa conceitos (nós) e suas relações (arestas). Diferente de listas lineares, grafos capturam complexidade e interconexões entre ideias.

## Para que serve?

- Mapear conexões conceituais no [[30_Conhecimento|repertório]]
- Suportar descoberta de conhecimento relacionado
- Integrar com [[RAG]] para contexto relacional
- Visualizar estrutura do FabioOS
- Alimentar recomendações e análise

## Onde entra no FabioOS?

[[60_Sistemas|Sistemas]] > [[Grafos_de_Conhecimento]] → análise:
- Descoberta de conceitos relacionados
- Mapas visuais em [[10_Mapas|dashboards]]
- Análise de lacunas de conhecimento
- Sugestão de próximas notas a criar

## Como usar?

1. **Extrair conceitos**: Identificar nós em notas MD
2. **Definir relações**: Links, tags, referências cruzadas
3. **Construir grafo**: Estrutura relacional
4. **Consultar**: Pathfinding, centralidade, comunidades

## Exemplo de relações no FabioOS

```
IA ← Automação → n8n ← GitHub
 ↓
RAG ← Banco_Vetorial ← Claude_Code
 ↓
30_Conhecimento (contém IA, Automação, Tecnologia)
 ↓
20_Projetos (usam IA, Automação)
```

## Tecnologias recomendadas

| Ferramenta | Tipo | Uso |
|-----------|------|-----|
| Neo4j | Grafo nativo | Consultas complexas |
| NetworkX | Python lib | Análise offline |
| Graphviz | Visualização | Diagramas |
| Obsidian Graph | Built-in | Vis. exploratória |

## Relações

- ↔ [[RAG]] — complementar
- ↔ [[Banco_Vetorial]] — alternativa
- ↔ [[Obsidian]] — plugins de grafo
- ↔ [[INDEX]] — estrutura base

## Próximas ações

- [ ] Mapear estrutura atual como grafo
- [ ] Implementar extração de relações
- [ ] Conectar com [[Obsidian]] graph view
- [ ] Criar algoritmos de recomendação
- [ ] Visualizar em [[Dashboard]]
