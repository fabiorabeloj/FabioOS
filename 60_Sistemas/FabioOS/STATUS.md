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

## 3. Onde o Bloco C (foco) está agora

- ✅ **Claude:** Core Spec v0.1 + `megatron_core.py` + `intake_flow.py` (prova mínima §9:
  5 payloads fake → classifica → **trava de redação** → fila "Aguardando Fabio" → log;
  token nunca vaza). Contrato congelado: `60_Sistemas/MEGATRON/v1/examples/intake_queue.sample.json`.
- 🟡 **Codex:** `universal_intake_adapter.py` + `email_intake_dry_run.py` adaptados ao schema
  (dry-run seguro, bloqueia gravação fora do vault). Taxonomia alinhada ao Core Spec §4
  (bug "coordenação→pietraos" corrigido em 2026-07-01).
- 🟡 **Cursor:** Agentarium consome `intake_queue.json`; Bugbot mapeou revisão do projeto
  em 7 ondas (`50_Registros/Relatorios/Plano_Bugbot_*`).

## 4. Dívida técnica conhecida (a resolver, não urgente)

1. **Dois classificadores** (`megatron_core.DOMINIOS` vs `email_intake.DOMAIN_RULES`) —
   convergir: o adapter deve delegar ao Core, não manter taxonomia própria.
2. `email_intake`: "responsável pelo aluno" caiu em `pessoal` em vez de `pietraos` —
   revisar matching de keywords (zona Codex).
3. RAG hardening (MAX_CHARS 6000→~1200) adiado para janela com CPU livre.
4. STATUS/roadmap/painel tinham deriva documental — este arquivo é agora a fonte única.

## 5. Próxima ação recomendada

1. **Codex:** convergir taxonomia (adapter delega ao `megatron_core.classificar_intake`);
   ligar conectores fake→reais mantendo dry-run.
2. **Cursor:** construir a fila "Aguardando Fabio" + campo de comando natural contra o
   `intake_queue.sample.json`; autorizar Onda 1 do Bugbot (entradas sensoriais).
3. **Fabio:** decidir quando ligar o primeiro canal real (WhatsApp Pietra) — só depois do
   loop provado nas 3 fontes (email/whatsapp/pdf fake).
4. **Claude:** repetir a prova §9 para WhatsApp e PDF fake (mesmo contrato).

## 6. Regras ativas (invioláveis)

- Sem push/canal externo/n8n ativo/WhatsApp/apagar sem **aprovação humana explícita**.
- Sem tocar `60_Sistemas/RAG/fabioos_db/` sem lock.
- Segredo/credencial nunca em log, RAG ou Git (redação obrigatória).
- Registrar lock em `Registro_Frentes_Ativas.md` antes de artefato compartilhado.
