---
tipo: registro-operacional
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, multiagente, locks, coordenacao, frentes-ativas]
criado_em: 2026-06-27
atualizado_em: 2026-07-02
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
| ROTEAMENTO_CAPACIDADES | Codex | `Protocolo_Roteamento_Capacidades_IA.md`, `60_Sistemas/FabioOS/bootstrap/CLAUDE.md`, `Inventario_Skills.md`, changelog | concluida | 2026-06-27 | Capacidades instaladas agora possuem regra de roteamento; subagentes Codex precisam reteste por falha de spawn |

| MCP_FABIOOS | Claude | `60_Sistemas/MCP_FabioOS/` (novo); leitura read-only de `fabioos_db` e `Grafo/data` | em andamento | 2026-06-27 | Fase 15: MCP FastMCP que CONSULTA RAG/Grafo/vault. Só leitura desses artefatos; nao reindexar/apagar; sem push sem OK |

| INTERINATO_CODEX | Codex | `60_Sistemas/FabioOS/Interinato_Codex_2026-06-27_a_2026-06-29.md`, `STATUS.md`, `NEXT_ACTIONS.md`, OpenClaw Workboard `fabioos` | em andamento | 2026-06-27 | Coordenacao interina ate 2026-06-29 13:00 America/Sao_Paulo; Claude segue lider estrutural; nao tocar `MCP_FABIOOS`, RAG DB, Grafo data, OpenClaw auth/runtime ou push sem OK |

| MEMORIA_PESSOAL_PROFISSIONAL | Codex | `60_Sistemas/FabioOS/Protocolo_Ingestao_Memoria_Pessoal_Profissional.md`, `05_Raw_Sources/_compat_sources/chatgpt/`, `05_Raw_Sources/_compat_sources/email/`, `40_Wiki/_compat_wiki/memoria/` | em desenho | 2026-06-27 | Absorver ChatGPT e e-mails por camadas: inventario, consentimento, triagem, fonte bruta, resumo seguro e 40_Wiki/_compat_wiki/RAG; nao ler ou arquivar emails em massa sem escopo aprovado |

| DOMINIOS_PERMISSOES_V0 | Codex | `60_Sistemas/FabioOS/Matriz_Dominios_Dados_Permissoes_2026-06-28.md`, `60_Sistemas/FabioOS/scripts/classificar_dado_fabioos.py`, `60_Sistemas/FabioOS/classificacoes/`, dashboard, mapa e changelog | concluida | 2026-06-28 | Classificador local v0 implementado e testado; nao tocou RAG DB, Grafo data, MCP_FABIOOS, OpenClaw auth/runtime ou push |

| SPEC_DRIVEN_V0 | Codex | `60_Sistemas/FabioOS/Protocolo_Spec_Driven_FabioOS.md`, `60_Sistemas/FabioOS/templates/Template_SPEC_FabioOS.md`, `60_Sistemas/FabioOS/specs/`, `60_Sistemas/FabioOS/scripts/gerar_spec_fabioos.py`, dashboard, mapa e changelog | concluida | 2026-06-28 | Fluxo SPEC -> plano -> tarefas -> testes -> changelog implementado localmente; nao tocou RAG DB, Grafo data, MCP_FABIOOS, OpenClaw auth/runtime ou arquivo untracked fora da frente |

| MOBILE_GATEWAY_V0 | Codex | `60_Sistemas/FabioOS/scripts/mobile_gateway_fabioos.py`, `60_Sistemas/FabioOS/Mobile_Gateway_FabioOS_v0.md`, `60_Sistemas/FabioOS/specs/`, `00_Inbox/mobile/`, dashboard e changelog | concluida | 2026-06-28 | Captura mobile local via navegador/LAN implementada e testada; gateway rodando na porta 8787; nao tocou MCP_FABIOOS, RAG DB, Grafo data, OpenClaw auth/runtime, n8n externo ou push |

| GOOGLE_CATALOGOS_V0 | Codex | `60_Sistemas/FabioOS/Conectores_Google_Catalogo_v0.md`, `40_Wiki/_compat_wiki/memoria/Mapa_Conectores_Google_FabioOS.md`, `05_Raw_Sources/_compat_sources/email/_restrito/`, `05_Raw_Sources/_compat_sources/drive/_restrito/`, `.gitignore`, dashboard e changelog | concluida | 2026-06-28 | Gmail/Drive catalogados em leitura; detalhes restritos fora do Git; sem envio, exclusao, rotulo, exportacao, API externa, RAG/Grafo ou push |

| INVENTARIO_FERRAMENTAS_IA_V0 | Codex | `60_Sistemas/FabioOS/scripts/inventario_ferramentas_ia.py`, `60_Sistemas/FabioOS/Inventario_Ferramentas_IA_Local_2026-06-28.md`, dashboard e changelog | concluida | 2026-06-28 | Inventario gerado sem revelar tokens; OpenClaw/Cursor/Hermes existem mas CLIs nao estao no PATH; n8n nao esta ouvindo em 5678; OpenRouter env ausente |

| MATRIZ_APTIDAO_IAS | Codex | `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Repertorio/IA/Modelos_e_IAs/Matriz_de_Aptidao_das_IAs_FabioOS.md`, `STATUS.md`, `NEXT_ACTIONS.md`, mapa, roteamento, specs, skills, agentes e changelog | concluida | 2026-06-29 | Matriz criada e conectada ao prompt mestre, roteamento, specs, skills, agentes, STATUS/NEXT_ACTIONS e mapa; sem instalar, sem chamar API, sem mexer em tokens, RAG DB, MCP_FABIOOS, OpenClaw runtime, n8n externo ou push |

| LLM_WIKI_OPERACIONAL | Codex | `50_Registros/Auditoria/Reentrada_Codex_FabioOS.md`, `30_Projetos/FabioOS/LLM_Wiki_FabioOS.md`, `60_Sistemas/Wiki/`, `10_Dashboard/`, `10_Dashboard/_entrada/index.md`, `50_Registros/Logs_Agentes/log.md`, `STATUS.md`, `NEXT_ACTIONS.md`, changelog | concluida | 2026-06-29 | LLM Wiki operacional formalizada; sem migracao em massa, sem automacao externa, sem RAG reindex, sem MCP runtime, sem OpenClaw/n8n externo e sem push |

| PILOTO_LLM_WIKI_GOVERNANCA | Codex | `05_Raw_Sources/_compat_sources/fabios/2026-06-29_governanca-operacional-pontos-cegos.md`, `40_Wiki/_compat_wiki/conceitos/governanca-operacional-fabios.md`, `30_Projetos/FabioOS/LLM_Wiki_FabioOS.md`, `10_Dashboard/_entrada/index.md`, `50_Registros/Logs_Agentes/log.md`, `CHANGELOG_FabioOS.md`, `NEXT_ACTIONS.md` | concluida | 2026-06-29 | Piloto pequeno executado; uma fonte preservada, uma pagina existente atualizada, uma pagina wiki criada; sem API, sem RAG reindex, sem MCP runtime, sem push |

| ROADMAP_FASES_V2 | Codex | `60_Sistemas/FabioOS/Roadmap_Fases_FabioOS_v2_2026-06-29.md`, `Plano_Mestre`, `Painel_Pendencias`, `STATUS`, `NEXT_ACTIONS`, mapa e changelog | concluida | 2026-06-29 | Fases revisadas; Roadmap v2 criado com Governanca Operacional como proxima frente; sem runtime, sem API, sem push |

| FASE17_GOVERNANCA_OPERACIONAL | Codex | `50_Registros/Decisoes/Constituicao_Operacional_FabioOS.md`, `60_Sistemas/Governanca/`, `60_Sistemas/Agentes/`, `60_Sistemas/Protocolos/`, `60_Sistemas/Seguranca/`, `60_Sistemas/Memoria/`, `60_Sistemas/Conhecimento/`, `60_Sistemas/Padroes/`, `60_Sistemas/Observabilidade/`, `10_Dashboard/Governanca_FabioOS.md` | concluida | 2026-06-29 | Camada documental de governanca operacional criada; sem runtime, sem API, sem alterar credenciais, sem push |

| SPEC_MEGATRON_V1 | Codex | `60_Sistemas/FabioOS/specs/2026-06-29_megatron-v1-ignorancia-explicita.md`, `NEXT_ACTIONS`, changelog | concluida | 2026-06-29 | SPEC documental para MEGATRON v1 criada; sem implementar codigo, sem runtime, sem API, sem push |

| NORMALIZACAO_OBSIDIAN_V2 | Codex | `60_Sistemas/FabioOS/Mapa_Canonico_Pastas_Obsidian_v2_2026-06-29.md`, `50_Registros/Auditoria/Auditoria_Pastas_Obsidian_2026-06-29.md`, `60_Sistemas/FabioOS/Plano_Normalizacao_Pastas_Obsidian_2026-06-29.md`, `10_Dashboard/Estrutura_Obsidian_FabioOS.md`, `60_Sistemas/FabioOS/bootstrap/CLAUDE.md`, mapa, status e changelog | concluida | 2026-06-29 | Taxonomia canonica v2 criada; pastas legadas marcadas; nenhuma migracao fisica em massa; sem apagar, sem mover, sem push |

| ESTRUTURA_FISICA_LLM_WIKI | Codex | `05_Raw_Sources/`, `20_Areas/`, `40_Wiki/`, `70_Skills/`, `80_Specs/`, dashboards, ADR, auditoria, estrutura LLM Wiki, STATUS/NEXT_ACTIONS, mapa e changelog | concluida | 2026-06-29 | Estrutura fisica visivel no Obsidian criada com READMEs e documentos; sem mover `05_Raw_Sources/_compat_sources/`/`40_Wiki/_compat_wiki/`, sem apagar, sem RAG/Grafo, commit local autorizado sem push |

| LIMPEZA_VISUAL_RAIZ_OBSIDIAN | Codex | `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/`, `90_Arquivo/Descartes_Visuais_Obsidian_2026-06-29/`, `.obsidian/app.json`, `50_Registros/Relatorios/`, `STATUS.md`, `NEXT_ACTIONS.md`, `50_Registros/Logs_Agentes/log.md`, changelog | concluida | 2026-06-29 | Pastas legadas arquivadas sem apagar; placeholders `Sem titulo` renomeados/arquivados; arquivos tecnicos ocultos no Obsidian; `sources`, `wiki` e `schema` preservados no disco por compatibilidade tecnica; sem RAG/Grafo/OpenClaw/n8n/push |

| RAG_REINDEX_POS_LIMPEZA_OBSIDIAN | Codex | `60_Sistemas/RAG/scripts/ingest_vault.py`, `query_rag.py`, `batch_validate_rag.py`, `fabioos_db/`, relatorios de validacao | concluida | 2026-06-29 | Reindexacao executada para alinhar fontes RAG aos caminhos reais apos limpeza visual; `1206` chunks; validacao `10/10` e `0` falhas; sem API externa, sem `--generate`, sem push |

| ESTRUTURA_CANONICA_COMPLETA_OBSIDIAN | Codex | `00_Inbox/`, `60_Sistemas/`, `60_Sistemas/FabioOS/Estrutura_Canonica_Completa_Obsidian_2026-06-29.md`, STATUS, NEXT_ACTIONS, dashboard de estrutura e changelog | concluida | 2026-06-29 | Estrutura visual proposta pelo Fabio formalizada; arquivos soltos de `60_Sistemas/` foram movidos para subpastas coerentes; notas de teste da Inbox preservadas em Triagem; sem apagar conhecimento, sem RAG/Grafo/OpenClaw/n8n/push |

| LINKS_POS_MIGRACAO_V1 | Codex | wikilinks `wiki/` e `sources/`, `60_Sistemas/FabioOS/Ordens_Arquiteto_Para_Codex_2026-06-29.md`, changelog | concluida | 2026-06-29 | Lote 0 concluiu auditoria; duplicata `wiki/` recriada foi preservada em `90_Arquivo`; links restantes listados para handoff por estarem em zona RAG/Cursor ja suja; sem tocar RAG, MEGATRON, MCP, runtime, db ou push |

| PROMOCAO_FASE12_PILOTO | Claude | `50_Registros/Decisoes/ADR_2026-06-29_Promocao_Fase12_RAG_Piloto.md`, `STATUS.md`, `NEXT_ACTIONS.md` | concluida | 2026-06-29 | Revisada evidencia 10/10 (1206 chunks, modo recuperacao, 0 vazamentos) e promovida Fase 12 a piloto; hardening (MAX_CHARS, ficha tecnica) diferido para Fase 12.1; NENHUM reindex, NENHUMA edicao no `fabioos_db`, sem API externa, sem commit, sem push |

| MEGATRON_COORDENADOR_NUCLEO | Claude | `60_Sistemas/MEGATRON/v1/megatron.py`, `60_Sistemas/MEGATRON/v1/registry.py` (novo), contrato `run()` dos agentes, `60_Sistemas/MEGATRON/v1/tests/golden_questions.py`, `STATUS.md`, `NEXT_ACTIONS.md` | em andamento | 2026-06-29 | Fatias 1-4 da spec [[60_Sistemas/FabioOS/specs/2026-06-29_megatron-coordenador]]; define o contrato `Resultado`; sem tocar apresentacao (Cursor) nem governanca/roadmap (Codex); sem reindex RAG, sem push |
| CURSOR_APRESENTACAO_MEGATRON | Cursor | `60_Sistemas/MEGATRON/v1/apresentacao.py` (novo), `60_Sistemas/Cursor/` (mockup briefing) | reservada | 2026-06-29 | Consome o `Resultado` congelado (ver Ordens); `render(resultado)->str` + mockup visual; NAO toca `megatron.py`/`registry.py`/agentes/RAG/MCP/governanca; sem push |
| CODEX_GOVERNANCA_POS_FASE12 | Codex | `Painel_Pendencias_FabioOS.md`, `Roadmap_Fases_FabioOS_v2_2026-06-29.md`, `60_Sistemas/MEGATRON/agentes/Registro_Agentes.md` (doc), `60_Sistemas/Governanca/` INDEX, wikilinks | reservada | 2026-06-29 | Atualiza Painel (1795->1206, Fase 12 piloto, MEGATRON 16.1 ativo), Roadmap e doc do contrato de agente; ZERO codigo MEGATRON/RAG/MCP; nao toca STATUS/NEXT_ACTIONS (Claude) nem apresentacao (Cursor); sem push |

| N8N_LOCAL_OPERACAO | Codex | container Docker `n8n`, porta `5678`, `60_Sistemas/n8n/`, relatorio/changelog da operacao | concluida | 2026-06-29 | Container `n8n` iniciado e painel validado em `127.0.0.1:5678`; workflows locais validados; nao tocou OpenClaw/Evolution, RAG, MEGATRON, MCP, credenciais reais ou push |
| PRIMUS_OPERACAO_56 | Codex | `05_Raw_Sources/PRIMUS/`, `30_Projetos/PRIMUS/`, `40_Wiki/PRIMUS/`, `80_Specs/PRIMUS/`, log, barramento e changelog PRIMUS | concluida | 2026-06-30 | Project ChatGPT PRIMUS vasculhado; Changelog 5.6 formalizado; cockpit operacional e specs Vector/WorldCycle/Villain/MissionContract criados; Missao 0001 segue bloqueada ate validar pagina/trecho de 5 CatalogEntries; sem RAG/MCP/OpenClaw/n8n/push |
| PDF_DROP_TRIGGER_V0 | Codex | `00_Inbox/pdfs/`, `60_Sistemas/FabioOS/scripts/watch_pdf_drop.py`, `60_Sistemas/n8n/Workflows/FabioOS_DropPDF_Aprende.json`, barramento/log/changelog | concluida | 2026-06-30 | Porta de entrada da SPEC `pipeline-pdf-aprende` implementada: detecta PDF e entrega caminho/metadados ao Claude/documentalista; sem OCR, sem RAG, sem Stirling auth, sem push |
| OBSIDIAN_REVITALIZACAO | Codex | `.obsidian/graph.json`, `10_Dashboard/`, `40_Wiki/_MOCs/`, log, barramento e changelog | concluida | 2026-06-30 | Graph View atualizado para pastas canonicas; dashboard/MOC criados; wikilinks adicionados; nao tocou codigo MEGATRON/RAG nem reindex |
| OBSIDIAN_PRIMUS_MOCS | Codex | `40_Wiki/_MOCs/MOC_PRIMUS.md`, `40_Wiki/PRIMUS/`, `80_Specs/PRIMUS/`, dashboards e auditoria de links | concluida | 2026-06-30 | PRIMUS ganhou MOC central, Enciclopedia E, Instancias I, Persistencia P, template e SPEC para novos nos; sem PDF extraction, sem RAG/reindex |
| PRIMUS_DND_WIKILINKS | Codex | `40_Wiki/PRIMUS/Fontes_Oficiais_DND/`, MOCs PRIMUS, auditoria/changelog | concluida | 2026-06-30 | PHB/DMG/MM extraidos como indices seguros de pagina/categoria/ancora/destino PRIMUS; sem coluna text, sem dump integral, sem RAG/reindex |
| PRIMUS_GOOGLE_DOC_RELEITURA | Codex | `50_Registros/Auditoria/Releitura_GoogleDoc_PRIMUS_2026-07-01.md`, `40_Wiki/PRIMUS/Arquivo_Consultavel_PRIMUS.md`, `80_Specs/PRIMUS/Spec_Operadores_Mundo_PRIMUS.md`, fila/MOC/log/changelog | concluida | 2026-07-01 | Google Doc relido com otica atual: prioridade muda para R(X), ProblemGenerator, Arquivo Consultavel e operadores de mundo; sem editar Google Doc, sem RAG/reindex |
| PRIMUS_RPG_DOCX_RELEITURA | Codex | `50_Registros/Auditoria/Releitura_GoogleDrive_Rpg_Docx_PRIMUS_2026-07-01.md`, `30_Projetos/PRIMUS/Mapa_Digestao_Rpg_Docx_PRIMUS.md`, `30_Projetos/PRIMUS/CatalogEntries_Candidatas_Rpg_Docx_PRIMUS.md`, MOC, Matriz de Fontes, Digestor, fila, log e changelog | concluida | 2026-07-01 | `Rpg .docx` relido como fonte-mae restrita; criado funil seguro de digestao e CatalogEntries candidatas; sem editar Drive, sem dump integral, sem RAG/reindex |
| MARKDOWNIZACAO_SEGURA_E_APOSTILAS | Codex | `80_Specs/PRIMUS/Spec_Markdownizacao_Segura_Livros_PRIMUS.md`, `30_Projetos/PRIMUS/Plano_Markdownizacao_Livros_PRIMUS.md`, `80_Specs/EscolaOS/Spec_Ingestao_Apostilas_EscolaOS.md`, `20_Areas/EscolaOS/Pipeline_Apostilas_para_Obsidian.md`, nos seguros PRIMUS | concluida | 2026-07-01 | Formalizada a regra: livros restritos viram stubs/CatalogEntries/abstracoes; apostilas autorais podem virar Markdown completo; sem dump protegido, sem RAG/reindex |
| PRIMUS_DND_CORE_CATALOGO | Codex | `40_Wiki/PRIMUS/Fontes_Oficiais_DND/Catalogo_DND_Core_Consolidado.md`, ADR, auditoria, changelog, MOCs e READMEs | concluida | 2026-07-01 | Stubs massivos foram considerados inviaveis para Obsidian; PHB/DMG/MM ficam como catalogo consolidado e notas so sao promovidas seletivamente; sem coluna `text`, sem dump integral, sem RAG/reindex |
| PRIMUS_CONCEITOS_LIVROS | Codex | `40_Wiki/PRIMUS/conceitos/`, `40_Wiki/PRIMUS/README.md`, auditoria, log e changelog | concluida | 2026-07-01 | Ordem do Claude executada: 14 conceitos fortes adicionados, MOC atualizado e links DeltaP corrigidos; sem stubs massivos, sem texto protegido, sem RAG/reindex |
| EMAIL_INTAKE_DRY_RUN | Codex | `60_Sistemas/FabioOS/scripts/email_intake_dry_run.py`, SPEC, diagnostico, inbox email, log e changelog | concluida | 2026-07-01 | Ponte local criada para payloads autorizados do Gmail/n8n; classifica e gera triagem restrita; sem OAuth proprio, sem envio, sem alterar mensagens, sem RAG/Grafo |
| INBOX_UNIVERSAL_V01 | Codex | `60_Sistemas/FabioOS/schemas/universal_intake_schema.json`, `universal_intake_adapter.py`, `universal_intake_validator.py`, examples, SPEC, relatorio e changelog | concluida | 2026-07-01 | Alinhado ao MEGATRON Core Spec v0.1; gera fila consumivel pelo Cursor com Gmail/WhatsApp/PDF fake; summary redigido para segredo; sem RAG, sem envio, sem runtime externo |
| N8N_PIETRA_DRY_RUN_BRIDGE | Codex | `60_Sistemas/n8n/scripts/pietra_whatsapp_dry_run_bridge.py`, `FabioOS_WhatsApp_Pietra_DryRun.*`, payload fake, relatorio e changelog | concluida | 2026-07-01 | Bridge n8n/Evolution -> `pietra_conversa.conversar()` em dry-run; sem envio WhatsApp, sem API externa, sem RAG e sem alterar motor Pietra |
| INTAKE_CLASSIFIER_CONVERGENCE | Codex | `60_Sistemas/FabioOS/scripts/email_intake_dry_run.py`, exemplos fake existentes, relatorio e changelog | concluida | 2026-07-01 | Email dry-run delega ao `megatron_core.classificar_intake()`; WhatsApp/PDF fake validados pelo mesmo contrato; sem acao externa e sem alterar core |
| INTAKE_DISPATCH_CONTRACT_GUARD | Codex | `intake_queue.sample.json`, `universal_intake_schema.json`, `universal_intake_validator.py`, relatorio e changelog | concluida | 2026-07-01 | IDs unicos e validador anti-duplicata para a mesa de despacho; sem tocar UI/Agentarium, sem aprovar item real, sem RAG/API/push |
| INTAKE_ADAPTER_OUTPUT_GUARD | Codex | `60_Sistemas/FabioOS/scripts/universal_intake_adapter.py`, relatorio e changelog | concluida | 2026-07-01 | Adapter escreve por padrao em fila dedicada `state/intake_queue.codex_adapter.json`; `--output` relativo validado; sem tocar fila viva, arquivista, UI, RAG/API/push |
| INTAKE_COMMAND_EXTRACTOR | Codex | `60_Sistemas/FabioOS/scripts/intake_command_extract.py`, `universal_intake_adapter.py`, relatorio e changelog | concluida | 2026-07-01 | Comando natural agora extrai produto/serie/tema/prazo e anexa `extracao` opcional; sem tocar Agentarium, arquivista, RAG/API/push |
| MEGATRON_INFRA_DISTRIBUIDA | Codex | `60_Sistemas/MEGATRON/infra/`, `80_Specs/MEGATRON/2026-07-02_infra-distribuida-hardware-megatron.md`, ADR, dashboard e changelog | concluida | 2026-07-02 | Hardware/Core/GPU/NAS modelados como nos configuraveis; nenhum servico real alterado, sem RAG reindex, sem compra, sem push |
| MEGATRON_COMPUTE_MANAGER_LLM | Codex | `60_Sistemas/MEGATRON/infra/llm_router.py`, `model_registry.example.json`, SPEC, ADR, dashboard e changelog | concluida | 2026-07-02 | LLMs/modelos formalizados por alias e politica de tarefa/custo/privacidade; nenhum modelo chamado, sem API, sem runtime, sem push |
| OPENCLAW_RECUPERACAO_BORDA | Codex | `60_Sistemas/OpenClaw/`, `80_Specs/OpenClaw/`, ADR, auditoria, dashboard e changelog | concluida | 2026-07-02 | OpenClaw reposicionado como gateway de borda opcional; diagnostico local feito; nenhum runtime/token/firewall/QR alterado, sem envio externo, sem RAG reindex, sem push |
| GARGALOS_PKM_LOOP_OPERACIONAL | Codex | `40_Wiki/FabioOS/Gargalos_Sistemicos_FabioOS_MEGATRON.md`, `60_Sistemas/Obsidian/`, `80_Specs/MEGATRON/2026-07-02_loop-operacional-fechado-megatron.md`, MOCs, dashboard e changelog | concluida | 2026-07-02 | Gargalos sistemicos formalizados como mapa PKM; links auditados com 0 destinos orfaos; sem runtime, sem API, sem RAG reindex, sem push |

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
- 2026-06-28 - `MOBILE_GATEWAY_V0` concluida. Gateway HTTP local criado para capturas via celular em `00_Inbox/mobile/`; servidor testado por `GET /health` e `POST /api/capture` com `dry_run`.
- 2026-06-28 - `GOOGLE_CATALOGOS_V0` concluida. Gmail e Google Drive catalogados por conectores em modo leitura; detalhes locais/restritos ficaram fora do Git.
- 2026-06-28 - `INVENTARIO_FERRAMENTAS_IA_V0` concluida. Script local inventariou comandos, env vars sem valores, diretorios, processos, portas e papeis recomendados para Cursor, Hermes, OpenClaw, n8n, OpenRouter, RAG e Grafo.
- 2026-06-29 - `MATRIZ_APTIDAO_IAS` concluida. Matriz formal criada para definir vocacao, limites, riscos, testes e permanencia das IAs/modelos/ferramentas do FabioOS.
- 2026-06-29 - `LLM_WIKI_OPERACIONAL` concluida. Reentrada, ADR, documento central, schema, protocolos de ingest/query/lint, index/log e dashboards RAG/MCP + LLM Wiki criados; piloto ficou pendente de autorizacao humana.
- 2026-06-29 - `PILOTO_LLM_WIKI_GOVERNANCA` concluida. Fonte de governanca preservada, pagina wiki criada, pagina LLM Wiki existente atualizada e index/log/changelog atualizados.
- 2026-06-29 - `ROADMAP_FASES_V2` concluida. As fases 0-23 foram revisadas, status real corrigido e roadmap v2 proposto ate a fase 29.
- 2026-06-29 - `FASE17_GOVERNANCA_OPERACIONAL` concluida. Constituicao, permissoes, contratos, concluido, anti-caos, seguranca, memorias, assimilacao, metadados, observabilidade, ADR e dashboard criados.
- 2026-06-29 - `SPEC_MEGATRON_V1` concluida. SPEC de ignorancia explicita, resposta com fontes e limites read-only/propose-only criada para a proxima fase tecnica.
- 2026-06-29 - `NORMALIZACAO_OBSIDIAN_V2` concluida. Auditoria, mapa canonico, plano de normalizacao e dashboard de estrutura criados; `60_Sistemas/FabioOS/bootstrap/CLAUDE.md`, Plano Mestre, Protocolo Operacional, STATUS/NEXT_ACTIONS, indices e changelog conectados; sem mover/apagar arquivos.
- 2026-06-29 - `ESTRUTURA_FISICA_LLM_WIKI` concluida. Pastas fisicas `05_Raw_Sources`, `20_Areas`, `40_Wiki`, `70_Skills` e `80_Specs` criadas com READMEs; documentos de estrutura, proposta, mapa e ADR criados; `sources` e `wiki` preservados como compatibilidade.
- 2026-06-29 - `LIMPEZA_VISUAL_RAIZ_OBSIDIAN` concluida. Pastas historicas da raiz foram movidas para `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/`; placeholders `Sem titulo` foram renomeados e arquivados; arquivos tecnicos foram ocultados na navegacao do Obsidian; `sources`, `wiki` e `schema` permanecem no disco por compatibilidade tecnica.
- 2026-06-29 - `RAG_REINDEX_POS_LIMPEZA_OBSIDIAN` concluida. `fabioos_db` foi reindexado com corpus operacional de alto sinal (`1206` chunks), caminhos reais pos-limpeza e validacao `10/10` em modo recuperacao, sem API externa.
- 2026-06-29 - `PROMOCAO_FASE12_PILOTO` concluida. Claude (arquiteto-chefe) revisou a evidencia bruta `validacao_pos_ranking_2026-06-29.json` (1206 chunks reais, 10/10 bom, 0 vazamentos) e promoveu a Fase 12 RAG a piloto via [[50_Registros/Decisoes/ADR_2026-06-29_Promocao_Fase12_RAG_Piloto]]; hardening de precisao diferido para Fase 12.1; sem reindex, sem commit, sem push.
- 2026-06-29 - `ESTRUTURA_CANONICA_COMPLETA_OBSIDIAN` concluida. A arvore preferencial do Fabio foi formalizada, `00_Inbox/Teste/` foi esvaziada com preservacao em `00_Inbox/Triagem/`, `00_Inbox/Email_para_Processar_FabioOS.md` foi movido para `00_Inbox/Processar/` e `60_Sistemas/` ficou sem arquivos `.md` soltos na raiz.
- 2026-06-30 - `PRIMUS_OPERACAO_56` concluida. Changelog 5.6 extraido do Project ChatGPT PRIMUS, formalizado e convertido em cockpit operacional minimo com Vector Engine, WorldCycle, Villain Engine, Mission Contract, Cantina Board, DeltaP Log e proxima acao validavel.
- 2026-07-01 - `PRIMUS_GOOGLE_DOC_RELEITURA` concluida. Google Doc PRIMUS relido com otica operacional atual; prioridade deslocada para R(X), ProblemGenerator, Arquivo Consultavel e operadores de mundo.
- 2026-07-01 - `PRIMUS_RPG_DOCX_RELEITURA` concluida. Google Drive `Rpg .docx` relido como fonte-mae restrita; criado mapa de digestao e CatalogEntries candidatas sem dump integral, sem RAG/reindex e sem alterar runtime.
- 2026-07-01 - `MARKDOWNIZACAO_SEGURA_E_APOSTILAS` concluida. Criada regra operacional para gerar MDs de livros e apostilas: restritos entram como stubs/CatalogEntries/abstracoes; apostilas autorais entram como conhecimento completo.
- 2026-07-01 - `PRIMUS_DND_CORE_CATALOGO` concluida. A tentativa de `10603` stubs mostrou risco de poluir o grafo; substituida por catalogo consolidado e regra de promocao seletiva.
- 2026-07-01 - `PRIMUS_CONCEITOS_LIVROS` concluida. Livros FREE renderam conceitos fortes; D&D Core gerou apenas abstracoes de design; MOC de conceitos passou a ser o hub para evitar bolinhas soltas.
- 2026-07-01 - `EMAIL_INTAKE_DRY_RUN` concluida. Diagnostico do modulo de e-mail feito; conector Gmail do Codex respondeu, mas FabioOS local nao tinha ponte; criado script dry-run para triagem restrita de payload autorizado.
- 2026-07-01 - `INBOX_UNIVERSAL_V01` concluida. Codex criou schema, adaptador, validador e payloads fake; e-mail dry-run agora tambem emite fila universal no contrato do Cursor.
- 2026-07-01 - `N8N_PIETRA_DRY_RUN_BRIDGE` concluida. Criado bridge local e workflow n8n importavel para transformar payload WhatsApp/Evolution em proposta Pietra, sempre com aprovacao humana e sem envio externo.
- 2026-07-01 - `INTAKE_CLASSIFIER_CONVERGENCE` concluida. Relatorio Markdown legado do e-mail passou a usar o mesmo MEGATRON Core da fila universal; email/WhatsApp/PDF fake foram revalidados.
- 2026-07-01 - `INTAKE_DISPATCH_CONTRACT_GUARD` concluida. Sample congelado da fila ganhou IDs unicos e o validador passou a bloquear duplicatas, protegendo os botoes Aprovar/Rejeitar do Agentarium.
- 2026-07-01 - `INTAKE_ADAPTER_OUTPUT_GUARD` concluida. `universal_intake_adapter.py` deixou de usar a fila viva como destino padrao e passou a validar `--output` relativo sem crash.
- 2026-07-01 - `INTAKE_COMMAND_EXTRACTOR` concluida. Comandos como `prova do 8o ano sobre Africa para amanha` passam a gerar `extracao` estruturada no card do Intake Universal.
- 2026-07-02 - `MEGATRON_INFRA_DISTRIBUIDA` concluida. Core, GPU, NAS e workers foram formalizados como nos por capacidade, com registry JSON, script de validacao/roteamento, SPEC, ADR e roadmap.
- 2026-07-02 - `MEGATRON_COMPUTE_MANAGER_LLM` concluida. Criado roteador v0 para escolher alias/modelo por tarefa, classe de dado, custo, qualidade e privacidade, sem chamar API.
- 2026-07-02 - `OPENCLAW_RECUPERACAO_BORDA` concluida. OpenClaw foi diagnosticado como gateway local vivo, mas ambiguo; a decisao agora e trata-lo como borda opcional com teste minimo antes de mobile/QR/WhatsApp real.
- 2026-07-02 - `GARGALOS_PKM_LOOP_OPERACIONAL` concluida. Gargalos do FabioOS/MEGATRON foram convertidos em nota evergreen, protocolo PKM de links/nos, template Obsidian e SPEC do loop operacional fechado.
