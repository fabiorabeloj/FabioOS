---
tipo: registro-operacional
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, multiagente, locks, coordenacao, frentes-ativas]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Registro de Frentes Ativas

## Funcao

Evitar que Codex, Claude ou outro agente apague, sobrescreva, reindexe ou commite trabalho de outra frente sem acordo explicito.

## Regra operacional

Antes de mexer em artefato compartilhado, o agente deve registrar a frente aqui.

Artefatos compartilhados incluem:

- banco RAG em `60_Sistemas/RAG/fabioos_db/`;
- scripts em `60_Sistemas/RAG/scripts/`;
- workflows n8n;
- mapa, painel, status e changelog;
- arquivos de governanca;
- `.gitignore`;
- qualquer arquivo que outro agente tenha declarado em uso.

## Frentes ativas

| Frente | Dono | Arquivos/artefatos | Estado | Inicio | Regra |
|---|---|---|---|---|---|
| RAG_RESTORE | Codex | `60_Sistemas/RAG/fabioos_db/`, `60_Sistemas/RAG/ingest_run_restore.*.log` | concluida | 2026-06-27 | Reindexacao restaurada com `1795` chunks; nao reindexar novamente sem novo lock |
| COORD_CLAUDE_CODEX | Codex | `60_Sistemas/FabioOS/Prompt_Para_Claude_Coordenacao_2026-06-27.md`, `60_Sistemas/FabioOS/Relatorio_Coordenacao_Sem_Colisao_2026-06-27.md`, `Registro_Frentes_Ativas.md` | concluida | 2026-06-27 | Prompt e relatorio criados; nao tocar em RAG DB, commits, OpenClaw runtime ou processos sem novo lock |
| COMMITS_TEMATICOS | Claude | working tree por tema (higiene wiki P1/P2, scripts RAG, relatorios RAG, OpenClaw docs, coordenacao/retomada); index do Git | em andamento | 2026-06-29 | So preparar grupos + scan de segredos + pedir OK humano; stage explicito por arquivo; sem `git add -A`; sem push; nao tocar `fabioos_db`; nao matar processos |

## Frentes observadas

| Frente | Dono | Observacao |
|---|---|---|
| Claude Code local | Claude | Processo `claude.exe` ativo no Windows; nao encerrar nem sobrescrever trabalho sem leitura do Git/status |
| OpenClaw local | OpenClaw | Tray ativo; nao alterar configuracao sem registro |

## Regra anti-apagamento

Nenhum agente deve executar operacao que apague ou recrie base compartilhada sem:

1. verificar este registro;
2. verificar processos relacionados;
3. registrar frente ativa;
4. gerar backup quando aplicavel;
5. registrar log da acao;
6. atualizar STATUS/NEXT_ACTIONS.

## Encerramento de frente

Ao concluir, alterar `Estado` para `concluida`, registrar resultado e apontar o relatorio/changelog correspondente.

## Historico de encerramento

- 2026-06-27 - `RAG_RESTORE` concluida. Colecao `fabioos` restaurada com `1795` chunks; consultas de status validadas; incidente registrado em [[60_Sistemas/FabioOS/Incidente_Coordenacao_RAG_2026-06-27]].
- 2026-06-27 - `COORD_CLAUDE_CODEX` concluida. Prompt para Claude e relatorio de zonas de posse criados para evitar nova colisao.
