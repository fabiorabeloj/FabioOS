---
tipo: wiki
area: projetos
projeto: FabioOS
sistema: Pietra
status: ativo
camada: camada-5
tags: [pietra, atendimento, classificacao, whatsapp, escola, camada-5]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Sistema Pietra

## Função no FabioOS

[DECISÃO] O Sistema Pietra é o **módulo de atendimento inteligente** do FabioOS — classifica mensagens recebidas de pais e responsáveis, sugere respostas padronizadas e encaminha para aprovação humana antes de qualquer envio externo.

## O que este sistema faz

[FATO] O Pietra opera em três etapas: classifica a mensagem por categoria (11 categorias definidas), sugere uma resposta baseada em modelo, e aguarda aprovação humana para envio.

**Nunca envia mensagens de forma autônoma.**

Categorias:

| Categoria | Sensibilidade |
|---|---|
| financeiro | Alta — redirecionar à secretaria |
| secretaria | Média |
| coordenação | Média |
| professor | Baixa |
| material | Baixa |
| horário | Baixa |
| prova | Média |
| matrícula | Média |
| segunda chamada | Média |
| ocorrência | Alta — sempre escalonar |
| dúvida pedagógica | Média |

## O que este sistema não deve fazer

- Enviar mensagens sem aprovação humana explícita
- Informar notas, ocorrências ou dados financeiros automaticamente
- Tomar decisões pedagógicas ou administrativas
- Comprometer a escola em respostas automáticas

## Relação com outras ferramentas

| Ferramenta | Relação |
|---|---|
| [[wiki/sistemas/openclaw]] | Gateway futuro: WhatsApp → Pietra (Fase 11) |
| [[wiki/sistemas/n8n]] | Webhook → classificação → log automático (Fase 10) |
| [[wiki/sistemas/claude-code]] | Claude Code gera respostas sugeridas agora |
| [[wiki/projetos/escola]] | Escola gera materiais; Pietra comunica |

## Uso atual

- [x] Documentação: `60_Sistemas/Pietra/Sistema_Pietra.md`
- [x] Catálogo de intents: `60_Sistemas/Pietra/intents/INTENTS_CATALOGO.md`
- [x] Respostas-modelo: `60_Sistemas/Pietra/respostas-modelo/RESPOSTAS_MODELO.md`
- [x] Regras de classificação: `60_Sistemas/Pietra/regras/REGRAS_CLASSIFICACAO.md`
- [ ] Nenhuma mensagem real processada ainda — aguardando primeiro uso

## Uso futuro

- [ ] Webhook n8n para captura automática de mensagens (Fase 10)
- [ ] Gateway WhatsApp via OpenClaw (Fase 11)
- [ ] RAG para buscar respostas anteriores similares (Fase 12)
- [ ] Dashboard de atendimentos com métricas (Fase 21)

## Critério de sucesso

[DECISÃO] A Fase 9 estará concluída quando:

> "Uma mensagem simulada é classificada corretamente e recebe resposta sugerida."

Teste objetivo: enviar 5 mensagens-teste ao Claude Code e verificar se a classificação e a resposta sugerida estão adequadas para cada categoria.

## Links internos

- [[60_Sistemas/Pietra/Sistema_Pietra]]
- [[wiki/projetos/escola]]
- [[wiki/sistemas/openclaw]]
- [[wiki/indices/mapa-fabios]]
- [[60_Sistemas/FabioOS/Protocolo_Operacional_FabioOS]]
