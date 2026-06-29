---
tipo: mapa-canonico
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, obsidian, pastas, taxonomia, llm-wiki, governanca]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Mapa Canonico de Pastas do Obsidian v2

## Funcao

Definir a estrutura oficial de pastas do FabioOS a partir da mentalidade LLM Wiki, RAG, MCP, MEGATRON, governanca operacional e multiplos agentes.

Este documento governa onde novos arquivos devem ser criados.

## Principio

O FabioOS nao e apenas um vault de notas.

Ele e uma arquitetura operacional com quatro camadas:

```text
captura -> fonte preservada -> conhecimento compilado -> acao governada
```

Por isso, cada pasta deve ter uma funcao unica.

## Estrutura canonica v2

| Pasta | Papel canonico | O que entra aqui | O que nao entra aqui |
|---|---|---|---|
| `00_Inbox/` | Captura temporaria | Ideias, textos, prints, entradas mobile, itens sem triagem | Conhecimento final, decisoes permanentes, scripts |
| `00_Arquitetura/` | Constituicao conceitual | Modelo formal, ontologia, epistemologia, arquitetura maior | Logs, tarefas, documentos operacionais pequenos |
| `05_Raw_Sources/` | Fonte bruta preservada | PDFs, prints, cursos, conversas, transcricoes, radar tecnologico e evidencias | Sintese final ou opiniao sem fonte |
| `10_Dashboard/` | Painel operacional | Dashboards vivos, control planes, visoes executivas | Mapas antigos puramente navegacionais |
| `20_Areas/` | Areas continuas da vida | Saude, estudos, financas pessoais, escola como area recorrente | Projetos com entrega definida |
| `30_Projetos/` | Projetos ativos | FabioOS, ProductOS, entregas com inicio/fim, iniciativas concretas | Conhecimento generico, fontes brutas |
| `40_Wiki/` | Conhecimento processado | Conceitos, sistemas, entidades, projetos, repertorios e MOCs | Dump bruto, log de sessao, codigo runtime |
| `50_Registros/` | Historico e prova | Changelogs, sessoes, auditorias, ADRs, decisoes, logs humanos | Conteudo bruto nao analisado |
| `60_Sistemas/` | Sistemas, automacoes e tecnologia | RAG, MCP, MEGATRON, n8n, OpenClaw, agentes, scripts, protocolos | Notas pessoais soltas |
| `70_Skills/` | Skills humanas e operacionais | Habilidades reutilizaveis, capacidades e guias de uso | Codigo runtime sem documentacao |
| `80_Specs/` | Specs executaveis | Planos, requisitos, riscos, aceite e testes | Ideias soltas sem escopo |
| `90_Arquivo/` | Arquivo morto ou encerrado | Materiais preservados sem uso ativo | Itens pendentes ou fontes a processar |
| `schema/` | Regras de qualidade | Schemas, criterios de qualidade, fluxos formais | Conteudo operacional diario |
| `.agents/` | Skills do Codex/FabioOS | Skills locais e comandos migrados | Documentacao humana principal |
| `.claude/` | Configuracao Claude Code | Commands, agents, hooks e config project-level | Fontes, wiki ou decisoes |
| `.codex/` | Configuracao Codex | Config e agentes do Codex | Segredos reais ou tokens |

## Pastas legadas preservadas

Estas pastas existem e nao devem ser apagadas. Elas ficam em modo legado ate migracao por lote:

| Pasta legada | Destino canonico futuro | Regra |
|---|---|---|
| `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/` | `10_Dashboard/` ou `40_Wiki/_MOCs/` | Mapas vivos viram dashboards; mapas navegacionais viram MOCs. |
| `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/` | `30_Projetos/` ou `20_Areas/` | Projetos ativos migram para `30_Projetos/`; rotinas permanentes migram para `20_Areas/`. |
| `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/30_Conhecimento/` | `40_Wiki/` | Conhecimento estruturado vira wiki processada. |
| `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Decisoes/` | `50_Registros/Decisoes/` | Decisoes futuras devem virar ADR, constituicao ou registro em `50_Registros/Decisoes/`. |
| `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Repertorio/` | `40_Wiki/` | Repertorio vira subcamada/conteudo processado na wiki. |
| `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/50_Fontes/` | `05_Raw_Sources/` | Fontes brutas novas entram em `05_Raw_Sources/`. |
| `sources/` | `05_Raw_Sources/` | Compatibilidade operacional para scripts/RAG/MCP ate migracao. |
| `wiki/` | `40_Wiki/` | Compatibilidade operacional para links/RAG/MCP ate migracao. |

## Regra para novos arquivos

Antes de criar arquivo novo, responder:

1. E entrada ainda bruta? -> `00_Inbox/` ou `05_Raw_Sources/`
2. E conhecimento compilado? -> `40_Wiki/`
3. E skill reutilizavel? -> `70_Skills/`
4. E projeto com entrega? -> `30_Projetos/`
5. E decisao, auditoria, changelog ou sessao? -> `50_Registros/`
6. E sistema, script, agente ou protocolo tecnico? -> `60_Sistemas/`
7. E painel vivo? -> `10_Dashboard/`
8. E spec executavel? -> `80_Specs/`

Se nao houver resposta clara, salvar em `00_Inbox/` e registrar pendencia de triagem.

## Regra para migracao

Migrar somente por lotes pequenos:

1. Escolher no maximo 5 arquivos.
2. Verificar links de entrada e saida com busca textual.
3. Mover com caminho explicito.
4. Atualizar links.
5. Criar nota de redirecionamento se o caminho antigo for muito citado.
6. Rodar scan de segredos se houver commit.
7. Registrar no changelog.
8. Reindexar RAG/Grafo somente apos aprovacao.

## Relacao com MEGATRON

MEGATRON deve usar este mapa como classificador de destino.

Exemplos:

- pergunta conceitual -> consultar `40_Wiki/` e, durante transicao, `wiki/`;
- decisao de arquitetura -> escrever em `50_Registros/Decisoes/`;
- automacao -> documentar em `60_Sistemas/`;
- entrada mobile -> capturar em `00_Inbox/`;
- fonte externa -> preservar em `05_Raw_Sources/` ou, enquanto houver compatibilidade, `sources/`;
- status operacional -> atualizar `10_Dashboard/`, `STATUS` e `NEXT_ACTIONS`.

## Decisao

A partir de 2026-06-29, esta e a estrutura canonica v2 do FabioOS.

Pastas legadas continuam validas como historico, mas nao devem receber novos conteudos sem motivo explicito.
