---
tipo: especificacao-agente
area: 60_Sistemas
projeto: FabioOS
sistema: MEGATRON
agente: RAG
status: especificado
prioridade: 4
tags: [megatron, agente, rag, busca-semantica, fontes, chroma]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Agente RAG

## Identidade

| Campo | Valor |
|---|---|
| Nome | RAG |
| ID | `agent.rag` |
| Domínio | FabioOS |
| Estado | especificado |
| Prioridade | 4 |
| Dono humano | Fabio |
| Identidade pública | MEGATRON interno |

## Missão

Ingerir conhecimento curado do vault em memória semântica local e responder consultas com fontes, citações e declaração explícita de ignorância quando não houver evidência suficiente.

## Entradas

| Entrada | Origem | Formato |
|---|---|---|
| Notas curadas | `40_Wiki/_compat_wiki/`, `60_Sistemas/`, `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/30_Conhecimento/`, `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Decisoes/`, `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/` | Markdown |
| Pergunta | usuário, MEGATRON ou agente | texto |
| Filtro de busca | MEGATRON | pasta, domínio, tags |
| Exclusões | Arquitetura RAG | lista de pastas |

## Saídas

| Saída | Destino | Formato |
|---|---|---|
| Índice vetorial | Chroma local | vetores + metadados |
| Resposta fundamentada | MEGATRON / usuário | texto com fontes |
| Lista de fontes | MEGATRON / usuário | caminhos + wikilinks |
| Relatório de lacuna | Dashboard / Arquivista | pergunta sem fonte |
| Log de consulta | `50_Registros/Agentes/` | Markdown sem dados sensíveis |

## Ferramentas

- Scripts em `60_Sistemas/RAG/scripts/`.
- Chroma local.
- Embeddings locais `bge-m3`.
- Busca textual auxiliar com `rg`.
- Leitura da [[60_Sistemas/RAG/Arquitetura_RAG_FabioOS]].

## Permissões

| Classe de ação | Permitida | Condição |
|---|---|---|
| Leitura | Sim | Pastas liberadas para indexação |
| Escrita segura | Sim | Índice local e logs sanitizados |
| Indexação | Sim | Excluir pastas sensíveis |
| Escrita em wiki | Não na v1 | Encaminhar síntese ao Arquivista |
| Dados sensíveis | Não | Excluir `05_Raw_Sources/_compat_sources/_inbox/` e logs Pietra |
| Envio externo | Não | Fora do escopo |
| Commit | Não | Encaminhar para SafeCommit |

## Limites

- Não indexar `05_Raw_Sources/_compat_sources/_inbox/`, logs Pietra, `.obsidian/`, `.claude/`, `00_Inbox/` bruto ou dados não triados.
- Não responder além das fontes recuperadas.
- Não tratar resultado sem fonte como certeza.
- Não substituir wiki; apenas consultar.
- Não enviar conteúdo sensível para embeddings remotos por padrão.

## Riscos

| Risco | Impacto | Mitigação |
|---|---|---|
| Indexar dado sensível | Vazamento local ou futuro | Lista de exclusões rígida |
| Resposta sem fonte | Alucinação | Regra da Ignorância Explícita |
| Chunk ruim | Resposta fraca | Chunking por cabeçalhos |
| Índice desatualizado | Resposta obsoleta | Reindexação incremental |
| Custo de modelo | Uso excessivo | Modelos locais e logging |

## Critérios de aceite

- [ ] Indexa a primeira leva de pastas autorizadas.
- [ ] Preserva metadados: caminho, arquivo, cabeçalho, tags e wikilinks.
- [ ] Responde com fontes.
- [ ] Declara quando não encontrou evidência suficiente.
- [ ] Não indexa pastas proibidas.
- [ ] Gera log sanitizado de consulta.

## Logs

Registrar:

- data;
- tipo: ingestão ou consulta;
- pastas indexadas;
- número de chunks;
- pergunta;
- fontes recuperadas;
- status: respondido, baixa confiança ou sem fonte;
- erro, se houver.

## Relação com MEGATRON

MEGATRON aciona RAG para responder perguntas, buscar contexto antes de decisões e alimentar outros agentes. RAG devolve contexto com fontes; MEGATRON decide se responde, pergunta ao usuário, aciona Arquivista ou registra lacuna.

## Implementação mínima

1. Usar Chroma local e embeddings locais conforme a arquitetura da Fase 12.
2. Ingerir apenas `40_Wiki/_compat_wiki/`, `60_Sistemas/`, `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/30_Conhecimento/`, `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Decisoes/` e `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/`.
3. Criar consulta top-k com fontes.
4. Validar com 10 perguntas reais.

## Evolução futura

- Filtros por domínio.
- Reindexação incremental por hash.
- Integração com Dashboard.
- Integração com grafo Neo4j.
- MCP FabioOS para consulta semântica.
- Separação futura entre RAG pessoal, RAG PietraOS e RAG PrimusOS.

## Relações

- [[60_Sistemas/RAG/Arquitetura_RAG_FabioOS]]
- [[60_Sistemas/MEGATRON/agentes/specs/Agente_Arquivista]]
- [[60_Sistemas/MEGATRON/agentes/specs/Agente_Dashboard]]
- [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]]
