---
tipo: roadmap
area: FabioOS
projeto: FabioOS
status: proposto
tags: [fabios, roadmap, fases, megatron, governanca, llm-wiki, rag, mcp]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Roadmap de Fases FabioOS v2 - 2026-06-29

## Funcao

Revisar as 23 fases originais do FabioOS a partir do estado real do projeto e reformular a ordem de implantacao sem apagar o historico.

Este documento nao substitui imediatamente o [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]. Ele e uma proposta operacional v2 para corrigir status, inserir novas fundacoes e orientar as proximas frentes.

## Diagnostico

As fases 0-23 originais foram boas para iniciar o FabioOS, mas ficaram defasadas em quatro pontos:

1. **Status real mudou**: RAG, Grafo, MCP FabioOS e MEGATRON v0 ja avancaram mais do que o plano mestre indica.
2. **Governanca virou fundacao**: sem permissoes, contratos, definicao de concluido e seguranca, qualquer automacao externa aumenta risco.
3. **LLM Wiki virou arquitetura central**: conhecimento nao deve ser apenas salvo ou indexado; deve ser compilado, conectado, mantido e auditado.
4. **Ferramentas novas precisam de gate**: Cursor, Hermes, OpenClaw, OpenRouter, Google, n8n e modelos externos devem entrar por competencia, custo, risco e teste, nao por acumulacao.

## Principios da reformulacao

- Preservar fases antigas como historico.
- Corrigir status real antes de planejar novas frentes.
- Inserir governanca antes de escala.
- Separar memoria, acao, automacao, produto e dominios.
- Transformar ferramentas em capacidades testaveis.
- Manter TraderOS e PrimusOS como dominios importantes, mas depois da fundacao operacional.
- Nao promover automacao externa sem aprovacao humana, log e rollback.

## Estado real resumido

| Bloco | Estado real em 2026-06-29 |
|---|---|
| Vault, Git, Claude/Codex, skills | base criada |
| LLM Wiki inicial | criada e agora formalizada como operacional |
| EscolaOS e PietraOS | bases documentais criadas |
| n8n | workflows/desenhos existem, ativacao e reconciliacao pendentes |
| OpenClaw/Mobile | gateway/canal parcial, estabilidade pendente |
| RAG | banco local restaurado/validado; precisa governanca de RAG por dominio |
| Grafo | grafo minimo local criado/validado; dados pesados regeneraveis |
| MCP FabioOS | v0 read-only criado/configurado; depende de retestes |
| MEGATRON | v0 existe como interface minima; v1 precisa ignorancia explicita, logs e acao controlada |
| Matriz de IAs | criada; virou gate de escolha de modelos/ferramentas |
| Governanca operacional | conceito e piloto criados; camada completa ainda pendente |

## Remapeamento das fases antigas

| Fase antiga | Nome antigo | Status corrigido | Decisao v2 |
|---:|---|---|---|
| 0 | Definicao do sistema | concluida | manter historico |
| 1 | Fundacao do vault | concluida | manter historico |
| 2 | GitHub/versionamento | concluida | manter historico |
| 3 | Workstation IA | concluida | manter e revisar inventario periodicamente |
| 4 | Claude Code project-level | concluida/parcial | ampliar para Codex, skills e subagentes |
| 4.5 | Saneamento tecnico | concluida | manter como base |
| 5 | LLM Wiki inicial | concluida | promover para LLM Wiki operacional |
| 6 | Bootstrap de contexto | concluida | manter e reforcar com `10_Dashboard/_entrada/index.md`/`50_Registros/Logs_Agentes/log.md` |
| 7 | Camada 1 ferramentas | concluida | manter |
| 7.5 | Protocolo/Ingestao | concluida/parcial | unificar com protocolos LLM Wiki |
| 8 | Sistema Escola | concluida base | evoluir depois com RAG/Google/n8n |
| 8.5 | Comandos Escola | concluida base | testar em casos reais |
| 9 | Sistema Pietra | concluida base | so automatizar com permissao e aprovacao |
| 10 | n8n operacional | parcial | manter como ativacao controlada |
| 11 | OpenClaw porta externa | parcial | estabilizar antes de WhatsApp real |
| 12 | RAG | validada/local | corrigir de futuro para ativo controlado |
| 13 | Grafo | concluida/local | corrigir de futuro para ativo controlado |
| 14 | MCPs prontos | parcial | transformar em control plane |
| 15 | MCP FabioOS | v0 read-only | manter como etapa propria |
| 16 | Manus | futuro | mover para ferramenta de pesquisa, nao fase central |
| 16.5 | Cursor | instalado/manual | virar oficina de software na fase de interface/testes |
| 17 | Hermes | instalado/nao integrado | manter opcional ate provar CLI/API/logs |
| 18 | Trader | futuro | mover para dominio finalistico pos-governanca |
| 19 | PRIMUS | futuro | mover para dominio finalistico pos-governanca |
| 20 | Google | planejado/parcial catalogado | manter, mas dry-run antes de automacao |
| 21 | Dashboards | planejado | ampliar para observabilidade |
| 22 | Seguranca/permissoes | continua | promover para fase urgente |
| 23 | Producao controlada | futuro | manter depois de observabilidade |

## Roadmap v2 proposto

### Fundacao historica

| Fase | Nome | Status | Criterio de aceite |
|---:|---|---|---|
| 0 | Definicao do FabioOS | concluida | FabioOS explicado como arquitetura cognitiva operacional |
| 1 | Vault Obsidian | concluida | toda entrada tem destino inicial |
| 2 | Git/GitHub | concluida | vault versionavel e restauravel |
| 3 | Workstation IA | concluida | ferramentas principais instaladas/inventariadas |
| 4 | Agentes, skills e comandos | concluida/parcial | agentes iniciais e skills documentadas |
| 5 | LLM Wiki inicial | concluida | `05_Raw_Sources/_compat_sources/`, `40_Wiki/_compat_wiki/`, `60_Sistemas/Wiki/schema/` funcionando |
| 6 | Bootstrap de contexto | concluida | nova sessao consegue retomar por arquivos |
| 7 | Camada operacional basica | concluida | ferramentas e protocolos centrais documentados |
| 8 | EscolaOS base | concluida | templates e comandos escolares existem |
| 9 | PietraOS base | concluida | intents, respostas e regras existem |

### Infra ativa controlada

| Fase | Nome | Status | Proxima acao |
|---:|---|---|---|
| 10 | n8n controlado | parcial | reconciliar workflows, credenciais e teste dry-run |
| 11 | OpenClaw/Mobile Gateway | parcial | estabilizar auth, logs, QR e escopo antes de WhatsApp |
| 12 | RAG FabioOS | ativo/local | criar ficha tecnica, golden questions e politica de reindex |
| 13 | Grafo FabioOS | ativo/local | evoluir ontologia e filtros por dominio |
| 14 | MCPs e conectores | parcial | catalogar por risco e teste |
| 15 | MCP FabioOS | v0 read-only | retestar nativo e manter sem escrita |
| 16 | MEGATRON v1 | proxima tecnica | ignorancia explicita, roteamento, logs e acao proposta |

### Fundacao institucional obrigatoria

| Fase | Nome | Status | Entregaveis |
|---:|---|---|---|
| 17 | Governanca operacional | criada/documental | constituicao, matriz de permissoes, definicao de concluido, anti-caos, seguranca |
| 18 | Contratos de agentes | planejada | contratos para pesquisador, tecnico, documentador, revisor, escola, trader, primus, seguranca, memoria e meta |
| 19 | Padroes de memoria e metadados | planejada | separacao de memorias, frontmatter controlado, tipos de nota, politicas por dominio |
| 20 | LLM Wiki em escala | planejada | ingest/query/lint recorrentes, fontes processadas, wiki sem duplicacao |

### Integracoes profissionais

| Fase | Nome | Status | Entregaveis |
|---:|---|---|---|
| 21 | Google e email controlados | planejada/parcial | Gmail/Drive por escopo, sem envio externo, classificacao de privacidade |
| 22 | Data Platform | candidata | PostgreSQL/Supabase para tarefas, estados, custos e metadados, se dashboard exigir |
| 23 | Dashboards e observabilidade | planejada | status de agentes, RAG, MCP, n8n, OpenClaw, custos, erros e tarefas |
| 24 | Automacao persistente | planejada | n8n/Python/Hermes somente com logs, retries e aprovacao |
| 25 | Producao controlada | futuro | Docker/VPS/cloud, backup, rollback, ambientes e incidentes |

### Dominios finalisticos e produto

| Fase | Nome | Status | Observacao |
|---:|---|---|---|
| 26 | TraderOS | futuro | sem automacao financeira; foco em diario, risco e revisao |
| 27 | PrimusOS | futuro | lore, continuidade, personagens e regras |
| 28 | ProductOS | futuro | produto externo, usuarios, Stripe, Resend, PostHog, suporte |
| 29 | Local AI e Hardware Lab | futuro | so apos medir custo, privacidade, carga e necessidade real |

## Proxima ordem recomendada

1. **Revisar Fase 17 - Governanca operacional**: validar a constituicao, permissoes, contratos, concluido, anti-caos e seguranca com Claude/Fabio.
2. **Fase 16 - MEGATRON v1**: revisar [[60_Sistemas/FabioOS/specs/2026-06-29_megatron-v1-ignorancia-explicita]] e implementar ignorancia explicita e roteamento com base em RAG/Grafo/MCP, mas sem acao externa.
3. **Fase 12/13 hardening**: fichas tecnicas de RAG e Grafo, golden questions, logs e politica de reindex.
4. **Fase 21 - Google/email controlados**: dry-run por escopo pequeno, sem envio e sem leitura em massa.
5. **Fase 23 - Dashboards/observabilidade**: tornar agentes, custos, erros e tarefas visiveis.
6. **Fase 10/11 - n8n/OpenClaw ativacao**: so depois de governanca e observabilidade minima.

## Decisoes de arquitetura

### Decisao 1 - Governanca antes de automacao

Nao ativar WhatsApp, e-mail externo, workflows criticos, escrita MCP ou agente autonomo persistente antes da fase 17.

### Decisao 2 - RAG e Grafo nao sao mais futuros

RAG e Grafo ja existem. A tarefa agora nao e "criar", mas governar, testar, medir e escopar por dominio.

### Decisao 3 - MEGATRON nao e capstone distante

MEGATRON v0 ja existe como conceito/interface minima. Ele vira fase 16 porque e o sistema nervoso central que precisa coordenar as demais fases.

### Decisao 4 - Cursor e Hermes nao sao donos do sistema

Cursor e oficina de software. Hermes e opcional para persistencia. Ambos entram quando houver criterio, teste e log.

### Decisao 5 - Produto e hardware ficam depois

ProductOS, hardware local e infraestrutura cloud so entram depois de custo, privacidade, observabilidade e caso de uso real.

## Criterios para promover uma fase

Uma fase so muda para `ativa` ou `piloto` quando tiver:

1. objetivo claro;
2. entradas e saidas;
3. arquivos/protocolos criados;
4. permissao e risco definidos;
5. teste minimo executado;
6. log ou changelog;
7. proxima acao clara;
8. rollback ou forma de parar;
9. impacto em custo/privacidade avaliado;
10. referencia em STATUS/NEXT_ACTIONS.

## Lacunas abertas

- Plano mestre original precisa ser atualizado para apontar para este roadmap v2.
- Painel de pendencias precisa refletir fase 17 como prioridade.
- Governanca operacional documental foi criada; falta revisao humana e aplicacao em RAG/MCP/n8n/OpenClaw.
- MEGATRON v1 ainda precisa de spec.
- RAG/Grafo precisam de fichas tecnicas e golden questions por dominio.
- n8n/OpenClaw precisam de ativacao com observabilidade, nao so configuracao.
- Cursor e Hermes precisam de criterio pratico de entrada.

## Recomendacao final

O FabioOS deve parar de tentar "adicionar mais uma ferramenta" por algumas rodadas e consolidar a instituicao interna.

Ordem recomendada:

```text
Governanca -> MEGATRON v1 -> RAG/Grafo/MCP hardening -> Google/email dry-run -> Dashboard/observabilidade -> n8n/OpenClaw controlados -> dominios/produto
```

Isso preserva ambicao sem virar caos.
