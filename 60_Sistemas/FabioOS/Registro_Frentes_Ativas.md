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
| COMMITS_TEMATICOS | Claude | commits tematicos de coordenacao, retomada, RAG, higiene, OpenClaw, Obsidian e Fase 13 | concluida | 2026-06-27 | Frente encerrada sem push; stage explicito usado; `fabioos_db` preservado; checklist pre-commit registrado separadamente |
| ROTEAMENTO_CAPACIDADES | Codex | `Protocolo_Roteamento_Capacidades_IA.md`, `CLAUDE.md`, `Inventario_Skills.md`, changelog | concluida | 2026-06-27 | Capacidades instaladas agora possuem regra de roteamento; subagentes Codex precisam reteste por falha de spawn |

| MCP_FABIOOS | Claude | `60_Sistemas/MCP_FabioOS/` (novo); leitura read-only de `fabioos_db` e `Grafo/data` | em andamento | 2026-06-27 | Fase 15: MCP FastMCP que CONSULTA RAG/Grafo/vault. Só leitura desses artefatos; nao reindexar/apagar; sem push sem OK |

| INTERINATO_CODEX | Codex | `60_Sistemas/FabioOS/Interinato_Codex_2026-06-27_a_2026-06-29.md`, `STATUS.md`, `NEXT_ACTIONS.md`, OpenClaw Workboard `fabioos` | em andamento | 2026-06-27 | Coordenacao interina ate 2026-06-29 13:00 America/Sao_Paulo; Claude segue lider estrutural; nao tocar `MCP_FABIOOS`, RAG DB, Grafo data, OpenClaw auth/runtime ou push sem OK |

| MEMORIA_PESSOAL_PROFISSIONAL | Codex | `60_Sistemas/FabioOS/Protocolo_Ingestao_Memoria_Pessoal_Profissional.md`, `sources/chatgpt/`, `sources/email/`, `wiki/memoria/` | em desenho | 2026-06-27 | Absorver ChatGPT e e-mails por camadas: inventario, consentimento, triagem, fonte bruta, resumo seguro e wiki/RAG; nao ler ou arquivar emails em massa sem escopo aprovado |

| DOMINIOS_PERMISSOES_V0 | Codex | `60_Sistemas/FabioOS/Matriz_Dominios_Dados_Permissoes_2026-06-28.md`, `60_Sistemas/FabioOS/scripts/classificar_dado_fabioos.py`, `60_Sistemas/FabioOS/classificacoes/`, dashboard, mapa e changelog | concluida | 2026-06-28 | Classificador local v0 implementado e testado; nao tocou RAG DB, Grafo data, MCP_FABIOOS, OpenClaw auth/runtime ou push |

| SPEC_DRIVEN_V0 | Codex | `60_Sistemas/FabioOS/Protocolo_Spec_Driven_FabioOS.md`, `60_Sistemas/FabioOS/templates/Template_SPEC_FabioOS.md`, `60_Sistemas/FabioOS/specs/`, `60_Sistemas/FabioOS/scripts/gerar_spec_fabioos.py`, dashboard, mapa e changelog | concluida | 2026-06-28 | Fluxo SPEC -> plano -> tarefas -> testes -> changelog implementado localmente; nao tocou RAG DB, Grafo data, MCP_FABIOOS, OpenClaw auth/runtime ou arquivo untracked fora da frente |

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
- 2026-06-27 - `COMMITS_TEMATICOS` concluida. Commits locais de coordenacao, retomada, RAG, higiene, OpenClaw, Obsidian e Fase 13 foram criados sem push; o checklist pre-commit sem colisao ficou registrado como governanca.
- 2026-06-27 - `ROTEAMENTO_CAPACIDADES` concluida. Protocolo criado para obrigar consulta a skills, comandos, agentes, subagentes, scripts, MCPs, RAG e grafo antes de execucao manual.
- 2026-06-28 - `DOMINIOS_PERMISSOES_V0` concluida. Matriz de dominios/dados/permissoes e classificador local v0 criados; dashboard passou a exibir classificacoes.
- 2026-06-28 - `SPEC_DRIVEN_V0` concluida. Protocolo, template, gerador local de SPEC e primeira SPEC real criados; dashboard passou a exibir SPECs.
