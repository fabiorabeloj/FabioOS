---
tipo: arquitetura
area: 60_Sistemas
projeto: MEGATRON
status: proposto
versao: 1.0
tags: [fabios, megatron, hardware, homelab, ia-local, nos, infraestrutura]
criado_em: 2026-07-02
atualizado_em: 2026-07-02
---

# Arquitetura de Hardware MEGATRON/FabioOS v1.0

## Funcao

Projetar o MEGATRON como pequeno datacenter domestico modular, de baixo consumo, preparado para IA local, automacoes 24/7, RAG, MCP, OpenClaw, n8n, bancos e agentes.

Esta arquitetura nao compra hardware por ansiedade. Ela separa:

- servicos;
- dados;
- modelos;
- GPU;
- armazenamento;
- rede;
- energia;
- governanca.

## Tese

O MEGATRON deve ser uma infraestrutura composta por nos independentes.

```text
Usuario
  -> MEGATRON Core
  -> servicos FabioOS
  -> RAG / MCP / agentes
  -> GPU Node quando necessario
  -> NAS para persistencia
  -> workers futuros
```

O computador fisico e apenas uma encarnacao temporaria do Core.

## Principios

1. Modularidade antes de potencia bruta.
2. Core sempre ligado; GPU so quando necessaria.
3. Dados preservados fora do compute.
4. Nos descobertos por configuracao, nao por hardcode.
5. Servicos com portas, healthcheck e permissao declarados.
6. API externa e IA local coexistem por politica de custo/privacidade.
7. Sem acao externa sem aprovacao humana.

## Visao fisica

```text
Internet
  |
Firewall / VPN
  |
Switch 2.5G agora; 10G depois
  |
  +-- MEGATRON Core
  |     - Docker
  |     - MEGATRON v1
  |     - Agentarium / chat
  |     - n8n
  |     - OpenClaw bridge
  |     - RAG local
  |     - MCP FabioOS
  |     - PostgreSQL/Qdrant futuros
  |
  +-- GPU Node via OCuLink ou worker dedicado
  |     - Ollama / vLLM / Open WebUI
  |     - modelos locais
  |     - jobs de inferencia pesada
  |
  +-- NAS
  |     - vault snapshots
  |     - PDFs
  |     - modelos
  |     - backups
  |     - datasets
  |
  +-- Clientes
        - notebook
        - desktop
        - celular
        - tablet
```

## Hardware alvo

### Core

Alvo proposto: AOOSTAR GEM12+ Pro ou classe equivalente.

Capacidades desejadas:

- CPU moderna de 8 cores / 16 threads;
- 64 GB RAM como ponto de conforto;
- possibilidade de 128 GB se a plataforma suportar;
- dois slots NVMe;
- dual LAN 2.5G;
- USB4;
- OCuLink;
- baixo consumo em idle;
- operacao 24/7.

Observacao: o fornecedor AOOSTAR lista o GEM12+ Pro com Ryzen 7 PRO 8845HS, dois slots DDR5-5600 ate 128 GB, dois M.2 2280 NVMe e OCuLink. Antes de comprar, confirmar revisao exata do modelo, disponibilidade, garantia, tipo de OCuLink e limites de SSD/RAM.

### GPU

GPU deve ser no independente ou eGPU via OCuLink.

Prioridade tecnica:

1. VRAM suficiente;
2. estabilidade;
3. custo por token local;
4. compatibilidade CUDA;
5. consumo sob controle.

Uma RTX 3090 24 GB segue como candidata pragmatica para IA local por VRAM, mas a decisao deve depender de preco real, estado da placa usada, consumo e necessidade medida. NVIDIA documenta a RTX 3090 como placa de 24 GB GDDR6X; isso confirma a premissa de VRAM, nao a compra automatica.

### NAS

NAS nao e compra inicial obrigatoria.

Ele entra quando:

- PDFs e datasets crescerem;
- backups precisarem de snapshots;
- modelos locais ocuparem espaco relevante;
- o Core nao puder mais ser ponto unico de falha dos dados.

### Energia

Desenho futuro:

```text
Energia solar
  -> inversor
  -> nobreak senoidal
  -> Core
  -> NAS
  -> switch
  -> roteador
```

Regra: o Core deve ser economico o bastante para ficar ligado. A GPU deve ser tratada como acelerador sob demanda.

## Aderencia atual do FabioOS

| Componente atual | Estado | Aderencia ao modelo distribuido | Ajuste necessario |
|---|---|---|---|
| MEGATRON v1 | ativo local | boa, mas ainda filesystem-first | adicionar leitura de `nodes.megatron.example.json` |
| Agentarium | ativo como UI | boa como interface cliente | consumir APIs/estado por endpoint estavel |
| RAG Chroma | ativo local | bom para v1, limitado para multi-node | manter single-writer ou migrar para Qdrant/pgvector |
| MCP FabioOS | read-only | excelente como interface padronizada | publicar endpoint/stdio por no |
| n8n | Docker local | bom para Core | externalizar URLs e credenciais |
| OpenClaw/Evolution | gateway local | bom como canal edge | tratar como servico de borda no registro |
| Open WebUI/Ollama | previstos/ativos parcialmente | bom para GPU Node | isolar em perfil `gpu` |
| Obsidian/Git | fonte humana/versionada | indispensavel | backups e snapshots no NAS |

## Componentes preparados para distribuicao

### 1. Servicos

Todo servico deve declarar:

- nome;
- no;
- porta;
- protocolo;
- healthcheck;
- classe de dado permitida;
- capacidade ofertada;
- perfil Docker ou comando.

### 2. Bancos

Separar por funcao:

- Chroma atual: recuperacao local simples;
- Qdrant futuro: vetor distribuivel e API HTTP/gRPC;
- PostgreSQL/Supabase futuro: estado estruturado, filas, eventos, custos, usuarios;
- filesystem/NAS: fontes brutas e snapshots.

### 3. Agentes

Agente nao escolhe maquina. Agente pede capacidade.

Exemplo:

```text
Agente RAG pede: vector_search
Registro responde: megatron-core / rag_chroma

Agente local-llm pede: local_llm_inference
Registro responde: gpu-oculink / ollama
```

### 4. APIs

Interfaces minimas:

| Endpoint | Funcao |
|---|---|
| `/health` | servico esta vivo |
| `/capabilities` | capacidades do no/servico |
| `/metrics` | uso basico, fila, latencia, custo |
| `/tasks` | receber tarefa futura |
| `/events` | emitir evento para barramento |

Na v0, isso pode ser apenas JSON local + scripts. Depois vira HTTP.

## Descoberta de nos

### v0 - configuracao estatica

Arquivo:

```text
60_Sistemas/MEGATRON/infra/nodes.megatron.example.json
```

E suficiente para:

- documentar topologia;
- testar roteamento;
- planejar containers;
- evitar hardcode.

### v1 - descoberta local

Opcoes:

- DNS local;
- Tailscale MagicDNS;
- mDNS;
- arquivo `nodes.megatron.local.json` gitignored;
- healthcheck periodico.

### v2 - control plane

Opcoes futuras:

- Postgres como registry;
- Consul;
- Kubernetes;
- Nomad;
- Docker Swarm;
- fila de tarefas com Trigger.dev/Temporal.

## Balanceamento de tarefas

Regra inicial:

```text
capacidade requerida
  -> filtrar nos ativos
  -> filtrar permissao de dado
  -> ordenar por prioridade/custo/localidade
  -> se nenhum no ativo, propor fallback
```

Exemplos:

| Tarefa | No preferencial | Fallback |
|---|---|---|
| consulta RAG | Core | API externa nao substitui fonte local |
| gerar resposta sensivel | Core local | humano, sem API |
| sumarizar publico | OpenRouter | local LLM se disponivel |
| inferencia local pesada | GPU Node | cloud GPU sob aprovacao |
| backup | NAS | disco externo |
| OCR pesado | Core/documentalista | Stirling/OCR dedicado |

## Roteamento de agentes

Contrato:

```json
{
  "task_id": "task_...",
  "capability": "vector_search",
  "data_class": "internal",
  "requires_gpu": false,
  "max_cost_usd": 0,
  "approval_required": false
}
```

O MEGATRON deve rotear por:

- capacidade;
- classe de dado;
- custo;
- disponibilidade;
- localidade;
- exigencia de aprovacao.

## Roadmap resumido

| Etapa | Hardware | Software |
|---|---|---|
| 0 | PC atual | registry de nos, docs, healthchecks |
| 1 | Core AOOSTAR | mover Docker/n8n/MEGATRON/RAG para Core |
| 2 | 64 GB + SSD 2/4 TB | separar dados/modelos/logs |
| 3 | GPU OCuLink | perfil `gpu`, Ollama/Open WebUI, roteamento local |
| 4 | NAS | backups, snapshots, modelos, datasets |
| 5 | rede 10G | NAS/GPU/Core com throughput maior |
| 6 | energia solar/nobreak | operacao 24/7 resiliente |

## Decisoes

- Nao acoplar o FabioOS ao AOOSTAR.
- Nao mover Chroma para multi-node agora.
- Nao ligar GPU local como requisito do MEGATRON.
- Preparar tudo para variaveis, perfis e capacidades.
- Tratar GPU como acelerador, nao como cerebro.

## Referencias externas consultadas

- AOOSTAR GEM12+ Pro: `https://aoostar.com/products/aoostar-gem12-pro-amd-r7-pro-8845hs-mini-pc`
- NVIDIA RTX 3090: `https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090-3090ti/`
- Docker Compose Profiles: `https://docs.docker.com/compose/how-tos/profiles/`
- Qdrant Installation / distributed ports: `https://qdrant.tech/documentation/installation/`

## Relacoes

- [[80_Specs/MEGATRON/2026-07-02_infra-distribuida-hardware-megatron]]
- [[60_Sistemas/MEGATRON/infra/Roadmap_Hardware_Software_MEGATRON]]
- [[00_Arquitetura/Plano_Orcamento_FabioOS_MEGATRON_2026]]
- [[10_Dashboard/MEGATRON]]
- [[60_Sistemas/FabioOS/specs/2026-07-01_MEGATRON_Core_Spec_v0.1]]
