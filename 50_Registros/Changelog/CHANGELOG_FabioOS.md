---
tipo: changelog
area: FabioOS
projeto: FabioOS
status: ativo
tags: [changelog, fabios, governanca, llm-wiki]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# CHANGELOG FabioOS

## 2026-06-29 - LLM Wiki operacional

Adotada a mentalidade LLM Wiki como camada central de memoria do FabioOS, distinguindo fontes brutas, wiki compilada, schema, ingest, query, lint, index, log, RAG, MCP, MEGATRON e multiplos cerebros especializados.

Arquivos principais:

- `30_Projetos/FabioOS/LLM_Wiki_FabioOS.md`
- `50_Registros/Decisoes/ADR_FabioOS_LLM_Wiki.md`
- `60_Sistemas/Wiki/Schema_Wiki_FabioOS.md`
- `60_Sistemas/Wiki/Protocolo_Ingest_LLM_Wiki.md`
- `60_Sistemas/Wiki/Protocolo_Query_LLM_Wiki.md`
- `60_Sistemas/Wiki/Protocolo_Lint_LLM_Wiki.md`
- `10_Dashboard/RAG_MCP_Control_Plane.md`
- `10_Dashboard/LLM_Wiki_FabioOS.md`
- `index.md`
- `log.md`

Restricoes respeitadas:

- sem commit;
- sem push;
- sem chamadas externas;
- sem reindexacao RAG;
- sem MCP runtime;
- sem n8n/OpenClaw externo;
- sem alterar credenciais.

## 2026-06-29 - Piloto LLM Wiki de governanca

Executado piloto pequeno da LLM Wiki no dominio FabioOS/Governanca.

Entrega:

- fonte preservada em `sources/fabios/2026-06-29_governanca-operacional-pontos-cegos.md`;
- pagina wiki criada em `wiki/conceitos/governanca-operacional-fabios.md`;
- pagina existente `30_Projetos/FabioOS/LLM_Wiki_FabioOS.md` atualizada com resultado do piloto;
- `index.md` e `log.md` atualizados;
- dashboard LLM Wiki e NEXT_ACTIONS atualizados.

Restricoes respeitadas:

- sem API externa;
- sem RAG reindex;
- sem MCP runtime;
- sem automacao n8n/OpenClaw;
- sem commit;
- sem push.

## 2026-06-29 - Roadmap Fases FabioOS v2

Revisadas as fases 0-23 contra o estado real do FabioOS.

Resultado:

- criado `60_Sistemas/FabioOS/Roadmap_Fases_FabioOS_v2_2026-06-29.md`;
- Plano Mestre passa a apontar para o Roadmap v2 como orientacao operacional atual;
- Painel de Pendencias passa a registrar Governanca Operacional como prioridade;
- RAG, Grafo, MCP FabioOS e MEGATRON v0 deixam de ser tratados como futuro abstrato e passam a ser capacidades ativas/controladas;
- fases novas foram propostas ate 29 para acomodar governanca, observabilidade, producao, ProductOS, TraderOS, PrimusOS e Local AI/Hardware Lab.

Restricoes respeitadas:

- sem commit;
- sem push;
- sem runtime externo;
- sem API externa;
- sem reindexacao.

## 2026-06-29 - Fase 17 Governanca Operacional

Criada a camada documental de Governanca Operacional do FabioOS.

Arquivos principais:

- `50_Registros/Decisoes/Constituicao_Operacional_FabioOS.md`
- `60_Sistemas/Governanca/Matriz_de_Permissoes_FabioOS.md`
- `60_Sistemas/Agentes/Contratos_de_Agentes_FabioOS.md`
- `60_Sistemas/Protocolos/Definicao_de_Concluido_FabioOS.md`
- `60_Sistemas/Protocolos/Protocolo_Anti_Caos_FabioOS.md`
- `60_Sistemas/Seguranca/Protocolo_de_Seguranca_FabioOS.md`
- `60_Sistemas/Memoria/Separacao_de_Memorias_FabioOS.md`
- `60_Sistemas/Conhecimento/Motor_de_Assimilacao_FabioOS.md`
- `60_Sistemas/Padroes/Padrao_de_Metadados_FabioOS.md`
- `60_Sistemas/Observabilidade/Metricas_e_Observabilidade_FabioOS.md`
- `50_Registros/Decisoes/ADR_FabioOS_Governanca_Operacional.md`
- `10_Dashboard/Governanca_FabioOS.md`

Restricoes respeitadas:

- sem runtime externo;
- sem API externa;
- sem alteracao de credenciais;
- sem automacao;
- sem commit;
- sem push.

## 2026-06-29 - SPEC MEGATRON v1

Criada a SPEC do MEGATRON v1 com Ignorancia Explicita.

Arquivo:

- `60_Sistemas/FabioOS/specs/2026-06-29_megatron-v1-ignorancia-explicita.md`

Escopo:

- consulta a memoria antes de responder;
- uso de RAG/Grafo/MCP read-only;
- limiar de confianca;
- resposta "nao sei ainda" quando nao houver fonte;
- proibicao de acao externa por padrao;
- logs e criterios de aceite.

Restricoes respeitadas:

- sem codigo;
- sem runtime;
- sem API externa;
- sem push.

## 2026-06-29 - Normalizacao de pastas Obsidian v2

Criada a camada de governanca de pastas para resolver incongruencias entre a estrutura historica do vault e a estrutura profissional/LLM Wiki.

Arquivos principais:

- `50_Registros/Auditoria/Auditoria_Pastas_Obsidian_2026-06-29.md`
- `60_Sistemas/FabioOS/Mapa_Canonico_Pastas_Obsidian_v2_2026-06-29.md`
- `60_Sistemas/FabioOS/Plano_Normalizacao_Pastas_Obsidian_2026-06-29.md`
- `10_Dashboard/Estrutura_Obsidian_FabioOS.md`

Decisao:

- `05_Raw_Sources/`, `10_Dashboard/`, `20_Areas/`, `30_Projetos/`, `40_Wiki/`, `50_Registros/`, `60_Sistemas/`, `70_Skills/`, `80_Specs/` e `90_Arquivo/` passam a ser destinos canonicos v2;
- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/`, `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/`, `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/30_Conhecimento/`, `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Decisoes/` e `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/50_Fontes/` ficam preservadas como pastas legadas;
- nao houve migracao fisica em massa;
- migracoes futuras devem ser pequenas, com revisao de backlinks e changelog.

Restricoes respeitadas:

- sem apagar arquivos;
- sem mover pastas;
- sem reindexar RAG;
- sem regenerar Grafo;
- sem commit;
- sem push.

## 2026-06-29 - Estrutura fisica LLM Wiki

Criada a estrutura fisica v1 do FabioOS na mentalidade LLM Wiki.

Pastas materializadas:

- `05_Raw_Sources/`
- `20_Areas/`
- `40_Wiki/`
- `70_Skills/`
- `80_Specs/`

Documentos principais:

- `60_Sistemas/Wiki/Estrutura_de_Pastas_LLM_Wiki_FabioOS.md`
- `50_Registros/Auditoria/Proposta_de_Migracao_Estrutural_FabioOS.md`
- `10_Dashboard/Mapa_Estrutural_FabioOS.md`
- `50_Registros/Decisoes/ADR_Estrutura_de_Pastas_LLM_Wiki_FabioOS.md`

Decisao:

- a estrutura nova passa a aparecer fisicamente no Obsidian;
- `sources/` e `wiki/` continuam preservados como compatibilidade operacional;
- nenhuma pasta antiga foi apagada;
- nenhum conteudo foi movido em massa;
- migracao real deve ocorrer por lote pequeno.

Restricoes respeitadas:

- sem apagar arquivos;
- sem mover `sources/` ou `wiki/`;
- sem reindexar RAG;
- sem regenerar Grafo;
- sem push.

## 2026-06-29 - Limpeza visual da raiz Obsidian

Executada a organizacao fisica da raiz do vault para reduzir duplicidade visual no Obsidian e alinhar a estrutura ao modelo LLM Wiki.

Movido para arquivo legado:

- `10_Mapas/`
- `20_Projetos/`
- `30_Conhecimento/`
- `40_Decisoes/`
- `40_Repertorio/`
- `50_Fontes/`
- `PRIMUS_Obsidian_Starter_v0_1/`

Destino:

- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/`

Arquivos soltos reorganizados:

- `RELATORIO_VALIDACAO_LINKS.md` -> `50_Registros/Relatorios/RELATORIO_VALIDACAO_LINKS.md`
- `Sem titulo*.base/canvas` -> `90_Arquivo/Descartes_Visuais_Obsidian_2026-06-29/` com nomes neutros de placeholder

Ocultado na navegacao do Obsidian via `.obsidian/app.json`:

- `AGENTS.md`
- `CLAUDE.md`
- `CODEX.md`
- `README.md`
- `log.md`
- `start_fabioos.ps1`
- `sources/`
- `wiki/`
- `schema/`
- diretorios tecnicos de agentes/configuracao

Decisao:

- nenhuma pasta ou arquivo foi apagado;
- `sources/`, `wiki/` e `schema/` permanecem na raiz por compatibilidade tecnica;
- backlinks textuais foram atualizados quando apontavam para caminhos legados;
- migracoes de conteudo util do legado devem ocorrer por lotes pequenos.

Restricoes respeitadas:

- sem apagar arquivos;
- sem reindexar RAG;
- sem regenerar Grafo;
- sem push.

## 2026-06-29 - Estrutura canonica completa Obsidian

Formalizada e aplicada a arvore visual solicitada pelo Fabio para o vault.

Criado:

- `60_Sistemas/FabioOS/Estrutura_Canonica_Completa_Obsidian_2026-06-29.md`

Reorganizado:

- `00_Inbox/Email_para_Processar_FabioOS.md` foi movido para `00_Inbox/Processar/`;
- `00_Inbox/Teste_MCP_Obsidian.md` e notas de teste de `00_Inbox/Teste/` foram preservadas em `00_Inbox/Triagem/`;
- `00_Inbox/Inbox.md` foi preservado em `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/00_Inbox/`;
- arquivos soltos de `60_Sistemas/` foram movidos para subpastas coerentes.

Resultado:

- `00_Inbox/` ficou alinhada as quatro gavetas canonicas;
- `60_Sistemas/` ficou sem arquivos `.md` soltos na raiz;
- caminhos textuais conhecidos foram atualizados;
- nada foi apagado;
- sem RAG/Grafo/OpenClaw/n8n/push.
