---
name: "source-command-session-changelog"
description: "Gera changelog de sessão e salva em 50_Registros/Changelog/"
---

# source-command-session-changelog

Use this skill when the user asks to run the migrated source command `session-changelog`.

## Command Template

Você é o gerador de changelog do FabioOS. Sua tarefa é documentar o que foi feito na sessão atual.

## O que fazer

1. **Verifique o git log** dos commits desta sessão:
```bash
git log --oneline --since="today" 2>/dev/null || git log --oneline -10
```

2. **Liste arquivos criados/modificados** na sessão:
```bash
git status --short
git diff --name-only HEAD~5 HEAD 2>/dev/null
```

3. **Gere o arquivo de changelog** em:
`50_Registros/Changelog/YYYY-MM-DD_<slug>.md`

4. **Estrutura do changelog:**
```yaml
---
tipo: changelog
area: 50_Registros
projeto: FabioOS
status: concluído
tags: [changelog, sessão]
criado_em: [hoje]
atualizado_em: [hoje]
---
```

Seções:
- **O que foi feito** — lista objetiva
- **Instalado/configurado** — ferramentas, MCPs, plugins, repos
- **Criado/modificado no vault** — notas, pastas, arquivos
- **Commits realizados** — hash + mensagem
- **Pendente** — o que ficou para próxima sessão
- **Próximas ações** — tarefas concretas

## Regras
- Baseie-se nos fatos do git log e git status — não invente
- Se não houver commits na sessão, liste o que foi feito na conversa
- Nomeie o arquivo com slug descritivo (ex: `2026-06-26_workstation-setup.md`)
