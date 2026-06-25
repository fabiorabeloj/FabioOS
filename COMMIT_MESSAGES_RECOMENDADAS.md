# Commit Messages Recomendadas — Implementação 2026-06-25

Use estas mensagens para fazer commits documentados:

```bash
# Passo 1: Correção de estrutura
git add -A
git commit -m "refactor: corrigir extensões .md.md para .md em 31 arquivos

- Renomeados todos os arquivos com extensão duplicada
- Validados todos os links internos
- Pronto para Obsidian"

# Passo 2: Índice e metadados
git commit -m "docs: criar INDEX.md e padrão de metadados

- INDEX.md com mapa completo do FabioOS
- Frontmatter YAML em todos os arquivos estruturais
- Tags padronizadas (#projeto, #automacao, #conceito)
- Convenções de naming documentadas"

# Passo 3: Completar arquivos
git commit -m "docs: completar estrutura de arquivos

Adicionado:
- RAG.md, Banco_Vetorial.md, MCP.md, Grafos_de_Conhecimento.md
- Filosofia.md, Geografia.md, RPG.md (preenchidos)
- Fontes: Livros, Artigos, Links, PDF (preenchidos)
- Sistemas: Claude_Code, GitHub, Obsidian, OpenRouter (documentados)
- Projetos: Atendimento_Pietra, Aprendizado, Changelog (preenchidos)"

# Passo 4: Validação
git commit -m "test: validar backlinks e gerar relatório

- Analisados 461 links internos
- Taxa de sucesso: 98.5%
- Corrigidos 6 problemas críticos
- Relatório completo em RELATORIO_VALIDACAO_LINKS.md"

# Passo 5: Automação Changelog
git commit -m "ci: implementar changelog automático com GitHub Actions

- Workflow em .github/workflows/changelog.yml
- Auto-update de 40_Decisoes/Changelog.md em cada push
- Convenção de commits: TIPO: Descrição
- Documentação em CHANGELOG_AUTOMATION.md"

# Passo 6: Implementação RAG
git commit -m "docs: documentar implementação de RAG com Chroma

- Scripts prontos em scripts/
- Ingestão, busca e integração Claude
- 3 fases de implementação documentadas
- Guia completo em RAG_IMPLEMENTATION.md"

# Passo 7: Expandir conteúdo
git commit -m "docs: expandir Tecnologia, Projetos e criar templates

- 30_Conhecimento/Tecnologia expandido com princípios e padrões
- 20_Projetos/IA expandido com arquitetura e roadmap
- TEMPLATE_NOVO_PROJETO.md para novos projetos
- Todos os links corrigidos"

# Final: Resumo
git commit -m "docs: resumo executivo de implementação

- RESUMO_IMPLEMENTACAO_FINAL.md
- Estatísticas completas
- Próximas ações prioritárias
- Checklist de validação
- [skip ci]"
```

---

## Commit em um único push (opção mais simples)

```bash
git add .
git commit -m "refactor: reestruturar FabioOS completo — implementação 2026-06-25

BREAKING CHANGES: Extensões .md.md corrigidas para .md

Estrutura:
- Corrigidas 31 arquivos com extensão duplicada
- Criado INDEX.md com mapa central
- Adicionados 15+ arquivos de documentação
- Validados 461 links internos (98.5% sucesso)

Documentação:
- RAG_IMPLEMENTATION.md (guia Chroma)
- CHANGELOG_AUTOMATION.md (GitHub Actions)
- RELATORIO_VALIDACAO_LINKS.md (análise)
- RESUMO_IMPLEMENTACAO_FINAL.md (executivo)

Expansão:
- Tecnologia expandido com princípios
- IA expandido com arquitetura
- Projetos completados
- TEMPLATE_NOVO_PROJETO.md criado

Links:
- Todos os [[30_Conhecimento/IA.md]] corrigidos para [[IA]]
- [[80_Sistemas]] corrigido para [[60_Sistemas]]
- Pipe syntax padronizado

Próximos passos:
- [ ] Validar no Obsidian
- [ ] Ativar GitHub Actions
- [ ] Implementar RAG Fase 1
- [ ] Integrar com Dashboard"

git push
```

---

## Verificar status antes de fazer push

```bash
# Ver o que vai ser enviado
git log --oneline -n 5

# Ver tamanho dos arquivos
du -sh .

# Verificar se há sensíveis
git diff HEAD --stat

# Confirmar nenhum token/secret
grep -r "OPENAI_API_KEY\|token\|secret" . --exclude-dir=.git
```

---

## Timeline recomendado

| Quando | Ação |
|--------|------|
| Imediatamente | Fazer commit com estrutura |
| Hoje +1h | Testar no Obsidian |
| Hoje +2h | Ativar GitHub Actions |
| Amanhã | Começar RAG Fase 1 |
| Esta semana | RAG completo + integrações |
| Próxima semana | Agentes e automações avançadas |

---

Bom push! 🚀
