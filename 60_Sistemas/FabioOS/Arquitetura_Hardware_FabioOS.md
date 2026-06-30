---
tipo: referencia
area: 60_Sistemas
projeto: FabioOS
status: ativo
autor: Claude (arquiteto-chefe)
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [fabios, hardware, infraestrutura, gpu, orcamento, ai-os]
---

# Arquitetura de Hardware — FabioOS como AI OS local

> Valores em BRL são **estimativas de mercado** (verificar no momento da compra).
> O caminho assumido: FabioOS local-first (RAG, embeddings, LLMs locais, stack
> Docker, agentes autônomos).

## Diagnóstico: o reindex lento é hardware?

**Parcialmente.** Foram 3 fatores:
- **~50% hardware:** `bge-m3` (560M params) em **CPU** é o gargalo. Sem GPU, embeddings são lentos.
- **~30% auto-infligido:** rodei o reindex com watcher + extrações + stack Docker competindo.
- **~20% modelo:** bge-m3 é pesado; modelo menor / ONNX-quantizado é mais rápido em CPU.

## A alavanca #1: GPU (NVIDIA/CUDA)

Uma GPU muda a ordem de grandeza:
- Embeddings (reindex): de **~30-50 min → segundos**.
- Permite **LLMs locais** (Ollama) p/ OpenHands, Browser Use, Dify — **sem pagar API**.
- É também o que torna o **MEGATRON autônomo** (cérebro LLM local — ver
  [[60_Sistemas/FabioOS/MEGATRON_Autonomia_Sem_Claude]]).

## Princípio que vale mais que specs

**Separe a máquina de trabalho do runtime de IA.** Coloque stack Docker +
embeddings + modelos num **box dedicado** (o "host" da sua arquitetura Coolify).
Seu notebook nunca compete; o reindex roda no servidor enquanto você trabalha.

## Orçamentos (estimativas BRL)

### Tier 0 — Custo zero (regra operacional)
**R$ 0.** Rodar reindex só com a máquina quieta (sem watcher/extrações juntos) +
usar modelo de embedding menor. Resolve a dor imediata sem comprar nada.

### Tier 1 — Upgrade da máquina atual ⭐ recomendado p/ começar
| Item | Estimativa |
|---|---|
| RAM +32GB (total 32-48GB) | R$ 600 – 1.000 |
| GPU usada **RTX 3090 24GB** (melhor custo p/ IA) | R$ 3.000 – 4.500 |
| _(alt. GPU nova RTX 4060 Ti 16GB)_ | R$ 3.000 – 3.800 |
| **Total** | **~R$ 3.600 – 5.500** |

Embeddings rápidos + LLMs locais 7-14B. Mas ainda compete com seu trabalho.

### Tier 2 — Mini-servidor dedicado ⭐ recomendado p/ AI OS sério
| Item | Estimativa |
|---|---|
| CPU Ryzen 7/9 | R$ 1.500 – 2.500 |
| RAM 64GB | R$ 1.200 – 1.800 |
| GPU RTX 3090 24GB usada | R$ 3.000 – 4.500 |
| NVMe 1-2TB + placa-mãe + fonte 750W + gabinete | R$ 2.000 – 3.000 |
| **Total** | **~R$ 8.000 – 12.000** |

Roda a stack inteira 24/7 (Coolify/Supabase/Dify/Ollama/RAG). Notebook só conecta.

### Tier 3 — Workstation forte
| Item | Estimativa |
|---|---|
| Ryzen 9 / Threadripper + 128GB | R$ 6.000 – 10.000 |
| GPU RTX 4090 24GB | R$ 12.000 – 16.000 |
| **Total** | **~R$ 20.000 – 30.000** |

LLMs locais 30-70B + embeddings + stack, tudo folgado.

### Alternativa — Nuvem (sem capex)
GPU sob demanda (RunPod / Vast.ai): **RTX 3090/4090 ~US$ 0,30-0,50/h**. Paga só
quando reindexar/rodar modelo grande. Bom p/ testar antes de investir; ruim p/
dados muito sensíveis (saem da máquina).

## Recomendação do arquiteto

1. **Agora (R$0):** reindex só com máquina quieta + modelo menor se quiser.
2. **Curto prazo (~R$4-5k):** Tier 1 (RAM + RTX 3090 usada) — destrava embeddings e LLM local.
3. **Quando for sério:** Tier 2 (mini-servidor dedicado) — é o que desacopla tudo e
   torna o FabioOS um AI OS de verdade, com MEGATRON podendo ter cérebro LLM local.

## Relações
- [[60_Sistemas/FabioOS/MEGATRON_Autonomia_Sem_Claude]]
- [[50_Registros/Decisoes/ADR_2026-06-29_Stack_Operacional_e_Barramento_Capacidades]]
- [[60_Sistemas/FabioOS/Stack_Tier2_Provisionamento_2026-06-29]]
