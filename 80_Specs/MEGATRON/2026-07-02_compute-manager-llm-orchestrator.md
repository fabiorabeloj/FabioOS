---
tipo: spec
area: 80_Specs
projeto: MEGATRON
status: aceito
fase: compute-manager
tags: [fabios, megatron, compute-manager, llm-router, observabilidade, custos]
criado_em: 2026-07-02
atualizado_em: 2026-07-02
---

# SPEC - Compute Manager e LLM Orchestrator do MEGATRON

## Problema

O MEGATRON esta deixando de ser um conjunto de agentes e passando a ser uma infraestrutura operacional.

O gargalo real deixa de ser "qual LLM e melhor?" e passa a ser:

```text
qual modelo, em qual no, com qual custo, para qual classe de dado, com qual prioridade?
```

## Objetivo

Criar uma camada de decisao para:

- escolher modelo por tarefa;
- escolher no por capacidade;
- aplicar politica de privacidade;
- controlar custo;
- registrar observabilidade;
- permitir fallback.

## Entrega v0

- Documento de arquitetura: [[60_Sistemas/MEGATRON/infra/Compute_Manager_LLM_Orchestrator]]
- `model_registry.example.json`
- `llm_router.py`
- ADR de orquestracao de modelos
- changelog

## Fora do escopo

- chamar APIs reais;
- instalar Ollama/Qwen/DeepSeek;
- alterar `chat_bridge.py`;
- alterar Agentarium;
- criar chaves;
- enviar dados externos;
- fazer push.

## Contrato

Entrada:

```json
{
  "task": "coding",
  "data_class": "internal",
  "quality": "balanced",
  "prefer_local": false
}
```

Saida:

```json
{
  "ok": true,
  "selected": {
    "alias": "coding_model",
    "provider": "codex",
    "execution_mode": "agent_tool"
  },
  "approval_required": false
}
```

## Regras

- Agentes chamam aliases, nao provedores.
- `forbidden_external`, `restricted` e `no_rag` nao podem ir para cloud.
- `private` exige minimizacao ou aprovacao.
- Se nao houver modelo elegivel, devolver fallback honesto.
- O roteador v0 nao chama API.

## Criterios de aceite

- [x] `llm_router.py validate` retorna `ok=true`.
- [x] `route --task coding --data-class internal` escolhe `coding_model`.
- [x] `route --task ocr --data-class restricted --include-future` escolhe modelo local futuro.
- [x] `route --task architecture --data-class internal --quality high` escolhe modelo de arquitetura.
- [x] `route --task architecture --data-class forbidden_external --quality high` bloqueia cloud.
- [x] `py_compile` passa.
- [x] Nenhum segredo versionado.

## Evolucao

- Integrar ao `chat_bridge.py` como modo `--route-model`.
- Registrar metricas de custo/latencia no barramento.
- Exibir alias/modelo escolhido no Agentarium.
- Criar `model_registry.local.json` gitignored.
- Criar A/B testing entre modelos por tarefa.
