---
tipo: painel
area: 10_Mapas
projeto: FabioOS
status: ativo
tags: [pendencias, backlog, roadmap, controle, trilhos]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Painel de Pendências do FabioOS

## Função

Fonte única e versionada de tudo que está **aberto, deixado para trás ou planejado** no FabioOS. Garante que nenhuma pendência se perca entre sessões. Deve ser lido no início de cada sessão, junto com o último changelog.

> **Regra:** uma pendência só sai daqui quando for concluída (vira changelog) ou descartada (com motivo registrado).

## Contexto

Criado após a migração da operação para o Claude Desktop (Fase 11). Reflete a decisão de organizar o trabalho futuro em **trilhos** — pessoal/aprendizado primeiro, empresarial em seguida — com Trader e PRIMUS movidos para o final.

**Marco (2026-06-27):** caminho crítico ao MEGATRON ligado de ponta a ponta — RAG (12) + Grafo (13) + MCP FabioOS (15) + **MEGATRON v0** (capstone). **Próximo:** MEGATRON v1 (Ignorância Explícita por limiar) → depois trilho empresarial (Pietra/n8n).

**Marco (2026-06-29):** as fases 0-23 foram revisadas no [[60_Sistemas/FabioOS/Roadmap_Fases_FabioOS_v2_2026-06-29]]. A prioridade operacional passa a ser Governanca Operacional antes de escalar automacoes externas.

---

## 1. Pendências abertas (não esquecer)

Itens já iniciados ou identificados que aguardam conclusão.

- [ ] **[Fase 10]** Importar `FabioOS_Webhook_Inbox.json` no n8n → configurar credencial Obsidian API → ativar → testar com curl
- [ ] **[Fase 11]** Instalar Evolution API (Docker porta 8080) → criar instância → QR Code WhatsApp → webhook→n8n → importar `FabioOS_WhatsApp_Pietra.json` → ativar → testar
- [ ] **[n8n]** Reconciliar nomes: changelog cita "webhook-inbox", mas o n8n real tem `FabioOS — Webhook Arquivista` (ativo) e `FabioOS — Captura para Obsidian` (inativo)
- [ ] **[Segurança]** Migrar `GITHUB_TOKEN` hardcoded em `~/.claude/settings.json` para variável de ambiente
- [ ] **[Ingestão]** Implementar `/ingest-drive-doc` (depende de MCP Google Drive) e `/ingest-repo`
- [ ] **[Wiki]** Criar páginas: `conceitos/rag.md`, `conceitos/llm-wiki.md`, `sistemas/mcp-servers.md`, `projetos/trader.md`
- [ ] **[Arquitetura]** Derivar ontologia operacional do `00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON.md` quando iniciar Fase 13 — Grafo
- [ ] **[RAG]** Reexecutar as 10 perguntas do `60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG.md` apos ajuste de ranking/recencia
- [ ] **[Fase 17]** Criar Governanca Operacional completa: Constituicao, Matriz de Permissoes, Contratos de Agentes, Definicao de Concluido, Anti-Caos e Seguranca
- [ ] **[Roadmap]** Revisar o Roadmap v2 com Claude/Fabio e decidir se vira roadmap oficial
- [ ] **[Obsidian]** Executar migracao piloto pequena seguindo [[50_Registros/Auditoria/Proposta_de_Migracao_Estrutural_FabioOS]]
- [ ] **[Memória]** Absorver ChatGPT/e-mails por protocolo seguro: ver [[40_Wiki/_compat_wiki/memoria/Mapa_Memoria_Fabio]] e [[60_Sistemas/FabioOS/Protocolo_Ingestao_Memoria_Pessoal_Profissional]]
- [ ] **[Gmail profissional]** Solicitar autorização/conector antes de qualquer acesso ao e-mail `fabiofilosofia@colegiopietra.com.br`
- [ ] **[Escola]** Criar cronograma bimestral GEO e FIL 2026
- [ ] **[QA]** Testar cada comando `.claude/` com caso real

---

## 2. Roadmap por trilho

Ordem de execução acordada: **🧠 Pessoal/Aprendizado → 💼 Empresarial → 🔚 Final**. Infra transversal entra conforme exigida pelos outros trilhos.

### 🧠 Trilho Pessoal / Aprendizado — *prioridade atual*

- [x] **Fase 12 — RAG** — validada 10/10 (modo recuperação); v1 do MEGATRON tratará ignorância por limiar
- [x] **Fase 13 — Grafo de conhecimento** — 840 nós, 2680 arestas; ver [[60_Sistemas/Grafo/README_Grafo]]

### 💼 Trilho Empresarial / Profissional

- [ ] **Fase 10 — n8n** (ativação — ver pendências abertas)
- [ ] **Fase 11 — Pietra / WhatsApp** (ativação — ver pendências abertas)
- [ ] **Fase 20 — Integração Google** (Gmail, Drive, Calendar)
- [ ] **Fase 21 — Dashboards** (Escola, FabioOS)
- [ ] **Fase 23 — Produção controlada**

### ⚙️ Infra transversal (serve aos dois trilhos)

- [~] **Fase 14 — MCPs prontos** (filesystem/github/n8n/obsidian ativos)
- [x] **Fase 15 — MCP customizado FabioOS** (FastMCP, 5 ferramentas read-only, testado) — ver [[60_Sistemas/MCP_FabioOS/README_MCP_FabioOS]]
- [ ] **Fase 17 — Governanca Operacional** (prioridade v2)
- [ ] **Fase 22/23 — Seguranca, permissoes, dashboards e observabilidade** (continua)

### 🎯 Capstone — Interface do FabioOS

- [x] **MEGATRON v0** — interface mínima read-only/propose-only: roteia + consulta RAG/Grafo com fontes. Ver [[60_Sistemas/MEGATRON/v0/README_MEGATRON_v0]]
- [ ] **MEGATRON v1+** — Ignorância Explícita por limiar, síntese com aprovação, ação→agentes, interface visual

### 🔚 Final (movidos a pedido do Fabio)

- [ ] **Fase 18 — Sistema Trader**
- [ ] **Fase 19 — Sistema PRIMUS**

---

## 3. Concluído recentemente

- [x] Migração da operação para Claude Desktop — [[60_Sistemas/Claude_Code/Operacao_no_Claude_Desktop]]
- [x] Modelo Formal do FabioOS/MEGATRON — [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]]
- [x] Governança e revisão multiagente — [[60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente]]
- [x] Validação parcial RAG — ingestão restaurada com `1795` chunks e 10 perguntas testadas em modo recuperação; ver [[60_Sistemas/RAG/Relatorio_Validacao_RAG_2026-06-27]]
- [x] **Grafo (Fase 13)** — 840 nós, 2680 arestas; ver [[60_Sistemas/Grafo/README_Grafo]]
- [x] **MCP FabioOS (Fase 15) + MEGATRON v0 (capstone)** — caminho crítico ligado ponta a ponta; ver [[50_Registros/Changelog/2026-06-27_capstone-megatron-v0]]
- [x] **Protocolo de memória pessoal/profissional** — estrutura criada sem leitura de corpo de e-mail profissional; ver [[60_Sistemas/FabioOS/Inventario_Memoria_Pessoal_Profissional_2026-06-27]]
- [x] **Normalizacao Obsidian v2** — mapa canonico de pastas criado; pastas legadas preservadas; migracao fisica adiada para piloto seguro. Ver [[60_Sistemas/FabioOS/Mapa_Canonico_Pastas_Obsidian_v2_2026-06-29]]
- [x] **Estrutura fisica LLM Wiki** — pastas `05_Raw_Sources`, `20_Areas`, `40_Wiki`, `70_Skills` e `80_Specs` criadas com READMEs; `sources` e `wiki` preservadas como compatibilidade. Ver [[10_Dashboard/Mapa_Estrutural_FabioOS]]
- [x] Fases 0–9 (fundação → Pietra) — ver `50_Registros/Changelog/`
- [x] Visão de Interface registrada — [[60_Sistemas/FabioOS/Visao_Interface_FabioOS]]

---

## Como usar

1. No início da sessão: ler este painel + o último changelog.
2. Ao concluir uma pendência: marcar `[x]`, mover para a seção 3 e gerar changelog.
3. Ao descartar: remover com motivo registrado em `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Decisoes/` ou `50_Registros/`.
4. Ao surgir nova pendência: adicionar na seção 1 com a etiqueta `[Fase X]` ou `[Área]`.

## Relações

- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]
- [[60_Sistemas/FabioOS/Roadmap_Fases_FabioOS_v2_2026-06-29]]
- [[60_Sistemas/FabioOS/Visao_Interface_FabioOS]]
- [[60_Sistemas/Claude_Code/Operacao_no_Claude_Desktop]]
- [[40_Wiki/_compat_wiki/indices/mapa-fabios]]

## Próximas ações

- [ ] Repetir validação RAG completa após ajuste de ranking seguindo [[60_Sistemas/FabioOS/Roteiro_Execucao_Fase12_RAG]]
- [ ] Atualizar `60_Sistemas/FabioOS/bootstrap/CLAUDE.md` para incluir este painel na leitura obrigatória de início de sessão
- [ ] Atualizar `Plano_Mestre` refletindo Trader/PRIMUS no final e a Interface como capstone
