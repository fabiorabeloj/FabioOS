---
tipo: relatorio-operacional
area: 60_Sistemas
projeto: FabioOS
sistema: n8n
status: ativo
data: 2026-06-29
responsavel: Codex
tags: [fabios, n8n, docker, automacao, operacao]
---

# Relatorio de Operacao n8n - 2026-06-29

## Objetivo

Assumir uma frente segura enquanto Cursor trabalha no OpenClaw, sem tocar em OpenClaw/Evolution, RAG, MEGATRON, MCP ou credenciais reais.

## Estado encontrado

- Docker instalado e funcional.
- Imagem local existente: `docker.n8n.io/n8nio/n8n:latest`.
- Container existente: `n8n`.
- Estado inicial do container: parado ha cerca de 2 dias.
- Porta `5678`: sem listener antes da operacao.
- CLI `n8n`: nao instalada diretamente no Windows.
- Node/npm/npx: instalados no Windows.

## Acao executada

Comando executado:

```powershell
docker start n8n
```

## Resultado

- Container `n8n` iniciado com sucesso.
- Editor confirmado em: `http://127.0.0.1:5678/`
- Endpoints testados com HTTP `200`:
  - `http://127.0.0.1:5678/`
  - `http://127.0.0.1:5678/setup`
  - `http://127.0.0.1:5678/signin`
  - `http://127.0.0.1:5678/rest/settings`
- Listener interno confirmado:
  - `:::5678`
  - `127.0.0.1:5679` para task broker

## Workflows locais validados

Arquivos em `60_Sistemas/n8n/Workflows/`:

| Arquivo | JSON valido | Nos | Grupos de conexao |
|---|---:|---:|---:|
| `FabioOS_Intake_Orquestrador_Seguro.json` | sim | 9 | 8 |
| `FabioOS_Webhook_Inbox.json` | sim | 4 | 3 |
| `FabioOS_WhatsApp_Pietra.json` | sim | 8 | 6 |

## Importacao executada

O workflow `FabioOS - Webhook para Inbox` foi importado no n8n com o ID estavel:

```text
fabioosWebhookInbox
```

Ele foi importado como **inativo** por seguranca.

Tambem foi criado e importado como **inativo** o workflow-mae:

```text
FabioOS - Intake Orquestrador Seguro
ID: fabioosIntakeOrquestradorSeguro
```

Este workflow representa a cadeia profissional de entrada do FabioOS:

```text
entrada -> normalizacao -> validacao -> classificacao -> permissao -> roteamento -> rascunho -> auditoria -> resposta
```

Motivo:

- depende de credencial da Obsidian REST API;
- pode criar notas reais no vault;
- deve ser ativado manualmente apos conferencia visual.

## Workflows visiveis no painel

Ver `60_Sistemas/n8n/Workflows/INDEX_Workflows_n8n.md`.

## Workflows ativos segundo log do n8n

O log do container registrou:

- `FabioOS - WhatsApp para Pietra`
- `FabioOS — Webhook Arquivista`

## Alertas encontrados

1. O container atual monta apenas o volume `n8n_data` em `/home/node/.n8n`.
2. O vault `C:\Users\user\Desktop\FabioOs\FabioOs` nao esta montado em `/vault` no container atual.
3. Isso nao impede workflows que usam Obsidian REST API, mas impede fluxos que esperem escrever diretamente no filesystem montado.
4. O log contem requisicoes antigas/recorrentes para webhooks nao registrados:
   - `POST whatsapp-pietra-v2/connection-update`
   - `POST whatsapp-pietra`
5. Nao foi testado POST real nos webhooks para evitar criar notas, disparar automacoes ou colidir com OpenClaw/Evolution.

## Decisao operacional

O n8n foi colocado online em modo local, mas nao foi alterado por dentro.

Nao foram criadas credenciais.
Foi importado somente o workflow `FabioOS - Webhook para Inbox`, como inativo.
Nao foram disparados webhooks com efeito.
Nao foi ligado Evolution/OpenClaw.
Nao houve chamada externa.

## Proximo passo recomendado

1. Abrir `http://127.0.0.1:5678/`.
2. Confirmar se o login/setup aparece corretamente.
3. Conferir no painel se os workflows ativos correspondem aos arquivos versionados.
4. Se o Fabio autorizar, criar uma frente separada para:
   - exportar workflows ativos do n8n para comparar com Git;
   - corrigir endpoint `whatsapp-pietra-v2/connection-update`;
   - recriar o container com mount seguro do vault em `/vault`, se ainda for necessario.

## Limites respeitados

- Sem tocar OpenClaw/Evolution.
- Sem tocar RAG.
- Sem tocar MEGATRON.
- Sem tocar MCP.
- Sem expor tokens.
- Sem push.
