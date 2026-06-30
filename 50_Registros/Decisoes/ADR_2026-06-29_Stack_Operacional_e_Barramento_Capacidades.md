---
tipo: adr
area: 50_Registros
projeto: FabioOS
status: aceito
autor: Claude (arquiteto-chefe)
criado_em: 2026-06-29
atualizado_em: 2026-06-29
tags: [adr, arquitetura, stack, multiagente, capacidades, maestro, megatron, roadmap]
---

# ADR 2026-06-29 — Stack operacional do FabioOS e barramento de capacidades

## Contexto

O Fabio propôs uma stack de 13 projetos open-source (Coolify, OpenHands, Maxun,
Open WebUI, Browser Use, Langflow, Supabase, Stirling PDF, Crawl4AI, Dify +
Qdrant, Redis, Temporal) e uma visão do FabioOS como **sistema operacional de
agentes**. A conclusão dele — correta — é que *"a próxima evolução não é adicionar
ferramentas, mas construir um barramento de coordenação onde cada agente anuncia
suas capacidades e um orquestrador decide quem executa"*.

## Decisão

1. **Adotar a arquitetura, não instalar a stack de uma vez.** Os 13+3 projetos são
   a stack-alvo **certa**, mas são Docker/serviço/runtime — categoria que o FabioOS
   exige passar por **Matriz de Aptidão + SPEC + aprovação humana**, um de cada vez
   (mesma disciplina aplicada ao ruflo). Instalar tudo agora = 13× o risco do ruflo.
2. **MEGATRON é o Maestro.** O orquestrador da visão do Fabio já existe e está
   sendo construído. Os 13 tools são **agentes especializados** que ele roteará.
3. **Construir o barramento de capacidades agora** (feito nesta entrega):
   `registry.py` é um catálogo onde cada agente — interno ou futuro — **anuncia
   capacidades + status** (`ativo`/`planejado`/`gated`); o MEGATRON roteia por
   capacidade e é honesto sobre o que ainda não existe (ignorância explícita
   estendida a capacidades). `python megatron.py "o que voce pode fazer?"` lista o time.
4. **Adoção sequenciada e gated** (núcleo mínimo primeiro), nunca em bloco.

## Mapa: stack → camada → papel-agente → status

| Projeto | Camada | Papel (agente MEGATRON) | Prio | Status no registry | Pré-requisito |
|---|---|---|---|---|---|
| **Supabase** | Infra/Dados | banco (memória, vetores) | ⭐⭐⭐⭐⭐ | planejado | Docker/host; decidir vs Chroma atual |
| **Qdrant** | Infra/Dados | banco (vetores alto-desempenho) | ⭐⭐⭐⭐ | planejado | só se pgvector não bastar |
| **Redis** | Infra | cache/filas p/ agentes concorrentes | ⭐⭐⭐ | (infra) | quando houver concorrência real |
| **Coolify** | Infra/Deploy | infra (deploy, host) | ⭐⭐⭐⭐⭐ | gated | servidor próprio; **aprovação** |
| **Temporal** | Infra/Orquestração | automacao (tarefa longa) | ⭐⭐⭐ | gated | só p/ workflows duráveis |
| **Open WebUI** | Interface | interface (chat multimodelo) | ⭐⭐⭐⭐⭐ | planejado | Docker; chaves dos modelos |
| **OpenHands** | Agentes | programador (código, PR) | ⭐⭐⭐⭐⭐ | planejado | sandbox; **aprovação** (executa código) |
| **Browser Use** | Agentes | navegador (web, downloads) | ⭐⭐⭐⭐⭐ | gated | **aprovação** (age na web/WhatsApp/bancos) |
| **Crawl4AI** | Conhecimento/RAG | pesquisador (coleta→RAG) | ⭐⭐⭐⭐⭐ | planejado | alimenta o RAG atual |
| **Dify** | Conhecimento/Produtos | atendente (chatbot, workflows) | ⭐⭐⭐⭐⭐ | gated | Docker; integra Pietra/WhatsApp |
| **Stirling PDF** | Documentos | documentalista (PDF/OCR) | ⭐⭐⭐⭐ | planejado | Docker; alto valor p/ Escola |
| **Langflow** | Automação/Lab | laboratorio (protótipo de fluxo) | ⭐⭐⭐⭐ | planejado | Docker |
| **Maxun** | Coleta | coletor_visual (scraper visual) | ⭐⭐⭐ | planejado | Docker |
| **n8n** | Automação | automacao (recorrente) | — | gated (já no roadmap) | já previsto, Fabio-gated |

## Problemas que a stack resolve (faithful ao briefing do Fabio)

- **"Minhas IAs não agem"** → Browser Use + OpenHands (mãos e olhos digitais).
- **Conhecimento espalhado** → Crawl4AI + Dify + Supabase (tudo vira RAG pesquisável).
- **Trabalho manual** → OpenHands + Coolify (prompt → código → deploy).
- **WhatsApp só responde** → Dify + Browser Use (Pietra consulta banco/calendário/age).
- **Documentos (provas/PDFs)** → Stirling PDF (OCR, split por aluno, etc.).
- **Vários modelos dispersos** → Open WebUI (interface única, mesma memória).
- **Cada IA sozinha** → barramento de capacidades + MEGATRON Maestro (o gargalo-mor).

## Sequência de adoção (quando o Fabio autorizar runtime)

Núcleo mínimo funcional: **Supabase → Open WebUI → Dify → Browser Use → OpenHands**.
Cada um exige: aplicar Matriz de Aptidão → SPEC própria → instalar isolado/testar →
registrar lock → changelog. Coolify entra quando houver servidor; Crawl4AI alimenta
o RAG; Stirling PDF prioriza o caso Escola.

## Consequências

- A visão estratégica do Fabio fica **capturada e governada** (Radar Tecnológico
  aplicado a 13 ferramentas; Matriz de Aptidão como gate de cada adoção).
- O FabioOS ganha a **camada de coordenação** (capacidades + roteamento) que torna
  a stack utilizável de forma cooperativa — sem instalar nada invasivo agora.
- Ações de runtime/deploy/externo permanecem sob controle humano.

## Relações
- [[60_Sistemas/MEGATRON/v1/registry]]
- [[60_Sistemas/FabioOS/specs/2026-06-29_megatron-coordenador]]
- [[50_Registros/Barramento_Multiagente]]
- [[50_Registros/Decisoes/ADR_2026-06-29_Avaliacao_Ruflo_e_Absorcao]]
- [[60_Sistemas/FabioOS/Roadmap_Fases_FabioOS_v2_2026-06-29]]
