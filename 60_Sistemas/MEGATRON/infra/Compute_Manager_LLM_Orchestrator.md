---
tipo: arquitetura
area: 60_Sistemas
projeto: MEGATRON
status: proposto
tags: [fabios, megatron, compute-manager, llm-router, llm-orchestrator, custos, observabilidade]
criado_em: 2026-07-02
atualizado_em: 2026-07-02
---

# Compute Manager e LLM Orchestrator do MEGATRON

## Funcao

Definir o componente que decide onde uma tarefa deve rodar:

- qual agente;
- qual modelo;
- qual no fisico;
- qual custo aceitavel;
- qual politica de privacidade;
- qual fallback.

O Compute Manager nao e um LLM. E uma camada operacional.

## Problema

O MEGATRON nao deve perguntar "qual LLM usar?" em cada conversa.

Ele deve perguntar:

```text
qual capacidade esta tarefa exige?
qual classe de dado esta envolvida?
qual qualidade minima e necessaria?
qual custo e permitido?
qual no esta disponivel?
qual modelo atende melhor?
```

## Componentes

```text
Entrada
  -> Intake Universal
  -> Classificador
  -> Compute Manager
       -> Node Registry
       -> Model Registry
       -> Cost Policy
       -> Privacy Policy
       -> Observability
  -> Agente executor
  -> Log / memoria / aprovacao humana
```

## LLM Orchestrator

Subcomponente do Compute Manager responsavel por escolher modelos por papel.

Agentes nunca devem chamar diretamente:

```text
claude()
gpt()
gemini()
qwen()
```

Devem chamar aliases:

```text
architecture_model
coding_model
long_context_model
ocr_vision_model
cheap_classifier_model
local_private_model
voice_stt_model
voice_tts_model
```

## Matriz inicial de vocacao

| Papel | Modelo/ferramenta candidata | Uso |
|---|---|---|
| arquitetura/escrita longa | Claude | planejamento, docs, revisao estrutural |
| raciocinio geral/sintese | ChatGPT/OpenAI | integracao, matematica, estrategia |
| codigo/testes/git | Codex | implementacao local, refatoracao, commits |
| contexto gigante/PDF/video | Gemini | leitura longa e multimodal |
| OCR/visao local | Qwen-VL ou equivalente | OCR privado e classificacao visual |
| codigo barato/local | DeepSeek/Qwen coder | lotes baratos, refatoracao secundaria |
| voz para texto | Whisper local | notas de voz |
| voz do sistema | Piper/Kokoro local | fala local do MEGATRON |
| classificacao segura | MEGATRON Core deterministico | triagem, sensibilidade, dominio |

## Politica de privacidade

| Classe | Regra |
|---|---|
| public | pode usar cloud/API |
| internal | pode usar cloud com controle de custo |
| private | preferir local; cloud so com aprovacao/contexto minimo |
| restricted | local/humano; cloud bloqueada por padrao |
| no_rag | local/humano; nao indexar |
| forbidden_external | local/humano; jamais cloud/API |

## Politica de custo

1. Tarefa simples usa modelo barato/deterministico.
2. Tarefa arquitetural usa modelo premium quando justificado.
3. Tarefa em lote usa modelo barato/local.
4. Tarefa sensivel prioriza local/humano.
5. Todo uso de API deve gerar evento de custo.

## Observabilidade necessaria

O Compute Manager deve registrar:

- task_id;
- agente solicitante;
- alias de modelo;
- modelo real;
- no escolhido;
- latencia;
- custo estimado;
- tokens de entrada/saida quando houver;
- classe de dado;
- sucesso/falha;
- fallback usado;
- aprovacao humana quando aplicavel.

## Continuidade operacional

Apos reinicio, o Kernel/Compute Manager deve responder:

- quais tarefas estavam pendentes;
- quais estavam executando;
- quais falharam;
- quais podem ser reexecutadas;
- qual banco esta consistente;
- qual backup foi validado;
- quais servicos estao vivos.

## Relacao com hardware

GPU e apenas um no:

```text
task -> capability -> node -> model -> execution
```

Nao e o cerebro.

## Implementacao v0

Arquivos:

- `model_registry.example.json`;
- `llm_router.py`;
- `nodes.megatron.example.json`;
- `node_registry.py`.

O v0 nao chama APIs. Ele apenas decide e explica a decisao.

## Proximas acoes

- [ ] Integrar `llm_router.py` ao `chat_bridge.py` em modo read-only/propose-only.
- [ ] Criar `model_registry.local.json` gitignored com modelos realmente disponiveis.
- [ ] Adicionar telemetria de custo no barramento/event log.
- [ ] Exibir "modelo escolhido" no Agentarium.
- [ ] Criar fallback: premium -> barato -> local -> humano.
