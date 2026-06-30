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
6. Tension/Faction/Conflict Engine.
7. Engrenagem 6.
8. Mission Engine.
9. Player View / Cantina.
10. Banco relacional + grafo.
11. n8n como esteira.
12. OpenClaw como operador controlado.

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
- um conflito candidato com ator/local/motivo;
- contrato de missao;
- DeltaP previsto;
- WorldState recalculavel.
