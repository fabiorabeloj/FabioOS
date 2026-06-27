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

## Hierarquia corrigida

- Claude = lider operacional.
- Codex = apoio de engenharia, documentacao, revisao e execucao pontual.
- OpenClaw = ponte visual/observadora.
- Fabio = decisor humano.

## Limite atual

O OpenClaw ainda nao esta pronto para executar o agente de verdade.

Problemas observados:

- `openclaw models status` indica auth OpenAI ausente para o agente `main`;
- `fabioos-ponte` configurado com `claude-cli/claude-sonnet-4-6`;
- tentativa de rodar o agente falhou com `write EPIPE`;
- dentro do WSL `OpenClawGateway`, `claude` nao esta no `PATH`;
- nenhuma API key foi salva ou exposta.

## Pedido para voce

Quando assumir essa frente, decida a rota mais segura:

1. configurar Claude CLI no WSL do OpenClaw sem expor credenciais;
2. configurar OpenRouter/OpenAI como runtime do OpenClaw com limite de custo;
3. manter OpenClaw como painel visual e usar arquivos de handoff no vault como ponte principal.

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
