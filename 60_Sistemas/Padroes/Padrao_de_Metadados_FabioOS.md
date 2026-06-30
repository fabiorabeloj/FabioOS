---
tipo: padrao
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [metadados, frontmatter, obsidian, dataview, governanca]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Padrao de Metadados FabioOS

## Funcao

Padronizar frontmatter YAML para que Obsidian, Dataview, RAG, Grafo e agentes consigam classificar e recuperar conhecimento.

## Frontmatter base

```yaml
---
tipo:
area:
projeto: FabioOS
status:
tags: []
criado_em: YYYY-MM-DD
atualizado_em: YYYY-MM-DD
---
```

## Tipos controlados

| Tipo | Uso |
|---|---|
| fonte | material bruto preservado |
| wiki | conhecimento processado |
| decisao | decisao operacional ou arquitetural |
| adr | decisao em formato ADR |
| protocolo | regra de operacao |
| matriz | tabela normativa |
| contrato | contrato de agente |
| spec | especificacao |
| changelog | registro de mudanca |
| status | estado operacional |
| dashboard | painel de controle |
| auditoria | revisao ou relatorio |

## Status controlados

| Status | Significado |
|---|---|
| rascunho | incompleto |
| ativo | valido e em uso |
| aprovado | decisao aceita |
| piloto | testado em pequeno escopo |
| operacional | usado com confianca |
| revisar | exige revisao |
| superseded | substituido |
| arquivado | preservado, sem uso ativo |

## Prioridade

| Valor | Uso |
|---|---|
| P1 | risco alto ou bloqueio |
| P2 | importante, nao bloqueante |
| P3 | melhoria |
| P4 | referencia |

## Exemplo obrigatorio

```yaml
---
tipo: decisao
area: FabioOS
status: aprovada
data: 2026-06-29
origem: chatgpt
relacionado:
  - MEGATRON
  - Arquitetura Cognitiva Distribuida
---
```

## Regras

- Toda nota estrutural deve ter frontmatter.
- Datas usam `YYYY-MM-DD`.
- Tags devem ajudar busca, nao enfeitar.
- Se o status for `superseded`, apontar substituto.
- Dados sensiveis exigem campo `sensibilidade`.

## Relacoes

- [[60_Sistemas/Wiki/Schema_Wiki_FabioOS]]
- [[60_Sistemas/Memoria/Separacao_de_Memorias_FabioOS]]
- [[60_Sistemas/FabioOS/Matriz_Dominios_Dados_Permissoes_2026-06-28]]
