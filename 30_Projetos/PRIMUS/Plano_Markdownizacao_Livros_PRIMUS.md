---
tipo: plano
area: 30_Projetos
projeto: PRIMUS
status: ativo
fonte: [[80_Specs/PRIMUS/Spec_Markdownizacao_Segura_Livros_PRIMUS]]
criado_em: 2026-07-01
tags: [primus, markdown, obsidian, catalogo, livros]
---

# Plano de Markdownizacao de Livros - PRIMUS

## Funcao

Fazer o Obsidian crescer com nos reais sem transformar livros restritos em copia.

## O que Fabio Esperava

Criar MDs com:

- armas;
- itens;
- ideias;
- faccoes;
- criaturas;
- lugares;
- ganchos;
- regras;
- tabelas;
- missoes.

Isto e correto como objetivo, mas precisa de camadas.

## Camada 1 - Stubs Seguros

Criar paginas com:

```yaml
nome:
tipo:
fonte:
pagina:
license_status:
tags:
affects:
never_affects:
```

Sem copiar corpo textual.

## Camada 2 - Resumos Transformativos

Adicionar:

- funcao no PRIMUS;
- como usar em uma cena;
- riscos;
- relacoes;
- exemplos autorais.

## Camada 3 - Conteudo Autoral

Criar versoes proprias do PRIMUS:

- armas proprias;
- itens proprios;
- faccoes proprias;
- lugares proprios;
- criaturas proprias;
- missoes proprias.

## Camada 4 - Automacao

Gerar lote por lote:

1. `weapons`;
2. `equipment`;
3. `magic_items`;
4. `spells`;
5. `creatures`;
6. `factions`;
7. `planes`;
8. `missions`;
9. `encounter_patterns`;

## Proxima Execucao Recomendada

Gerar um lote pequeno de 20 stubs seguros:

- 5 equipamentos;
- 5 criaturas;
- 5 itens/artefatos como vetores;
- 5 procedimentos/ideias.

Depois validar se o Obsidian ficou legivel antes de gerar centenas.

## Nao Fazer

- nao gerar milhares de arquivos sem MOC;
- nao exportar texto integral;
- nao misturar material oficial e autoral sem frontmatter;
- nao reindexar RAG antes da validacao visual;
- nao tratar fonte restrita como conteudo publicavel.
