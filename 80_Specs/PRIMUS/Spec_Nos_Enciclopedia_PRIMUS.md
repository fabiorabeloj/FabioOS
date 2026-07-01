---
tipo: spec
area: 80_Specs
projeto: PRIMUS
status: ativo
classe_dado: interno
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, spec, enciclopedia, obsidian]
---

# SPEC - Nos de Enciclopedia PRIMUS

## Missao

Definir onde ficam e como nascem os markdowns de raças, itens, faccoes, lugares, criaturas, regras, missoes e persistencia do PRIMUS.

## Local Canonico

| Familia | Pasta | Indice |
|---|---|---|
| Personagens e opcoes | `40_Wiki/PRIMUS/Enciclopedia/Personagens_e_Opcoes/` | [[40_Wiki/PRIMUS/Enciclopedia/Personagens_e_Opcoes/README]] |
| Magias e poderes | `40_Wiki/PRIMUS/Enciclopedia/Magias_e_Poderes/` | [[40_Wiki/PRIMUS/Enciclopedia/Magias_e_Poderes/README]] |
| Itens e tesouros | `40_Wiki/PRIMUS/Enciclopedia/Itens_e_Tesouros/` | [[40_Wiki/PRIMUS/Enciclopedia/Itens_e_Tesouros/README]] |
| Criaturas | `40_Wiki/PRIMUS/Enciclopedia/Criaturas/` | [[40_Wiki/PRIMUS/Enciclopedia/Criaturas/README]] |
| Lugares | `40_Wiki/PRIMUS/Enciclopedia/Lugares/` | [[40_Wiki/PRIMUS/Enciclopedia/Lugares/README]] |
| Faccoes e culturas | `40_Wiki/PRIMUS/Enciclopedia/Faccoes_e_Culturas/` | [[40_Wiki/PRIMUS/Enciclopedia/Faccoes_e_Culturas/README]] |
| Regras e procedimentos | `40_Wiki/PRIMUS/Enciclopedia/Regras_e_Procedimentos/` | [[40_Wiki/PRIMUS/Enciclopedia/Regras_e_Procedimentos/README]] |
| Missoes e encontros | `40_Wiki/PRIMUS/Instancias/` | [[40_Wiki/PRIMUS/Instancias/README]] |
| Persistencia | `40_Wiki/PRIMUS/Persistencia/` | [[40_Wiki/PRIMUS/Persistencia/README]] |

## Contrato de Nota

Cada nota deve conter:

- `primus_id` estavel;
- `familia` e `subtipo`;
- `fonte` ou `catalogentry`;
- `licenca`;
- `validacao`;
- link para [[40_Wiki/_MOCs/MOC_PRIMUS]];
- link para o indice da familia.

## Promocao

| Status | Regra |
|---|---|
| `rascunho` | Entrada criada por captura, ainda sem validacao. |
| `catalogado` | Tem fonte e tipo definidos. |
| `validado` | Tem evidencia rastreavel. |
| `pool-ready` | Pode alimentar CatalogPool, RAG ou Grafo com restricoes respeitadas. |

## Restricoes

- Conteudo `Restricted` nunca entra como dump integral.
- PDFs restritos geram resumo, metadados, pagina/ancora e decisao operacional.
- Fontes livres podem gerar texto mais detalhado, desde que mantenham atribuicao.

## Template

- [[40_Wiki/PRIMUS/Templates/Template_Entrada_Enciclopedia_PRIMUS]]
