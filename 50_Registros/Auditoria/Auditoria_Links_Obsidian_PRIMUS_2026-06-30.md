---
tipo: auditoria
area: 50_Registros
projeto: FabioOS
status: ativo
classe_dado: interno
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [fabios, obsidian, auditoria, links, primus]
---

# Auditoria - Links Obsidian e PRIMUS

## Diagnostico

A primeira revitalizacao do Obsidian melhorou cores e alguns MOCs, mas nao criava ainda uma malha suficiente para receber milhares de notas futuras do PRIMUS.

## Medicao

| Item | Resultado |
|---|---|
| Wikilinks quebrados no vault | 351 |
| Causa principal | legado, compatibilidade e links antigos para `sources/`, `wiki/`, `10_Mapas/`, `50_Fontes/`, `30_Conhecimento/` |
| PRIMUS potencialmente solto | 4 notas operacionais |
| Risco | mapas bonitos, mas nos sem caminho canonico |

## Acao Corretiva Nesta Rodada

- Criado [[40_Wiki/_MOCs/MOC_PRIMUS]].
- Criada [[40_Wiki/PRIMUS/Enciclopedia/README]].
- Criadas familias para personagens, magias, itens, criaturas, lugares, faccoes, regras, instancias e persistencia.
- Criada [[80_Specs/PRIMUS/Spec_Nos_Enciclopedia_PRIMUS]].
- Criado [[40_Wiki/PRIMUS/Templates/Template_Entrada_Enciclopedia_PRIMUS]].

## Fora do Escopo

- Nao corrigir os 351 links em massa nesta rodada.
- Nao mover legado enquanto outras frentes estao sujas.
- Nao extrair PDF restrito.
- Nao reindexar RAG.

## Proxima Rodada Recomendada

1. Corrigir links quebrados por lote e por pasta.
2. Comecar por dashboards vivos e PRIMUS.
3. Deixar `90_Arquivo/` por ultimo, pois muitos links quebrados sao legado historico.
