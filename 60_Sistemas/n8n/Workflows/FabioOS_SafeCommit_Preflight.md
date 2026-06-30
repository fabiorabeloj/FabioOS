---
tipo: sistema
area: 60_Sistemas
projeto: FabioOS
sistema: n8n
workflow: FabioOS_SafeCommit_Preflight
status: importado-inativo
data: 2026-06-29
tags: [fabios, n8n, safecommit, seguranca, git]
---

# Workflow: FabioOS - SafeCommit Preflight

## Objetivo

Fornecer uma cadeia visual de preflight para commits seguros.

Este workflow recebe uma lista de arquivos e/ou diff, escaneia sinais de segredo, classifica risco e devolve um plano de commit seguro.

## O que ele nao faz

- Nao executa `git add`.
- Nao executa commit.
- Nao executa push.
- Nao le arquivos do host.
- Nao grava no vault.
- Nao chama API externa.

## Endpoint

```text
POST http://127.0.0.1:5678/webhook/fabios-safecommit-preflight
```

## Entrada esperada

```json
{
  "titulo": "registrar operacao n8n",
  "files": [
    "60_Sistemas/n8n/Workflows/INDEX_Workflows_n8n.md"
  ],
  "diff": "conteudo opcional do diff"
}
```

## Cadeia

1. Webhook - Preflight
2. Normalizar Diff e Arquivos
3. Scan de Segredos
4. Classificar Risco
5. Plano de Commit Seguro
6. Auditoria
7. Responder Preflight

## Resposta

Retorna:

- `status`: `safe_to_review`, `needs_human_review` ou `blocked`;
- `findings`: achados sem exibir valores;
- `plan`: comandos de stage por caminho explicito;
- `audit`: resumo sem efeitos externos.

## Decisao

Este workflow fica inativo por padrao.

Pode ser ativado para testes porque nao possui efeito externo, mas a saida continua consultiva.

## Relacoes

- [[60_Sistemas/MEGATRON/agentes/specs/Agente_SafeCommit]]
- [[60_Sistemas/Governanca/Matriz_de_Permissoes_FabioOS]]
- [[60_Sistemas/n8n/Workflows/INDEX_Workflows_n8n]]
