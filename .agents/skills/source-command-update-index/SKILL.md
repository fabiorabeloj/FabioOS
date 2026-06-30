---
name: "source-command-update-index"
description: "Atualiza o índice/mapa do FabioOS (sources/README.md e wiki/README.md)"
---

# source-command-update-index

Use this skill when the user asks to run the migrated source command `update-index`.

## Command Template

Você é o atualizador de índices do FabioOS. Sua tarefa é manter os índices `sources/README.md` e `wiki/README.md` sincronizados com o estado real das pastas.

## O que fazer

1. **Liste todos os arquivos** em `sources/repositorios/` e `wiki/`
2. **Compare** com a tabela de índice atual em `sources/README.md`
3. **Adicione entradas faltantes** à tabela, com:
   - Nome (link Obsidian)
   - Status (lido do frontmatter)
   - Categoria (lido do frontmatter ou inferido)
4. **Remova entradas** que apontem para arquivos inexistentes
5. **Atualize** `atualizado_em` no frontmatter do README
6. Repita para `wiki/README.md` se existir conteúdo em `wiki/`

## Regras
- Não reescreva o README inteiro — apenas atualize a tabela
- Não altere as seções de texto explicativo
- Mostre ao usuário quais entradas foram adicionadas/removidas antes de salvar
