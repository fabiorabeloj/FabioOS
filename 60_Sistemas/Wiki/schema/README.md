---
tipo: schema
area: schema
projeto: FabioOS
status: ativo
tags: [schema, convenções, regras, llm-wiki]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Schema — FabioOS LLM-Wiki

## Função

Regras, convenções, templates, categorias e instruções de manutenção para o sistema LLM-Wiki do FabioOS.

## Estrutura do vault (3 camadas)

```
sources/         ← fontes brutas: resumos de repos, artigos, PDFs, notas originais
wiki/            ← páginas geradas/organizadas por IA: entidades, conceitos, índices
schema/          ← este diretório: regras, templates, convenções, instruções
```

## Onde ficam repositórios técnicos

Repositórios com `.git`, `node_modules` e código-fonte ficam **fora do vault**:

```
C:\Users\user\claude-extensions\<nome-do-repo>\
```

Para cada repo clonado fora do vault, existe uma nota-fonte em:

```
sources/repositorios/<nome-do-repo>.md
```

## Convenções de frontmatter

Toda nota do vault deve ter:

```yaml
---
tipo: [fonte | wiki | schema | inventário | documentação | changelog]
area: [sources | wiki | schema | 00_Inbox | 10_Mapas | ...]
projeto: FabioOS
status: [ativo | arquivado | rascunho | concluído | pendente]
tags: [lista de tags]
criado_em: YYYY-MM-DD
atualizado_em: YYYY-MM-DD
---
```

## Padrão de nota estrutural

```md
# Título

## Função

## Contexto

## Como usar

## Relações

## Próximas ações
- [ ]
```

## Migração futura

Quando aprovada, a migração consolidará o conhecimento permanente do FabioOS em `wiki/`. A estrutura atual (00_Inbox, 10_Mapas, etc.) coexiste até a migração ser validada.

## Relações

- [[sources/repositorios/]] — notas-fonte de todos os repos clonados
- [[wiki/]] — páginas geradas a partir das fontes
