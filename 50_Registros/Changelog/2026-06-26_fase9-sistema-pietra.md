---
tipo: changelog
area: registros
projeto: FabioOS
status: concluído
fase: 9
tags: [changelog, fase-9, pietra, atendimento, classificacao]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Changelog — Fase 9: Sistema Pietra

## Resumo

Criação do Sistema Pietra — atendimento inteligente para mensagens escolares com 11 categorias, 12 respostas-modelo, regras de classificação, escalonamento e privacidade. O Pietra classifica mensagens e sugere respostas; o envio é sempre responsabilidade humana.

## Arquivos criados

### Sistema e documentação

| Arquivo | Descrição |
|---|---|
| `60_Sistemas/Pietra/Sistema_Pietra.md` | Doc operacional: módulos, fluxo, categorias, integração futura |
| `wiki/projetos/pietra.md` | Wiki do projeto: função, uso atual/futuro, critério de sucesso |

### Módulos operacionais

| Arquivo | Conteúdo |
|---|---|
| `60_Sistemas/Pietra/intents/INTENTS_CATALOGO.md` | 11 categorias com gatilhos, nível de sensibilidade e condição de escalonamento |
| `60_Sistemas/Pietra/respostas-modelo/RESPOSTAS_MODELO.md` | 12 respostas-modelo editáveis por tipo de situação |
| `60_Sistemas/Pietra/regras/REGRAS_CLASSIFICACAO.md` | Processo de classificação, escalonamento obrigatório, privacidade, logs |

## Arquivos atualizados

- `wiki/indices/mapa-fabios.md` — Pietra atualizado para ativo; fase 9 concluída; próxima: 10
- `60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS.md` — fase 9 concluída com entregáveis listados

## Decisões registradas

- **Pietra nunca envia mensagens autonomamente** — apenas prepara para aprovação humana
- **11 categorias** definidas com sensibilidade: baixa (professor, material, horário), média (secretaria, prova, matrícula, etc.), alta (financeiro em disputa, ocorrência)
- **Escalonamento obrigatório** para: bullying, agressão, ameaças legais, dados financeiros em disputa, qualquer situação de risco
- **LGPD explícita**: notas individuais, situação financeira e dados de saúde nunca em respostas automáticas
- **Logs anonimizados**: registrar categoria e ação, nunca nome ou número completo

## Integração futura mapeada

| Fase | Integração |
|---|---|
| 10 | n8n webhook → classificação → log automático |
| 11 | OpenClaw (WhatsApp) → Pietra |
| 12 | RAG sobre respostas anteriores |
| 21 | Dashboard de atendimentos |

## Próxima fase

**Fase 10 — n8n operacional:** criar o primeiro workflow real com webhook gerando nota em `sources/_inbox/`.

## Relações

- [[60_Sistemas/Pietra/Sistema_Pietra]]
- [[wiki/projetos/pietra]]
- [[wiki/sistemas/n8n]]
- [[wiki/sistemas/openclaw]]
- [[50_Registros/Changelog/2026-06-26_fase8-sistema-escola]]
