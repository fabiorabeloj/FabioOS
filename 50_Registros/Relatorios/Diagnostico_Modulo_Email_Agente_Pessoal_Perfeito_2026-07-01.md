---
tipo: relatorio
area: 50_Registros
projeto: FabioOS
status: concluido
classe_dado: interno
criado_em: 2026-07-01
tags: [fabios, email, gmail, diagnostico, agente-pessoal]
---

# Diagnostico do Modulo de E-mail - Agente Pessoal Perfeito

## Diagnostico

O FabioOS ja possui decisao, memoria e conectores de leitura para Gmail, mas nao
possui ainda um modulo local de e-mail fim a fim. O agente `Inbox` existe, porem
esta limitado a arquivos em `00_Inbox/` e fontes locais. Ele nao consulta Gmail,
nao valida OAuth, nao cria triagem de e-mail e nao gera tarefas a partir da caixa.

## Evidencias

- `60_Sistemas/MEGATRON/agentes/implementacao/claude/inbox.py` varre apenas
  `00_Inbox/`.
- `60_Sistemas/MEGATRON/agentes/specs/Agente_Inbox.md` define mensagens externas
  como futuro/encaminhamento, mas nao implementa Gmail.
- `60_Sistemas/FabioOS/Conectores_Google_Catalogo_v0.md` registra Gmail pessoal
  conectado em modo leitura, com decisao de nao ingerir em massa.
- `00_Inbox/Processar/Email_para_Processar_FabioOS.md` mostra que houve lote
  piloto, mas a proxima thread real ainda depende de escolha humana.
- `apps/agentarium/backend/src/agents/fabioAgents.ts` lista `Email Inbox` como
  agente planejado, nao ativo.
- `60_Sistemas/n8n/Workflows/FabioOS_Webhook_Inbox.json` recebe entrada generica,
  mas nao tem gatilho Gmail/OAuth.

## Teste do conector

O conector Gmail disponivel no Codex respondeu ao perfil e a uma busca pequena em
Inbox recente. Isso indica que, nesta sessao, o problema nao e falta de acesso do
Codex ao Gmail pessoal. A falha esta na ausencia de uma ponte operacional local
entre Gmail e FabioOS.

Por privacidade, este relatorio nao versiona remetentes, assuntos ou snippets
reais da amostra.

## Causa provavel

Arquitetura incompleta:

```text
Gmail conectado no Codex
  -> sem export padronizado
  -> sem script local de intake
  -> sem workflow Gmail n8n aprovado
  -> agente Inbox so enxerga arquivos locais
```

## Correcao segura aplicada

Criado o modulo local:

- `60_Sistemas/FabioOS/scripts/email_intake_dry_run.py`
- `60_Sistemas/FabioOS/specs/2026-07-01_email-intake-dry-run.md`
- `60_Sistemas/FabioOS/examples/email_intake_sample.json`

Ele recebe payload JSON/JSONL autorizado, classifica e gera relatorio restrito em:

`05_Raw_Sources/_compat_sources/email/_restrito/triagens/`

## O que ele faz

- Normaliza mensagem.
- Classifica dominio: PietraOS, EscolaOS, financeiro, FabioOS, PRIMUS ou pessoal.
- Classifica urgencia.
- Classifica sensibilidade.
- Detecta anexos.
- Gera bucket e acao sugerida.
- Mascara remetente.
- Omite snippet por padrao no Markdown salvo.

## O que ele nao faz

- Nao acessa Gmail sozinho.
- Nao guarda credenciais.
- Nao envia e-mail.
- Nao arquiva, deleta ou marca como lido.
- Nao cria rascunho no Gmail.
- Nao indexa RAG/Grafo.
- Nao escreve fora do vault.

## Pendencias humanas

- Escolher escopo do primeiro lote real: por exemplo, 10 mensagens recentes da
  Inbox ou uma thread especifica.
- Confirmar se o canal sera Codex Gmail connector, n8n Gmail OAuth ou ambos.
- Autorizar explicitamente qualquer criacao de rascunho ou resposta futura.
- Se usar n8n, configurar credencial OAuth Gmail no painel local.

## Teste minimo

```powershell
python 60_Sistemas/FabioOS/scripts/email_intake_dry_run.py `
  --input 60_Sistemas/FabioOS/examples/email_intake_sample.json `
  --stdout
```

Resultado esperado:

- 2 mensagens classificadas;
- uma escolar com urgencia maior;
- uma newsletter/promocional como ruido/FYI;
- nenhum efeito externo.

## Proximos passos

1. Rodar lote real pequeno com payload exportado pelo conector Gmail.
2. Gerar uma triagem restrita local.
3. Promover apenas tarefas/resumos aprovados para Obsidian visivel.
4. Depois criar workflow n8n Gmail -> Email Intake Dry-Run -> Dashboard.
