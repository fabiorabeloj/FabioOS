---
tipo: wiki
area: sistemas
projeto: FabioOS
status: pendente
camada: camada-1
tags: [openclaw, gateway, conversacional, whatsapp, telegram, camada-1]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# OpenClaw

## Função no FabioOS

[DECISÃO] O OpenClaw é a **porta externa conversacional do FabioOS** — permite interação com o sistema via WhatsApp, Telegram, Slack ou outros canais, roteando mensagens para agentes e workflows sem exigir acesso direto ao computador.

## O que essa ferramenta faz

[FATO] Plataforma de gateway conversacional que conecta canais de mensagens a agentes de IA e automações. Permite receber mensagens externas, classificá-las e acionar ferramentas ou fluxos correspondentes.

No FabioOS, o OpenClaw deve cumprir:

- Receber mensagens por WhatsApp, Telegram ou outros canais
- Classificar a mensagem: tipo, urgência, sistema destinatário
- Rotear para o agente correto (escola, trader, vault, etc.)
- Acionar workflows no n8n ou chamar o Claude Code
- Retornar resposta ao canal de origem com aprovação humana quando necessário

Fluxo planejado:

```
mensagem externa (WhatsApp/Telegram)
        ↓
     OpenClaw
        ↓
  classificação
        ↓
agente correto / n8n / Claude Code
        ↓
resposta + aprovação humana (quando necessário)
```

[FATO] Status atual: **não implantado**. Mencionado no Plano Mestre e em `60_Sistemas/OpenClaw.md` do vault. Nenhuma instância ativa configurada.

## O que essa ferramenta não deve fazer

- Enviar mensagens externas de forma totalmente autônoma sem aprovação humana
- Dar acesso irrestrito ao vault ou ao sistema de arquivos por canais externos
- Processar dados sensíveis (credenciais, dados financeiros, dados de alunos) via canal não criptografado

## Relação com outras ferramentas

| Ferramenta | Relação |
|---|---|
| [[wiki/sistemas/n8n]] | n8n executa workflows acionados pelo OpenClaw |
| [[wiki/sistemas/claude-code]] | Claude Code pode ser acionado por fluxos do OpenClaw |
| [[wiki/sistemas/obsidian]] | Destino final de capturas via OpenClaw |

## Uso atual

- [ ] Nenhum — **pendente de implantação** (Fase 11)

## Uso futuro

- [ ] Gateway de entrada para o Sistema Pietra (atendimento escolar por WhatsApp)
- [ ] Captura de ideias: mensagem → `sources/_inbox/`
- [ ] Acionamento de agentes por canal conversacional
- [ ] Notificações de saída: n8n → OpenClaw → WhatsApp do usuário

## Riscos e cuidados

- **Segurança de canal**: mensagens externas devem ser tratadas como não confiáveis — nunca executar comandos literais vindos de canal externo
- **Aprovação humana obrigatória**: toda ação sensível (envio de email, publicação, acesso a dados) deve ter etapa de confirmação antes da execução
- **Autenticação**: implementar verificação de identidade do remetente antes de acionar agentes

## Próximas ações

- [ ] Estudar documentação do OpenClaw em `60_Sistemas/OpenClaw.md`
- [ ] Definir arquitetura de integração com n8n
- [ ] Implementar na Fase 11 após n8n estar operacional

## Links internos

- [[wiki/indices/mapa-fabios]]
- [[wiki/sistemas/n8n]]
- [[wiki/sistemas/claude-code]]
- [[wiki/sistemas/obsidian]]
- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]
