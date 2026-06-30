---
tipo: sistema
area: 60_Sistemas
projeto: FabioOS
sistema: n8n
workflow: FabioOS_Intake_Orquestrador_Seguro
status: importado-inativo
data: 2026-06-29
tags: [fabios, n8n, orquestracao, intake, agentes, seguranca]
---

# Workflow: FabioOS - Intake Orquestrador Seguro

## Objetivo

Ser a cadeia-mae de entrada do FabioOS no n8n.

Ele recebe uma entrada generica, normaliza, valida, classifica, aplica politica de permissao, roteia para agente/sistema, monta um rascunho Obsidian e responde com auditoria.

## Principio

Complexidade boa nao e quantidade de nos. E cadeia com controle.

Este workflow e deliberadamente **sem efeito externo**:

- nao grava arquivo;
- nao chama RAG;
- nao chama OpenRouter;
- nao envia WhatsApp;
- nao aciona OpenClaw;
- nao cria credenciais.

## Endpoint

```text
POST http://127.0.0.1:5678/webhook/fabios-intake
```

## Entrada esperada

```json
{
  "titulo": "Ideia para FabioOS",
  "conteudo": "Texto a processar",
  "origem": "manual",
  "canal": "web",
  "tipo": "texto"
}
```

## Cadeia

1. Webhook - Entrada Universal
2. Normalizar Entrada
3. Validar Schema e Seguranca
4. Classificar Dominio e Intencao
5. Aplicar Politica de Permissao
6. Roteador de Agente
7. Montar Rascunho Obsidian
8. Preparar Auditoria
9. Responder Sem Efeito Externo

## Roteamentos possiveis

| Intencao | Agente sugerido | Permissao padrao | Destino sugerido |
|---|---|---|---|
| captura | `agent.inbox` | propose_only | `00_Inbox/Triagem` |
| arquivamento | `agent.arquivista` | propose_only | `40_Wiki/_MOCs` |
| consulta_semantica | `agent.rag` | read_only | `60_Sistemas/RAG` |
| pre_commit | `agent.safecommit` | propose_only | `50_Registros/Auditoria` |
| status_operacional | `agent.dashboard` | propose_only | `10_Dashboard` |
| atendimento_escolar | `agent.inbox` | manual_approval | `00_Inbox/Triagem` |

## Visualizacao

- Painel: http://127.0.0.1:5678/
- Workflow: http://127.0.0.1:5678/workflow/fabioosIntakeOrquestradorSeguro

## Ativacao

Manter inativo ate decisao humana.

Para testar sem efeitos externos, usar o modo de teste do n8n ou ativar temporariamente sabendo que o endpoint apenas responde JSON e nao escreve no vault.

## Evolucao futura

1. Adicionar gravacao segura em `00_Inbox/Capturas/`.
2. Conectar ao Arquivista para transformar captura aprovada em nota.
3. Conectar ao RAG em modo read-only.
4. Conectar ao Dashboard para observabilidade.
5. Adicionar fila/retry para tarefas longas.
6. Adicionar token obrigatorio no webhook.
7. Adicionar trilha de custo e modelo quando houver API externa.
