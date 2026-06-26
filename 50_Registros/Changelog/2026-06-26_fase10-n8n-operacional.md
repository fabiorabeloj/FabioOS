---
tipo: changelog
area: registros
projeto: FabioOS
status: parcialmente-concluído
fase: 10
tags: [changelog, fase-10, n8n, workflow, webhook, automação]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Changelog — Fase 10: n8n Operacional

## Resumo

Criação da infraestrutura documentada do n8n no FabioOS: estrutura de pastas, README operacional, workflow de produção completo (JSON importável) e documentação técnica. O workflow está pronto para importar e ativar — a execução do teste final depende de configuração manual de 2 minutos (token Obsidian + import).

**Status:** Workflow criado e documentado. Ativação pendente (importar JSON + configurar credencial).

## Arquivos criados

| Arquivo | Descrição |
|---|---|
| `60_Sistemas/n8n/README.md` | Operação do n8n: Docker, import, credencial Obsidian, padrão de docs |
| `60_Sistemas/n8n/Workflows/FabioOS_Webhook_Inbox.md` | Documentação completa do workflow (10 seções padrão CLAUDE.md) |
| `60_Sistemas/n8n/Workflows/FabioOS_Webhook_Inbox.json` | Workflow importável com 4 nós: Webhook → Code → HTTP Request → Responder |

## Arquivos atualizados

- `wiki/sistemas/n8n.md` — uso atual atualizado, próximas ações revisadas, riscos ampliados
- `wiki/indices/mapa-fabios.md` — fase 10 em andamento, próxima: 11

## Arquitetura do workflow FabioOS_Webhook_Inbox

```
POST /webhook/fabios-inbox
        ↓
[Code: Gerar Nota]
  · filename = YYYY-MM-DD_slug.md
  · frontmatter: tipo/origem/status/tags/capturado_em
        ↓
[HTTP Request: Salvar no Vault]
  · PUT https://host.docker.internal:27124/vault/sources/_inbox/{filename}
  · Auth: Bearer {OBSIDIAN_TOKEN}
  · SSL: skip (certificado auto-assinado)
        ↓
[Responder: JSON]
  · { status: "ok", arquivo: "...", mensagem: "..." }
```

## Decisões registradas

- **host.docker.internal** em vez de `localhost` — n8n roda em Docker, Obsidian no host
- **Obsidian REST API** como ponte de escrita — não requer remontar o contêiner Docker
- **`sources/_inbox/` como destino** — todas as entradas externas passam por triagem antes de integrar ao vault
- **SSL ignorado no nó HTTP** — certificado auto-assinado do Obsidian não impede a operação
- **Workflow inativo por padrão** — ativação manual é obrigatória (alinhado com protocolo de aprovação)

## Para ativar (checklist de 2 minutos)

```
[ ] Abrir http://localhost:5678
[ ] Workflows → Import → selecionar FabioOS_Webhook_Inbox.json
[ ] Credentials → Add → HTTP Header Auth
    Name: Obsidian API Token
    Header Name: Authorization
    Header Value: Bearer [token do plugin Local REST API]
[ ] No workflow importado: nó "Salvar no Vault" → selecionar a credencial
[ ] Ativar o workflow (toggle)
[ ] Testar:
    curl -X POST http://localhost:5678/webhook/fabios-inbox \
      -H "Content-Type: application/json" \
      -d '{"titulo":"Teste Fase 10","conteudo":"Webhook funcionando.","tipo":"texto","origem":"webhook"}'
[ ] Confirmar nota criada em sources/_inbox/
```

## Próxima fase

**Fase 11 — OpenClaw:** gateway conversacional via WhatsApp. Integração com Pietra para classificação automática de mensagens.

## Relações

- [[60_Sistemas/n8n/README]]
- [[60_Sistemas/n8n/Workflows/FabioOS_Webhook_Inbox]]
- [[wiki/sistemas/n8n]]
- [[wiki/sistemas/obsidian]]
- [[sources/README]]
- [[50_Registros/Changelog/2026-06-26_fase9-sistema-pietra]]
