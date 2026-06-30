---
tipo: prompt-operacional
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, claude, codex, coordenacao, multiagente]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Prompt para Claude - Coordenacao sem Colisao

## Prompt para colar no Claude

```text
Leia o contexto do FabioOS e continue a partir do ultimo changelog.

Antes de qualquer acao, leia obrigatoriamente:
- 60_Sistemas/FabioOS/bootstrap/CLAUDE.md
- 60_Sistemas/FabioOS/Registro_Frentes_Ativas.md
- 60_Sistemas/FabioOS/STATUS.md
- 60_Sistemas/FabioOS/NEXT_ACTIONS.md
- 60_Sistemas/FabioOS/Incidente_Coordenacao_RAG_2026-06-27.md
- 60_Sistemas/FabioOS/Relatorio_Coordenacao_Sem_Colisao_2026-06-27.md
- 60_Sistemas/RAG/Relatorio_Validacao_RAG_2026-06-27.md

Estado real:
- Houve colisao entre agentes na frente RAG.
- A colecao RAG foi restaurada pelo Codex e esta validada com 1795 chunks.
- Nao reindexe RAG.
- Nao apague `60_Sistemas/RAG/fabioos_db/`.
- Nao mate processos Python, Claude, Codex, OpenClaw, Node ou Docker sem confirmacao humana explicita.
- Antes de mexer em artefato compartilhado, registre a frente em `Registro_Frentes_Ativas.md`.

Divisao de trabalho atual:
- Codex fica com coordenacao, relatorios de handoff, validacao de estado e documentacao de locks.
- Claude deve assumir apenas a frente de organizacao/revisao/commit tematico, se o usuario autorizar.
- Claude nao deve tocar no banco RAG nem iniciar ingestao.
- Claude nao deve sobrescrever documentos novos de coordenacao do Codex.

Sua frente recomendada:
1. Rode `git status --short`.
2. Leia `Relatorio_Coordenacao_Sem_Colisao_2026-06-27.md`.
3. Prepare uma proposta de commits por tema, sem stage automatico amplo.
4. Para cada commit, use stage explicito por arquivo.
5. Antes de qualquer commit, rode scan de segredos.
6. Mostre a lista de arquivos staged e a mensagem proposta.
7. Aguarde OK humano antes de commitar.
8. Nao fazer push.

Zonas proibidas para Claude nesta retomada:
- `60_Sistemas/RAG/fabioos_db/`
- qualquer processo de ingestao RAG
- logs runtime
- arquivos de credenciais
- `.codex/config.toml`
- processos do Codex

Zonas que Claude pode revisar/preparar sem colisao, com cuidado:
- agrupamento de commits tematicos;
- docs de higiene de vault ja alterados;
- OpenClaw/WhatsApp docs, se nao houver processo runtime envolvido;
- frontmatter/wiki, com stage explicito.

Regra central:
Se a acao pode apagar, recriar, reindexar, mover ou commitar trabalho de outro agente, ela exige lock em `Registro_Frentes_Ativas.md` e confirmacao humana.
```

## Observacao

Este prompt existe para reduzir a necessidade de o usuario atuar como mensageiro entre Codex e Claude.
