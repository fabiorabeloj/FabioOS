---
tipo: documentacao
area: 60_Sistemas
projeto: FabioOS
status: ativo
fase: 12
tags: [rag, scripts, python, validacao, chroma, bge-m3]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Scripts RAG — Guia Operacional

## Funcao

Documentar os scripts em `60_Sistemas/RAG/scripts/` para execucao segura, reproduzivel e alinhada ao [[60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG]].

## Contexto

- Embeddings locais: `BAAI/bge-m3`
- Banco: Chroma em `60_Sistemas/RAG/fabioos_db/`
- Colecao: `fabioos`
- **Sempre usar o venv:** `60_Sistemas/RAG/.venv/Scripts/python.exe`

Instalacao (uma vez, com aprovacao):

```powershell
60_Sistemas\RAG\.venv\Scripts\pip.exe install -r 60_Sistemas\RAG\requirements.txt
```

---

## Scripts

### `ingest_vault.py`

Indexa pastas autorizadas no Chroma. **Destrutivo para o indice** — so rodar com lock e backup quando aplicavel.

```powershell
60_Sistemas\RAG\.venv\Scripts\python.exe 60_Sistemas\RAG\scripts\ingest_vault.py
```

### `query_rag.py`

Consulta semantica. Por padrao: **modo recuperacao** (sem API, sem custo).

```powershell
# Recuperacao (recomendado)
60_Sistemas\RAG\.venv\Scripts\python.exe 60_Sistemas\RAG\scripts\query_rag.py "O que e o FabioOS?" --k 5

# Geracao com Claude (exige ANTHROPIC_API_KEY e flag explicita)
60_Sistemas\RAG\.venv\Scripts\python.exe 60_Sistemas\RAG\scripts\query_rag.py "Explique o RAG" --generate
```

**Ranking operacional:** consultas sobre fase/status/pendencias recebem boost para `Painel_Pendencias`, `STATUS`, `NEXT_ACTIONS` e `mapa-fabios`.

**Cache:** `get_model()` mantem o embedding carregado na mesma sessao Python.

### `batch_validate_rag.py`

Executa automaticamente:

- 10 perguntas de aceitacao do plano de validacao;
- 5 consultas de seguranca (secao 4.5);
- gera JSON em `60_Sistemas/RAG/validacao_pos_ranking_YYYY-MM-DD.json`.

```powershell
60_Sistemas\RAG\.venv\Scripts\python.exe 60_Sistemas\RAG\scripts\batch_validate_rag.py --k 5
```

Ultima execucao bem-sucedida: **2026-06-29** — ver [[60_Sistemas/RAG/Relatorio_Validacao_RAG_2026-06-29_Cursor]].

---

## Criterios de qualidade

| Metrica | Alvo |
|---|---|
| Aceitacao | >= 8/10 `bom` |
| Seguranca | 0 retorno de paths proibidos (`.codex/config.toml`, `sources/_inbox`, `.env`) |
| Modo padrao | recuperacao, sem API |

## Relacoes

- [[60_Sistemas/RAG/Arquitetura_RAG_FabioOS]]
- [[60_Sistemas/FabioOS/Roteiro_Execucao_Fase12_RAG]]
- [[60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG]]
- [[wiki/conceitos/rag]]
- [[60_Sistemas/Cursor/README_Cursor_FabioOS]]

## Proximas acoes

- [ ] Integrar batch ao `start_fabioos.ps1` ou dashboard (quando Codex/Claude aprovarem)
- [ ] Reindexacao incremental apos novos docs LLM Wiki / matriz de aptidao
