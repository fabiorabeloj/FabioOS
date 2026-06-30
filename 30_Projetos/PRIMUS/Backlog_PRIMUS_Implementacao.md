---
tipo: backlog
area: 30_Projetos
projeto: PRIMUS
status: ativo
fonte: [[05_Raw_Sources/PRIMUS/2026-06-30_chatgpt_project_primus_inventario_logs]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, backlog, implementacao, roadmap]
---

# Backlog de Implementacao PRIMUS

## Ordem Correta

1. Ontologia formal.
2. DeltaP e WorldState derivado.
3. CatalogEntries reais. Iniciado em [[CatalogEntries_Lote_0001_PRIMUS]].
4. CatalogPool. Iniciado em [[CatalogPool_0001_PRIMUS]].
5. Validadores V(E), V(I), V(P).
6. Vector Engine e WorldCycle.
7. Tension/Faction/Conflict Engine.
8. Villain Engine e Liga de Viloes Persistente.
9. Engrenagem 6.
10. Mission Contract.
11. Mission Engine.
12. Player View / Cantina.
13. Banco relacional + grafo.
14. n8n como esteira.
15. OpenClaw como operador controlado.

## Nao Fazer Ainda

- Executar Missao 0001.
- Adicionar Godbound/ACKS como runtime.
- Criar simulacao continua.
- Criar app antes de schema minimo.
- Deixar IA decidir sem fila/log/changelog.

## Primeiro Marco Funcional

PRIMUS sera minimamente funcional quando existir:

- 20 CatalogEntries reais;
- V(E) aplicado;
- CatalogPool;
- Changelog 5.6 formalizado;
- Vector Engine;
- WorldCycle;
- um conflito candidato com ator/local/motivo;
- contrato de missao;
- DeltaP previsto;
- WorldState recalculavel.
