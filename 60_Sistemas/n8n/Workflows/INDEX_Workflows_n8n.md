---
tipo: indice
area: 60_Sistemas
projeto: FabioOS
sistema: n8n
status: ativo
data: 2026-06-29
tags: [fabios, n8n, workflows, automacao]
---

# Indice de Workflows n8n

## Acesso

- Painel n8n: http://127.0.0.1:5678/
- Lista visual: abrir o painel e entrar em **Workflows**.

## Workflows existentes no n8n local

| Workflow | ID | Estado observado | Visualizar |
|---|---|---|---|
| FabioOS - Intake Orquestrador Seguro | `fabioosIntakeOrquestradorSeguro` | importado, inativo por seguranca | http://127.0.0.1:5678/workflow/fabioosIntakeOrquestradorSeguro |
| FabioOS - SPEC para Plano de Execucao | `fabioosSpecPlanoExecucao` | importado, inativo por seguranca | http://127.0.0.1:5678/workflow/fabioosSpecPlanoExecucao |
| FabioOS - SafeCommit Preflight | `fabioosSafeCommitPreflight` | importado, inativo por seguranca | http://127.0.0.1:5678/workflow/fabioosSafeCommitPreflight |
| FabioOS - Webhook para Inbox | `fabioosWebhookInbox` | importado, inativo por seguranca | http://127.0.0.1:5678/workflow/fabioosWebhookInbox |
| FabioOS - WhatsApp para Pietra | `fabioosWhatsappPietraV2` | ativo segundo log do n8n | http://127.0.0.1:5678/workflow/fabioosWhatsappPietraV2 |
| FabioOS - WhatsApp Pietra Dry Run | `fabioosWhatsappPietraDryRun` | pronto para importar; seguro por padrao | importar `FabioOS_WhatsApp_Pietra_DryRun.json` |
| FabioOS - WhatsApp para Pietra (desativado) | `fabioosWhatsappPietra` | legado/desativado | http://127.0.0.1:5678/workflow/fabioosWhatsappPietra |
| FabioOS - Webhook Arquivista | `o0B7C9gBC3UOOf1H` | ativo segundo log do n8n | http://127.0.0.1:5678/workflow/o0B7C9gBC3UOOf1H |
| FabioOS - Captura para Obsidian | `JDZA4lXZSn3uMMqj` | existente no n8n local | http://127.0.0.1:5678/workflow/JDZA4lXZSn3uMMqj |

## Decisao de ativacao

O workflow `FabioOS - Webhook para Inbox` foi importado como inativo.

Motivo:

- exige credencial/integração com Obsidian REST API;
- poderia criar notas reais no vault;
- deve ser ativado manualmente apos conferencia visual e credenciais.

## Proximos workflows recomendados

1. `Inbox HTTP seguro`: webhook com token, validacao de campos e escrita controlada em `00_Inbox/Capturas/`.
2. `Arquivista local`: pegar capturas aprovadas e criar nota em `40_Wiki/` sem chamar API externa.
3. `Preflight SafeCommit`: gatilho manual para rodar checklist antes de commit.
4. `Dashboard operacional`: gatilho manual/agenda para consolidar STATUS/NEXT_ACTIONS sem alterar runtime.

## Cadeia-mae

O workflow `FabioOS - Intake Orquestrador Seguro` e o desenho inicial da cadeia-mae.

Ele nao substitui os workflows especificos; ele decide qual trilha deve ser acionada:

```text
entrada -> validar -> classificar -> permissao -> roteador -> rascunho -> auditoria -> resposta
```

## Cadeia de seguranca

O workflow `FabioOS - SafeCommit Preflight` representa a trilha visual de seguranca antes de commits:

```text
diff/arquivos -> scan segredos -> risco -> plano stage explicito -> auditoria -> resposta
```

## Cadeia de autoconstrucao

O workflow `FabioOS - SPEC para Plano de Execucao` transforma uma demanda em plano auditavel:

```text
SPEC -> gate de excelencia -> tarefas -> donos -> gates -> testes -> aceite
```

Ele e util para decidir se uma fase esta madura para implementacao antes de qualquer codigo.

## Cadeia Pietra dry-run

O workflow `FabioOS - WhatsApp Pietra Dry Run` transforma um payload Evolution/WhatsApp em proposta
do PietraOS, sem envio externo:

```text
Evolution -> n8n webhook -> bridge local :8791 -> pietra_conversa -> proposta + cartao -> resposta dry-run
```

Antes de importar, iniciar o bridge:

```powershell
python 60_Sistemas/n8n/scripts/pietra_whatsapp_dry_run_bridge.py --serve --port 8791
```

## Limites

- Nenhum webhook real foi disparado nesta rodada.
- Nenhuma credencial foi criada.
- Nenhuma mensagem WhatsApp foi enviada.
- OpenClaw/Evolution nao foram alterados.
