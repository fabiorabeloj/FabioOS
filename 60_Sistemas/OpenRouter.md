---
tipo: sistema
area: tecnologia
status: ativo
tags: [tecnico, IA, LLM]
criado_em: 2026-06-25
atualizado_em: 2026-06-25
---

# OpenRouter

## O que é?

OpenRouter é um agregador de APIs de LLM que permite usar múltiplos modelos (Claude, GPT-4, Llama, etc) através de uma interface unificada.

## Para que serve?

- Accesso a múltiplos LLMs com API única
- Fallback automático entre modelos
- Otimização de custos
- Integração com [[n8n]], [[Claude Code]] e automações
- Roteamento inteligente de requests

## Modelos disponíveis

| Modelo | Provedor | Velocidade | Custo |
|--------|----------|-----------|-------|
| Claude 3.5 Sonnet | Anthropic | Rápido | Médio |
| GPT-4 Turbo | OpenAI | Médio | Alto |
| Llama 2 70B | Meta | Rápido | Baixo |
| Mistral Large | Mistral | Muito rápido | Muito baixo |

## Onde entra no FabioOS?

[[60_Sistemas|Sistemas]] > [[OpenRouter]] → roteamento:
- Fallback se Claude indisponível
- Otimização de custo-benefício
- Experimentação com modelos
- Integração com [[n8n]] workflows

## Configuração

1. **Criar conta**: https://openrouter.ai
2. **Gerar API key**: Adicionar em `.env` (não commitar!)
3. **Configurar cliente**: [[Claude_Code]], [[n8n]], scripts
4. **Monitorar uso**: Dashboard de custos

## Relações

- ↔ [[Claude_Code]] — cliente Python/CLI
- ↔ [[n8n]] — automações
- ↔ [[MCP]] — protocolo de contexto
- ↔ [[RAG]] — augmentação de contexto

## Próximas ações

- [ ] Configurar fallback entre modelos
- [ ] Documentar estratégia de custo
- [ ] Testar latência por modelo
- [ ] Integrar com n8n workflows
