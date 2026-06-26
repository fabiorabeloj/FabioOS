---
tipo: registro
area: 60_Sistemas
projeto: FabioOS
sistema: MEGATRON
status: ativo
tags: [megatron, agentes, registro, inventario]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Registro de Agentes MEGATRON

## Função

Inventário oficial dos agentes especificados para MEGATRON. Este registro indica prioridade, estado, domínio, permissões, dependências e próxima ação.

## Registro inicial

| Agente | Prioridade | Domínio | Estado | Permissão máxima | Dependências | Próxima ação |
|---|---:|---|---|---|---|---|
| SafeCommit | 1 | FabioOS | especificado | escrita segura + commit aprovado | Git, `/check-secrets`, `/session-changelog`, `/safe-commit` | Criar agente `.claude/agents/safe-commit.md` ou comando orquestrador |
| Arquivista | 2 | FabioOS | especificado | escrita segura em notas | `sources/`, `wiki/`, `/archive-source`, `/source-to-wiki` | Testar com uma entrada real de `00_Inbox/` |
| Inbox | 3 | FabioOS | especificado | leitura + roteamento + escrita de tarefa | `00_Inbox/`, `sources/_inbox/`, Arquivista, Pietra, RAG | Criar rotina manual de triagem |
| RAG | 4 | FabioOS | especificado | indexação local + consulta | Chroma, embeddings locais, `60_Sistemas/RAG/` | Validar ingestão da primeira leva |
| Dashboard | 5 | FabioOS | especificado | leitura + escrita de painel | Registro_Agentes, Painel de Pendências, changelogs, logs | Criar painel textual mínimo |

## Estado de implementação (2026-06-26)

> Existe **implementação mínima criada e testada** dos 5 agentes em `implementacao/claude/` (executados uma vez com sucesso; RAG aguarda deps da Fase 12). **Os agentes NÃO foram promovidos a `piloto`** — ainda falta **revisão humana do código** antes de qualquer promoção de estado. O estado oficial permanece `especificado`.

## Matriz de dependências

```text
SafeCommit
  └─ independente; protege todas as demais entregas

Arquivista
  └─ depende de fontes e schemas existentes

Inbox
  ├─ depende de Arquivista para transformação
  └─ encaminha casos para Pietra, Escola, RAG ou humano

RAG
  ├─ depende de wiki/ e 60_Sistemas/ organizados
  └─ alimenta MEGATRON, Dashboard e futuros agentes

Dashboard
  ├─ depende de logs dos agentes
  └─ consolida pendências, status e alertas
```

## Regras de promoção de estado

| De | Para | Exigência |
|---|---|---|
| especificado | rascunho-implementacao | Spec aprovada e caminho técnico definido |
| rascunho-implementacao | piloto | Execução manual documentada |
| piloto | operacional | 3 execuções reais com logs aceitáveis |
| operacional | automatizado | Gatilho definido, limites claros e aprovação humana quando sensível |

## Pendências de registro

- [ ] Criar IDs estáveis para agentes (`agent.safecommit`, `agent.arquivista`, etc.).
- [ ] Criar formato padrão de log em `50_Registros/Agentes/`.
- [ ] Decidir quando cada spec deve virar `.claude/agents/*.md`.
- [ ] Decidir quais agentes terão workflow n8n no futuro.

## Relações

- [[60_Sistemas/MEGATRON/agentes/README_Agentes]]
- [[60_Sistemas/MEGATRON/agentes/templates/Template_Agente]]
- [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]]
