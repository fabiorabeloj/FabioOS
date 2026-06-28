---
tipo: inventario
area: 60_Sistemas
projeto: FabioOS
status: rascunho
tags: [fabios, capacidades, cursor, hermes, agentes]
criado_em: 2026-06-28
atualizado_em: 2026-06-28
---

# Capacidades Locais - Cursor e Hermes

## Objetivo

Registrar ferramentas instaladas no PC para que FabioOS use capacidades existentes antes de improvisar.

## Cursor

Status: detectado.

Evidencia local:

- executavel encontrado em `C:\Users\user\AppData\Local\Programs\cursor\Cursor.exe`.
- pasta principal encontrada em `C:\Users\user\AppData\Local\Programs\cursor`.

Uso recomendado:

- edicao assistida de codigo;
- revisao visual de arquivos;
- trabalho manual supervisionado no repositorio FabioOS;
- alternativa de IDE quando VS Code/Codex/Claude precisarem de apoio.

Limite:

- nao usar Cursor como agente autonomo ate registrar comandos/CLI disponiveis.

## Hermes IA Agent

Status: detectado localmente; ainda nao integrado ao FabioOS.

Evidencia local:

- executavel encontrado em `C:\Users\user\AppData\Local\hermes\hermes-agent\apps\desktop\release\win-unpacked\Hermes.exe`.
- instalador encontrado em `C:\Users\user\Desktop\Hermes-Setup.exe`.
- estado local de aplicacao detectado em `C:\Users\user\AppData\Local\com.nousresearch.hermes.setup\`.

Leitura correta:

- instalado nao significa integrado;
- integrado nao significa autorizado a agir autonomamente;
- qualquer uso com acesso a arquivos, contas, agentes ou API precisa de escopo e registro.

Proxima verificacao:

- identificar CLI/API;
- entender se ele atua como agente, ponte de comunicacao, automacao local ou app visual;
- registrar no OpenClaw Workboard se houver integracao segura.

Regra:

Nao assumir que Hermes esta operacional para o FabioOS ate haver comando, endpoint, interface ou fluxo confirmado. Por enquanto ele e uma capacidade instalada em avaliacao.
