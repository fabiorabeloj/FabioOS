---
tipo: spec
area: 80_Specs
projeto: EscolaOS
status: ativo
criado_em: 2026-07-01
tags: [escolaos, apostilas, obsidian, ingestao, aulas]
---

# SPEC - Ingestao de Apostilas EscolaOS

## Objetivo

Transformar apostilas, provas, revisoes, planos de aula e materiais docentes do Fabio em conhecimento vivo no Obsidian.

## Diferenca para Livros Restritos

Se a apostila for autoral do Fabio, ela pode virar Markdown completo.

Se contiver texto de terceiros, ela entra por camadas:

```text
autoral -> nota completa
terceiros/licenciado -> resumo seguro
duvidoso -> quarentena
```

## Saidas Possiveis

| Entrada | Saida no Obsidian |
|---|---|
| apostila autoral | nota completa + mapa de conceitos |
| plano de aula | sequencia didatica |
| prova | prova + gabarito + matriz de habilidades |
| revisao | roteiro de estudo + flashcards |
| slides | resumo de aula + topicos |
| PDFs de terceiros | fonte restrita + resumo seguro |

## Estrutura Recomendada

```text
05_Raw_Sources/EscolaOS/
  -> arquivo original preservado

20_Areas/EscolaOS/
  -> operacao docente e planejamento

40_Wiki/EscolaOS/
  -> conceitos, temas, habilidades e mapas

80_Specs/EscolaOS/
  -> regras de ingestao e formatos
```

## Pipeline

```text
Apostila enviada
  -> preservar fonte
  -> classificar autoria/licenca
  -> extrair topicos
  -> criar mapa de conceitos
  -> gerar notas por tema
  -> gerar atividades/provas/revisoes
  -> conectar ao RAG somente apos aprovacao
```

## Frontmatter Minimo

```yaml
tipo:
area: EscolaOS
disciplina:
ano:
bimestre:
origem:
autoria:
classe_dado:
status:
tags:
```

## Criterios de Aceite

- a apostila original fica rastreavel;
- cada nota gerada aponta para a fonte;
- conteudo autoral fica separado de conteudo de terceiros;
- a nota e util para aula, revisao ou avaliacao;
- nao ha material sensivel de aluno exposto.

## Primeiro Piloto

Quando Fabio enviar a primeira apostila:

1. criar fonte bruta em `05_Raw_Sources/EscolaOS/`;
2. gerar uma nota-mapa;
3. gerar 3 notas conceituais;
4. gerar 1 revisao;
5. gerar 1 banco de questoes;
6. registrar changelog.
