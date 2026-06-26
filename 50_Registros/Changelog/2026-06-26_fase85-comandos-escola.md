---
tipo: changelog
area: registros
projeto: FabioOS
status: concluído
fase: 8.5
tags: [changelog, fase-8.5, escola, comandos, agentes]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Changelog — Fase 8.5: Comandos e Agente Escola

## Resumo

Implementação dos comandos slash do Sistema Escola e expansão completa do agente `school-assistant`. O FabioOS agora pode criar provas, revisões, gabaritos e comunicados via `/criar-prova`, `/criar-revisao`, `/criar-gabarito` e `/criar-comunicado`.

## Arquivos criados

### Comandos slash (`.claude/commands/`)

| Arquivo | Função |
|---|---|
| `criar-prova.md` | Gera prova com questões e gabarito separado (aprovação antes de salvar) |
| `criar-revisao.md` | Gera revisão com explicação, exemplos e exercícios |
| `criar-gabarito.md` | Extrai gabarito de prova existente com critérios de correção |
| `criar-comunicado.md` | Gera comunicado com aprovação humana obrigatória antes de envio |

## Arquivos atualizados

### Agente (`.claude/agents/`)

- `school-assistant.md` — expandido de esqueleto para agente operacional completo:
  - Identidade: GEO e FIL, 6º ao 9º ano
  - Tabela de adaptação por nível de turma
  - Regras pedagógicas completas (prova / revisão / comunicado)
  - Fluxo de trabalho padrão com aprovação antes de salvar
  - Lista do que não fazer
  - Links para todos os comandos slash

## Inventário atual de comandos (.claude/commands/)

| Comando | Sistema |
|---|---|
| `/archive-source` | FabioOS — arquivar fonte bruta |
| `/source-to-wiki` | FabioOS — transformar fonte em wiki |
| `/update-index` | FabioOS — atualizar mapa e índices |
| `/check-secrets` | Segurança — verificar credenciais |
| `/session-changelog` | FabioOS — registrar sessão |
| `/safe-commit` | Git — commit com verificação |
| `/criar-prova` | Escola — gerar prova |
| `/criar-revisao` | Escola — gerar revisão |
| `/criar-gabarito` | Escola — extrair gabarito |
| `/criar-comunicado` | Escola — gerar comunicado |

## Próximas ações

- [ ] Testar `/criar-prova` com `2026_9A_GEO_B2_PROVA.md` (critério de sucesso da Fase 8)
- [ ] Testar `/criar-revisao` com conteúdo real de FIL B1 para 8B
- [ ] Criar cronograma bimestral GEO e FIL 2026
- [ ] Avaliar necessidade de `/preparar-aula` e `/organizar-cronograma` na Fase 9

## Relações

- [[60_Sistemas/Escola/Sistema_Escola]]
- [[wiki/projetos/escola]]
- [[50_Registros/Changelog/2026-06-26_fase8-sistema-escola]]
