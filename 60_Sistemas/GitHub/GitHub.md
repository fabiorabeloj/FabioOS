---
tipo: sistema
area: tecnologia
status: ativo
tags: [tecnico, versionamento, Git]
criado_em: 2026-06-25
atualizado_em: 2026-06-25
---

# GitHub

## O que é?

GitHub é plataforma de versionamento e colaboração baseada em Git. Armazena histórico completo do FabioOS e permite colaboração e CI/CD.

## Para que serve?

- Versionamento do vault Obsidian
- Backup automático do FabioOS
- Histórico completo de mudanças
- Integrações com [[n8n]] e automações
- Controle de acesso e auditoria

## Onde entra no FabioOS?

[[60_Sistemas|Sistemas]] > [[GitHub]] → core:
- Sincronização: Obsidian → GitHub (via n8n)
- Backup: histórico completo
- Integrações: webhooks, Actions, API
- Colaboração: Pull Requests, Issues

## Workflows integrados

1. **Sync automático** (n8n): Obsidian → GitHub a cada mudança
2. **Triggers**: GitHub eventos → n8n → Obsidian
3. **Segurança**: Secrets, credenciais não comitadas
4. **Histórico**: Changelog automático via commits

## Regras de segurança (CLAUDE.md)

- ✓ Ignorar `.env`, `.secret`, tokens em `.gitignore`
- ✓ Mensagens de commit descritivas
- ✓ Nunca commitar senhas ou API keys
- ✗ Não expor dados pessoais

## Relações

- ↔ [[Obsidian]] — sincronização bidirecional
- ↔ [[n8n]] — automações
- ↔ [[Claude_Code]] — scripts versionados
- ↔ [[MCP]] — integração via protocolo

## Próximas ações

- [ ] Revisar `.gitignore` e segredos
- [ ] Documentar workflows automatizados
- [ ] Implementar GitHub Actions
- [ ] Criar process de PR reviews
