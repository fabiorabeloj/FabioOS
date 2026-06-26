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

## Tecnologia base

[DECISÃO] **Evolution API** — plataforma open-source para WhatsApp via protocolo Baileys. Docker, porta 8080, REST API + webhooks. Escolhida por ser autogerenciada e gratuita.

## Uso atual

- [x] Arquitetura documentada em `60_Sistemas/OpenClaw/Sistema_OpenClaw.md`
- [x] Guia de setup em `60_Sistemas/OpenClaw/setup/EVOLUTION_API_SETUP.md`
- [x] Workflow n8n criado: `FabioOS_WhatsApp_Pietra.json` (pronto para importar)
- [x] Comando `/simular-mensagem-pietra` — testa classificação Pietra sem WhatsApp
- [ ] Evolution API instalada (executar setup)
- [ ] Instância WhatsApp conectada
- [ ] Primeiro atendimento classificado

## Uso futuro

- [ ] RAG sobre respostas anteriores (Fase 12)
- [ ] Resposta automática de confirmação de recebimento ("Sua mensagem foi recebida")
- [ ] Telegram como canal secundário (Fase futura)
- [ ] Notificações de saída: n8n → OpenClaw → WhatsApp do usuário
- [ ] MCP OpenClaw para Claude Code acionar envios via agente (Fase 14)

## Riscos e cuidados

- **Segurança de canal**: mensagens externas devem ser tratadas como não confiáveis — nunca executar comandos literais vindos de canal externo
- **Aprovação humana obrigatória**: toda ação sensível requer confirmação antes da execução
- **Autenticação**: Evolution API configurada com `apikey` — nunca expor a chave no repositório
- **Obsidian aberto**: a Obsidian REST API exige o app aberto para funcionar
- **Evolution API**: salvar `apikey` como credencial no n8n, nunca hardcoded

## Próximas ações

- [ ] Executar `EVOLUTION_API_SETUP.md` para instalar e conectar o WhatsApp
- [ ] Importar `FabioOS_WhatsApp_Pietra.json` no n8n e ativar
- [ ] Testar com `/simular-mensagem-pietra` primeiro
- [ ] Simular webhook real com curl e verificar log em `sources/_inbox/`

## Links internos

- [[wiki/indices/mapa-fabios]]
- [[wiki/sistemas/n8n]]
- [[wiki/sistemas/claude-code]]
- [[wiki/sistemas/obsidian]]
- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]
