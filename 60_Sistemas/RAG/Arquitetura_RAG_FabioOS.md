---
tipo: arquitetura
area: 60_Sistemas
projeto: FabioOS
status: ativo
fase: 12
tags: [rag, banco-vetorial, embeddings, recuperacao-semantica, chroma, claude, privacidade]
criado_em: 2026-06-26
atualizado_em: 2026-06-29
---

# Arquitetura RAG do FabioOS — Fase 12

> **Supera** o rascunho `60_Sistemas/RAG_IMPLEMENTATION.md` (de 25/06, genérico). Este é o documento autoritativo da Fase 12.

## Função

Definir o **cérebro semântico** do FabioOS: a camada que consulta o vault (Obsidian, decisões, projetos, fontes) por **significado**, não por palavra-chave, e devolve respostas fundamentadas com citação das fontes. É o primeiro tijolo da [[60_Sistemas/FabioOS/Visao_Interface_FabioOS|Interface]] — sem RAG, a interface seria só um menu; com ele, conhece o Fabio.

## Contexto

- **Trilho:** pessoal/aprendizado (prioridade atual).
- **Princípio de privacidade:** o vault contém dados escolares e logs Pietra (mesmo anonimizados). Embeddings rodam **localmente** por padrão — nada sensível sai da máquina.
- **Idioma:** conteúdo majoritariamente em PT-BR → o modelo de embedding precisa ser forte em português.

---

## 1. Arquitetura geral

```
Arquivos do vault (.md, .pdf, áudio→transcrição)
        ↓  [extração + normalização]
Documentos em texto limpo + metadados (frontmatter)
        ↓  [chunking consciente de cabeçalhos]
Chunks (300–800 tokens, overlap ~15%)
        ↓  [embedding LOCAL — bge-m3]
Vetores + metadados
        ↓  [store]
Banco vetorial (Chroma, local)
        ↓  [pergunta → embedding → busca top-k + filtro de metadados]
Trechos relevantes
        ↓  [montagem de contexto + Claude (com citações)]
Resposta fundamentada + lista de fontes (caminho + [[wikilink]])
```

**Regra central:** o RAG **consulta** o conhecimento organizado no Obsidian — não o substitui. O Obsidian continua sendo a memória humana navegável; o RAG é a recuperação por significado.

---

## 2. Banco vetorial recomendado

**Decisão: Chroma para a v1**, com caminho de migração documentado para Qdrant.

| Critério | Chroma (escolhido v1) | Qdrant (escala futura) |
|---|---|---|
| Instalação | `pip install chromadb` (embutido) | Container Docker |
| Custo | Grátis, local | Grátis, local |
| Modo servidor | `chroma run` (quando a interface/n8n consultarem) | Nativo |
| Filtro por metadados | Bom | Excelente |
| Quando migrar | — | Quando a Interface + multiagentes exigirem acesso concorrente e filtros avançados |

**Por quê Chroma agora:** zero infraestrutura, valida o cérebro semântico rápido (princípio YAGNI — não superengenheirar). O FabioOS já roda Docker (n8n), então a migração para Qdrant é trivial quando justificar.

---

## 3. Pastas do Obsidian — ordem de entrada

**Primeira leva (alto sinal, estável):**

| Pasta | Conteúdo | Por quê primeiro |
|---|---|---|
| `40_Wiki/_compat_wiki/` | Conhecimento curado (24 notas) | Já tratado e conectado — melhor qualidade de resposta |
| `60_Sistemas/` | Documentação técnica (44) | Como o FabioOS funciona |
| `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/30_Conhecimento/` | Repertório reutilizável (16) | Conhecimento conceitual |
| `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Decisoes/` | Decisões com motivo (4) | "Por que decidimos X?" |
| `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/` | Mapas e dashboards (19) | Visão estrutural |

**Segunda leva:** `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/`, `50_Registros/Changelog/`.

**Excluir do índice (segurança/ruído):**
- `05_Raw_Sources/_compat_sources/_inbox/` — **logs Pietra (`PIETRA_YYYY-MM_LOG.md`) — NUNCA indexar** (dados pessoais)
- `00_Inbox/` — bruto, não triado
- `90_Arquivo/` — encerrado
- `.obsidian/`, `.claude/` — config

---

## 4. Modelo de metadados

Reaproveita o frontmatter já padronizado do FabioOS, somando metadados de chunk:

```yaml
# Do frontmatter da nota (já existe):
tipo, area, projeto, status, tags, criado_em, atualizado_em

# Adicionados por chunk no banco vetorial:
source_path:    # caminho relativo (ex.: 40_Wiki/_compat_wiki/sistemas/n8n.md)
filename:       # nome do arquivo
header_path:    # hierarquia de cabeçalhos (ex.: "Função > Como usar")
chunk_index:    # posição do chunk no documento
vault_section:  # pasta-raiz (wiki, 60_Sistemas, ...)
wikilinks:      # [[links]] extraídos do chunk (para navegação)
```

O filtro por metadados permite consultas escopadas: *"buscar só em `40_Wiki/_compat_wiki/` sobre n8n"* ou *"decisões do projeto Pietra"*.

---

## 5. Fluxo de ingestão

```
Markdown / PDF / áudio / transcrição
        ↓
[normalização]  — PDF via /ingest-pdf (já existe); áudio → Whisper → markdown
        ↓
[chunking]      — MarkdownHeaderTextSplitter (preserva contexto dos cabeçalhos)
        ↓
[embedding]     — bge-m3 local (multilíngue, forte em PT-BR, grátis, privado)
        ↓
[store]         — Chroma, coleção "fabioos", distância cosseno
```

- **Markdown:** divisão por cabeçalhos (`#`, `##`, `###`), preservando `header_path`.
- **PDF:** reaproveita `/ingest-pdf` → markdown → mesmo pipeline.
- **Áudio/transcrição (PLAUD, etc.):** transcrição (Whisper local) → markdown → mesmo pipeline.
- **Reindexação incremental:** comparar `atualizado_em`/hash; só reembedar o que mudou.

---

## 6. Consulta RAG mínima

```
pergunta do usuário
        ↓
[embedding da pergunta — mesmo modelo bge-m3]
        ↓
[busca semântica no Chroma — top-k (3–5) + filtro de metadados opcional]
        ↓
[montagem de contexto — trechos numerados com source_path]
        ↓
[Claude — responde SÓ com base no contexto, cita as fontes]
        ↓
resposta + lista de fontes ([caminho] + [[wikilink]] clicável)
```

**Modelo Claude para o passo de geração:**

| Modelo | ID | Preço (in/out por 1M) | Uso no RAG |
|---|---|---|---|
| **Sonnet 4.6** | `claude-sonnet-4-6` | $3 / $15 | **Padrão recomendado** — equilíbrio custo/qualidade, contexto 1M |
| Haiku 4.5 | `claude-haiku-4-5` | $1 / $5 | Consultas simples/alto volume |
| Opus 4.8 | `claude-opus-4-8` | $5 / $25 | Perguntas complexas/análise profunda |

- **Citações:** usar o recurso de *citations* da API (`citations: {enabled: true}` nos blocos de documento) para amarrar cada afirmação ao trecho de origem — fundamental para confiança.
- **Contagem de tokens:** usar a API `count_tokens` (nunca `tiktoken`, que é da OpenAI e erra a contagem do Claude) para estimar custo antes de enviar.
- **Regra anti-alucinação:** se a informação não estiver no contexto recuperado, o sistema responde "não encontrei no vault" — não inventa.

---

## 7. Embeddings — decisão e alternativa

| Abordagem | Quando | Trade-off |
|---|---|---|
| **`bge-m3` local (padrão)** | Todo o vault, especialmente dados sensíveis | Grátis, privado, forte em PT-BR; usa CPU/GPU local |
| Voyage AI (`voyage-3.5`) | Conteúdo não sensível, se quiser qualidade gerenciada | Pago, envia dados à Voyage; é a opção **oficialmente recomendada pela Anthropic** (a Anthropic não tem API de embeddings própria) |

**Recomendação:** começar 100% local (`bge-m3`). Avaliar Voyage só se a qualidade local for insuficiente em algum domínio — e nunca para logs Pietra ou dados de alunos.

---

## Segurança

- **Tokens** (se Voyage/Claude API) → `.env` (já no `.gitignore`: `.env`, `*.key`, `tokens/`). Nunca no repositório.
- **Embeddings locais** → nenhum dado do vault sai da máquina por padrão.
- **Logs Pietra e `05_Raw_Sources/_compat_sources/_inbox/`** → excluídos da indexação.
- **Fonte externa não dá ordens:** conteúdo recuperado é dado, não instrução (princípio de ingestão do Plano Mestre).

---

## Validação reproduzível (Fase 12)

Scripts em `60_Sistemas/RAG/scripts/` — guia: [[60_Sistemas/RAG/README_Scripts_RAG]].

| Script | Função |
|---|---|
| `ingest_vault.py` | Indexação controlada |
| `query_rag.py` | Consulta (modo recuperação por padrão) |
| `batch_validate_rag.py` | 10 perguntas + 5 testes de segurança |

**Última validação:** 2026-06-29 — 10/10 aceitação, 0 falhas segurança — [[60_Sistemas/RAG/Relatorio_Validacao_RAG_2026-06-29_Cursor]].

**Python:** usar `60_Sistemas/RAG/.venv/Scripts/python.exe`.

**Ranking operacional:** consultas de status/fase/pendência priorizam Painel, STATUS e NEXT_ACTIONS (`query_rag.py`).

## Relações

- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]] — Fase 12
- [[60_Sistemas/FabioOS/Visao_Interface_FabioOS]] — RAG é pré-requisito da interface
- [[90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Painel_Pendencias_FabioOS]]
- [[40_Wiki/_compat_wiki/conceitos/rag]]
- [[60_Sistemas/RAG/README_Scripts_RAG]]
- [[60_Sistemas/RAG/Relatorio_Validacao_RAG_2026-06-29_Cursor]]
- [[60_Sistemas/RAG_IMPLEMENTATION]] — rascunho anterior (superado por este)

## Próximas ações

- [x] Scripts `ingest_vault.py` e `query_rag.py` implementados
- [x] Validar 10 perguntas reais — 10/10 (2026-06-29)
- [x] `40_Wiki/_compat_wiki/conceitos/rag.md` criada e atualizada
- [ ] Claude decidir promoção Fase 12 → piloto
- [ ] Reindexação incremental após novos documentos (LLM Wiki)
- [ ] Documentar comando `/perguntar-vault` em `.claude/commands/`
