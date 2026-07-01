---
tipo: spec
area: 60_Sistemas
projeto: FabioOS
status: implementado
classe_dado: interno
criado_em: 2026-07-01
tags: [fabios, email, gmail, inbox, agente-pessoal, dry-run]
---

# SPEC - Email Intake Dry-Run

## Objetivo

Transformar e-mails autorizados em triagem operacional do FabioOS sem acao
externa, sem envio automatico e sem indexacao RAG/Grafo.

## Contexto

Na hipotese do agente pessoal perfeito, e-mail e uma porta sensorial central.
Hoje o Gmail esta acessivel pelo conector do Codex, mas o FabioOS local nao tem
um agente de e-mail operacional. O agente Inbox atual apenas lista arquivos em
`00_Inbox/`.

## Escopo v0

- Receber payload JSON/JSONL exportado por conector autorizado.
- Normalizar campos de mensagem.
- Classificar dominio, urgencia, sensibilidade e bucket.
- Gerar relatorio Markdown em pasta restrita gitignored.
- Exigir aprovacao humana para qualquer acao posterior.

## Fora de escopo

- OAuth proprio.
- IMAP/SMTP.
- Envio, arquivamento, exclusao ou marcacao como lido.
- Criacao de rascunho no Gmail.
- Leitura em massa sem escopo.
- RAG/Grafo.

## Contrato de entrada

```json
{
  "emails": [
    {
      "id": "gmail-message-id",
      "thread_id": "gmail-thread-id",
      "from_": "Nome <email@dominio>",
      "subject": "Assunto",
      "snippet": "Resumo curto",
      "labels": ["INBOX", "UNREAD"],
      "has_attachment": false,
      "attachments": [],
      "email_ts": "2026-07-01T09:00:00-03:00"
    }
  ]
}
```

## Saida

Arquivo Markdown em:

`05_Raw_Sources/_compat_sources/email/_restrito/triagens/`

Opcionalmente, com `--queue-json` ou `--write-queue`, o mesmo payload passa a
emitir a fila universal do MEGATRON Core Spec v0.1, consumivel pelo Cursor:

`60_Sistemas/MEGATRON/v1/state/intake_queue.json`

Campos por mensagem:

- fingerprint;
- remetente mascarado;
- assunto;
- dominio;
- urgencia;
- sensibilidade;
- bucket;
- acao sugerida;
- flags;
- anexos;
- nota de que o snippet foi omitido por padrao.

## Criterios de aceite

- [x] Script local criado.
- [x] Nao exige credenciais locais.
- [x] Nao envia nem altera mensagens.
- [x] Saida padrao em pasta restrita gitignored.
- [x] Teste smoke com payload sintetico.
- [ ] Conectar export real do conector Gmail/n8n em lote aprovado.
- [ ] Expor contagem/status no Dashboard/Agentarium.
- [x] Emitir fila universal compatível com o contrato do Cursor.

## Comando

```powershell
python 60_Sistemas/FabioOS/scripts/email_intake_dry_run.py `
  --input 60_Sistemas/FabioOS/examples/email_intake_sample.json `
  --stdout
```

Para gerar relatorio restrito:

```powershell
python 60_Sistemas/FabioOS/scripts/email_intake_dry_run.py `
  --input caminho/do/payload_gmail.json
```

Para emitir a fila universal:

```powershell
python 60_Sistemas/FabioOS/scripts/email_intake_dry_run.py `
  --input 60_Sistemas/FabioOS/examples/intake_gmail_fake.json `
  --queue-json
```

## Relacoes

- [[60_Sistemas/MEGATRON/agentes/specs/Agente_Inbox]]
- [[60_Sistemas/FabioOS/Conectores_Google_Catalogo_v0]]
- [[60_Sistemas/FabioOS/Decisao_Roteamento_Email_Google_Gemini_OpenClaw_2026-06-27]]
- [[00_Inbox/Processar/Email_para_Processar_FabioOS]]
