---
tipo: auditoria
area: 50_Registros
projeto: PRIMUS
status: concluida
criado_em: 2026-07-01
tags: [primus, auditoria, conceitos, obsidian, nota-vs-dado]
---

# Auditoria - Markdownizacao de Conceitos PRIMUS

## Escopo

Execucao da ordem do Claude registrada no barramento em 2026-07-01 08:51:34:
aplicar o metodo de markdownizacao de conceitos de livro, sem stubs massivos e
sem texto protegido.

## Resultado

- Conceitos existentes antes: 5 nos + MOC.
- Conceitos adicionados: 14 nos.
- Total atual em `40_Wiki/PRIMUS/conceitos/`: 19 nos de conceito + 1 MOC.
- MOC atualizado: [[40_Wiki/PRIMUS/conceitos/MOC_Conceitos_Design_PRIMUS]].
- README PRIMUS atualizado para apontar para o MOC de conceitos.

## Nos derivados de SWN/WWN free

- [[40_Wiki/PRIMUS/conceitos/frente-de-faccao-e-projetos]]
- [[40_Wiki/PRIMUS/conceitos/reacao-do-mundo-entre-sessoes]]
- [[40_Wiki/PRIMUS/conceitos/regiao-com-tags-e-problemas]]
- [[40_Wiki/PRIMUS/conceitos/npc-com-agenda-e-alavancas]]
- [[40_Wiki/PRIMUS/conceitos/site-com-proposito-e-perigo]]
- [[40_Wiki/PRIMUS/conceitos/rumor-com-fonte-e-incerteza]]
- [[40_Wiki/PRIMUS/conceitos/missao-com-situacao-nao-trilho]]
- [[40_Wiki/PRIMUS/conceitos/recompensa-com-consequencia]]

## Nos abstratos derivados de D&D Core

- [[40_Wiki/PRIMUS/conceitos/classe-como-fantasia-operacional]]
- [[40_Wiki/PRIMUS/conceitos/encontro-como-pressao-de-recursos]]
- [[40_Wiki/PRIMUS/conceitos/tesouro-como-vetor-de-decisao]]
- [[40_Wiki/PRIMUS/conceitos/monstro-como-funcao-dramatica]]
- [[40_Wiki/PRIMUS/conceitos/premissa-de-mundo-como-gerador-de-tensao]]
- [[40_Wiki/PRIMUS/conceitos/viagem-planar-como-custo-e-risco]]

## Validacao de seguranca

- Nenhum texto integral de PDF foi versionado.
- Nenhuma tabela, statblock, lista de itens, lista de criaturas ou regra protegida
  foi copiada para o 40_Wiki.
- D&D permanece em Modo Catalogo: dados no PRIMUS Index/SQLite e no catalogo
  consolidado; apenas conceitos abstratos entram como nos.
- Cada novo no possui pelo menos dois wikilinks para o motor PRIMUS ou conceitos
  relacionados.

## Ajustes de grafo

Links antigos para `[[Spec_DeltaP]]` foram corrigidos para
`[[Spec_DeltaP_PRIMUS|DeltaP]]` nos conceitos existentes, reduzindo risco de notas
soltas no grafo.

## Proxima acao recomendada

Criar uma checagem automatica leve para conceitos PRIMUS:

- frontmatter `tipo: conceito`;
- minimo de dois wikilinks;
- proibicao de termos que indiquem tabela/statblock/dump;
- link obrigatorio para pelo menos um componente do motor PRIMUS.
