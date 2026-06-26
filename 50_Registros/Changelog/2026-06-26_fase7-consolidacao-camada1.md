---
tipo: changelog
area: registros
projeto: FabioOS
status: concluído
fase: 7
tags: [changelog, fase-7, wiki, camada-1, documentação]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Changelog — Fase 7: Consolidação da Camada 1

## Resumo

Criação das 10 páginas wiki dos sistemas centrais da Camada 1 do FabioOS. Cada página documenta função, uso atual, uso futuro, riscos e relações com os demais sistemas, seguindo o padrão LLM-Wiki do schema.

## Arquivos criados

### wiki/sistemas/ — 10 páginas novas

| Arquivo | Sistema | Status no FabioOS |
|---|---|---|
| `wiki/sistemas/obsidian.md` | Obsidian | ativo |
| `wiki/sistemas/claude-code.md` | Claude Code | ativo |
| `wiki/sistemas/n8n.md` | n8n | ativo |
| `wiki/sistemas/github.md` | GitHub | ativo |
| `wiki/sistemas/chatgpt.md` | ChatGPT | manual (sem integração técnica) |
| `wiki/sistemas/openrouter.md` | OpenRouter | pendente de teste |
| `wiki/sistemas/openclaw.md` | OpenClaw | não implantado (Fase 11) |
| `wiki/sistemas/hermes-agent.md` | Hermes Agent | opcional (Fase 17) |
| `wiki/sistemas/manus.md` | Manus | não integrado (Fase 16) |
| `wiki/sistemas/cursor.md` | Cursor | não integrado (Fase 16.5) |

## Arquivos atualizados

- `wiki/indices/mapa-fabios.md` — Camada 1 atualizada com links para as 10 páginas; fase 7 marcada como concluída; próxima fase definida como 8

## Padrão aplicado

Cada página segue:
- Frontmatter com `tipo: wiki`, `camada: camada-1`, `status:` e `tags:`
- Marcadores `[FATO]` / `[INTERPRETAÇÃO]` / `[DECISÃO]` para distinguir origem da informação
- Seções: Função no FabioOS, O que faz, O que não deve fazer, Relação com outras ferramentas, Uso atual, Uso futuro, Riscos e cuidados, Próximas ações, Links internos
- Links internos Obsidian (`[[wiki/sistemas/x]]`) para todos os sistemas relacionados

## Decisões registradas

- Obsidian é o território central — nenhuma IA substitui como repositório principal
- Hermes Agent tem critério de entrada explícito: só ativar quando C.Code + n8n + OpenClaw não resolverem
- GITHUB_TOKEN hardcoded em `settings.json` identificado como risco — migrar para variável de ambiente
- OpenRouter e OpenClaw marcados como pendentes de teste/implantação — não inventar status técnico

## Próximas ações da Fase 8

- [ ] Estruturar `wiki/projetos/escola.md`
- [ ] Expandir agente `school-assistant`
- [ ] Criar estrutura de pastas para materiais da Escola em `sources/`

## Relações

- [[wiki/indices/mapa-fabios]]
- [[schema/fluxo-wiki]]
- [[schema/qualidade-wiki]]
- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]
- [[50_Registros/Changelog/2026-06-26_workstation-setup]]
