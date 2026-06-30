---
tipo: provisionamento
area: 60_Sistemas
projeto: FabioOS
status: aguardando-segredos
autor: Claude (arquiteto-chefe)
criado_em: 2026-06-29
atualizado_em: 2026-06-29
tags: [fabios, stack, tier2, provisionamento, supabase, dify, openhands, browser-use, docker]
---

# Stack Tier-2 — Provisionamento (aguardando segredos do Fabio)

> Tier-1 já no ar (Crawl4AI, Stirling PDF :8081, Open WebUI :3000). Estes quatro
> **não rodam sem decisão/segredo seu** — abaixo está exatamente o que cada um
> precisa. Preencha os campos e eu subo. Portas livres: 8080 e 5678 já ocupadas
> (evolution-api, n8n); use 3000 (Open WebUI), 8081 (Stirling).

## 1. Supabase ⭐⭐⭐⭐⭐ — banco central (Postgres + Auth + Storage + Vetores)

**Recomendação:** começar pelo **Supabase Cloud** (free tier em supabase.com) em vez
de self-host. O self-host são ~10 containers + 4 segredos gerados; o cloud te dá
Postgres+pgvector+Auth+Storage em minutos, sem manutenção.

- **Se cloud:** você cria o projeto e me passa `SUPABASE_URL` + `SUPABASE_ANON_KEY`
  (e `SERVICE_ROLE_KEY` se for escrita). Eu ligo o RAG/memória a ele.
- **Se self-host:** preciso que você defina `POSTGRES_PASSWORD` e `JWT_SECRET`; eu
  uso o `docker-compose` oficial. Porta studio: 8000.

**O que falta de você:** decidir cloud vs self-host + as chaves.

## 2. Dify ⭐⭐⭐⭐⭐ — plataforma de agentes/RAG/chatbots

- **Como:** `git clone` do repo Dify → `docker compose up -d` (multi-container).
- **Precisa:** uma `SECRET_KEY` (gero aleatória) + chaves de modelo (Anthropic/
  OpenAI/OpenRouter) **configuradas na UI** depois de subir. Porta sugerida: 8082.
- **Risco:** baixo (roda local). Só não expor à internet sem auth.

**O que falta de você:** OK para subir + qual chave de modelo usar na UI.

## 3. OpenHands ⭐⭐⭐⭐⭐ — desenvolvedor autônomo ⚠️

- **Como:** `docker run` com a imagem oficial, montando o docker socket (ele
  **cria containers** e **executa código**) + workspace.
- **Precisa:** `LLM_API_KEY` (Anthropic/OpenRouter) + `LLM_MODEL`. Porta 3001
  (3000 é do Open WebUI).
- **Risco:** ALTO — agente autônomo que escreve e roda código. **Sandbox
  obrigatório** (ele já isola em container, mas monta o socket). Recomendo rodar
  só contra repositórios de teste no início, nunca direto no vault.

**O que falta de você:** chave de modelo + OK explícito de risco + escopo (qual
repo/pasta ele pode tocar).

## 4. Browser Use ⭐⭐⭐⭐⭐ — agente navegador ⚠️

- **Como:** `pip install browser-use` no venv (playwright já instalado p/ Crawl4AI).
- **Precisa:** `ANTHROPIC_API_KEY` ou `OPENAI_API_KEY` (ele usa LLM p/ decidir
  cliques). 
- **Risco:** ALTO — controla um navegador real (pode logar em Gmail, WhatsApp Web,
  bancos). **Nunca** em sites sensíveis sem você assistindo. Começar com tarefas
  read-only em sites públicos.

**O que falta de você:** chave de modelo + OK de risco + lista de tarefas/sites
permitidos.

## Resumo — o que preciso de você para destravar o tier-2

| Tool | Preciso de você | Posso subir sozinho depois? |
|---|---|---|
| Supabase | cloud-vs-selfhost + chaves | sim |
| Dify | OK + chave de modelo | sim |
| OpenHands | chave de modelo + OK de risco + escopo | sim (sandbox) |
| Browser Use | chave de modelo + OK de risco + sites | sim |

## Governança

Cada um entra com lock no Registro_Frentes_Ativas + changelog. Chaves vão em
`.env` gitignored, **nunca** commitadas (scan obrigatório). OpenHands/Browser Use
são `gated` no Maestro até você aprovar o risco.

## Relações
- [[50_Registros/Decisoes/ADR_2026-06-29_Stack_Operacional_e_Barramento_Capacidades]]
- [[60_Sistemas/MEGATRON/v1/registry]]
