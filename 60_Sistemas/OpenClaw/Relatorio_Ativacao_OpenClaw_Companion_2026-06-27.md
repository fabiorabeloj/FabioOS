---
tipo: relatorio-operacional
area: 60_Sistemas
projeto: FabioOS
sistema: OpenClaw
status: gateway-local-ativo
tags: [openclaw, companion, gateway-local, wsl, agente-local, megatron]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Relatório de Ativação do OpenClaw Companion

## Função

Registrar a ativação local do OpenClaw Companion como nó operacional do FabioOS/MEGATRON no Windows.

## Resultado

O OpenClaw Companion foi atualizado, configurado e ativado como gateway local.

Estado validado em 2026-06-27:

| Item | Estado |
|---|---|
| OpenClaw Companion/Tray | Ativo no Windows |
| Versão do Tray | `0.6.3` |
| Distro WSL | `OpenClawGateway` |
| Sistema da distro | Ubuntu 24.04 LTS |
| OpenClaw CLI no WSL | `2026.5.28` |
| Gateway local | Ativo |
| Porta | `18789` |
| Bind | `127.0.0.1` / loopback |
| Health HTTP | `200` |
| RPC | `ok` |
| Node mode | `EnableNodeMode: true` |
| MCP local | `EnableMcpServer: false` |

## O que foi feito

1. Verificada a instalação anterior do OpenClaw Tray.
2. Identificado que a versão antiga travava no setup do WSL.
3. Baixado o instalador oficial x64 da release `v2026.6.10`.
4. Validado SHA256 do instalador contra o arquivo oficial da release.
5. Validada assinatura Authenticode do instalador.
6. Atualizado o Companion para `0.6.3`.
7. Criada e validada a distro WSL `OpenClawGateway`.
8. Instalado o OpenClaw CLI dentro do WSL.
9. Configurado o gateway em modo local/loopback.
10. Pareado o operador e o nó Windows.
11. Reiniciado o Tray para carregar `EnableNodeMode: true`.
12. Validado listener local em `127.0.0.1:18789`.

## Adequação ao FabioOS

O OpenClaw Companion passa a cumprir o papel de **nó local do MEGATRON**:

- expor capacidades locais controladas do computador;
- manter gateway WSL isolado;
- permitir integrações futuras com agentes;
- funcionar como ponte local, não como memória principal.

O Companion não substitui:

- Obsidian como memória;
- Git como versionamento;
- n8n como orquestrador de workflows;
- Evolution API como ponte WhatsApp.

## Capacidades locais habilitadas

| Capacidade | Estado | Observação |
|---|---|---|
| `system.run` | Habilitada | Com sandbox ativo e outbound bloqueado. |
| Canvas | Habilitada | Para automação visual/local. |
| Screen | Habilitada | Consentimento de gravação ainda não concedido. |
| Camera | Habilitada | Consentimento de gravação ainda não concedido. |
| Location | Habilitada | Usar apenas com finalidade explícita. |
| Browser proxy | Habilitada | Ponte local futura. |
| TTS | Desabilitada | Pode ser habilitada depois. |
| STT | Desabilitada | Pode ser habilitada depois. |

## Limites atuais

- Ainda não há canal de conversa externo configurado no OpenClaw.
- Ainda não há MCP local exposto pelo Companion.
- Ainda não há modelo/autenticação de LLM configurado dentro do OpenClaw.
- A comunicação por WhatsApp continua na frente Evolution API + n8n.
- O gateway está em loopback; não recebe conexões de outros dispositivos na rede.

## Riscos

- `system.run` deve permanecer com sandbox ativo.
- Capacidades de tela/câmera exigem governança e consentimento explícito.
- Tokens gerados pelo OpenClaw ficam fora do repositório e não devem ser copiados para notas.
- Não usar o Companion como canal externo irrestrito de comandos.

## Critérios de aceite cumpridos

- [x] Companion atualizado.
- [x] Distro `OpenClawGateway` criada.
- [x] Gateway respondendo em `127.0.0.1:18789`.
- [x] HTTP health retornando `200`.
- [x] Serviço do gateway em estado `running`.
- [x] Tray reiniciado com `nodeMode: true`.
- [x] Log local indica `connection.status: Connected`.

## Próximas ações

- [ ] Testar uma ação local inofensiva via OpenClaw.
- [ ] Definir se `EnableMcpServer` deve ser ativado na Fase 14.
- [ ] Revisar se Camera/Screen devem permanecer habilitados por padrão.
- [ ] Conectar esta camada ao Dashboard dos agentes.
- [ ] Manter WhatsApp como frente separada: Evolution API -> n8n -> FabioOS.

## Relações

- [[60_Sistemas/OpenClaw/Sistema_OpenClaw]]
- [[60_Sistemas/OpenClaw/Diagnostico_OpenClaw_Local_2026-06-27]]
- [[60_Sistemas/OpenClaw/Roteiro_Ativacao_OpenClaw_Evolution_2026-06-27]]
- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]
- [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]]
