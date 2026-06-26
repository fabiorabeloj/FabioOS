---
name: "source-command-ingest-doc"
description: "Processa documento local (DOCX, TXT, MD) ou conteúdo colado e preserva em sources/docs/ do FabioOS"
---

# source-command-ingest-doc

Use this skill when the user asks to run the migrated source command `ingest-doc`.

## Command Template

Você é o ingestor de documentos do FabioOS. Sua tarefa é processar um documento local ou conteúdo fornecido pelo usuário e preservá-lo como fonte estruturada.

## Entrada esperada

O usuário deve fornecer uma das opções:
1. **Caminho local do arquivo** — ex: `C:\Users\user\Downloads\relatorio.txt`
2. **Conteúdo colado diretamente** — texto do documento
3. **Descrição e pontos principais** — se o documento não puder ser lido diretamente

Se não forneceu nenhuma, pergunte: "Qual documento deseja arquivar? Informe o caminho do arquivo ou cole o conteúdo."

## Tipos de documento suportados

| Formato | Estratégia |
|---|---|
| `.txt` | Leitura direta com Read |
| `.md` | Leitura direta com Read |
| `.docx` | Pedir que usuário copie o texto |
| `.odt` | Pedir que usuário copie o texto |
| Conteúdo colado | Processar diretamente |

Se o formato não for legível diretamente, informar: "Este formato não é lido diretamente. Cole o texto do documento aqui."

## Categorias de documento

Classificar o documento antes de salvar:

| Tipo | Destino |
|---|---|
| Material escolar (aviso, planilha, gabarito externo) | `sources/docs/` com tag `escola` |
| Relatório técnico ou corporativo | `sources/docs/` |
| Transcrição de áudio ou reunião | `sources/docs/` com tag `transcricao` |
| Google Docs / Drive exportado | Preferir `/ingest-drive-doc` |

## Frontmatter obrigatório

```yaml
---
tipo: fonte
origem: arquivo
formato: [txt / docx / md / outro]
nome_original: [nome do arquivo com extensão]
titulo: [título do documento, se diferente do nome do arquivo]
autor: [autor, ou "desconhecido"]
caminho_original: [caminho local, se disponível]
capturado_em: [hoje em YYYY-MM-DD]
status: bruto
tags: [2-4 tags relevantes]
---
```

## Estrutura da nota-fonte

```markdown
# [Título do documento]

## Identificação
- **Arquivo original:** [nome]
- **Formato:** [formato]
- **Autor:** [autor]
- **Capturado em:** [hoje]

## Conteúdo

[Texto completo ou síntese, dependendo do tamanho:
- Documentos curtos (< 500 palavras): preservar integralmente
- Documentos médios (500–2000 palavras): síntese + trechos relevantes
- Documentos longos (> 2000 palavras): síntese estruturada com pontos principais]

## Por que está aqui

[Contexto: relevância para o FabioOS ou sistema específico]

## Próximas ações

- [ ] Avaliar com /check-source-quality
- [ ] Transformar em wiki com /source-to-wiki (se relevante)
```

## Nomenclatura do arquivo

```
sources/docs/[YYYY-MM-DD]_[slug].md

Exemplos:
  sources/docs/2026-06-26_aviso-reuniao-pedagogica.md
  sources/docs/2026-06-26_relatorio-desempenho-turmas.md
```

## Regra de segurança

Se o documento contiver dados pessoais de alunos (nomes, notas, situação), alertar o usuário antes de salvar: "Este documento contém dados pessoais. Deseja anonimizar antes de arquivar?"

## Fluxo completo

1. Receber caminho ou conteúdo
2. Tentar leitura direta; se falhar, pedir conteúdo colado
3. Classificar o tipo de documento
4. Montar nota-fonte com frontmatter
5. Mostrar ao usuário para revisão
6. Aguardar aprovação
7. Salvar em `sources/docs/`
8. Informar caminho criado
