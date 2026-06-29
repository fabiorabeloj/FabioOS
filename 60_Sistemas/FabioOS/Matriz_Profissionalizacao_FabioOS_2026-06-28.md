---
tipo: matriz
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, megatron, profissionalizacao, tecnologia, roadmap]
criado_em: 2026-06-28
atualizado_em: 2026-06-28
---

# Matriz de Profissionalizacao do FabioOS

## Funcao

Avaliar tecnologias, anuncios e novas ideias pelo que elas ensinam para a estrutura do FabioOS.

## Matriz

| Sinal / tecnologia | Ensinamento estrutural | Entra como | Prioridade |
|---|---|---|---|
| Agentes | Sistemas modernos operam por papeis especializados | MEGATRON + agentes com limites | Alta |
| MCP | Ferramentas precisam de contrato padrao | Fases 14-15 | Alta |
| RAG | Memoria precisa ser consultavel com fonte | Fase 12 | Alta |
| Grafo | Conhecimento precisa de relacoes, nao so busca | Fase 13 | Alta |
| Python | Automacoes locais precisam ser auditaveis | Scripts, workers, validadores | Alta |
| n8n | Gatilhos externos precisam de fluxo visual e credenciais | Fases 10, 11, 20, 23 | Alta |
| PostgreSQL/Supabase | Markdown nao resolve estado operacional estruturado | Subfase 20.5 | Media-alta |
| Dashboard | Sistema profissional precisa ser visivel | Fase 21 | Alta |
| Observabilidade | Sem logs, custo e erro, agente vira caixa-preta | Subfase 21.5 | Alta |
| Seguranca/privacidade | Automacao sem permissao vira risco | Fase 22 + 22.5 | Critica |
| Deploy/VPS/Docker | Producao exige ambiente reprodutivel | Fase 23 + 23.5 | Media |
| Cursor | Desenvolvimento maior precisa de oficina especializada | Fase 16.5 | Media |
| Hermes | Pode ser executor, mas exige contrato e logs | Fase 17 opcional | Baixa ate prova |
| OpenClaw | Bom canal conversacional, mas instavel sem auth/escopo | Fase 11 controlada | Media |
| OpenRouter | Bom roteador de modelos, mas precisa teto de custo | 22.5 / geracao assistida | Media |
| Lovable/Framer | Bom para prototipo visual, ruim como base opaca | Prototipo descartavel | Baixa |
| Stripe/Resend | So fazem sentido quando houver produto externo | Fase 25 | Baixa agora |
| PostHog | Analytics so faz sentido com app/usuarios | 21.5 ou 25 | Baixa agora |
| MongoDB | Util se documentos/logs crescerem alem do vault | Avaliar depois | Baixa |
| Kafka/Kubernetes | Complexidade de escala antes da escala | Futuro distante | Baixa |
| Hardware local | Privacidade e custo podem melhorar, mas exige uso medido | Fase 26 | Baixa agora |

## Caminhos minimos de teste

| Capacidade | Caminho minimo antes de promover |
|---|---|
| Nova IA | Registrar papel, dados acessados, custo e limite; executar tarefa read-only |
| Novo MCP | Expor uma ferramenta read-only; testar erro, log e retorno com fonte |
| Novo workflow n8n | Rodar com payload falso; registrar entrada, saida e falha esperada |
| Novo banco | Definir tipo de dado; criar schema minimo; testar backup/restore |
| Novo dashboard | Mostrar fonte do dado, status e ultima atualizacao |
| Novo canal externo | Receber mensagem de teste sem envio real e sem acao destrutiva |
| Novo deploy | Criar ambiente separado, rollback e log de versao |
| Novo material de mercado | Rodar `radar_tecnologico.py`, revisar a analise e so entao decidir se vira SPEC, estudo ou descarte |

## Regra de decisao rapida

Se a tecnologia melhora **memoria, permissao, log, recuperacao, automacao ou deploy**, ela pode entrar no roadmap.

Se melhora apenas aparencia, hype ou sensacao de poder, fica em observacao.
