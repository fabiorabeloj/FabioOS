---
tipo: diagnostico
area: 50_Registros
projeto: FabioOS
status: registrado
data: 2026-06-29
responsavel: Codex
tags: [fabios, obsidian, raiz, wiki, diagnostico]
---

# Diagnostico - pasta `wiki/` recriada na raiz

## Achado

A pasta `wiki/` reapareceu na raiz do vault enquanto outras frentes estavam ativas.

Conteudo encontrado:

```text
wiki/conceitos/rag.md
```

## Comparacao

O arquivo e identico ao canônico:

```text
40_Wiki/_compat_wiki/conceitos/rag.md
```

Hash SHA256 igual para ambos.

## Decisao

Codex nao apagou nem moveu a pasta nesta rodada, porque:

- ha outras frentes ativas;
- o arquivo pode ter sido recriado por processo externo, Cursor, Claude, Obsidian ou automacao;
- apagar novamente sem descobrir a origem mascara o problema.

## Hipotese

Algum workflow, script, plugin ou nota ainda referencia/escreve no caminho legado `wiki/conceitos/rag.md`.

## Proxima acao recomendada

1. Claude/Cursor verificar qual processo esta recriando `wiki/`.
2. Procurar referencias a `wiki/conceitos/rag` em scripts, workflows e configuracoes.
3. Corrigir a origem para `40_Wiki/_compat_wiki/conceitos/rag.md`.
4. So depois arquivar/remover a duplicata da raiz.

## Limites respeitados

- Nao apagar.
- Nao mover.
- Nao alterar RAG.
- Nao reindexar.
- Sem push.
