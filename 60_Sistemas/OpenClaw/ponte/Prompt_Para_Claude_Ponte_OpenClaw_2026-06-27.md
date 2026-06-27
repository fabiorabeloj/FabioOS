---
tipo: prompt
area: 60_Sistemas
sistema: OpenClaw
status: pronto
criado_em: 2026-06-27
atualizado_em: 2026-06-27
tags: [openclaw, claude, codex, ponte, coordenacao]
---

# Prompt para Claude - Ponte Visual OpenClaw

Claude, voce permanece como lider operacional do FabioOS/MEGATRON.

O Codex configurou uma frente de apoio chamada `OPENCLAW_PONTE_VISUAL`, sem tocar na sua frente `MCP_FABIOOS`.

## O que foi feito

- Gateway OpenClaw estabilizado localmente.
- `loginctl enable-linger openclaw` aplicado dentro da distro `OpenClawGateway`.
- Gateway validado em `127.0.0.1:18789` com `Read probe: ok`.
- Gateway voltou para `loopback` porque o usuario adiou o QR Code/mobile.
- Agente OpenClaw `fabioos-ponte` registrado.
- Workspace do agente criado em `60_Sistemas/OpenClaw/ponte/`.
- Dashboard abriu e o usuario conseguiu acessar a tela.
- Identidade do agente ajustada para `FabioOS Ponte`.
- Modelo global do OpenClaw ajustado para `openrouter/free`.
- Modelo do agente `fabioos-ponte` ajustado para `openrouter/free`.
- Evento visual enviado para `agent:fabioos-ponte:status-visual`.
- Plugin `workboard` habilitado e gateway reiniciado com sucesso.
- Board `fabioos` criado com cinco cards de coordenacao.

## Hierarquia corrigida

- Claude = lider operacional.
- Codex = apoio de engenharia, documentacao, revisao e execucao pontual.
- OpenClaw = ponte visual/observadora.
- Fabio = decisor humano.

## Limite atual

O Workboard do OpenClaw esta operacional sem custo. O chat do agente ainda
depende de autenticacao OpenRouter para executar respostas.

Problemas observados:

- `openclaw models status` agora indica `openrouter/free`, mas sem auth;
- `openclaw models --agent fabioos-ponte status` tambem indica `openrouter/free`, mas sem auth;
- dentro do WSL `OpenClawGateway`, nao ha `wsl.exe` nem acesso ao Claude CLI do Windows;
- por isso a rota `claude-cli` foi descartada nesta etapa;
- uma janela local de autenticacao OpenRouter foi aberta para Fabio colar a chave com mascara;
- nenhuma API key foi salva no repo ou impressa no chat.
- `workboard.cards.list` confirma os cinco cards iniciais no board `fabioos`.

## Pedido para voce

Quando assumir essa frente, decida a rota mais segura:

1. confirmar se `openrouter:manual` existe em `main` e `fabioos-ponte`;
2. testar uma mensagem curta no Dashboard;
3. manter OpenClaw como painel visual e usar arquivos de handoff no vault como ponte principal;
4. antes de qualquer modelo pago, definir limite de custo no painel da OpenRouter.

Nao habilite envio automatico de WhatsApp.
Nao reindexe RAG.
Nao altere `fabioos_db/`.
Nao faca push sem autorizacao.
Nao toque no QR/mobile ate Fabio pedir novamente.

## Estado esperado

O usuario quer visualizar agentes trabalhando. A melhor entrega e um painel onde ele veja:

- Claude lider;
- Codex apoio;
- OpenClaw ponte;
- frentes ativas;
- proximo prompt recomendado;
- riscos de colisao.

## Arquivos relevantes

- `60_Sistemas/OpenClaw/ponte/README.md`
- `60_Sistemas/OpenClaw/ponte/AGENTS.md`
- `60_Sistemas/OpenClaw/ponte/HEARTBEAT.md`
- `60_Sistemas/OpenClaw/ponte/STATUS_PONTE.md`
- `60_Sistemas/FabioOS/Registro_Frentes_Ativas.md`
