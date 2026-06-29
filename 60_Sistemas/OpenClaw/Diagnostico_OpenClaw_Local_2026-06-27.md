---
tipo: diagnostico
area: 60_Sistemas
projeto: FabioOS
sistema: OpenClaw
status: diagnostico-local
tags: [openclaw, hermes, evolution-api, n8n, wsl, diagnostico]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Diagnóstico Local do OpenClaw

## Função

Registrar o estado real do OpenClaw e do Hermes Agent no computador local, para orientar a próxima decisão operacional do FabioOS sem misturar instalação, documentação e execução.

## Contexto

O FabioOS já documenta o [[60_Sistemas/OpenClaw/Sistema_OpenClaw]] como gateway conversacional baseado em Evolution API, WhatsApp e [[n8n]]. O usuário informou que acredita já ter o OpenClaw instalado no PC e demonstrou interesse em usar OpenClaw ou Hermes Agent como camada de agentes.

## Achados

| Item | Estado observado | Implicação |
|---|---|---|
| OpenClaw Tray | Instalado em `C:\Users\user\AppData\Local\OpenClawTray` | O aplicativo local existe. |
| Processo OpenClaw | `OpenClaw.Tray.WinUI.exe` em execução | Há app de bandeja ativo. |
| Versão | `0.6.0` | Instalação local identificável. |
| Gateway OpenClaw | Porta `18789` sem listener | O gateway operacional não está ativo. |
| WSL OpenClawGateway | Não existe em `wsl -l -v` | Setup do gateway não concluiu. |
| Log de setup | Falha em `preflight-wsl` | OpenClaw pediu atualização do WSL antes de continuar. |
| Node mode | `EnableNodeMode: false` em settings | O app não está operando como nó/agente ativo. |
| MCP OpenClaw | `EnableMcpServer: false` em settings | Não há MCP local exposto pelo OpenClaw. |
| Evolution API | Sem container, imagem ou volume Docker | Gateway WhatsApp ainda não está instalado. |
| n8n | Container `n8n` rodando na porta `5678` | Camada de automação está disponível. |
| Porta 8080 | Livre | Pode ser usada pela Evolution API. |
| Hermes Agent | Sem comando local encontrado | No FabioOS segue como camada opcional documentada, não implantada. |

## Interpretação

OpenClaw está instalado como aplicativo Windows, mas não está pronto para uso operacional no FabioOS. O componente que permitiria operação mais robusta, o gateway WSL `OpenClawGateway`, não foi criado porque o setup falhou na validação do WSL.

Para o objetivo imediato do FabioOS, especialmente atendimento Pietra por WhatsApp, o caminho mais concreto continua sendo:

```text
WhatsApp -> Evolution API -> n8n -> Pietra -> aprovação humana
```

OpenClaw Tray pode ser investigado como camada local de agentes, voz, tela, browser e automação assistida, mas ainda não substitui a Evolution API como gateway de WhatsApp.

Hermes Agent deve permanecer como camada opcional futura. Pela documentação atual do FabioOS, ele só deve entrar se houver uma função específica que [[Codex]], Claude Code, [[n8n]] e OpenClaw não resolvam melhor.

## Decisão recomendada

Priorizar OpenClaw/Evolution em duas trilhas separadas:

1. **Trilha operacional imediata:** instalar Evolution API em Docker e conectar ao workflow `FabioOS_WhatsApp_Pietra`.
2. **Trilha exploratória OpenClaw local:** corrigir WSL, completar setup do `OpenClawGateway` e avaliar se o MCP/local gateway agrega algo ao MEGATRON.

Não ativar Hermes Agent agora. Antes disso, definir caso de uso específico, limites, permissões e critério de reversão.

## Como usar

Esta nota serve como referência antes de qualquer ação de instalação:

- se o objetivo for WhatsApp/Pietra, seguir `60_Sistemas/OpenClaw/setup/EVOLUTION_API_SETUP.md`;
- se o objetivo for agente local OpenClaw, primeiro atualizar WSL e refazer setup do OpenClaw Tray;
- se o objetivo for autonomia contínua, abrir uma especificação separada para Hermes Agent antes de instalar qualquer coisa.

## Riscos

- Expor WhatsApp sem aprovação humana.
- Registrar dados pessoais em logs de atendimento.
- Habilitar capacidades locais do OpenClaw sem escopo claro.
- Transformar Hermes Agent em sistema paralelo ao FabioOS.
- Commitar chaves de API usadas em Evolution API, n8n ou OpenClaw.

## Próximas ações

- [x] Atualizar/validar WSL antes de completar o setup do OpenClaw Gateway.
- [x] Reexecutar setup do OpenClaw e verificar que a porta `18789` fica ativa.
- [x] Registrar OpenClaw como no local do MEGATRON; MCP permanece como decisao futura.
- [ ] Instalar Evolution API somente com chave local segura, sem salvar token no repositório.
- [ ] Validar o workflow `FabioOS_WhatsApp_Pietra` em modo teste, sem envio autônomo.
- [ ] Manter Hermes Agent como pendente até existir caso de uso concreto.

## Relações

- [[60_Sistemas/OpenClaw/Sistema_OpenClaw]]
- [[60_Sistemas/OpenClaw/setup/EVOLUTION_API_SETUP]]
- [[60_Sistemas/Hermes_Agent]]
- [[40_Wiki/_compat_wiki/sistemas/hermes-agent]]
- [[60_Sistemas/n8n/Workflows/FabioOS_WhatsApp_Pietra]]
- [[60_Sistemas/Pietra/Sistema_Pietra]]

## Atualização após ativação

Em 2026-06-27, o estado local foi atualizado:

| Item | Estado após ativação |
|---|---|
| OpenClaw Tray | Atualizado para `0.6.3` |
| Gateway WSL | `OpenClawGateway` criado e em execução |
| Porta local | `18789` ouvindo em loopback |
| Health HTTP | `200` |
| OpenClaw CLI | `2026.5.28` |
| Node mode | `EnableNodeMode: true` |
| Conexão do Tray | `Connected` em log local |

Relatório operacional: [[60_Sistemas/OpenClaw/Relatorio_Ativacao_OpenClaw_Companion_2026-06-27]]
