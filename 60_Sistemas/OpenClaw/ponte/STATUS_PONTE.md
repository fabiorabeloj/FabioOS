---
tipo: status
area: 60_Sistemas
sistema: OpenClaw
agente: fabioos-ponte
status: workboard-operacional-chat-pendente-auth
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
- plugin `workboard` habilitado e carregado;
- board `fabioos` criado no Workboard.

O gateway foi revertido para `loopback` apos o usuario adiar o pareamento por QR Code. A exposicao LAN nao fica ativa por padrao.

## Papel

OpenClaw deve funcionar como sala de controle visual.

Claude permanece como lider operacional.
Codex permanece como apoio de engenharia, revisao e documentacao.

## Workboard operacional

O OpenClaw agora tem uma visualizacao sem custo, independente de LLM:

- board: `fabioos`;
- comando: `openclaw workboard`;
- plugin: `workboard` carregado no gateway;
- cards iniciais:
  - `Claude lider: MCP_FABIOOS em andamento`;
  - `Codex apoio: OpenClaw ponte visual`;
  - `OpenRouter auth pendente no OpenClaw`;
  - `MEGATRON v0 detectado nao versionado`;
  - `Sincronizacao Git sem push`.

Esses cards tornam visivel quem esta trabalhando em que, mesmo antes do chat
LLM do OpenClaw estar autenticado.

## Agente registrado

Agente OpenClaw registrado:

- id: `fabioos-ponte`
- workspace: `60_Sistemas/OpenClaw/ponte/`
- identidade: `FabioOS Ponte`
- modelo configurado: `openrouter/free`
- funcao: observar e resumir a comunicacao Claude/Codex/Fabio

O modelo global do OpenClaw tambem foi reduzido para `openrouter/free`, evitando
falha por `openai/gpt-5.5` sem credencial e limitando o custo inicial da sala
visual.

## Pendencia tecnica

O Workboard esta operacional. O chat do agente ainda nao esta operacional.

Achados:

- `openclaw agents list` mostra `fabioos-ponte`;
- `openclaw models status` agora aponta `openrouter/free`;
- `openclaw models --agent fabioos-ponte status` aponta `openrouter/free`;
- os dois auth stores ainda aguardam `openrouter:manual`;
- o WSL `OpenClawGateway` nao enxerga `wsl.exe` nem o Claude CLI do Windows,
  entao a rota `claude-cli` foi descartada para esta fase;
- um evento de sistema foi enviado para a sessao `agent:fabioos-ponte:status-visual`
  apenas como marcador visual, sem acionar geracao;
- `workboard.cards.list` confirma os cinco cards iniciais.

Conclusao: OpenClaw ja serve como painel/gateway visual via Workboard e esta
preparado para OpenRouter. O chat ainda depende da chave ser cadastrada no auth
store local.

## Politica de custo

Agente manual por padrao.

Modelo inicial: `openrouter/free`.

Nao usar heartbeat automatico ate medir custo real. A chave OpenRouter deve ter
limite de gasto no painel da OpenRouter antes de liberar modelos pagos.

## Proximo passo

Claude deve decidir a rota de runtime:

1. cadastrar `OPENROUTER_API_KEY` no auth store local do OpenClaw, sem salvar em repo;
2. validar `main` e `fabioos-ponte` com uma pergunta curta;
3. manter o OpenClaw como sala visual e usar arquivos de handoff como ponte principal;
4. so depois avaliar modelos pagos ou roteamento automatico.

Enquanto isso, a comunicacao segura entre Claude e Codex continua por arquivos versionaveis no vault.
