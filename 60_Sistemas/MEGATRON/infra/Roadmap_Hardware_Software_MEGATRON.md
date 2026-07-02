---
tipo: roadmap
area: 60_Sistemas
projeto: MEGATRON
status: proposto
tags: [fabios, megatron, hardware, software, roadmap, nos]
criado_em: 2026-07-02
atualizado_em: 2026-07-02
---

# Roadmap Hardware + Software do MEGATRON

## Funcao

Converter a expansao fisica do MEGATRON em fases tecnicas de software. Cada compra so deve acontecer quando houver adaptacao correspondente no FabioOS.

## Regra governante

Comprar hardware sem preparar software gera maquina ociosa.

Preparar software sem medir uso gera arquitetura imaginaria.

O caminho correto e:

```text
medir uso -> preparar interface -> comprar modulo -> migrar servico -> validar -> registrar custo
```

## Regra financeira

Tokens/API sao prioridade antes de GPU, mas nao antes do Core 24/7.

```text
Core 24/7 primeiro
tokens com teto depois
GPU local so apos metricas
```

Ver decisao: [[50_Registros/Decisoes/ADR_2026-07-02_Tokens_vs_Hardware_MEGATRON]]

## Fase H0 - Estado atual

### Objetivo

Deixar o FabioOS pronto para distribuicao antes de comprar.

### Entregas

- [x] registrar arquitetura de nos;
- [x] criar `nodes.megatron.example.json`;
- [x] criar `node_registry.py`;
- [x] criar exemplo de Docker Compose com perfis;
- [ ] criar `nodes.megatron.local.json` gitignored quando houver hardware real;
- [ ] adicionar healthcheck real dos servicos locais;
- [ ] medir CPU/RAM/disco durante uma semana de uso.

### Criterio de sucesso

O MEGATRON consegue responder: "qual no executa esta capacidade?" sem depender de conhecimento humano implicito.

## Fase H1 - MEGATRON Core dedicado

### Hardware

- mini PC classe AOOSTAR GEM12+ Pro;
- 32 GB minimo, 64 GB recomendado;
- 1 TB NVMe minimo;
- dual LAN 2.5G.

### Software

- mover Docker/n8n para o Core;
- mover Agentarium/MEGATRON v1 para o Core;
- manter RAG local no Core;
- expor endpoints locais apenas via LAN/VPN;
- configurar backup Git + snapshot local.

### Criterio de sucesso

O notebook/desktop vira cliente. O Core continua operando mesmo se o notebook desligar.

## Fase H2 - Memoria e SSD

### Hardware

- 64 GB DDR5;
- segundo NVMe 2 TB ou 4 TB.

### Software

- separar volumes:
  - sistema;
  - dados;
  - modelos;
  - logs;
  - fontes;
- mover `fabioos_db` para volume claro;
- definir politica de backup de `05_Raw_Sources`, `40_Wiki`, `50_Registros` e bancos.

### Criterio de sucesso

Falha do sistema operacional nao implica perda de memoria do FabioOS.

## Fase H3 - GPU Node

### Hardware

- dock OCuLink;
- fonte ATX adequada;
- GPU NVIDIA com VRAM suficiente;
- prioridade candidata: RTX 3090 24 GB se custo/estado fizer sentido.

### Gate financeiro

Nao iniciar H3 sem:

- 2-3 meses de custo API/cloud GPU medido;
- lista de tarefas privadas ou massivas que exigem local;
- Core estabilizado;
- backup minimamente confiavel;
- teste local claro para o modelo escolhido.

### Software

- criar perfil Docker `gpu`;
- instalar runtime NVIDIA apenas no no GPU;
- expor servico local de inferencia (`ollama`, `vllm` ou equivalente);
- adicionar capacidade `local_llm_inference` ao registry;
- criar politica: quando usar local, OpenRouter ou humano.

### Criterio de sucesso

Uma tarefa de IA local roda no GPU Node sem alterar codigo de agente.

## Fase H4 - NAS

### Hardware

- NAS dedicado ou storage multi-HD;
- RAID/snapshot conforme necessidade;
- UPS.

### Software

- snapshots do vault;
- backup de PDFs/datasets/modelos;
- retencao semanal/mensal;
- teste de restore documentado.

### Criterio de sucesso

Restaurar o FabioOS em nova maquina a partir de Git + NAS.

## Fase H5 - Rede 10G

### Hardware

- switch 10G;
- NICs ou adaptadores quando necessario;
- cabos adequados.

### Software

- separar VLANs ou ao menos regras de firewall;
- mover trafego pesado NAS/GPU para rede interna;
- metricas de throughput.

### Criterio de sucesso

NAS e GPU nao travam a operacao diaria do Core.

## Fase H6 - Energia 24/7

### Hardware

- nobreak senoidal;
- roteador/switch/Core/NAS protegidos;
- solar quando fizer sentido.

### Software

- shutdown ordenado;
- monitoramento de energia;
- alerta de queda;
- modo degradado sem GPU.

### Criterio de sucesso

MEGATRON continua recebendo entradas e preservando estado durante instabilidade de energia.

## Backlog tecnico

- [ ] `nodes.megatron.local.json` gitignored;
- [ ] healthcheck HTTP para MEGATRON v1;
- [ ] healthcheck do n8n;
- [ ] healthcheck RAG;
- [ ] healthcheck OpenClaw/Evolution;
- [ ] registro de custo por chamada OpenRouter/local/cloud GPU;
- [ ] migracao Chroma -> Qdrant/pgvector se multi-writer virar requisito;
- [ ] fila de tarefas longa com n8n/Trigger.dev/Temporal;
- [ ] backup testado com restore real.
