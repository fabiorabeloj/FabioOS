---
tipo: status
area: 60_Sistemas
sistema: OpenClaw
agente: fabioos-ponte
status: ponte-registrada-runtime-pendente
criado_em: 2026-06-27
atualizado_em: 2026-06-27
tags: [openclaw, ponte, status, agentes]
---

# STATUS - Ponte Visual OpenClaw

## Estado

Gateway OpenClaw estabilizado com:

- `OpenClawGateway` em WSL;
- `Linger=yes` para o usuario `openclaw`;
- keepalive temporario da distro `OpenClawGateway`;
- gateway ouvindo em `127.0.0.1:18789`;
- probe admin OK.

O gateway foi revertido para `loopback` apos o usuario adiar o pareamento por QR Code. A exposicao LAN nao fica ativa por padrao.

## Papel

OpenClaw deve funcionar como sala de controle visual.

Claude permanece como lider operacional.
Codex permanece como apoio de engenharia, revisao e documentacao.

## Agente registrado

Agente OpenClaw registrado:

- id: `fabioos-ponte`
- workspace: `60_Sistemas/OpenClaw/ponte/`
- modelo configurado: `claude-cli/claude-sonnet-4-6`
- funcao: observar e resumir a comunicacao Claude/Codex/Fabio

## Pendencia tecnica

O agente aparece no painel, mas a execucao ainda nao esta operacional.

Achados:

- `openclaw agents list` mostra `fabioos-ponte`;
- `openclaw models status` aponta auth OpenAI ausente para o agente `main`;
- chamada do `fabioos-ponte` via `claude-cli/claude-sonnet-4-6` falhou com `write EPIPE`;
- no WSL `OpenClawGateway`, o comando `claude` nao esta disponivel no `PATH`;
- nao foi configurada API key no OpenClaw.

Conclusao: OpenClaw ja serve como painel/gateway visual, mas ainda nao como executor autonomo de agente FabioOS.

## Politica de custo

Agente manual por padrao. Nao usar heartbeat automatico ate medir custo real.

## Proximo passo

Claude deve decidir a rota de runtime:

1. usar Claude CLI dentro do OpenClaw WSL, se for possivel autenticar sem expor segredo;
2. usar OpenRouter/OpenAI com chave local segura, se o custo for aprovado;
3. manter o OpenClaw apenas como painel visual e usar arquivos de handoff como ponte principal.

Enquanto isso, a comunicacao segura entre Claude e Codex continua por arquivos versionaveis no vault.
