---
tipo: referencia
area: 60_Sistemas
projeto: PietraOS
status: ativo
autor: Claude (arquiteto-chefe)
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [pietraos, chatbot, enterprise, nlu, ux, padrao, benchmark]
---

# PietraOS — Padrão profissional (como chatbots de grandes empresas)

> Benchmark contra chatbots enterprise (bancos, iFood, operadoras). O que eles
> fazem, o que o PietraOS **já faz** e o **roadmap** para nível comercial.

## Checklist enterprise

| Capacidade | Grandes empresas | PietraOS |
|---|---|---|
| Conversa multi-turno + sessão | sim | ✅ `pietra_conversa.py` |
| **Slot-filling** (coleta dados que faltam) | sim | ✅ (ex.: "para qual aluno?") |
| **Persona/tom** consistente | sim | ✅ (config `persona`) |
| **Fallback + menu** quando não entende | sim | ✅ (menu; após 2 falhas → atendente) |
| **Handoff humano com contexto** | sim | ✅ (sensível escala com setor+prioridade) |
| **Guardrails / compliance** | sim | ✅ risco-gate + LGPD (sensível nunca auto) |
| Saudação + encerramento cordial | sim | ✅ |
| Horário de atendimento / fora de horário | sim | ✅ (parcial: mensagem fora-horário) |
| **NLU real** (intents + entities) | sim (LLM/NLU) | 🔜 hoje keyword; LLM local com GPU |
| **Rich messages** (botões, listas, cards) | sim | 🔜 UI Cursor + WhatsApp interactive |
| **Base de conhecimento** (FAQ via RAG) | sim | 🔜 RAG existe, plugar no FAQ |
| **Analytics/CSAT/dashboards** | sim | 🔜 relatório existe; dashboards Cursor |
| **WhatsApp Business API oficial** | sim | 🔜 piloto na Evolution (não-oficial) |
| Feedback loop / melhoria contínua | sim | 🔜 ReasoningBank loga erros de classificação |
| Multi-canal (WhatsApp/web/app) | sim | 🔜 |
| **Multi-tenant + isolamento de dados** | sim | ✅ (tenants isolados, LGPD) |

**Leitura:** o PietraOS já entrega o **núcleo enterprise** (conversa, slots, persona,
fallback, handoff, guardrails, multi-tenant). O que separa do nível comercial pleno
é **NLU por LLM** (precisa GPU), **rich messages** (UI), **RAG no FAQ** e o
**WhatsApp oficial** — todos no roadmap, nenhum bloqueia o piloto.

## Os 3 upgrades que mais elevam a percepção de qualidade

1. **NLU por LLM local** (quando houver GPU): entende mensagem bagunçada de pai,
   extrai entidades (aluno, data, valor) melhor que keyword. Reusa o `--llm` do MEGATRON.
2. **Botões/listas (WhatsApp interactive + cards no painel):** menos digitação, mais
   conversão. Cursor renderiza; o canal envia botões.
3. **FAQ com RAG:** dúvidas de baixo risco (horário, uniforme, calendário) respondidas
   direto da base da escola, com fonte — não template genérico.

## Princípio de qualidade

Chatbot profissional **não é o que responde tudo** — é o que **entende, coleta o
necessário, resolve o simples e entrega o difícil a um humano com contexto**, sempre
com tom institucional e sem nunca errar num caso sensível. É esse o padrão do PietraOS.

## Relações
- [[60_Sistemas/Pietra/pietra_conversa]]
- [[60_Sistemas/Pietra/PietraOS_Arquitetura_Multitenant]]
- [[60_Sistemas/FabioOS/MEGATRON_Autonomia_Sem_Claude]] (NLU por LLM local)
- [[60_Sistemas/FabioOS/Arquitetura_Hardware_FabioOS]] (GPU p/ NLU)
