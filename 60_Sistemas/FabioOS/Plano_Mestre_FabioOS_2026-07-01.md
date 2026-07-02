---
tipo: plano-mestre
area: 60_Sistemas
projeto: FabioOS
status: ativo
autor: Claude (arquiteto-chefe)
criado_em: 2026-07-01
atualizado_em: 2026-07-01
tags: [fabios, plano-mestre, frentes, feito-nao-feito, governanca, continuidade]
---

# Plano Mestre FabioOS — todas as frentes, feito × não-feito

> **O documento que responde:** o que existe, o que funciona, o que falta, quem é o
> dono, o que espera decisão do Fabio. Snapshot factual de 2026-07-01 (exploração
> completa do vault: 27 subsistemas, 108 frentes no Registro, 14 specs, 4 Bugbots).

## §1 Como ler / como manter

- **Substitui** o [[60_Sistemas/FabioOS/Roadmap_Fases_FabioOS_v2_2026-06-29|Roadmap v2]] (histórico) e a lista fóssil do NEXT_ACTIONS antigo.
- Legenda: ✅ feito · 🟢 funcional validado · 🟡 parcial · 📄 só documentado · ⛔ bloqueado · 💤 dormindo
- **Manutenção:** atualizar a cada marco (não a cada commit). Frente nova nasce AQUI, com dono e bloco. Item concluído muda de emoji, não some.
- Complementos vivos: [[60_Sistemas/FabioOS/STATUS|STATUS]] (estado macro) · [[60_Sistemas/FabioOS/Registro_Frentes_Ativas|Registro de Frentes]] (locks) · `coordenacao.py` (tempo real) · [[10_Mapas/Dashboard_Operacional_FabioOS|Dashboard Operacional]] (auto-gerado).

## §2 Estado macro (blocos A–F)

| Bloco | Estado | Uma linha |
|---|---|---|
| A · Fundação | ✅ | vault, git, agentes, LLM-Wiki, bases — concluído |
| B · Infra ativa | 🟢 | RAG piloto (1206 chunks 10/10), Grafo (840 nós), MCP read-only, MEGATRON v1 (golden 20/20) |
| C · Intake Universal | 🟢 | loop PROVADO nas 3 fontes: core→fila→aprovação→Obsidian; mesa v0.9.0; chat profissional |
| D · Verticais | 🟡 | Pietra multi-tenant funcional (dry-run) · EscolaOS templates sem uso real · PRIMUS 100% spec / 0% executável |
| E · Governança | 🟢 | barramento, locks, redação de segredo, ADRs, Bugbot 4 ondas |
| F · Futuro (gated) | ⛔ | canais reais, n8n ativo, push, produção — aguardam decisões do Fabio (§4) |

## §3 Inventário feito × não-feito (27 sistemas)

| Sistema | Dono | Estado | Evidência | O que falta |
|---|---|---|---|---|
| MEGATRON v1 (core+maestro+registry+reasoningbank) | claude | 🟢 | golden 20/20; boots v1.0 registrados 01/07 | daemon/agendamento (spec orchestrator) |
| MEGATRON intake (core/flow/arquivista/chat_bridge/coordenacao) | claude | 🟢 | prova §9 nas 3 fontes; testes ao vivo 01/07 | redigir `summary` no próprio megatron_core (Bugbot O2) |
| RAG | claude | 🟢 | 1206 chunks; 10/10; 0 vazamentos (29/06) | hardening 12.1 (MAX_CHARS) em janela de CPU livre; ficha técnica |
| Grafo | claude | 🟢 | 840 nós/2680 arestas; 0 falhas auditoria | ontologia por domínio (fase 13.x) |
| MCP_FabioOS | claude | 🟢 | server.py read-only rodando (2 instâncias) | encerrar/renovar frente no Registro; retestes |
| Wiki / LLM-Wiki | claude | 🟡 | schema+protocolos ingest/query; piloto executado | protocolo lint nunca rodado |
| Pietra (chatbot escolar) | codex | 🟢 | multi-tenant 5+ instâncias; bridge WhatsApp dry-run (002c1165) | canal real (gate ③); tenant piloto |
| n8n | codex | 🟡 | 6 workflows importáveis; Docker :5678 validado | sem Gmail Trigger; tudo inativo (correto até gate) |
| Email intake | codex | 🟡 | script+adapter+validator ok; convergido ao core (aada1ea1) | **upstream Gmail desconectado** (elo sensor nº1); unificar formato de id com intake_flow |
| PDF pipeline | claude/codex | 🟢 | drop folder+watcher+PyMuPDF; 5 PDFs processados | plugar classificação automática no drop; OCR Stirling (auth 401, Fabio) |
| OpenClaw | codex | 🟡 | tray ativo; ADR 02/07 reposiciona como gateway de borda | teste mínimo do ADR: OpenClaw→Intake→Agentarium→aprovação |
| Agentarium (backend+frontend) | cursor | 🟢 | v0.9.0: mesa de despacho E2E, 21 componentes, chat | telefone hardcoded config.ts L49→env; badge de modelo; histórico do chat por sessão |
| Chat MEGATRON | claude/cursor | 🟢 | olhos+memória+haiku-4.5 (4f2b80f6), testado ao vivo | avaliar Sonnet p/ conversa; limpar histórico ao recarregar |
| Coordenação (readout+barramento) | claude | 🟢 | coordenacao.py; barramento 78+ msgs | disciplina `status: resolvido` (ninguém fecha msgs) |
| EscolaOS | codex | 📄 | 4 templates prontos (PROVA/REVISAO/GABARITO/COMUNICADO) | **nunca usados em prova real** (gate ⑦) |
| PRIMUS specs/catálogo | codex | 🟢 | 20 specs; Index 10788 regs; 14 conceitos; V(E) pass | — |
| PRIMUS Missão 0001 | codex | ⛔ | rascunhos criados | 7 lacunas: fichas, mapa, 20 CatalogEntries reais, Vector Engine, WorldCycle, conflito detalhado, contrato YAML |
| PRIMUS Digestor | codex | 🟡 | scripts 01-06 + schema + smoke test | rodar lote pequeno real |
| Mobile Gateway | codex | 🟡 | porta 8787 funcional na LAN | teste real do celular; captura→intake |
| Google conectores | codex | 📄 | Gmail/Drive catalogados read-only (28/06) | export automático (mesmo elo do Email); gate ② |
| OpenRouter (roteador) | codex | 🟡 | llm_router.py+node_registry local; chat usa API real | teto de custo formal (gate ⑥); matriz por tarefa |
| Scripts operacionais | codex | 🟢 | launchers, health, smoke tests (8 arquivos) | — |
| Observabilidade | codex | 🟢 | reality_check + Dashboard auto (01/07); jardinagem 02/07 | 504 links quebrados a reduzir (era 529) |
| Memória pessoal/profissional | codex | 📄 | protocolo em desenho; piloto Gmail 3 threads feito | decidir se memória consolidada entra no RAG |
| Governança/protocolos/segurança | claude | 🟢 | locks, matriz permissões, anti-caos, redação validada | e-mails pessoais versionados no wiki (gate ④) |
| GitHub/versionamento | claude | 🟡 | 19 commits locais na branch coordenador | **push pendente** + blobs PDF ~19MB na história (gate ①) |
| TraderOS / Escola_SaaS / ProductOS | — | 💤 | só conceito | pós-consolidação (por design) |

## §4 Pendências por dono (acionável)

### Claude (eu)
1. Redigir `summary` dentro do `megatron_core.py` (hoje intake_flow/adapter redigem; o core cru vaza se chamado direto) — achado Bugbot Onda 2
2. Ficha técnica do RAG + hardening 12.1 com lock (janela de CPU livre)
3. Encerrar/renovar frente `MCP_FABIOOS` e marcar `INTERINATO_CODEX` como encerrada no Registro (zumbi desde 29/06)

### Codex
1. **Elo sensor nº1:** export Gmail→adapter (hoje o e-mail só anda com payload manual)
2. Unificar formato de id entre `intake_flow` e `universal_intake_adapter` (timestamp+hash × stable_hash)
3. Bugbot Onda 3 (contratos duplicados) quando Fabio autorizar; teste mínimo do ADR OpenClaw

### Cursor
1. Telefone real hardcoded em `apps/agentarium/backend/src/whatsapp/config.ts` L49 → env var (achado Bugbot O2)
2. Badge de modelo no chat + limpar histórico ao recarregar página
3. Bugbot Ondas 3–7 (aguarda gate ⑤)

### Fabio — decisões abertas (os 7 gates)
| # | Decisão | Contexto |
|---|---|---|
| ① | Push + limpeza de blobs | 19 commits locais sem backup remoto; 3 PDFs (~19MB) na história — limpar antes de push? |
| ② | Autorizar Gmail real | destrava o elo sensor nº1 (conta, escopo leitura) |
| ③ | Canal WhatsApp Pietra real | bridge dry-run pronta; definir tenant piloto |
| ④ | E-mails pessoais versionados no wiki | Bugbot O2 achou metadados versionados — aceitar ou mover p/ _restrito? |
| ⑤ | Autorizar Bugbot Ondas 3–7 | plano do Cursor pronto (contratos, scripts, RAG, Agentarium, doc×runtime) |
| ⑥ | Teto de custo OpenRouter | chat já usa haiku-4.5 (~$0.004/msg); formalizar limite mensal |
| ⑦ | Primeira prova real EscolaOS | templates prontos há 5 dias; 1 prova de Geografia destrava a vertical |

## §5 Ordem recomendada (arquiteto)

```text
1º  Fechar elos quebrados do intake ....... Gmail upstream + ids (Codex) + summary core (Claude)
2º  Decisões do Fabio em lote ............. os 7 gates de §4 (uma sessão de decisão)
3º  Piloto REAL ........................... EscolaOS 1ª prova OU tenant Pietra (o que ① e ③ liberarem)
4º  Consolidação .......................... Bugbot Ondas 3-7, hardening RAG, lint wiki, links quebrados
5º  PRIMUS marco funcional ................ as 7 lacunas da Missão 0001
```
**Justificativa:** o produto está a **1 elo** (sensor real) de operar ponta a ponta. Tudo o mais é ampliação; isto é destravamento.

## §6 Validações vivas (retestar em retomadas)

| Sistema | Teste versionado | Último resultado |
|---|---|---|
| RAG | `batch_validate_rag.py` / validacao_pos_ranking JSON | 10/10 bom, 0 vazamentos (29/06) |
| MEGATRON v1 | `v1/tests/golden_questions.py` | 20/20 (30/06) |
| Grafo | `audit_graph.py` | 0 falhas (27/06) |
| Intake Universal | `intake_flow.py` + `examples/prova_3fontes_fake.json` | 3 fontes provadas; trava §3 recusa sensível (01/07) |
| Mesa de Despacho | ciclo E2E do Bugbot v0.9.0 | approve/reject→arquivista ok (01/07) |
| Chat | `chat_bridge.py "status"` + endpoint /integrations/megatron/chat | bridge+haiku ao vivo (01/07) |
| Segurança | scan de linhas adicionadas pré-commit + injeções RAG | 0 credencial exposta |

## Relações
[[60_Sistemas/FabioOS/STATUS]] · [[60_Sistemas/FabioOS/NEXT_ACTIONS]] · [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]] · [[50_Registros/Barramento_Multiagente]] · [[50_Registros/Relatorios/Diagnostico_Operacional_Intake_Universal_2026-07-01_Claude]] · [[10_Mapas/Dashboard_Operacional_FabioOS]]
