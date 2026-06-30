---
tipo: relatorio
area: 60_Sistemas
projeto: FabioOS
fase: 13
status: auditoria-local
tags: [fabios, grafo, auditoria, fase-13]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Auditoria Local do Grafo FabioOS

## Funcao

Registrar metricas de consistencia e cobertura do grafo minimo da Fase 13.

## Resumo

| Metrica | Valor |
|---|---|
| Nos | 840 |
| Arestas | 2680 |
| Arestas orfas | 0 |
| Nos isolados | 0 |
| Conceitos referenciados sem arquivo | 291 |
| Nos conectados | 100.0% |

## Nos por tipo

| Tipo | Quantidade |
|---|---|
| Conceito | 330 |
| Decisao | 4 |
| Dominio | 11 |
| Log | 14 |
| Nota | 42 |
| Projeto | 19 |
| Sistema | 98 |
| Tag | 322 |

## Nos por dominio

| Dominio | Quantidade |
|---|---|
| FabioOS | 739 |
| PietraOS | 21 |
| PrimusOS | 80 |

## Arestas por tipo

| Relacao | Quantidade |
|---|---|
| classifica | 800 |
| documenta | 83 |
| pertence_a | 467 |
| referencia | 1330 |

## Top hubs

| No | Tipo | Grau | Entrada | Saida |
|---|---|---|---|---|
| Dominio:FabioOS | Dominio | 162 | 162 | 0 |
| Projeto:FabioOS | Projeto | 103 | 103 | 0 |
| Dominio:60_Sistemas | Dominio | 83 | 83 | 0 |
| 90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Mapa_Mestre_Fabio | Nota | 70 | 5 | 65 |
| wiki/indices/mapa-fabios | Conceito | 68 | 22 | 46 |
| 90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Mapa_de_TraderOS | Nota | 58 | 4 | 54 |
| 90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/INDEX | Nota | 56 | 1 | 55 |
| 90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Mapa_de_Escola | Nota | 54 | 4 | 50 |
| 90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/30_Conhecimento/Obsidian | Sistema | 53 | 34 | 19 |
| 90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Mapa_de_Filosofia | Nota | 46 | 4 | 42 |
| 90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/Fabio0S | Projeto | 46 | 19 | 27 |
| 90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/Trader | Projeto | 45 | 16 | 29 |
| 90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Mapa_de_Geografia | Nota | 43 | 4 | 39 |
| 00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON | Nota | 42 | 18 | 24 |
| 60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS | Sistema | 42 | 26 | 16 |

## Diagnostico

- Aprovado: nenhuma aresta orfa encontrada.
- Aprovado: nenhum no isolado encontrado.
- Conceitos referenciados sem arquivo: 291.
- Esta auditoria nao usa RAG, API externa, Neo4j ou Git.

## Proximas acoes

- [ ] Revisar conceitos referenciados sem arquivo e decidir quais devem virar notas wiki.
- [ ] Revisar top hubs para detectar mapas excessivamente centrais.
- [ ] Definir relacoes novas apenas quando houver fonte explicita.
