---
tipo: spec
area: 80_Specs
projeto: MEGATRON
status: aceito
fase: infra-hardware
tags: [fabios, megatron, spec, hardware, infraestrutura, nos]
criado_em: 2026-07-02
atualizado_em: 2026-07-02
---

# SPEC - Infraestrutura Distribuida e Hardware MEGATRON

## Problema

O FabioOS ja possui RAG, MCP, n8n, OpenClaw, Agentarium, MEGATRON v1 e agentes. Se tudo continuar preso a uma unica maquina e a caminhos locais implicitos, qualquer expansao de hardware exigira retrabalho.

## Objetivo

Preparar o MEGATRON para operar como infraestrutura de nos:

- Core;
- GPU;
- NAS;
- workers futuros;
- interfaces;
- canais externos.

## Escopo desta entrega

1. Formalizar arquitetura fisica/logica.
2. Definir registro configuravel de nos.
3. Definir interfaces minimas de descoberta, roteamento e servicos.
4. Criar roadmap hardware + software.
5. Criar utilitario local para validar e consultar o registro.

## Fora do escopo

- comprar hardware;
- instalar containers;
- subir Qdrant/Postgres/Ollama;
- migrar RAG;
- mover dados;
- alterar `megatron.py`, `registry.py` ou `chat_bridge.py`;
- mudar Agentarium;
- push.

## Contrato de nos

Todo no deve declarar:

```json
{
  "id": "megatron-core",
  "role": "core",
  "status": "active|target|future|disabled",
  "host": "megatron-core.local",
  "priority": 100,
  "capabilities": ["vector_search"],
  "services": [
    {
      "name": "rag_chroma",
      "protocol": "local",
      "endpoint": "60_Sistemas/RAG/fabioos_db",
      "health": "collection_count",
      "data_classes": ["public", "internal"]
    }
  ],
  "limits": {
    "gpu_required": false,
    "twenty_four_seven": true
  }
}
```

## Interface de descoberta

### v0

Arquivo local:

```text
60_Sistemas/MEGATRON/infra/nodes.megatron.example.json
```

### v1

Arquivo local privado:

```text
60_Sistemas/MEGATRON/infra/nodes.megatron.local.json
```

Esse arquivo deve ser gitignored quando existir.

### v2

Control plane em banco/servico:

- Postgres;
- Qdrant para vetores;
- endpoint `/capabilities`;
- endpoint `/health`.

## Roteamento

Entrada:

```json
{
  "capability": "local_llm_inference",
  "data_class": "internal",
  "requires_gpu": true,
  "approval_required": false
}
```

Saida:

```json
{
  "ok": true,
  "node": "gpu-oculink",
  "services": ["ollama", "open_webui"]
}
```

## Balanceamento inicial

1. Filtrar por capacidade.
2. Remover nos `disabled`.
3. Preferir `active`.
4. Aceitar `target` em planejamento.
5. Usar `future` apenas quando `--include-future`.
6. Ordenar por `priority`.
7. Se nao houver no, devolver fallback honesto.

## Criterios de aceite

- [x] Documento de arquitetura criado.
- [x] Roadmap hardware/software criado.
- [x] Registro JSON de nos criado.
- [x] Schema JSON criado.
- [x] Script `node_registry.py` criado.
- [x] `node_registry.py validate` retorna `ok=true`.
- [x] `route --capability vector_search` retorna no elegivel.
- [x] `route --capability local_llm_inference --include-future` retorna GPU Node futuro.
- [x] Nenhum servico real alterado.
- [x] Nenhum segredo versionado.

## Evolucao futura

- `nodes.megatron.local.json` real, gitignored;
- healthcheck de portas;
- integracao com `registry.py`;
- painel Agentarium mostrando nos e servicos;
- Qdrant/Postgres quando houver necessidade real;
- GPU Node apenas apos criterio de uso/custo.
