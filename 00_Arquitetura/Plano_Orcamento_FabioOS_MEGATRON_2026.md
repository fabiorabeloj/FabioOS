---
tipo: plano_estrategico
area: arquitetura
status: ativo
criado_em: 2026-06-27
atualizado_em: 2026-06-27
tags: [orcamento, custos, ia, hardware, openrouter, megatron, fabioos]
---

# Plano de Orcamento FabioOS / MEGATRON - 2026

## Missao

Organizar os custos do FabioOS/MEGATRON como um sistema profissional: assinaturas, APIs, automacoes, infraestrutura, backup e possivel hardware.

Este plano parte de uma premissa: o objetivo nao e gastar menos a qualquer custo; o objetivo e gastar certo, com controle, evidencia e retorno real.

## Definicao operacional

O FabioOS/MEGATRON esta se tornando um sistema operacional pessoal e institucional de conhecimento, automacao e agentes.

Na pratica, isso inclui:

- vault Obsidian como fonte de verdade;
- agentes funcionais e protocolos de governanca;
- RAG local para consulta semantica com fontes;
- Grafo local para mapa de conhecimento e dependencias;
- OpenRouter/API para sintese e automacao quando a IA externa agrega valor;
- n8n/OpenClaw/WhatsApp como camada futura de interface e automacao;
- Git/GitHub como memoria versionada;
- dashboards e registros para controle de estado.

## Estado local verificado

Levantamento feito em 2026-06-27:

| Item | Estado |
|---|---|
| CPU | Intel Core i7-3770, 4 cores / 8 threads |
| RAM | 16 GB |
| GPU | NVIDIA GTX 1050 Ti, ~4 GB VRAM |
| Disco principal | 446.6 GB |
| Livre em C: | 103.4 GB |

Implicacao: a maquina atual serve para vault, Git, scripts, RAG leve/moderado, grafo, Obsidian, Codex/Claude e automacoes locais. Ela nao e boa candidata para LLM local pesado, treino, fine-tuning ou inferencia GPU moderna.

## Custos ja existentes

O usuario informou que ja paga duas mensalidades: Claude e ChatGPT.

Valores de referencia atuais:

- ChatGPT Plus: US$20/mes, segundo Help Center da OpenAI.
- ChatGPT Pro: cerca de US$200/mes.
- Claude Pro: US$20/mes mensal ou US$17/mes com assinatura anual.
- Claude Max: a partir de US$100/mes, com nivel superior em torno de US$200/mes.

Decisao recomendada: manter ChatGPT + Claude enquanto ambos estiverem produzindo valor real. Eles sao ferramentas de operacao interativa, nao substituem a API. A API deve ser usada para automacoes, nao para conversas humanas longas que ja estao cobertas pelas mensalidades.

## Custos variaveis previstos

| Categoria | Recomendada agora | Quando subir |
|---|---:|---|
| OpenRouter/API | US$50 a US$100 de teto inicial | Subir para US$200 apos 7 dias de metricas reais. |
| n8n self-hosted | US$0 em software, custo local de manutencao | Migrar para cloud se precisar disponibilidade 24/7. |
| n8n Cloud | Evitar no inicio | Considerar Starter/Pro quando houver workflows em producao. |
| WhatsApp / Meta | Nao iniciar custo antes do fluxo estar fechado | Ativar quando OpenClaw/n8n tiverem caso de uso validado. |
| GPU cloud | Usar sob demanda, nao mensal fixo | Usar para lotes ou testes locais de modelo. |
| Hardware local | Nao comprar GPU agora | Planejar workstation quando carga real justificar. |
| Backup | Prioridade alta | Comprar/organizar antes de hardware caro. |

## Estrategia recomendada

### Fase A - Agora

Objetivo: profissionalizar sem inflar custo.

- Manter ChatGPT + Claude como assinaturas humanas de trabalho.
- OpenRouter com teto de US$100 e chaves separadas por uso quando possivel.
- RAG e Grafo continuam locais.
- `--generate` continua opt-in para nao mandar contexto externo por acidente.
- n8n/OpenClaw entram como piloto controlado, nao como producao 24/7.
- Criar rotina de custo semanal: modelo usado, finalidade, custo estimado e beneficio.

Orcamento incremental alem das assinaturas atuais:

| Item | Valor sugerido |
|---|---:|
| OpenRouter inicial | US$50 a US$100 |
| GPU cloud eventual | US$0 a US$30 |
| n8n Cloud | US$0 |
| Hardware novo | US$0 |
| Backup/armazenamento | priorizar compra simples se ainda nao existir |

### Fase B - Producao leve

Gatilho: WhatsApp, Inbox, RAG com geracao e dashboards funcionando semanalmente.

- OpenRouter mensal planejado: US$50 a US$150.
- n8n: self-host se a maquina ficar ligada; cloud Starter/Pro se precisar estabilidade.
- GPU cloud: usar por hora para tarefas especiais.
- Backup: no minimo 2 copias, uma local e uma externa/nuvem.

### Fase C - Workstation profissional

Gatilho: uso recorrente de IA local, processamento grande, agentes rodando diariamente, necessidade de privacidade ou custo de cloud GPU ficando alto.

Configuracao-alvo:

| Componente | Minimo profissional | Ideal MEGATRON |
|---|---|---|
| CPU | 8 a 12 cores modernos | 12 a 24 cores modernos |
| RAM | 64 GB | 128 GB |
| SSD | 2 TB NVMe | 4 TB NVMe + backup dedicado |
| GPU | 16 GB VRAM | 24 a 32 GB VRAM |
| Energia/refrigeracao | Estavel | Planejada para carga longa |

Regra: nao colocar uma GPU de ponta na maquina atual como eixo principal. O conjunto i7-3770 + 16 GB RAM + plataforma antiga criaria gargalo e risco de gasto mal aproveitado.

## Cloud GPU versus hardware local

Referencia atual de cloud GPU: Runpod lista RTX 4090 por cerca de US$0.69/h e RTX 5090 por cerca de US$0.99/h.

Leitura pratica:

| Uso mensal de GPU | Melhor caminho |
|---:|---|
| 0 a 30 horas | Cloud GPU sob demanda. |
| 30 a 150 horas | Cloud GPU ainda tende a ser melhor. |
| 150 a 300 horas | Comecar comparativo serio com hardware local. |
| 300+ horas | Hardware local pode fazer sentido, se o uso for estavel. |

Antes de comprar hardware, medir:

- quantas horas reais de processamento pesado por mes;
- quais modelos precisam rodar localmente;
- qual volume de dados e privado demais para API;
- custo mensal real de cloud GPU;
- quanto tempo de setup/manutencao voce aceita.

## O que nao fazer agora

- Nao assinar tudo ao mesmo tempo.
- Nao transformar OpenRouter em substituto de RAG local.
- Nao enviar o vault inteiro para API externa.
- Nao comprar GPU de ponta antes de medir carga real.
- Nao colocar WhatsApp/n8n em producao antes de logs, limites e fallback.
- Nao deixar API sem teto de gasto.

## O que fazer agora

1. Manter as assinaturas ja pagas como bancada humana de trabalho.
2. Usar OpenRouter como API controlada, com teto inicial de US$100.
3. Medir por 7 dias: chamadas, modelo, custo, finalidade e resultado.
4. Priorizar backup e organizacao de chaves antes de hardware.
5. Usar cloud GPU por hora se surgir tarefa pesada.
6. Reavaliar hardware somente depois de dados reais.

## Decisao governante

A melhor estrutura para o FabioOS/MEGATRON agora e:

> Assinaturas humanas para pensar e operar; RAG/Grafo locais para memoria; OpenRouter para automacao controlada; cloud GPU para experimentos; hardware novo somente quando a carga real provar necessidade.

Essa decisao preserva ambicao sem trocar arquitetura por ansiedade de compra.

## Addendum 2026-07-02 - Tokens/API vs hardware local

Decisao complementar: [[50_Registros/Decisoes/ADR_2026-07-02_Tokens_vs_Hardware_MEGATRON]]

### Tese

No estado atual do FabioOS, tokens/API valem mais que GPU local, mas nao valem mais que ter um Core 24/7.

Ordem correta:

```text
MEGATRON Core 24/7
-> teto controlado de tokens/API
-> RAM/SSD/backup conforme gargalo
-> GPU local somente apos metricas
```

### Por que nao GPU agora

- O gargalo atual ainda e software, orquestracao, fluxo, UI, logs e confiabilidade.
- Os melhores modelos externos continuam superiores para arquitetura, codigo e raciocinio complexo.
- Uma GPU local so vira investimento bom quando houver carga recorrente, privacidade forte ou processamento em massa.
- Sem Core/backup/observabilidade, a GPU acelera um sistema ainda imaturo.

### Por que nao so tokens

- Tokens nao criam operacao 24/7.
- Tokens nao mantem n8n, OpenClaw, Agentarium, filas, watchers e memoria operacional ligados.
- Tokens acabam; infraestrutura permanece.

### Politica operacional

- Usar API para tarefas de alto valor e automacoes medidas.
- Preferir OpenRouter/API com teto mensal, nao credito ilimitado.
- Registrar custo por tarefa antes de subir teto.
- Nao enviar dados `restricted`, `no_rag` ou `forbidden_external` para API externa.
- Medir 7 dias antes de aumentar gasto.

## Referencias

- OpenAI Help Center - ChatGPT Plus e Pro: `https://help.openai.com/`
- Claude pricing: `https://claude.com/pricing`
- OpenRouter models API: `https://openrouter.ai/api/v1/models`
- OpenRouter quickstart: `https://openrouter.ai/docs/quickstart`
- n8n pricing: `https://n8n.io/pricing/`
- Runpod pricing: `https://www.runpod.io/pricing`
