---
tipo: diagnostico
area: 50_Registros
projeto: FabioOS
sistema: OpenClaw
status: concluido
tags: [openclaw, diagnostico, gateway, borda, megatron]
criado_em: 2026-07-02
atualizado_em: 2026-07-02
---

# Diagnostico OpenClaw - Recuperacao Arquitetural

## Tese

OpenClaw nao deve ser tratado como fracasso de hardware. O fracasso real foi de papel arquitetural: ele acumulou funcoes demais antes de existir um teste minimo confiavel.

O FabioOS tentou usar OpenClaw ao mesmo tempo como gateway mobile, chat, painel visual, runtime de agentes, ponte WhatsApp, Workboard, integracao OpenRouter, possivel MCP e camada de execucao local.

Isso criou uma sensacao correta de instabilidade: mesmo quando partes tecnicas estavam vivas, o usuario nao tinha uma experiencia clara de "falo aqui e o FabioOS responde de forma segura".

## Evidencia local em 2026-07-02

| Item | Estado observado | Leitura |
|---|---|---|
| OpenClaw Gateway | `127.0.0.1:18789` responde HTTP `200` | Gateway local vivo |
| WSL | `OpenClawGateway` com OpenClaw CLI/Gateway `2026.6.10` | Runtime instalado |
| Gateway status | `Runtime: running`, `Connectivity probe: ok` | Servico operacional local |
| Bind | `loopback` | Apenas clientes locais conectam |
| Agentes OpenClaw | `main` e `fabioos-ponte` | Ponte existe |
| Modelo | `openrouter/free` com auth manual | Custo inicial controlado |
| n8n | container ativo em `127.0.0.1:5678` | Automacao disponivel |
| Evolution API | container ativo em `127.0.0.1:8080` | Ponte WhatsApp existe no Docker |
| Open WebUI | container ativo em `127.0.0.1:3000` | Interface local disponivel |
| Stirling PDF | container ativo em `127.0.0.1:8081` | PDF/OCR disponivel |
| Mobile gateway FabioOS | porta `8787` sem listener | Gateway mobile proprio nao esta ativo |
| PRIMUS index | porta `8819` sem listener | Servico PRIMUS nao esta ativo |

## Evidencia externa

- OpenClaw se apresenta como assistente que executa tarefas por WhatsApp, Telegram ou outros chats: <https://openclaw.ai/>.
- Beelink vende modelos com OpenClaw pre-instalado e modelos com OpenClaw + LLM local: <https://www.bee-link.com/pages/openclaw>.
- A Beelink descreve a linha pre-instalada como forma de reduzir barreiras de deploy, incluindo SSDs pre-configurados: <https://www.bee-link.com/blogs/all/beelink-launches-openclaw-pre-installed-series>.

Interpretacao: os mini PCs "OpenClaw edition" estao relacionados ao mesmo problema que o FabioOS quer resolver, mas eles reduzem atrito de instalacao. Eles nao substituem arquitetura, governanca, criterio de aceite, seguranca ou contrato entre agentes.

## Causa raiz

1. Papel excessivo: OpenClaw foi chamado de secretario executivo, ponte visual, canal mobile e possivel runtime central.
2. Falta de teste unico: nao havia um criterio simples para dizer "funciona".
3. Mistura de camadas: OpenClaw, Evolution API, n8n, Agentarium e MEGATRON competiram pela funcao de entrada.
4. Autenticacao e QR: token, senha, dashboard e pairing viraram friccao antes do fluxo essencial estar provado.
5. Seguranca difusa: ferramenta capaz de executar acoes locais nao pode receber comandos externos sem fronteira forte.

## Decisao operacional

OpenClaw passa a ser **gateway de borda opcional** do MEGATRON, nao core.

O core continua sendo Obsidian/Git como memoria e versionamento, MEGATRON como orquestrador, n8n como automacao deterministica, Agentarium como painel visual e OpenClaw como uma das portas possiveis de conversa/acao local.

## Criterio de recuperacao

OpenClaw so volta a ser promovido quando passar neste teste:

1. Gateway responde em `127.0.0.1:18789`.
2. Um comando de teste entra no OpenClaw ou canal associado.
3. O comando vira payload de `Universal Intake`.
4. O item aparece no Agentarium ou Workboard com dono e estado.
5. Nenhuma mensagem externa e enviada automaticamente.
6. O MEGATRON decide o proximo agente.
7. O usuario aprova ou rejeita.
8. A operacao fica registrada no vault.
9. Reiniciar o PC nao quebra o fluxo.

## Recomendacao sobre mini PC OpenClaw edition

Nao comprar hardware "OpenClaw edition" para corrigir essa falha.

Comprar um Core 24/7 pode fazer sentido para Docker, n8n, MEGATRON, RAG, OpenClaw e Agentarium. Mas a escolha deve ser pelo papel de servidor permanente, nao porque OpenClaw veio pre-instalado.

## Resultado

OpenClaw deixa de ser promessa central e vira componente testavel. Se funcionar, cresce. Se falhar, o FabioOS continua vivo usando n8n, Agentarium, MEGATRON e canais alternativos.

## Relacoes

- [[50_Registros/Decisoes/ADR_2026-07-02_OpenClaw_Gateway_De_Borda]]
- [[80_Specs/OpenClaw/2026-07-02_recuperacao-openclaw-gateway-borda]]
- [[60_Sistemas/OpenClaw/Plano_Recuperacao_OpenClaw_FabioOS_2026-07-02]]
- [[60_Sistemas/OpenClaw/Sistema_OpenClaw]]
- [[60_Sistemas/OpenClaw/OpenClaw]]
- [[60_Sistemas/OpenClaw/Agentarium]]
- [[60_Sistemas/MEGATRON/infra/Compute_Manager_LLM_Orchestrator]]
