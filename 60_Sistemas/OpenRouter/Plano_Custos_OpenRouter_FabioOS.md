---
tipo: plano_operacional
area: sistemas
sistema: OpenRouter
status: ativo
criado_em: 2026-06-27
atualizado_em: 2026-06-27
tags: [openrouter, custos, llm, roteamento, api, fabioos]
---

# Plano de Custos OpenRouter - FabioOS

## Missao

Definir como o FabioOS deve usar a API da OpenRouter com alta qualidade, custo controlado e risco baixo.

Plano estrategico relacionado: [[00_Arquitetura/Plano_Orcamento_FabioOS_MEGATRON_2026]].

Principio governante:

> Local primeiro. API quando agrega valor real. Premium somente com motivo registrado.

Este plano nao guarda API key, nao recomenda colar token em chat e nao substitui o RAG/Grafo local. A OpenRouter entra como camada de sintese, classificacao, fallback e automacao quando o contexto local ja foi reduzido ao minimo necessario.

## Fonte de precos

Precos consultados em 2026-06-27 via endpoint oficial:

- `GET https://openrouter.ai/api/v1/models`
- Referencia de uso: `https://openrouter.ai/docs/quickstart`

Os valores mudam. Antes de automatizacoes longas, reconsultar o endpoint de modelos.

## Camadas de uso

| Camada | Uso | Regra |
|---|---|---|
| 0 - Local | RAG, Grafo, scripts, validacoes, consultas sem geracao | Padrao inicial. Sem custo por token e menor exposicao de dados. |
| 1 - Economica | Triagem, classificacao, resumo curto, tarefas repetitivas | Usar por padrao em automacoes. |
| 2 - Balanceada | RAG com resposta sintetizada, codigo moderado, notas estruturadas | Usar quando qualidade importar mais que custo minimo. |
| 3 - Premium | Arquitetura, decisoes importantes, revisao final, tarefas sensiveis | Exige motivo registrado e preferencialmente aprovacao humana. |

## Modelos candidatos

Precos em USD por 1M tokens.

| Modelo | Entrada | Saida | Papel recomendado |
|---|---:|---:|---|
| `openrouter/free` | 0.00 | 0.00 | Testes, nunca dependencia critica. |
| `qwen/qwen3-coder:free` | 0.00 | 0.00 | Testes de codigo, sem garantia operacional. |
| `meta-llama/llama-3.3-70b-instruct:free` | 0.00 | 0.00 | Testes gerais, limites variaveis. |
| `openai/gpt-5-nano` | 0.05 | 0.40 | Classificacao barata e chamadas pequenas. |
| `mistralai/mistral-small-3.2-24b-instruct` | 0.075 | 0.20 | Triagem barata e resumo curto. |
| `deepseek/deepseek-v4-flash` | 0.09 | 0.18 | Automacoes economicas, alto volume. |
| `meta-llama/llama-3.3-70b-instruct` | 0.10 | 0.32 | Uso economico geral. |
| `openai/gpt-4o-mini` | 0.15 | 0.60 | Fallback barato OpenAI-compatible. |
| `deepseek/deepseek-chat-v3.1` | 0.21 | 0.79 | Raciocinio medio com custo controlado. |
| `openai/gpt-5-mini` | 0.25 | 2.00 | Padrao balanceado para FabioOS. |
| `google/gemini-2.5-flash` | 0.30 | 2.50 | RAG/sintese rapida com boa janela. |
| `anthropic/claude-haiku-4.5` | 1.00 | 5.00 | Alternativa Anthropic economica. |
| `google/gemini-2.5-pro` | 1.25 | 10.00 | Premium para arquitetura e revisao. |
| `openai/gpt-5` | 1.25 | 10.00 | Premium principal para decisoes do FabioOS. |
| `mistralai/mistral-large` | 2.00 | 6.00 | Premium alternativo com saida relativamente barata. |
| `openai/gpt-4.1` | 2.00 | 8.00 | Compatibilidade e raciocinio geral. |
| `openai/gpt-4o` | 2.50 | 10.00 | Multimodal/geral quando necessario. |
| `anthropic/claude-sonnet-4.5` | 3.00 | 15.00 | Premium critico, usar com parcimonia. |

## Custo estimado por tipo de chamada

| Tarefa | Tamanho estimado | Economica | Balanceada | Premium |
|---|---:|---:|---:|---:|
| Triagem curta | 2k entrada + 300 saida | ~US$0.0002 | ~US$0.0011 | ~US$0.0055 a US$0.0105 |
| RAG medio | 8k entrada + 1.5k saida | ~US$0.0010 | ~US$0.0050 a US$0.0061 | ~US$0.0250 a US$0.0465 |
| Arquitetura | 30k entrada + 5k saida | ~US$0.0035 | ~US$0.0175 a US$0.0215 | ~US$0.0875 a US$0.1650 |
| Revisao longa | 100k entrada + 10k saida | ~US$0.0100 | ~US$0.0450 a US$0.0550 | ~US$0.2250 a US$0.4500 |

Conclusao: o maior risco nao e uma chamada isolada. O risco real e automacao sem limite, loop, reprocessamento de vault inteiro ou envio de contexto bruto.

## Orcamento recomendado

Para a melhor estrutura inicial, recomendo comecar com teto de **US$100** na OpenRouter.

Distribuicao operacional:

| Centro de custo | Teto inicial | Uso |
|---|---:|---|
| `fabios-dev` | US$10 | Testes de scripts, comparacao de modelos e validacoes. |
| `fabios-rag` | US$25 | Respostas sintetizadas com fontes a partir do RAG local. |
| `fabios-automacoes` | US$25 | n8n, Inbox, Pietra, classificacoes e respostas curtas. |
| `fabios-premium` | US$40 | GPT-5/Gemini Pro/Sonnet para decisoes, revisoes e arquitetura. |

Se quiser comecar menor: US$50 tambem funciona, com premium mais restrito. Se as automacoes entrarem em producao diaria, subir para US$200 somente depois de 7 dias de metricas reais.

## Roteamento por tarefa

| Tarefa FabioOS | Modelo padrao | Fallback | Quando subir para premium |
|---|---|---|---|
| Inbox / triagem | `deepseek/deepseek-v4-flash` | `mistralai/mistral-small-3.2-24b-instruct` | Nunca, salvo caso sensivel. |
| Pietra / WhatsApp | `deepseek/deepseek-v4-flash` | `openai/gpt-5-nano` | Mensagem delicada, juridica, familiar ou de alto impacto. |
| Arquivista | `openai/gpt-5-mini` | `deepseek/deepseek-chat-v3.1` | Nota estrategica ou sintese complexa. |
| RAG com fontes | `openai/gpt-5-mini` | `google/gemini-2.5-flash` | Decisao importante ou resposta que vira documento oficial. |
| Codigo / scripts | `openai/gpt-5-mini` | `deepseek/deepseek-chat-v3.1` | Arquitetura, seguranca ou alteracao com alto risco. |
| Governanca / MEGATRON | `openai/gpt-5` | `google/gemini-2.5-pro` | Usar premium por padrao em decisoes estruturais. |
| Revisao final critica | `openai/gpt-5` | `anthropic/claude-sonnet-4.5` | Sempre registrar motivo e custo estimado. |

## Regras de privacidade

Nunca enviar para OpenRouter:

- tokens, API keys, `.env`, credenciais ou cookies;
- logs brutos de execucao;
- `fabioos_db/` ou bases vetoriais;
- `00_Inbox/` e `05_Raw_Sources/_compat_sources/_inbox/` sem triagem;
- dados pessoais sensiveis sem mascaramento;
- arquivos inteiros quando trechos bastam.

Fluxo correto:

1. Buscar localmente com RAG/Grafo/scripts.
2. Selecionar apenas os trechos necessarios.
3. Mascarar dados sensiveis.
4. Chamar OpenRouter com modelo adequado.
5. Registrar modelo, finalidade e custo estimado.

## Regras de operacao

- Usar `OPENROUTER_API_KEY` em variavel de ambiente local ou credencial do n8n.
- Nunca versionar chave real.
- Preferir chaves separadas por uso quando possivel: dev, RAG, automacoes, premium.
- Definir limite diario por automacao.
- Em loops ou lotes, exigir `--limit`, `--dry-run` ou amostragem inicial.
- Chamada premium deve registrar motivo em log operacional.
- `openrouter/auto` e modelos `:free` podem ser usados em teste, mas nao devem ser base de processo critico.

## Politica de geracao no RAG

O modo mais seguro continua sendo:

- `sem --generate`: recupera trechos e fontes localmente, sem custo e sem enviar conteudo externo.
- `com --generate`: permitido quando o usuario quer resposta sintetizada por LLM, com contexto minimo e custo estimado.

Para automacao: `--generate` deve ser opt-in explicito.

## Decisao recomendada

Adotar OpenRouter como camada de IA externa do FabioOS com teto inicial de **US$100**, roteamento por tarefa e premium controlado.

O objetivo nao e gastar menos a qualquer custo. O objetivo e gastar onde a inteligencia melhora o sistema: decisoes estruturais, sintese confiavel, automacoes bem limitadas e respostas com fontes.
