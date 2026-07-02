---
tipo: adr
area: 50_Registros
projeto: MEGATRON
status: aceito
tags: [adr, fabios, megatron, llm-router, compute-manager, modelos]
criado_em: 2026-07-02
---

# ADR - LLM Orchestrator e Compute Manager no MEGATRON

## Contexto

O FabioOS nao deve depender de um modelo universal. Claude, ChatGPT, Codex, Gemini, Qwen, DeepSeek, Whisper e modelos locais possuem vocacoes diferentes.

Se cada agente chamar um provedor diretamente, o sistema ficara caro, fragil e dificil de auditar.

## Decisao

Criar um LLM Orchestrator dentro do Compute Manager do MEGATRON.

Agentes devem solicitar aliases de capacidade:

- `architecture_model`;
- `coding_model`;
- `long_context_model`;
- `ocr_vision_model`;
- `cheap_classifier_model`;
- `voice_stt_model`;
- `voice_tts_model`.

O Orchestrator escolhe o provedor/modelo real com base em:

- tarefa;
- classe de dado;
- custo;
- qualidade;
- localidade;
- disponibilidade;
- fallback.

## Consequencias

### Positivas

- Trocar Claude/GPT/Gemini/Qwen nao quebra agentes.
- Permite controle de custo.
- Permite privacidade por classe de dado.
- Permite A/B testing e fallback.
- Prepara o MEGATRON para modelos locais e cloud juntos.

### Custos

- Mais uma camada de configuracao.
- Necessidade de telemetria real.
- Necessidade de manter registry de modelos.

## Regra

Nunca escrever:

```text
claude()
gpt()
gemini()
```

Escrever:

```text
architecture_model()
coding_model()
long_context_model()
ocr_vision_model()
```

## Relacoes

- [[60_Sistemas/MEGATRON/infra/Compute_Manager_LLM_Orchestrator]]
- [[80_Specs/MEGATRON/2026-07-02_compute-manager-llm-orchestrator]]
- [[60_Sistemas/MEGATRON/infra/model_registry.example.json]]
- [[60_Sistemas/MEGATRON/infra/llm_router.py]]
