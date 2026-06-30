---
tipo: schema
area: schema
projeto: FabioOS
status: ativo
tags: [schema, llm-wiki, qualidade, criterios]
criado_em: 2026-06-25
atualizado_em: 2026-06-25
---

# Critérios de Qualidade — Wiki FabioOS

## Função

Define os critérios mínimos que toda página `wiki/` deve atender antes de ser salva e commitada.

## Checklist obrigatório (toda página wiki)

### Estrutura
- [ ] Frontmatter completo com todos os campos obrigatórios
- [ ] Campo `fonte:` linkando à nota-fonte em `sources/`
- [ ] Seções: Função, Contexto, Como usar, Relações, Próximas ações

### Conteúdo
- [ ] Síntese clara — não cópia integral da fonte
- [ ] Sem informação inventada além do que está na fonte
- [ ] Distinção explícita marcada:
  - `[FATO]` — extraído diretamente da fonte
  - `[INTERPRETAÇÃO]` — inferência do curador
  - `[DECISÃO]` — escolha operacional do FabioOS
- [ ] Linguagem analítica e operacional (padrão FabioOS)

### Links
- [ ] Links Obsidian corretos: `[[nome-do-arquivo]]` (sem extensão)
- [ ] Pelo menos 1 link para conceito relacionado na wiki
- [ ] Link de volta à fonte no frontmatter

### Metadados
- [ ] `tipo: wiki` (não fonte, não schema)
- [ ] `status:` definido (ativo / rascunho / arquivado)
- [ ] `criado_em:` e `atualizado_em:` no formato YYYY-MM-DD
- [ ] `tags:` com pelo menos 2 categorias relevantes

## Frontmatter padrão completo

```yaml
---
tipo: wiki
area: wiki
projeto: FabioOS
status: ativo
fonte: [[sources/repositorios/nome]]
tags: [claude-code, llm, tool]
criado_em: YYYY-MM-DD
atualizado_em: YYYY-MM-DD
---
```

## Erros comuns a evitar

| Erro | Correto |
|---|---|
| Copiar fonte integralmente | Sintetizar em 30-50% do tamanho |
| Usar `[nome](link.md)` markdown | Usar `[[nome]]` Obsidian |
| Deixar `tipo: fonte` na wiki | Mudar para `tipo: wiki` |
| Omitir campo `fonte:` | Sempre linkar a origem |
| Inventar funcionalidades | Marcar como `[INTERPRETAÇÃO]` |
| Misturar fato e opinião | Usar marcadores `[FATO]` / `[INTERPRETAÇÃO]` |

## Escala de maturidade

| Nível | Critério |
|---|---|
| Rascunho | Frontmatter incompleto, sem links |
| Básico | Frontmatter completo, síntese presente |
| Qualificado | + Links internos corretos, distinção fato/interpretação |
| Maduro | + Integrado ao índice wiki/README.md, commitado |

## Relações

- [[schema/fluxo-wiki]]
- [[schema/README]]
- [[wiki/README]]
