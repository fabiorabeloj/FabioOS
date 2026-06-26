---
tipo: changelog
area: registros
projeto: FabioOS
status: parcialmente-concluído
fase: 11
tags: [changelog, fase-11, openclaw, evolution-api, whatsapp, n8n, pietra]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Changelog — Fase 11: OpenClaw (Gateway Conversacional)

## Resumo

Criação da arquitetura completa do OpenClaw — gateway conversacional baseado em Evolution API que integra WhatsApp ao Pietra via n8n. O fluxo completo está documentado e os workflows estão prontos para importar. A ativação depende da execução do setup da Evolution API (instalação Docker + conexão do número WhatsApp).

**Status:** Arquitetura criada. Setup Evolution API pendente.

## Arquivos criados

### Sistema OpenClaw

| Arquivo | Descrição |
|---|---|
| `60_Sistemas/OpenClaw/Sistema_OpenClaw.md` | Doc operacional: fluxo, módulos, estados, integração futura |
| `60_Sistemas/OpenClaw/setup/EVOLUTION_API_SETUP.md` | Passo a passo de instalação via Docker + QR Code |

### Workflow n8n

| Arquivo | Descrição |
|---|---|
| `60_Sistemas/n8n/Workflows/FabioOS_WhatsApp_Pietra.md` | Documentação completa (10 seções padrão CLAUDE.md) |
| `60_Sistemas/n8n/Workflows/FabioOS_WhatsApp_Pietra.json` | Workflow importável com 7 nós |

### Comando Claude Code

| Arquivo | Descrição |
|---|---|
| `.claude/commands/simular-mensagem-pietra.md` | `/simular-mensagem-pietra` — testa Pietra sem WhatsApp ou n8n |

## Arquivos atualizados

- `wiki/sistemas/openclaw.md` — tecnologia base definida, uso atual atualizado
- `wiki/indices/mapa-fabios.md` — fase 11 em andamento, próxima: 12
- `60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS.md` — fase 11 com entregáveis

## Arquitetura do workflow FabioOS_WhatsApp_Pietra

```
POST /webhook/whatsapp-pietra (Evolution API)
        ↓
[Extrair Dados]
  · texto, número anonimizado (****9999), nome, timestamp
  · filtra fromMe e mensagens sem texto
        ↓
[Ignorar?] — se fromMe ou sem texto: responde e descarta
        ↓
[Classificar Intent]
  · 11 categorias com palavras-gatilho do Pietra
  · pontuação por correspondências
  · verifica palavras de risco (advogado, PROCON, violência)
        ↓
[Montar Log e Notificação]
  · linha de log anonimizada para vault
  · mensagem de notificação para professor
        ↓
[Salvar Log no Vault]
  · POST → Obsidian API → sources/_inbox/PIETRA_YYYY-MM_LOG.md
        ↓
[Responder]
  · JSON: {status, categoria, nivel, acao}
```

## Decisões registradas

- **Evolution API** escolhida como backbone (open-source, Docker, REST+webhooks, Baileys)
- **Número anonimizado** no log: apenas 4 últimos dígitos (`****9999`)
- **fromMe ignorado**: mensagens enviadas pelo próprio número da escola não geram classificação
- **Escalonamento por palavras de risco**: "advogado", "PROCON", "violência" → `escalonar: true` independente da categoria
- **Log em `sources/_inbox/`**: arquivo por mês `PIETRA_YYYY-MM_LOG.md` — nunca commitar
- **`/simular-mensagem-pietra`**: comando para testar o fluxo sem precisar de WhatsApp ou n8n

## Para ativar (checklist)

```
[ ] Executar: docker run -d --name evolution-api -p 8080:8080 ... (ver EVOLUTION_API_SETUP.md)
[ ] Criar instância: POST /instance/create/escola
[ ] Escanear QR Code com WhatsApp do número da escola
[ ] Configurar webhook → n8n (WEBHOOK_GLOBAL_URL ou /webhook/set/escola)
[ ] Importar FabioOS_WhatsApp_Pietra.json no n8n
[ ] Ativar o workflow
[ ] Testar com curl simulando payload Evolution API
[ ] Confirmar log em sources/_inbox/PIETRA_2026-06_LOG.md
```

## Teste sem infraestrutura

```
/simular-mensagem-pietra "Boa tarde, quando é a prova de geografia do 9A?"
```
Classifica localmente, sem n8n ou WhatsApp.

## Próxima fase

**Fase 12 — RAG:** recuperação inteligente de conhecimento. Consultar fontes e wiki via busca semântica antes de sugerir respostas.

## Relações

- [[60_Sistemas/OpenClaw/Sistema_OpenClaw]]
- [[60_Sistemas/Pietra/Sistema_Pietra]]
- [[60_Sistemas/n8n/Workflows/FabioOS_WhatsApp_Pietra]]
- [[wiki/sistemas/openclaw]]
- [[50_Registros/Changelog/2026-06-26_fase10-n8n-operacional]]
