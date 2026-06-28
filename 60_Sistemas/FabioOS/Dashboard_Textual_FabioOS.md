---
tipo: sistema
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, dashboard, python, automacao, megatron]
criado_em: 2026-06-28
atualizado_em: 2026-06-28
---

# Dashboard Textual FabioOS

## Funcao

Automacao Python local que gera um painel operacional do FabioOS sem chamar APIs externas.

Script:

`60_Sistemas/FabioOS/scripts/dashboard_fabioos.py`

Saida padrao:

`10_Mapas/Dashboard_Operacional_FabioOS.md`

## O que verifica

- estado Git local;
- ultimo changelog;
- frentes ativas;
- pendencias do Painel e do NEXT_ACTIONS;
- presenca e contagem do RAG local;
- auditoria do Grafo;
- registro do MCP FabioOS no config local do Codex;
- workflows n8n versionados;
- inconsistencias conhecidas entre documentos recentes e antigos.

## Limites

- nao chama OpenRouter;
- nao usa token;
- nao le `auth.json`;
- nao reindexa RAG;
- nao executa workflow n8n;
- nao faz push;
- nao envia mensagens.

## Como usar

```powershell
60_Sistemas\RAG\.venv\Scripts\python.exe 60_Sistemas\FabioOS\scripts\dashboard_fabioos.py
```

## Relacao com MEGATRON

Este dashboard e uma primeira automacao local para preparar a futura interface MEGATRON. Ele transforma estado disperso em uma visao unica, legivel e versionavel.
