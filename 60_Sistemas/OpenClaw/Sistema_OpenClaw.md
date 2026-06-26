---
tipo: sistema
area: 60_Sistemas
projeto: FabioOS
sistema: OpenClaw
status: documentado-pendente-ativacao
tags: [openclaw, gateway, whatsapp, evolution-api, n8n, pietra]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Sistema OpenClaw — Gateway Conversacional

## Função

OpenClaw é a **porta externa do FabioOS**: recebe mensagens de canais externos (WhatsApp, futuramente Telegram), classifica-as pelo Pietra e aciona ações controladas — tudo com aprovação humana antes de qualquer resposta.

## Tecnologia base

[DECISÃO] **Evolution API** — plataforma open-source de integração com WhatsApp Business via protocolo Baileys. Roda em Docker, expõe REST API e webhooks. Escolhida por ser autogerenciada, gratuita e compatível com n8n.

```
WhatsApp Business (número da escola)
        ↓
  Evolution API         ← Docker, porta 8080
  (webhook ao receber)
        ↓
       n8n              ← workflow FabioOS_WhatsApp_Pietra
  (classifica + salva)
        ↓
  Pietra classifica
        ↓
  Professor recebe notificação
  (classificação + resposta sugerida)
        ↓
  Professor APROVA e ENVIA
```

## Módulos

```
60_Sistemas/OpenClaw/
├── Sistema_OpenClaw.md         ← este arquivo
├── setup/
│   └── EVOLUTION_API_SETUP.md  ← como instalar e configurar
└── logs/                       ← logs anonimizados (nunca committar)
```

## Fluxo completo de atendimento

### 1. Entrada
Pai/responsável envia mensagem para o número WhatsApp da escola.

### 2. Recepção (Evolution API)
A Evolution API recebe a mensagem e dispara um webhook para o n8n com payload:
```json
{
  "event": "messages.upsert",
  "data": {
    "key": { "remoteJid": "5511999999999@s.whatsapp.net" },
    "message": { "conversation": "Boa tarde, quando é a prova de geo?" },
    "pushName": "Nome do Remetente"
  }
}
```

### 3. Processamento (n8n — FabioOS_WhatsApp_Pietra)
1. Extrai número (anonimizado), mensagem e nome
2. Classifica intent por palavras-gatilho (INTENTS_CATALOGO.md)
3. Determina nível de sensibilidade (baixo / médio / alto)
4. Salva log anonimizado em `sources/_inbox/`
5. Prepara resposta-modelo do RESPOSTAS_MODELO.md
6. Envia notificação ao professor com: mensagem original + classificação + sugestão

### 4. Aprovação humana
O professor recebe a notificação, revisa a sugestão, edita se necessário e envia pelo canal oficial da escola.

**Regra central:** Evolution API pode RECEBER e NOTIFICAR. O professor ENVIA. A IA nunca envia mensagem externa de forma autônoma.

## Estados de mensagem

| Estado | Descrição |
|---|---|
| `recebida` | Chegou pela Evolution API |
| `classificada` | Pietra identificou o intent |
| `escalada` | Encaminhada diretamente ao coordenador |
| `sugerida` | Resposta preparada, aguardando aprovação |
| `aprovada` | Professor aprovou a resposta |
| `enviada` | Resposta transmitida pelo professor |
| `nao-classificada` | Triagem manual necessária |

## Nomeação de logs

```
logs/PIETRA_[YYYY-MM]_LOG.md
```

Formato do log (anonimizado):
```
| 2026-06-26 14:32 | WhatsApp | prova | médio | sugerida | pendente |
| 2026-06-26 14:45 | WhatsApp | ocorrência | alto | escalada | coordenação |
```

Nunca registrar: nome completo, número de telefone completo, dados de alunos identificáveis.

## Integração futura

| Fase | Expansão |
|---|---|
| 12 | RAG: buscar respostas anteriores similares antes de sugerir |
| 14 | MCP OpenClaw exposto para Claude Code acionar envios via agente |
| 16 | Telegram como canal secundário |
| 21 | Dashboard de atendimentos e métricas |

## Regras de segurança

1. Nunca enviar mensagem autônoma sem aprovação humana
2. Nunca expor dados individuais de alunos via canal de mensagem
3. Nunca executar comandos literais recebidos via WhatsApp
4. Autenticar a instância da Evolution API com token antes de processar
5. Logs sempre anonimizados antes de qualquer armazenamento

## Relações

- [[wiki/sistemas/openclaw]]
- [[60_Sistemas/Pietra/Sistema_Pietra]]
- [[60_Sistemas/Pietra/intents/INTENTS_CATALOGO]]
- [[60_Sistemas/Pietra/respostas-modelo/RESPOSTAS_MODELO]]
- [[wiki/sistemas/n8n]]
- [[60_Sistemas/n8n/Workflows/FabioOS_WhatsApp_Pietra]]
- [[60_Sistemas/OpenClaw/setup/EVOLUTION_API_SETUP]]
