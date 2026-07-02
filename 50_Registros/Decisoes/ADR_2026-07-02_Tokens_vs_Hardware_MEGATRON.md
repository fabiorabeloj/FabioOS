---
tipo: adr
area: 50_Registros
projeto: MEGATRON
status: aceito
tags: [adr, fabios, megatron, orcamento, tokens, hardware, gpu, api]
criado_em: 2026-07-02
---

# ADR - Tokens/API vs Hardware Local no MEGATRON

## Contexto

Fabio avaliou se vale mais a pena comprar hardware local ou investir em tokens/API para acelerar o FabioOS/MEGATRON.

O sistema ja usa assinaturas humanas de IA e esta evoluindo para:

- Intake Universal;
- Agentarium;
- OpenClaw;
- n8n;
- RAG;
- MCP;
- PRIMUS;
- PietraOS;
- MEGATRON como orquestrador.

O risco e comprar GPU cedo demais, antes de existir carga recorrente que justifique IA local pesada. O risco oposto e gastar tudo em tokens e continuar sem infraestrutura 24/7 para automacoes, filas, gateway, dashboard e memoria operacional.

## Decisao

A prioridade correta e:

```text
1. MEGATRON Core 24/7
2. tokens/API com teto mensal e telemetria
3. RAM/SSD conforme gargalo real
4. GPU local apenas apos metricas
5. NAS/backup antes de escalar dados sensiveis
```

Portanto:

- **tokens/API valem mais que GPU agora**;
- **Core 24/7 vale mais que comprar apenas tokens**;
- **GPU local nao deve ser compra inicial**;
- **credito API deve ser controlado por teto, nao comprado como cheque em branco**.

## Politica de investimento recomendada

### Se o orcamento for limitado

| Prioridade | Uso |
|---|---|
| 1 | Core 24/7 para Docker, n8n, OpenClaw, MEGATRON, RAG e Agentarium |
| 2 | teto mensal pequeno de API/OpenRouter |
| 3 | backup/SSD/RAM |
| 4 | GPU local |

### Se houver cerca de R$ 6.000

| Alocacao | Motivo |
|---|---|
| ~50% Core 24/7 | infraestrutura permanente |
| ~15-25% tokens/API | melhores modelos para desenvolvimento e automacoes |
| restante reserva | RAM, SSD, backup, dock eGPU ou GPU futura |

Os percentuais importam mais do que os valores exatos.

## Regra operacional de tokens

Tokens/API devem ser usados para:

- automacoes com saida estruturada;
- revisoes de codigo/documento;
- sintese de entradas publicas/internas;
- tarefas em que modelos frontier vencem modelos locais;
- fallback quando IA local nao existir.

Tokens/API nao devem ser usados para:

- jogar o vault inteiro para fora;
- processar dado `restricted`, `no_rag` ou `forbidden_external`;
- tarefas repetitivas que Python resolve;
- reprocessamento em massa sem cache;
- agentes em loop sem limite.

## Gate para comprar GPU local

Comprar GPU so quando pelo menos 3 criterios forem verdadeiros:

- gasto recorrente de API/GPU cloud ficar relevante por 2-3 meses;
- houver tarefas privadas demais para API externa;
- houver fila real de inferencia local, OCR, embeddings ou modelos rodando diariamente;
- o Core ja estiver estabilizado;
- backup e energia estiverem razoavelmente resolvidos;
- houver modelo local definido e teste de aceite.

## Gate para aumentar tokens/API

Aumentar teto de tokens quando:

- houver log de uso por 7 dias;
- houver custo por tarefa;
- houver taxa de sucesso;
- houver fallback;
- o MEGATRON souber dizer qual modelo usar por tipo de tarefa.

## Decisao pratica

Para o estado atual do FabioOS:

```text
Comprar GPU agora: nao.
Comprar apenas tokens e ignorar Core: nao.
Comprar Core + teto controlado de tokens: sim.
```

## Referencias

- OpenAI API Pricing: `https://developers.openai.com/api/docs/pricing`
- Anthropic Claude API Pricing: `https://platform.claude.com/docs/en/about-claude/pricing`
- Gemini API Pricing: `https://ai.google.dev/gemini-api/docs/pricing`
- OpenRouter Pricing: `https://openrouter.ai/pricing`
- Arquitetura distribuida: [[60_Sistemas/MEGATRON/infra/Arquitetura_Hardware_MEGATRON_FabioOS_v1]]
- Orcamento MEGATRON: [[00_Arquitetura/Plano_Orcamento_FabioOS_MEGATRON_2026]]
