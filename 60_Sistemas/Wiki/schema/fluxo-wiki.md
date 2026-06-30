---
tipo: schema
area: schema
projeto: FabioOS
status: ativo
tags: [schema, llm-wiki, fluxo, workflow]
criado_em: 2026-06-25
atualizado_em: 2026-06-25
---

# Fluxo Mínimo LLM-Wiki — FabioOS

## Função

Define o fluxo controlado de transformação de fontes brutas em conhecimento estruturado no FabioOS.

## O fluxo

```
1. CAPTURA
   sources/<tipo>/<nome>.md
   (criado manualmente ou via /archive-source)
          ↓
2. ANÁLISE
   Claude lê a fonte, extrai: o que é, para que serve, relações
   NÃO inventa informação além da fonte
          ↓
3. SÍNTESE
   Claude gera rascunho de wiki/<categoria>/<nome>.md
   Usuário REVISA e APROVA o rascunho antes de salvar
          ↓
4. LINKAGEM
   Página wiki recebe:
   - Link de volta à fonte (frontmatter: fonte)
   - Links internos Obsidian para conceitos relacionados
   - Atualização no índice wiki/README.md
          ↓
5. VERSIONAMENTO
   git add + git commit (após /check-secrets)
```

## Categorias de destino

| Tipo de fonte | Categoria wiki | Caminho |
|---|---|---|
| Repositório GitHub | sistemas | `wiki/sistemas/<nome>.md` |
| Conceito técnico | conceitos | `wiki/conceitos/<nome>.md` |
| Pessoa/empresa | entidades | `wiki/entidades/<nome>.md` |
| Projeto ativo | projetos | `wiki/projetos/<nome>.md` |

## Regras do fluxo

1. **Uma fonte por vez** — não processar em batch sem aprovação
2. **Revisão humana obrigatória** antes de salvar qualquer página wiki
3. **Fonte nunca modificada** — apenas wiki/ é escrito
4. **Sem ingestão automática** — o usuário aciona cada transformação
5. **Distinção obrigatória:** `[FATO]` vs `[INTERPRETAÇÃO]` vs `[DECISÃO]`

## Como acionar

```
/source-to-wiki sources/repositorios/nome-do-repo.md
```

Ou usar o agente `wiki-curator` diretamente.

## Próximas ações

- [ ] Testar fluxo com `sources/repositorios/gsd-core.md` → `wiki/sistemas/gsd-core.md`
- [ ] Testar com `sources/repositorios/claude-mem.md` → `wiki/sistemas/claude-mem.md`
- [ ] Após 3 testes validados, avaliar automação via n8n

## Relações

- [[schema/qualidade-wiki]]
- [[wiki/README]]
- [[sources/README]]
- [[60_Sistemas/Claude_Code/Workstation_FabioOS]]
