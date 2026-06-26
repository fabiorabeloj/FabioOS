---
tipo: wiki
area: sistemas
projeto: FabioOS
status: ativo
camada: camada-1
tags: [openrouter, ia, roteamento, api, llm, camada-1]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# OpenRouter

## Função no FabioOS

[DECISÃO] O OpenRouter é a **camada de roteamento de IAs** do FabioOS — ponto único de acesso a múltiplos modelos (Claude, GPT, Gemini, Llama, Mistral e outros) via API unificada, sem necessidade de gerenciar múltiplas chaves separadas.

## O que essa ferramenta faz

[FATO] API gateway que unifica acesso a dezenas de modelos de linguagem de diferentes provedores. Mesma interface OpenAI-compatível para todos os modelos. Cobrança pay-per-token por modelo escolhido.

No FabioOS, o OpenRouter cumpre:

- Acesso programático a múltiplos LLMs via uma única API
- Fallback automático entre modelos se um estiver indisponível
- Comparação de modelos com o mesmo prompt
- Redução de custo ao rotear tarefas simples para modelos menores
- Base para automações n8n que precisam de IA sem depender de um único provedor

[FATO] Configurado no FabioOS como provedor de API para acesso programático. Detalhes de configuração ativa: pendente de teste — registrado em `60_Sistemas/` mas integração técnica não validada nesta sessão.

## O que essa ferramenta não deve fazer

- Substituir o Claude Code como operador do repositório
- Ser usado para enviar dados sensíveis do vault a modelos não auditados
- Tornar-se único ponto de dependência — manter acesso direto aos provedores principais como backup

## Relação com outras ferramentas

| Ferramenta | Relação |
|---|---|
| [[wiki/sistemas/chatgpt]] | GPT-4/GPT-4o acessíveis via OpenRouter |
| [[wiki/sistemas/n8n]] | n8n pode chamar OpenRouter em workflows de IA |
| [[wiki/sistemas/claude-code]] | Claude Code pode usar OpenRouter para tarefas auxiliares |

## Uso atual

- [x] Conta configurada e mencionada na workstation do FabioOS
- [ ] Integração técnica ativa: **pendente de teste**
- [ ] Nenhum workflow n8n usa OpenRouter ainda

## Uso futuro

- [ ] Nó HTTP do n8n → OpenRouter → resposta de IA em workflows
- [ ] Comparação de modelos para tarefas específicas (ex: resumo, classificação, extração)
- [ ] Fallback de modelo quando Claude estiver indisponível

## Riscos e cuidados

- **Chave de API**: a chave do OpenRouter não deve estar em arquivos commitados — usar variável de ambiente ou secrets do n8n
- **Custo por token**: modelos caros (GPT-4o, Claude 3 Opus) podem gerar custo alto em automações — monitorar uso
- **Privacidade dos dados**: avaliar quais dados do FabioOS podem ser enviados a modelos externos

## Próximas ações

- [ ] Confirmar se a chave do OpenRouter está configurada em variável de ambiente ou no n8n
- [ ] Criar primeiro workflow n8n que use OpenRouter para classificação simples
- [ ] Documentar modelos preferidos por tipo de tarefa

## Links internos

- [[wiki/indices/mapa-fabios]]
- [[wiki/sistemas/chatgpt]]
- [[wiki/sistemas/n8n]]
- [[wiki/sistemas/claude-code]]
- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]
