---
tipo: indice
area: FabioOS
projeto: FabioOS
status: ativo
tags: [index, llm-wiki, navegacao, agentes]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# index - FabioOS

## Funcao

Entrada semantica compacta para agentes e humanos navegarem o FabioOS antes de criar, consultar ou atualizar conhecimento.

Este arquivo nao substitui `wiki/README.md` nem `wiki/indices/mapa-fabios.md`. Ele e o ponto inicial da LLM Wiki operacional.

## Arquitetura e governanca

- [[CLAUDE]] - regras canonicas de operacao.
- [[AGENTS]] - ponteiro para agentes que leem AGENTS.md.
- [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]] - modelo formal.
- [[30_Projetos/FabioOS/LLM_Wiki_FabioOS]] - decisao operacional da LLM Wiki.
- [[60_Sistemas/FabioOS/Roadmap_Fases_FabioOS_v2_2026-06-29]] - roadmap v2 das fases do FabioOS.
- [[60_Sistemas/FabioOS/Mapa_Canonico_Pastas_Obsidian_v2_2026-06-29]] - taxonomia oficial de pastas do Obsidian.
- [[60_Sistemas/FabioOS/Plano_Normalizacao_Pastas_Obsidian_2026-06-29]] - plano de migracao segura das pastas legadas.
- [[50_Registros/Auditoria/Auditoria_Pastas_Obsidian_2026-06-29]] - auditoria das duplicacoes de nomes e numeros.
- [[10_Dashboard/Estrutura_Obsidian_FabioOS]] - painel rapido para decidir onde salvar arquivos.
- [[60_Sistemas/Wiki/Estrutura_de_Pastas_LLM_Wiki_FabioOS]] - documento principal da estrutura fisica LLM Wiki.
- [[50_Registros/Auditoria/Proposta_de_Migracao_Estrutural_FabioOS]] - proposta de migracao estrutural.
- [[50_Registros/Decisoes/ADR_Estrutura_de_Pastas_LLM_Wiki_FabioOS]] - ADR da decisao de pastas.
- [[10_Dashboard/Mapa_Estrutural_FabioOS]] - mapa visual da estrutura fisica.
- [[10_Dashboard/Governanca_FabioOS]] - painel da Fase 17 Governanca Operacional.
- [[50_Registros/Decisoes/Constituicao_Operacional_FabioOS]] - constituicao operacional.
- [[60_Sistemas/Governanca/Matriz_de_Permissoes_FabioOS]] - niveis de permissao.
- [[60_Sistemas/FabioOS/specs/2026-06-29_megatron-v1-ignorancia-explicita]] - SPEC da proxima fase tecnica do MEGATRON.
- [[50_Registros/Decisoes/ADR_FabioOS_LLM_Wiki]] - ADR da LLM Wiki.
- [[50_Registros/Auditoria/Reentrada_Codex_FabioOS]] - auditoria de reentrada.
- [[wiki/conceitos/governanca-operacional-fabios]] - conceito operacional de governanca do FabioOS.

## Wiki

- [[40_Wiki/README]] - camada-alvo de conhecimento processado.
- [[wiki/README]] - indice da pasta wiki.
- [[wiki/indices/mapa-fabios]] - mapa navegavel.
- [[90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/30_Conhecimento/LLM_Wiki_Pattern]] - fonte conceitual.
- [[60_Sistemas/Claude_Code/project_llmwiki_architecture]] - memoria de arquitetura LLM Wiki.
- [[schema/fluxo-wiki]] - fluxo minimo existente.
- [[schema/qualidade-wiki]] - criterio de qualidade existente.
- [[60_Sistemas/Wiki/Schema_Wiki_FabioOS]] - schema operacional.
- [[60_Sistemas/Wiki/Protocolo_Ingest_LLM_Wiki]] - ingest.
- [[60_Sistemas/Wiki/Protocolo_Query_LLM_Wiki]] - query.
- [[60_Sistemas/Wiki/Protocolo_Lint_LLM_Wiki]] - lint.
- [[sources/fabios/2026-06-29_governanca-operacional-pontos-cegos]] - fonte do piloto LLM Wiki de governanca.

## RAG, MCP e agentes

- [[10_Dashboard/RAG_MCP_Control_Plane]] - painel de RAG/MCP.
- [[80_Specs/README]] - camada de specs executaveis.
- [[70_Skills/README]] - camada de skills humanas e operacionais.
- [[60_Sistemas/RAG/Arquitetura_RAG_FabioOS]] - arquitetura RAG.
- [[60_Sistemas/MCP/Inventario_MCP]] - inventario MCP.
- [[60_Sistemas/MEGATRON/agentes/README_Agentes]] - agentes MEGATRON.
- [[60_Sistemas/Skills/Inventario_Skills]] - skills.
- [[90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Repertorio/IA/Modelos_e_IAs/Matriz_de_Aptidao_das_IAs_FabioOS]] - matriz de aptidao.

## Status operacional

- [[60_Sistemas/FabioOS/STATUS]] - estado atual.
- [[60_Sistemas/FabioOS/NEXT_ACTIONS]] - proximas acoes.
- [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]] - locks/frentes.
- [[50_Registros/Changelog/CHANGELOG_FabioOS]] - changelog consolidado.
- [[log]] - log cronologico da LLM Wiki.

## Regra para agentes

Antes de criar pagina nova, ler:

1. `CLAUDE.md`;
2. `index.md`;
3. `log.md`;
4. `wiki/README.md`;
5. schema/protocolo aplicavel;
6. arquivos existentes encontrados por busca.
