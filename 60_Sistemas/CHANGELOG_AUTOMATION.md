---
tipo: automação
area: tecnologia
status: planejamento
tags: [tecnico, changelog, automacao, github, n8n]
criado_em: 2026-06-25
atualizado_em: 2026-06-25
---

# Changelog Automation — Integração GitHub + Obsidian

## O que é?

Automação que sincroniza commits do GitHub com o arquivo `[[Changelog]]` do FabioOS, mantendo histórico automático de mudanças.

## Para que serve?

- Manter Changelog.md sempre atualizado
- Registrar automatically todas as mudanças
- Rastrear quem mudou o quê e quando
- Integrar histórico Git com repositório Obsidian
- Gerar relatórios de atividade

## Arquitetura

```
GitHub Event (commit/push)
    ↓ [Webhook]
n8n Workflow
    ↓ [Parse commit message]
Format entry
    ↓ [Append to Changelog.md]
Obsidian (atualiza local)
    ↓ [Git sync]
GitHub (backup)
```

## Opção 1: GitHub Actions (Recomendado — mais simples)

### Passo 1: Criar workflow

Criar arquivo `.github/workflows/changelog.yml`:

```yaml
name: Update Changelog

on:
  push:
    branches:
      - main
      - master

jobs:
  changelog:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Update Changelog
        run: |
          COMMIT_MSG=$(git log -1 --pretty=%B)
          COMMIT_HASH=$(git log -1 --pretty=%h)
          COMMIT_DATE=$(git log -1 --pretty=%cd --date=short)
          AUTHOR=$(git log -1 --pretty=%an)
          
          echo "## [${COMMIT_DATE}]" >> TEMP_CHANGELOG
          echo "" >> TEMP_CHANGELOG
          echo "**Autor:** ${AUTHOR}" >> TEMP_CHANGELOG
          echo "**Commit:** [\`${COMMIT_HASH}\`](https://github.com/USER/REPO/commit/${COMMIT_HASH})" >> TEMP_CHANGELOG
          echo "" >> TEMP_CHANGELOG
          echo "${COMMIT_MSG}" >> TEMP_CHANGELOG
          echo "" >> TEMP_CHANGELOG
          cat 40_Decisoes/Changelog.md >> TEMP_CHANGELOG
          mv TEMP_CHANGELOG 40_Decisoes/Changelog.md

      - name: Commit Changelog
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add 40_Decisoes/Changelog.md
          git commit -m "docs: atualizar changelog [skip ci]"
          git push
```

### Passo 2: Configurar permissões

Em Settings → Actions → General:
- Permitir GitHub Actions criar PRs/commits
- Permitir read/write permissions

## Opção 2: n8n Webhook (Mais flexível)

### Passo 1: Criar webhook no n8n

1. Criar novo workflow
2. Trigger: Webhook
3. Configurar URL: `https://[n8n-instance]/webhook/fabios-changelog`

### Passo 2: Parser de commits

```json
{
  "tipo": "{{ commit.message | split(':')[0] }}",
  "descricao": "{{ commit.message | split(':')[1] }}",
  "autor": "{{ commit.author.name }}",
  "hash": "{{ commit.sha | slice(0, 7) }}",
  "data": "{{ now() | dateFormat('YYYY-MM-DD') }}"
}
```

### Passo 3: Atualizar Changelog

Nodes:
1. **HTTP**: GET Changelog.md atual
2. **Code**: Parse + prepend nova entrada
3. **GitHub**: Push atualizado

## Convenção de commit para Changelog

Use prefixos:

```
TIPO: Descrição breve

[Descrição detalhada]
[Impacto]
[Próximas ações]
```

**Tipos recomendados:**

| Tipo | Descrição | Exemplo |
|------|-----------|---------|
| INFRA | Mudança estrutural | INFRA: Renomear extensões .md.md |
| FEAT | Nova feature | FEAT: Criar INDEX.md |
| DOCS | Documentação | DOCS: Expandir Automaçao.md |
| FIX | Correção | FIX: Links quebrados |
| REFACTOR | Reorganização | REFACTOR: Reorganizar 30_Conhecimento |
| TEST | Testes/validação | TEST: Validar backlinks |

## Exemplo de entrada Changelog

```markdown
## [2026-06-25]

### INFRA: Corrigidas extensões .md.md → .md
**Autor:** Claude  
**Commit:** [abc1234](https://github.com/FabioOs/main/commit/abc1234)

Renomeados 31 arquivos com extensão duplicada.

**Impacto:** Links Obsidian funcionam corretamente.
**Próximas ações:** Testar no Obsidian.
```

## Fluxo recomendado

1. **Local**: Edita arquivo, faz commit com mensagem clara
2. **GitHub**: Webhook dispara n8n
3. **n8n**: Processa mensagem, formata entrada
4. **Changelog**: Atualiza automaticamente
5. **Obsidian**: Git sync puxa mudanças

## Próximas ações

### Fase 1 (Esta semana)
- [ ] Escolher entre GitHub Actions ou n8n
- [ ] Implementar primeiro webhook
- [ ] Testar com 1 commit real
- [ ] Validar formato Changelog

### Fase 2 (Próximas semanas)
- [ ] Implementar tipos de commit
- [ ] Criar templates de PR
- [ ] Integrar com Dashboard
- [ ] Gerar relatórios de atividade

### Fase 3 (Futuro)
- [ ] Auto-generate release notes
- [ ] Integrar com versioning semântico
- [ ] Criar alertas para tipos específicos
- [ ] Analytics de produtividade

---

**Status:** 🟡 Planejado  
**Prioridade:** 🟠 Média  
**Esforço estimado:** 2-4 horas  
**Complexidade:** Média

## Referências

- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [n8n Docs](https://docs.n8n.io)
- [Keep a Changelog](https://keepachangelog.com/)
- [[integracao-n8n-github]]
