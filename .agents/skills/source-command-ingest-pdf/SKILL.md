---
name: "source-command-ingest-pdf"
description: "Preserva e extrai conteúdo de um PDF em sources/pdfs/ do FabioOS"
---

# source-command-ingest-pdf

Use this skill when the user asks to run the migrated source command `ingest-pdf`.

## Command Template

Você é o ingestor de PDFs do FabioOS. Sua tarefa é preservar um PDF como fonte bruta e extrair seu conteúdo principal.

## Entrada esperada

O usuário deve fornecer uma das opções:
1. **Caminho local do PDF** — ex: `C:\Users\user\Downloads\artigo.pdf`
2. **Texto extraído do PDF** — conteúdo já copiado do documento
3. **Resumo e dados do PDF** — título, autor, data e pontos principais (se não for possível extrair o texto)

Se não forneceu nenhuma, pergunte: "Qual PDF deseja arquivar? Informe o caminho, cole o texto extraído, ou descreva o documento."

## Tentativa de leitura direta

Se um caminho for fornecido, tente ler com a ferramenta Read. Se falhar (PDF não é texto legível), informe ao usuário: "Não consigo ler PDF binário diretamente. Extraia o texto (Ctrl+A, Ctrl+C no Acrobat ou navegador) e cole aqui."

## Frontmatter obrigatório

```yaml
---
tipo: fonte
origem: pdf
titulo: [título do documento]
autor: [autor, ou "desconhecido"]
editora_ou_fonte: [editora, site ou instituição]
data_publicacao: [YYYY-MM-DD ou YYYY ou "desconhecida"]
num_paginas: [número, se conhecido]
caminho_original: [caminho do arquivo, se disponível]
capturado_em: [hoje em YYYY-MM-DD]
status: bruto
confiabilidade: pendente
tags: [2-4 tags relevantes]
---
```

## Estrutura da nota-fonte

```markdown
# [Título do PDF]

## Identificação
- **Autor:** [autor]
- **Fonte/Editora:** [origem]
- **Data de publicação:** [data]
- **Capturado em:** [hoje]

## Resumo

[Síntese do conteúdo principal — 3 a 10 parágrafos dependendo da extensão do documento. Não copiar integralmente se for muito longo.]

## Pontos principais

- [ponto 1]
- [ponto 2]
- [ponto 3]

## Trechos relevantes (opcional)

> "[citação direta se houver trecho especialmente importante]"

## Por que está aqui

[Contexto: por que este PDF é relevante para o FabioOS ou para um sistema específico]

## Próximas ações

- [ ] Avaliar com /check-source-quality
- [ ] Transformar em wiki com /source-to-wiki (se relevante)
```

## Nomenclatura do arquivo

```
sources/pdfs/[YYYY-MM-DD]_[slug-do-titulo].md

Exemplos:
  sources/pdfs/2026-06-26_edital-concurso-professor-2026.md
  sources/pdfs/2026-06-26_livro-didatico-geo-9ano-cap3.md
```

## Regras

- Nunca copiar PDFs integrais com centenas de páginas — sintetizar
- Marcar como `[FATO]` o que está no documento, `[INTERPRETAÇÃO]` o que é inferência
- Se o PDF tiver dados pessoais de alunos, alertar o usuário e não commitar sem anonimização

## Fluxo completo

1. Receber caminho ou conteúdo do PDF
2. Tentar leitura direta; se falhar, pedir extração pelo usuário
3. Montar nota-fonte com frontmatter
4. Mostrar ao usuário para revisão
5. Aguardar aprovação
6. Salvar em `sources/pdfs/`
7. Informar caminho criado
