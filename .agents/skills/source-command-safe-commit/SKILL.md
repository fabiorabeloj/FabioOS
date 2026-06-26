---
name: "source-command-safe-commit"
description: "Prepara e executa commit seguro no FabioOS (check-secrets + stage + commit)"
---

# source-command-safe-commit

Use this skill when the user asks to run the migrated source command `safe-commit`.

## Command Template

Você é o assistente de commit seguro do FabioOS. Execute o fluxo completo de commit com verificação de segurança.

## Fluxo obrigatório

### Etapa 1 — Estado atual
```bash
git status
git diff --stat HEAD
```
Mostre ao usuário o resumo do que será commitado.

### Etapa 2 — Verificação de segurança
Execute o mesmo scan de `/check-secrets`:
- Padrões: api_key, token, secret, password, Bearer, ghp_, sk-, anthropic
- Se encontrar credencial real: PARE e avise. Não continue.

### Etapa 3 — Verificar .gitignore
Confirme que estes arquivos NÃO estão sendo incluídos:
- `.env`, `.env.*`
- `*.key`, `*.pem`, `*.secret`
- `.Codex.json` (se contiver tokens)
- `settings.local.json` com credenciais

### Etapa 4 — Propor mensagem de commit
Siga o padrão Conventional Commits:
- `feat:` — nova funcionalidade
- `docs:` — documentação
- `chore:` — manutenção/configuração
- `fix:` — correção
- `refactor:` — reorganização

Proposta de mensagem baseada no conteúdo staged.

### Etapa 5 — Aguardar aprovação
Mostre ao usuário:
1. Lista de arquivos a commitar
2. Mensagem proposta
3. Resultado do check de segurança

Só execute `git commit` após o usuário confirmar.

### Etapa 6 — Commit
```bash
git commit -m "mensagem aprovada"
```

## Regras
- Nunca fazer push sem instrução explícita do usuário
- Nunca usar `--no-verify`
- Em caso de dúvida sobre sensíveis, sempre parar e perguntar
