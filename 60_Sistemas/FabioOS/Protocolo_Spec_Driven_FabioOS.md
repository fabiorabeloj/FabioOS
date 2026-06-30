---
tipo: protocolo
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, spec-driven, desenvolvimento, governanca, megatron]
criado_em: 2026-06-28
atualizado_em: 2026-06-28
---

# Protocolo Spec-Driven FabioOS

## Funcao

Transformar ideias, ferramentas, fases futuras e automacoes em especificacoes antes de qualquer implementacao relevante.

O FabioOS passa a tratar desenvolvimento como:

```text
SPEC -> plano -> tarefas -> implementacao -> testes -> changelog -> dashboard
```

## Quando usar

Criar SPEC antes de:

- implementar fase nova;
- instalar ferramenta relevante;
- criar agente;
- alterar RAG/Grafo/MCP/n8n/OpenClaw;
- expor dados a servico externo;
- criar dashboard visual;
- mexer em deploy, custos, permissao ou automacao sensivel.

## Quando nao precisa

Nao exige SPEC completa:

- correcao pequena de texto;
- ajuste simples em link;
- commit de changelog;
- leitura ou auditoria read-only;
- script auxiliar descartavel sem efeito permanente.

## Estrutura minima da SPEC

Toda SPEC deve responder:

1. qual problema resolve;
2. qual objetivo;
3. o que esta fora de escopo;
4. que dominio/dados/permissoes envolve;
5. arquitetura proposta;
6. plano de tarefas;
7. criterio de aceite;
8. testes minimos;
9. riscos;
10. rollback;
11. changelog esperado.

## Gates obrigatorios

| Gate | Pergunta |
|---|---|
| Dominio | Qual dominio do FabioOS e afetado? |
| Dados | Que tipo de dado entra ou sai? |
| Permissao | Precisa de aprovacao humana? |
| Custo | Usa API, assinatura, cloud ou recurso caro? |
| Logs | Como a execucao sera registrada? |
| Teste | Como provar que funcionou? |
| Rollback | Como desligar ou reverter? |

## Papel das IAs

Antes de escolher a IA/ferramenta para uma SPEC, consultar [[90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Repertorio/IA/Modelos_e_IAs/Matriz_de_Aptidao_das_IAs_FabioOS]].

Se a SPEC criar, alterar ou consultar conhecimento persistente, consultar tambem [[30_Projetos/FabioOS/LLM_Wiki_FabioOS]], `10_Dashboard/_entrada/index.md`, `50_Registros/Logs_Agentes/log.md` e [[60_Sistemas/Wiki/Schema_Wiki_FabioOS]].

| Agente/IA | Papel |
|---|---|
| Fabio | Decide prioridade e aprova riscos |
| MEGATRON | Roteia capacidade, contexto e dominio |
| Claude | Arquitetura, revisao e lideranca estrutural |
| Codex | Implementacao local, testes e verificacao |
| Cursor | Oficina para software maior e interface |
| n8n/OpenClaw | Execucao externa somente com logs e aprovacao |

## Implementacao v0

Script:

`60_Sistemas/FabioOS/scripts/gerar_spec_fabioos.py`

Template:

`60_Sistemas/FabioOS/templates/Template_SPEC_FabioOS.md`

Saida padrao:

`60_Sistemas/FabioOS/specs/`

## Regra

Se uma tarefa parecer grande, cara, sensivel, externa ou irreversivel, ela deve virar SPEC antes de virar codigo.
