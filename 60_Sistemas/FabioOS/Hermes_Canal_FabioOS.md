---
tipo: guia
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [hermes, whatsapp, cursor, canal, inbox]
criado_em: 2026-06-30
---

# Canal WPP Pessoal · MEGATRON (inbox + Cursor)

> **Vocabulário:** leia [[60_Sistemas/FabioOS/Vocabulario_MEGATRON_Hermes]] — **MEGATRON** fala com você; **Hermes IA** é outro produto (`.exe`).

## O que você quer vs o que existe

| Nome | O que é | Integrado? |
|---|---|---|
| **MEGATRON** | Assistente que **responde** no WhatsApp e no Agentarium | Sim |
| **Canal WPP pessoal** | Evolution `fabioos-pessoal` + n8n + Agentarium | Sim |
| **Hermes IA** (app `.exe`) | Agente autônomo no PC | Não integrado |
| **`hermes` no mapa** | ID legado do agente visual | Só painel; voz = MEGATRON |

## Como funciona (hoje)

```
Você (WhatsApp pessoal)
    ↓
Evolution API (fabioos-pessoal)
    ↓
n8n (modo pessoal)
    ↓
Agentarium /integrations/whatsapp/message
    ↓
00_Inbox/Processar/Hermes_Canal_Fabio.md   ← Cursor lê daqui
    ↓
Cursor / Codex / Claude executam
```

**MEGATRON responde no WhatsApp** (linguagem natural + comandos). Mensagens não-comando também vão para a inbox do Cursor.

## Como falar pelo WhatsApp

1. WhatsApp pessoal conectado (`fabioos-pessoal` = `open`).
2. Envie mensagem para **você mesmo** (ou conversa pessoal monitorada).
3. Formato recomendado (prefixo opcional mas ajuda):

```text
FabioOS, preciso revisar o Agentarium amanhã
```

Ou sem prefixo — no modo pessoal mensagens **suas** (`fromMe`) são aceitas.

4. Abra o **Cursor** e diga:

```text
Leia 00_Inbox/Processar/Hermes_Canal_Fabio.md e continue a partir da última mensagem Hermes.
```

## O que Hermes faz com a mensagem

- Classifica (família, escola, trabalho, código, etc.)
- **Escola** → encaminha conceito para Pietra (nunca responde como pessoal)
- **Código/GitHub** → marca Codex
- **Geral** → fica na inbox para Cursor
- Cria rascunho — **não envia** nada de volta no WhatsApp

## Hermes IA (app instalado)

Caminho: `%LOCALAPPDATA%\hermes\hermes-agent\...\Hermes.exe`

Esse app é **outra camada** (agente autônomo). Ainda não está ligado ao FabioOS. O canal WhatsApp + inbox + Cursor é o caminho **imediato** para “ter com quem falar”.

Integrar Hermes IA depois exige: CLI/API, escopo, logs e aprovação (Fase 17).

## Teste sem WhatsApp

```powershell
.\test_whatsapp_personal_message.ps1
```

Depois abra `00_Inbox/Processar/Hermes_Canal_Fabio.md` — deve ter entrada nova.

## Segurança

- `WHATSAPP_AUTO_SEND=false` — nunca envia resposta automática
- Grupos desligados por padrão
- Telefone mascarado nos logs

## Relações

- [[60_Sistemas/Agentes/Hermes_Agent]]
- [[60_Sistemas/OpenClaw/Relatorio_Ativacao_WhatsApp_Pessoal_2026-06-27]]
- [[60_Sistemas/OpenClaw/Agentarium]]
