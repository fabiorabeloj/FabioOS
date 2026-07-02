---
tipo: status
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, status, continuidade, multiagente, intake-universal]
criado_em: 2026-06-27
atualizado_em: 2026-07-01
---

# STATUS — FabioOS

> **Estado canônico de continuidade.** Qualquer sessão retoma por aqui + `NEXT_ACTIONS.md`
> + `50_Registros/Barramento_Multiagente.md`. Reescrito em 2026-07-01 (o conteúdo
> anterior 27–29/06 estava defasado; histórico preservado no Git).

## 1. O que o FabioOS é hoje

Arquitetura cognitiva operacional do Fabio, com **3 cérebros** coordenados por arquivos:
- **Claude** = arquiteto-chefe / governança / MEGATRON Core / RAG / MCP.
- **Codex** = engenharia / infra / schema / conectores / PRIMUS.
- **Cursor** = interface / Agentarium / revisão (Bugbot).

A **espinha do produto** deixou de ser "instalar ferramentas" e passou a ser o
**INTAKE UNIVERSAL + controle humano** (MEGATRON Core Spec v0.1): toda entrada de
qualquer canal → normaliza → classifica → sensibilidade → domínio → agente →
proposta → **aprovação humana** → log → memória. Nada externo/sensível age sozinho.

## 2. Estrutura real em BLOCOS (substitui a lista de 23/30 fases numeradas)

| Bloco | Frente | Estado | Dono |
|---|---|---|---|
| **A · Fundação** | vault, Git, agentes/skills, LLM-Wiki, bases EscolaOS/PietraOS | ✅ concluído | Claude/Codex |
| **B · Infra ativa** | RAG (piloto, 1206 chunks, 10/10), Grafo mínimo, MCP read-only (5 tools), MEGATRON v1 Maestro (golden 20/20) | 🟢 ativo/piloto | Claude |
| **C · Intake Universal** | Core Spec v0.1, `megatron_core.py` (classificador), `intake_flow.py` (**prova §9 fechada**), schema+adapter+conectores, fila secretário | 🟡 **em prova** (espinha atual) | Claude+Codex+Cursor |
| **D · Verticais/produto** | PietraOS (chatbot escolar multi-tenant, LGPD), EscolaOS (Geo+Filo), PRIMUS (RPG, runtime+index 10788 regs) | 🟢 em construção | Codex/Claude |
| **E · Governança/segurança** | Barramento multiagente, locks, redação de segredo, ADR Nota-vs-Dado, política LGPD | 🟢 contínuo | Claude |
| **F · Futuro (gated)** | canais reais (WhatsApp/Gmail), n8n ativo, dashboards/observabilidade, TraderOS, produção Docker/VPS | 🔒 bloqueado até prova + aprovação | — |

**Resposta à pergunta "ainda são 23 fases?":** não. O plano original (0–23) já tinha sido
remapeado para 30 fases numeradas (v2, 29/06) e mesmo esse ficou obsoleto com o pivô para
o Intake Universal. A numeração virou ruído; a estrutura real são os **6 blocos acima**.
O roadmap v2 continua como histórico em `Roadmap_Fases_FabioOS_v2_2026-06-29.md`.

**Inventário completo feito × não-feito (27 sistemas, pendências por dono, 7 gates do
Fabio, ordem recomendada):** [[60_Sistemas/FabioOS/Plano_Mestre_FabioOS_2026-07-01|PLANO MESTRE]] ← fonte canônica de "o que falta".

## 3. Onde o Bloco C (foco) está agora — LOOP FECHADO (fim de 2026-07-01)

- ✅ **Claude:** Core Spec + classificador + prova §9 nas **3 fontes** (gmail/whatsapp/pdf)
  + **arquivista** (aprovação humana → nota no Obsidian; trava §3: sensível nunca vira nota)
  + **chat_bridge** (o chat do Agentarium ganhou olhos/memória: status, fila, aprova <id>,
  manda pro <agente>, tarefa natural) + `coordenacao.py` (readout multiagente).
- ✅ **Codex:** Inbox Universal v0.1 (schema+adapter+validator), bridge WhatsApp Pietra
  dry-run, convergência dos classificadores ao core, extrator de comando natural.
- ✅ **Cursor:** Agentarium **v0.9.0** — Mesa de Despacho (approve/reject chama o arquivista,
  E2E validado), chat MEGATRON (profissionalizado: haiku-4.5 + estado real + histórico).
- **O que resta no C:** o elo sensor real (export Gmail — Codex) e os gates do Fabio.

## 4. Dívida técnica conhecida (a resolver, não urgente)

1. **Dois classificadores** (`megatron_core.DOMINIOS` vs `email_intake.DOMAIN_RULES`) —
   convergir: o adapter deve delegar ao Core, não manter taxonomia própria.
2. `email_intake`: "responsável pelo aluno" caiu em `pessoal` em vez de `pietraos` —
   revisar matching de keywords (zona Codex).
3. RAG hardening (MAX_CHARS 6000→~1200) adiado para janela com CPU livre.
4. STATUS/roadmap/painel tinham deriva documental — este arquivo é agora a fonte única.

## 5. Próxima ação recomendada (ordem do Plano Mestre §5)

1. **Fechar elos quebrados do intake:** export Gmail→adapter + unificar ids (Codex);
   redigir summary no core (Claude).
2. **Fabio:** sessão de decisão dos **7 gates** (Plano Mestre §4): push+blobs, Gmail real,
   WhatsApp Pietra, e-mails no wiki, Bugbot 3–7, teto OpenRouter, 1ª prova EscolaOS.
3. **Piloto real:** EscolaOS 1ª prova OU tenant Pietra (o que os gates liberarem).
4. **Consolidação:** Bugbot Ondas 3–7, hardening RAG, lint wiki, links quebrados.
5. **PRIMUS:** as 7 lacunas da Missão 0001 (marco funcional).

## 6. Regras ativas (invioláveis)

- Sem push/canal externo/n8n ativo/WhatsApp/apagar sem **aprovação humana explícita**.
- Sem tocar `60_Sistemas/RAG/fabioos_db/` sem lock.
- Segredo/credencial nunca em log, RAG ou Git (redação obrigatória).
- Registrar lock em `Registro_Frentes_Ativas.md` antes de artefato compartilhado.
