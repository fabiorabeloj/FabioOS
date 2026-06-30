---
tipo: wiki
area: sistemas
projeto: FabioOS
status: ativo
camada: camada-1
tags: [n8n, automação, workflow, docker, camada-1]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# n8n

## Função no FabioOS

[DECISÃO] O n8n é a **camada de automação previsível do FabioOS** — executa fluxos estruturados que conectam sistemas externos ao vault, dispara ações a partir de eventos e orquestra tarefas repetíveis sem intervenção manual.

## O que essa ferramenta faz

[FATO] Plataforma de automação de workflows open-source com interface visual (node-based). Suporta centenas de integrações via nós nativos e permite lógica customizada com JavaScript.

No FabioOS, o n8n cumpre:

- Receber webhooks e eventos externos
- Capturar links, emails, mensagens e arquivos
- Acionar APIs externas (Google, GitHub, Telegram, etc.)
- Salvar informações no vault via filesystem ou REST API
- Enviar notificações e rascunhos para aprovação humana
- Orquestrar fluxos com etapas de revisão humana

[FATO] Rodando via Docker: contêiner `docker.n8n.io/n8nio/n8n`, porta `5678:5678`, volume `n8n_data` (dados persistidos). Status atual: ativo (iniciado em 2026-06-26 após 2 horas parado).

[FATO] Dois MCPs configurados no FabioOS:
- `n8n-docs` (stdio): documentação dos nós — Connected ✅
- `n8n-mcp` (HTTP `localhost:5678`): execução de workflows — dependente do Docker estar ativo

## O que essa ferramenta não deve fazer

- Tomar decisões que afetam dados externos sem aprovação humana
- Enviar emails, mensagens ou publicar conteúdo em modo totalmente automático
- Substituir o Claude Code na edição e organização do vault
- Operar com credenciais de produção sem revisão de segurança do workflow

## Relação com outras ferramentas

| Ferramenta | Relação |
|---|---|
| [[wiki/sistemas/obsidian]] | Destino final de muitos workflows (salvar notas) |
| [[wiki/sistemas/claude-code]] | Claude Code documenta e constrói automações |
| [[wiki/sistemas/openclaw]] | OpenClaw pode acionar workflows n8n via webhook |
| [[wiki/sistemas/n8n-mcp]] | MCP para documentação dos nós disponíveis |
| [[wiki/conceitos/mcp]] | n8n-mcp expõe execução de workflows a agentes |

## Uso atual

- [x] Docker ativo: contêiner `n8n`, porta 5678, volume `n8n_data`
- [x] MCP `n8n-docs` conectado (documentação de nós)
- [x] MCP `n8n-mcp` configurado (execução via HTTP)
- [x] Workflow `FabioOS - Webhook para Inbox` criado e pronto para importar
- [x] Documentação de operação em `60_Sistemas/n8n/README.md`

**Para ativar o primeiro workflow:**
1. Abrir http://localhost:5678
2. Importar `60_Sistemas/n8n/Workflows/FabioOS_Webhook_Inbox.json`
3. Criar credencial `Obsidian API Token` (Settings → Local REST API)
4. Ativar o workflow

## Uso futuro

- [ ] Testar webhook → nota em `sources/_inbox/` (critério Fase 10)
- [ ] Email recebido → rascunho de resposta → aprovação humana
- [ ] Webhook do OpenClaw → acionar agente correto (Fase 11)
- [ ] Workflow Pietra: mensagem → classificação → log automático
- [ ] Integração com Google Drive, Gmail e Calendar (Fase 20)

## Riscos e cuidados

- **Docker parado**: se o Docker não estiver ativo, o MCP `n8n-mcp` falha — verificar `docker ps` antes de sessões de automação
- **Obsidian fechado**: a REST API (porta 27124) só funciona com o app aberto
- **Workflows sem aprovação**: nenhum workflow deve publicar, enviar ou apagar sem etapa de confirmação humana
- **Credenciais no n8n**: armazenadas no volume Docker (`n8n_data`) — fazer backup antes de recriar o contêiner
- **Porta 5678 exposta**: se o computador estiver em rede, a porta está acessível por outros dispositivos — avaliar firewall
- **host.docker.internal**: obrigatório quando n8n (Docker) chama serviços do host (Obsidian API) — `localhost` não funciona de dentro do contêiner

## Próximas ações

- [ ] Importar e ativar `FabioOS_Webhook_Inbox.json` no n8n UI
- [ ] Configurar credencial Obsidian API Token no n8n
- [ ] Executar teste mínimo: `curl -X POST http://localhost:5678/webhook/fabios-inbox ...`
- [ ] Confirmar nota criada em `sources/_inbox/`

## Links internos

- [[wiki/indices/mapa-fabios]]
- [[wiki/sistemas/obsidian]]
- [[wiki/sistemas/claude-code]]
- [[wiki/sistemas/n8n-mcp]]
- [[wiki/sistemas/openclaw]]
- [[wiki/conceitos/mcp]]
- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]
