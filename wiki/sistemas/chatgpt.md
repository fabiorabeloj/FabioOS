---
tipo: wiki
area: sistemas
projeto: FabioOS
status: ativo
camada: camada-1
tags: [chatgpt, ia, estratégia, planejamento, openai, camada-1]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# ChatGPT

## Função no FabioOS

[DECISÃO] O ChatGPT funciona como **consultor estratégico e planejador externo** do FabioOS — orienta, estrutura e formaliza planos, mas não opera diretamente no repositório. Complementa o Claude Code sem substituí-lo.

## O que essa ferramenta faz

[FATO] Interface web e API da OpenAI para modelos GPT. Suporta conversas longas, geração de documentos, análise de textos e raciocínio multi-etapa. Disponível via browser (chat.openai.com) e via API (OpenRouter ou direta).

No FabioOS, o ChatGPT cumpre:

- Desenhar fases e planos de implementação
- Organizar e estruturar decisões complexas
- Comparar ferramentas e abordagens antes de executar
- Ajudar a escrever prompts para outras IAs
- Formalizar documentos de arquitetura (como o Plano Mestre)
- Raciocinar sobre prioridades e trade-offs estratégicos

[INTERPRETAÇÃO] O ChatGPT tende a ser mais forte em raciocínio estratégico e síntese de alto nível; o Claude Code é mais forte em execução técnica local e manutenção de contexto no repositório. Os dois se complementam.

## O que essa ferramenta não deve fazer

- Editar arquivos do vault diretamente (sem integração técnica configurada)
- Substituir o Claude Code na operação do repositório
- Ser a única IA consultada — decisões críticas devem considerar múltiplas fontes
- Receber dados sensíveis (tokens, credenciais, dados de alunos) em conversas

## Relação com outras ferramentas

| Ferramenta | Relação |
|---|---|
| [[wiki/sistemas/claude-code]] | Claude Code executa o que o ChatGPT planeja |
| [[wiki/sistemas/openrouter]] | OpenRouter pode rotear chamadas para GPT via API |
| [[wiki/sistemas/obsidian]] | Planos do ChatGPT devem ser salvos no vault |

## Uso atual

- [x] Usado manualmente via browser para planejamento de fases
- [x] Gerou o Plano Mestre de Implantação do FabioOS
- [ ] Sem integração técnica direta com o repositório

## Uso futuro

- [ ] Integração via OpenRouter para chamadas programáticas em n8n
- [ ] Agente de planejamento em workflows de automação
- [ ] Consulta paralela com Claude para decisões críticas

## Riscos e cuidados

- **Contexto não persistido**: o ChatGPT não lembra sessões anteriores sem plugins — planos devem ser salvos no vault imediatamente
- **Dados sensíveis**: nunca enviar tokens, credenciais, dados de alunos ou informações sigilosas a IAs externas
- **Divergência entre IAs**: ChatGPT e Claude podem dar respostas contraditórias — usar o vault como árbitro da decisão final

## Próximas ações

- [ ] Salvar outputs estratégicos do ChatGPT em `sources/research/` ou `40_Decisoes/`
- [ ] Definir quando usar ChatGPT vs Claude Code como critério operacional

## Links internos

- [[wiki/indices/mapa-fabios]]
- [[wiki/sistemas/claude-code]]
- [[wiki/sistemas/openrouter]]
- [[wiki/sistemas/obsidian]]
- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]
