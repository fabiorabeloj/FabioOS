---
tipo: wiki
area: sistemas
projeto: FabioOS
status: ativo
camada: camada-1
tags: [github, versionamento, backup, git, camada-1]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# GitHub

## Função no FabioOS

[DECISÃO] O GitHub é a **camada de versionamento e segurança histórica do FabioOS** — garante que o vault seja auditável, recuperável e rastreável ao longo do tempo. Não substitui o Obsidian como interface de leitura nem o Claude Code como operador.

## O que essa ferramenta faz

[FATO] Plataforma de versionamento baseada em Git. Armazena o histórico completo de mudanças, permite recuperação de versões anteriores e suporta automações via GitHub Actions.

No FabioOS, o GitHub cumpre:

- Backup contínuo do vault após cada sessão de trabalho
- Histórico de mudanças por fase (commits semânticos)
- Rastreabilidade: quem mudou o quê e por quê
- Recuperação de versões anteriores de notas e documentos
- Ponto de integração futuro com GitHub Actions e CI/CD

[FATO] Repositório atual: `fabiorabeloj/FabioOS` (público). Branch principal: `main`. MCP `github` configurado globalmente (`~/.claude/settings.json`) com token de acesso.

[FATO] Padrão de commits do FabioOS: Conventional Commits (`feat:`, `docs:`, `chore:`, `fix:`), mensagem em português ou inglês, Co-Authored-By Claude quando aplicável.

## O que essa ferramenta não deve fazer

- Ser usado como interface de leitura ou edição de notas (o Obsidian faz isso)
- Receber commits com tokens, senhas, chaves de API ou dados sensíveis
- Ser usado para armazenar arquivos binários grandes (PDFs, imagens volumosas)
- Receber força-push em `main` sem justificativa crítica

## Relação com outras ferramentas

| Ferramenta | Relação |
|---|---|
| [[wiki/sistemas/obsidian]] | Vault do Obsidian é o repositório versionado |
| [[wiki/sistemas/claude-code]] | Claude Code executa os commits e push |
| [[wiki/sistemas/n8n]] | Futuro: GitHub Actions pode acionar n8n |

## Uso atual

- [x] Repositório `fabiorabeloj/FabioOS` ativo e sincronizado
- [x] `.gitignore` configurado: tokens, logs, `.claude/settings.local.json`, `.claude/skills/`
- [x] MCP `github` configurado (stdio) — Connected ✅
- [x] Commits por fase: histórico de Fase 3 a Fase 7 registrado
- [x] Branch `main` sincronizado com `origin/main`

## Uso futuro

- [ ] GitHub Actions para backup automático diário do vault
- [ ] Workflow CI que roda `/check-secrets` antes de aceitar PR
- [ ] Badge de status no README do repositório
- [ ] Integração com n8n via webhook de push (Fase 10/20)

## Riscos e cuidados

- **GITHUB_TOKEN em `~/.claude/settings.json`**: token hardcoded em texto plano no arquivo global — não commitado, mas exposto em disco; migrar para `$env:GITHUB_TOKEN` futuramente
- **Repositório público**: o vault do FabioOS é público — nunca commitar dados pessoais, dados de alunos, informações sigilosas ou credenciais
- **Commits grandes**: sessões com muitos arquivos devem usar commits separados por tema para facilitar revisão e recuperação

## Próximas ações

- [ ] Migrar `GITHUB_TOKEN` de `settings.json` para variável de ambiente
- [ ] Adicionar `README.md` descritivo ao repositório público
- [ ] Avaliar tornar o repositório privado se dados sensíveis forem adicionados futuramente

## Links internos

- [[wiki/indices/mapa-fabios]]
- [[wiki/sistemas/obsidian]]
- [[wiki/sistemas/claude-code]]
- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]
