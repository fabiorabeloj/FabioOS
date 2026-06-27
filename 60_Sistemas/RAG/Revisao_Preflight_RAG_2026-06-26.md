---
tipo: revisao
area: 60_Sistemas
projeto: FabioOS
status: rascunho
fase: 12
tags: [rag, preflight, revisao, seguranca, validacao]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Revisão Pré-flight — Scripts RAG Fase 12

## Função

Registrar revisão técnica prévia dos scripts RAG antes de instalar dependências, ingerir o vault ou consultar a base semântica.

Escopo revisado:

```text
60_Sistemas/RAG/scripts/ingest_vault.py
60_Sistemas/RAG/scripts/query_rag.py
60_Sistemas/RAG/requirements.txt
60_Sistemas/RAG/.gitignore
```

## Resultado geral

Os scripts estão coerentes com a Fase 12 e compilam sem erro de sintaxe. A configuração de raiz do vault está correta para a estrutura atual:

```text
60_Sistemas/RAG/scripts -> FabioOs/FabioOs
```

Ainda assim, há ajustes recomendados antes da primeira ingestão real.

---

## 1. Validações executadas

- [x] `python -m py_compile` em `ingest_vault.py` e `query_rag.py`.
- [x] Verificação de `requirements.txt`.
- [x] Verificação de `.gitignore` local do RAG.
- [x] Confirmação de que `60_Sistemas/RAG/fabioos_db/` está ignorado pelo Git.
- [x] Revisão das exclusões de ingestão.

## 2. Achados

## 2.1 P1 — Ingestão pode indexar logs locais dos agentes

**Arquivo:** `60_Sistemas/RAG/scripts/ingest_vault.py`

**Problema:** `INCLUDE_DIRS` inclui `60_Sistemas/`. Dentro dessa pasta existe ou pode existir:

```text
60_Sistemas/MEGATRON/agentes/logs/agentes_log.md
```

Esse caminho está ignorado pelo Git, mas o script percorre o filesystem diretamente com `rglob("*.md")`. A exclusão atual não contém `logs/`, `agentes/logs` ou `agentes_log.md`.

**Impacto:** logs runtime locais podem ser indexados no banco vetorial, contrariando a regra de não indexar runtime e possíveis dados sensíveis.

**Recomendação antes da ingestão:**

Adicionar exclusões como:

```python
"logs/",
"/logs/",
"agentes/logs",
"agentes_log"
```

ou, melhor, usar um filtro por caminhos proibidos explícitos.

## 2.2 P2 — Geração com Claude ocorre automaticamente se `ANTHROPIC_API_KEY` existir

**Arquivo:** `60_Sistemas/RAG/scripts/query_rag.py`

**Problema:** se a variável `ANTHROPIC_API_KEY` estiver no ambiente, o script envia o contexto recuperado para a API Anthropic automaticamente.

**Impacto:** ainda que a ingestão seja local, a consulta pode enviar trechos do vault para serviço externo sem uma flag explícita de geração.

**Recomendação:**

Manter modo recuperação como padrão e exigir uma flag explícita:

```text
--generate
```

Assim, a presença da chave no ambiente não muda o comportamento sem intenção humana.

## 2.3 P2 — Falha em um Markdown pode abortar a ingestão inteira

**Arquivo:** `60_Sistemas/RAG/scripts/ingest_vault.py`

**Problema:** `frontmatter.load(f)` não está protegido por `try/except` por arquivo.

**Impacto:** um Markdown com frontmatter inválido pode interromper toda a ingestão.

**Recomendação:**

Capturar exceções por arquivo, registrar `skipped_files` e continuar a ingestão.

## 2.4 P3 — Reindexação é destrutiva por padrão

**Arquivo:** `60_Sistemas/RAG/scripts/ingest_vault.py`

**Problema:** o script executa `delete_collection(COLLECTION)` antes de recriar a coleção.

**Impacto:** aceitável para v1, mas impede ingestão incremental e pode apagar índice útil sem confirmação.

**Recomendação:**

Manter para v1, mas declarar no output:

```text
Reindexação limpa: coleção anterior será apagada.
```

Futuro: adicionar modo incremental por hash.

## 2.5 P3 — ID do modelo Claude deve ser validado antes do uso pago

**Arquivo:** `60_Sistemas/RAG/scripts/query_rag.py`

**Problema:** `CLAUDE_MODEL = "claude-sonnet-4-6"` depende de disponibilidade real na API local/configurada.

**Impacto:** consulta com geração pode falhar em tempo de execução.

**Recomendação:**

Antes de usar geração, validar o modelo disponível ou tornar o modelo configurável por variável de ambiente.

---

## 3. O que está adequado

- Banco vetorial local `fabioos_db/` está protegido por `.gitignore`.
- Dependências principais estão listadas, incluindo `python-frontmatter`.
- Escopo inicial prioriza pastas de alto sinal.
- `sources/_inbox/`, `00_Inbox/`, `.claude/`, `.obsidian/`, `.git`, `90_Arquivo` e `fabioos_db` estão excluídos.
- Modo recuperação sem chave de API permite testar busca sem enviar dados externos.
- Chunking por cabeçalho é adequado para primeira versão.

## 4. Recomendação antes de executar a Fase 12

Antes de instalar dependências e rodar `ingest_vault.py`, corrigir pelo menos:

- [ ] P1: excluir logs runtime dos agentes.
- [ ] P2: exigir flag explícita para geração externa com Claude.

Depois:

- [ ] Rodar ingestão.
- [ ] Verificar lista de arquivos indexados.
- [ ] Executar as 10 perguntas do [[60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG]].
- [ ] Registrar relatório de validação.

## Relações

- [[60_Sistemas/RAG/Arquitetura_RAG_FabioOS]]
- [[60_Sistemas/FabioOS/Roteiro_Execucao_Fase12_RAG]]
- [[60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG]]
- [[60_Sistemas/MEGATRON/agentes/specs/Agente_RAG]]
