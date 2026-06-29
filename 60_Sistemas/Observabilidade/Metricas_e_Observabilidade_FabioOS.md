---
tipo: dashboard
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [observabilidade, metricas, agentes, custos, logs]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Metricas e Observabilidade FabioOS

## Funcao

Definir como o FabioOS sabe se esta funcionando.

## Metricas minimas

| Metrica | Frequencia | Fonte |
|---|---|---|
| notas criadas por semana | semanal | Git/Obsidian |
| fontes preservadas | semanal | `sources/` |
| paginas wiki criadas/atualizadas | semanal | `wiki/` |
| decisoes registradas | semanal | `50_Registros/Decisoes/` |
| tarefas concluidas | semanal | NEXT_ACTIONS / Tasks |
| projetos ativos/parados | semanal | dashboards |
| automacoes funcionando/falhando | semanal | n8n/OpenClaw logs |
| commits realizados | semanal | Git |
| agentes usados | semanal | registros de agentes |
| custos de API | mensal | logs/custos |
| erros recorrentes | semanal | auditorias |
| arquivos sem categoria | mensal | lint |
| notas orfas | mensal | lint/grafo |
| tempo desde ultima revisao | semanal | STATUS |

## Futuro dashboard

Deve exibir:

- status do Obsidian;
- status do GitHub;
- status do n8n;
- status do OpenClaw;
- status dos agentes;
- status dos RAGs;
- status dos MCPs;
- status dos backups;
- custos;
- alertas;
- ultimos erros;
- proximas revisoes.

## Logs obrigatorios

Toda execucao relevante deve registrar:

- data;
- agente;
- objetivo;
- ferramenta;
- arquivos afetados;
- resultado;
- erro;
- custo, se houver;
- proxima acao.

## Relacoes

- [[10_Dashboard/RAG_MCP_Control_Plane]]
- [[60_Sistemas/Protocolos/Protocolo_Anti_Caos_FabioOS]]
- [[60_Sistemas/Protocolos/Definicao_de_Concluido_FabioOS]]
