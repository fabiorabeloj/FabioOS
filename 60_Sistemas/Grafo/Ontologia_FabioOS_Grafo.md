---
tipo: ontologia
area: 60_Sistemas
projeto: FabioOS
fase: 13
status: minimo-funcional
tags: [fabios, grafo, ontologia, neo4j, fase-13]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Ontologia Operacional do Grafo FabioOS

## Funcao

Traduzir o Modelo Formal do FabioOS para uma ontologia operacional simples,
pronta para ser representada em JSON agora e em Neo4j no futuro.

## Principio

O grafo registra somente relacoes observaveis no vault ou inferencias
conservadoras a partir de caminhos e metadados.

## Tipos de nos

| Tipo | Fonte principal | Exemplo |
|---|---|---|
| `Nota` | Arquivo Markdown | `wiki/indices/mapa-fabios.md` |
| `Sistema` | `60_Sistemas/` ou frontmatter | `RAG`, `OpenClaw`, `FabioOS` |
| `Projeto` | `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/`, `30_Projetos/` ou frontmatter | `PRIMUS`, `Pietra` |
| `Conceito` | `wiki/conceitos/` ou wikilink conceitual | `RAG`, `Banco Vetorial` |
| `Dominio` | Pasta raiz ou dominio canonico | `FabioOS`, `PietraOS`, `PrimusOS` |
| `Tag` | Frontmatter ou tags Markdown | `rag`, `agentes` |
| `Arquivo` | Artefato nao Markdown futuro | reservado |

## Tipos de relacoes

| Relacao | Quando usar |
|---|---|
| `referencia` | Uma nota contem wikilink para outra nota ou conceito |
| `pertence_a` | Uma nota fica dentro de pasta, dominio, sistema ou projeto |
| `classifica` | Uma nota declara tag ou tipo |
| `documenta` | Uma nota em `60_Sistemas/` descreve sistema ou ferramenta |
| `usa_ferramenta` | Relacao explicita entre sistema/agente e ferramenta |
| `depende_de` | Relacao explicita de dependencia |

## Propriedades minimas de no

```yaml
id:
tipo:
nome:
caminho:
dominio:
status:
fonte_principal:
confianca:
```

## Propriedades minimas de relacao

```yaml
origem:
destino:
tipo:
fonte:
confianca:
observacao:
```

## Mapeamento inicial por caminho

| Caminho | Tipo principal | Dominio |
|---|---|---|
| `00_Arquitetura/` | Nota | FabioOS |
| `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/` | Nota | FabioOS |
| `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/PRIMUS` | Projeto | PrimusOS |
| `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/` | Projeto | FabioOS |
| `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/30_Conhecimento/` | Conceito | FabioOS |
| `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Decisoes/` | Nota | FabioOS |
| `50_Registros/` | Nota | FabioOS |
| `60_Sistemas/Pietra` | Sistema | PietraOS |
| `60_Sistemas/MEGATRON` | Sistema | FabioOS |
| `60_Sistemas/RAG` | Sistema | FabioOS |
| `60_Sistemas/OpenClaw` | Sistema | FabioOS |
| `wiki/conceitos/` | Conceito | FabioOS |
| `wiki/projetos/pietra` | Projeto | PietraOS |
| `wiki/indices/` | Nota | FabioOS |

## Regras de seguranca

- Nao indexar `00_Inbox/`.
- Nao indexar `sources/_inbox/`.
- Nao indexar `.obsidian/`, `.claude/`, `.codex/`, `.git/`.
- Nao indexar `.venv/`, `node_modules/`, `site-packages/`.
- Nao indexar `fabioos_db/`.
- Nao indexar logs runtime.

## Criterio de evolucao

A ontologia so deve crescer quando uma nova relacao for:

1. observavel no vault;
2. util para pergunta relacional;
3. representavel sem expor dados sensiveis;
4. compativel com futura exportacao para Neo4j.
