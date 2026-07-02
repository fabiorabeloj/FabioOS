---
tipo: changelog
area: MEGATRON
projeto: FabioOS
status: registrado
tags: [fabios, megatron, llm-router, compute-manager, changelog]
criado_em: 2026-07-02
---

# Changelog - Compute Manager e LLM Orchestrator

## Adicionado

- Documento `Compute_Manager_LLM_Orchestrator`.
- SPEC do Compute Manager / LLM Orchestrator.
- ADR para impedir chamadas diretas a provedores.
- `model_registry.example.json`.
- `llm_router.py`, roteador deterministico de modelos.

## Validacoes executadas

- `python -m py_compile 60_Sistemas/MEGATRON/infra/llm_router.py` - OK.
- `llm_router.py validate` - `ok=true`.
- `route --task coding --data-class internal` - seleciona `coding_model` / `codex_local`.
- `route --task ocr --data-class restricted --include-future` - seleciona `ocr_vision_model` / `qwen_vl_local`.
- `route --task architecture --data-class internal --quality high` - seleciona `architecture_model`.
- `route --task architecture --data-class forbidden_external --quality high` - bloqueia cloud e retorna fallback.

## Limites

- Nenhuma API chamada.
- Nenhum modelo instalado.
- Nenhum segredo criado.
- Nenhum runtime alterado.
- Nenhum push.
