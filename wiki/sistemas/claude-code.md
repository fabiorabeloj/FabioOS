---
tipo: wiki
area: sistemas
projeto: FabioOS
status: ativo
camada: camada-1
tags: [claude-code, agente, operador, ia, camada-1]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Claude Code

## Função no FabioOS

[DECISÃO] O Claude Code é o **operador técnico principal do FabioOS** — o agente que lê, cria, edita e organiza arquivos no vault, executa Git, cria automações e mantém o projeto coerente entre sessões.

## O que essa ferramenta faz

[FATO] CLI da Anthropic que executa um agente Claude com acesso a ferramentas de filesystem, shell, Git e MCPs configurados. Opera dentro do repositório guiado por `CLAUDE.md` e pelos arquivos em `.claude/`.

No FabioOS, o Claude Code cumpre:

- Ler e escrever arquivos Markdown no vault
- Executar Git (add, commit, push, log, status)
- Criar e manter páginas da wiki (`wiki/`)
- Arquivar fontes em `sources/`
- Executar comandos slash (`.claude/commands/`)
- Acionar agentes especializados (`.claude/agents/`)
- Verificar arquivos sensíveis antes de commits
- Gerar changelogs e documentação técnica
- Interagir com MCPs configurados no projeto

[FATO] Configuração project-level em `.claude/`: 6 comandos, 4 agentes, 3 skills (gsd-core, huashu-design, taste-skill). Plugins globais: claude-mem, superpowers, obsidian-skills, ui-ux-pro-max.

[FATO] Modelo atual: Claude Sonnet 4.6.

## O que essa ferramenta não deve fazer

- Substituir o Obsidian como repositório central de conhecimento
- Tomar decisões estratégicas sem consulta ao usuário
- Fazer push sem aprovação explícita
- Mover ou apagar pastas sem plano confirmado
- Operar em modo autônomo contínuo sem checkpoint humano
- Commitar credenciais ou dados sensíveis

## Relação com outras ferramentas

| Ferramenta | Relação |
|---|---|
| [[wiki/sistemas/obsidian]] | Vault que o Claude Code opera |
| [[wiki/sistemas/github]] | Executa commits e push no repositório |
| [[wiki/sistemas/n8n]] | Pode criar e documentar automações n8n |
| [[wiki/sistemas/gsd-core]] | GSD fornece skills de planejamento e execução |
| [[wiki/sistemas/claude-mem]] | Memória persistente entre sessões |
| [[wiki/conceitos/mcp]] | Usa MCPs para acessar sistemas externos |

## Uso atual

- [x] CLAUDE.md com identidade, regras e leitura obrigatória de sessão
- [x] `.claude/commands/`: archive-source, source-to-wiki, update-index, check-secrets, session-changelog, safe-commit
- [x] `.claude/agents/`: vault-architect, wiki-curator, security-reviewer, school-assistant
- [x] `.claude/skills/`: gsd-core (junction), huashu-design (junction), taste-skill (junction)
- [x] Plugins: claude-mem v13.8.1, superpowers v6.0.3, obsidian-skills v1.0.1, ui-ux-pro-max v2.6.2
- [x] MCPs ativos: filesystem, context7, github, playwright-mcp, n8n-docs, claude-mem interno

## Uso futuro

- [ ] Hooks de SessionStart customizados para o FabioOS
- [ ] Comando `/ingest-url` e família de ingestão (Fase 7.5)
- [ ] Agente `school-assistant` expandido (Fase 8)
- [ ] Integração com RAG via MCP customizado (Fase 12/15)

## Riscos e cuidados

- **Contexto de sessão**: sem `CLAUDE.md` e leitura obrigatória, cada sessão começa sem memória — risco de inconsistência
- **Commits automáticos**: nunca executar `git push` sem mostrar resumo antes
- **Comandos destrutivos**: `rm -rf`, `git reset --hard`, rename de pastas principais exigem confirmação
- **Tokens em arquivos**: sempre rodar `/check-secrets` antes de commit

## Próximas ações

- [ ] Testar cada comando slash com caso real
- [ ] Criar comando `/ingest-url` para Fase 7.5
- [ ] Expandir agente `school-assistant` quando Fase 8 iniciar

## Links internos

- [[wiki/indices/mapa-fabios]]
- [[wiki/sistemas/obsidian]]
- [[wiki/sistemas/gsd-core]]
- [[wiki/sistemas/claude-mem]]
- [[wiki/conceitos/mcp]]
- [[60_Sistemas/Claude_Code/Claude_Project_Config]]
- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]
