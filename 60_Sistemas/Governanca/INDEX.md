---
tipo: indice
area: 60_Sistemas
projeto: FabioOS
status: ativo
criado_em: 2026-06-29
atualizado_em: 2026-06-29
tags: [fabios, governanca, contratos, protocolos, megatron]
---

# Governanca FabioOS

## Funcao

Centralizar contratos, permissoes, locks e regras operacionais que impedem o FabioOS de virar acumulacao caotica de ferramentas.

## Camadas

1. Constituicao e modelo formal.
2. Matriz de permissoes.
3. Contratos de agentes e resultados.
4. Locks e frentes ativas.
5. Auditoria, changelog e handoffs.

## Documentos centrais

| Documento | Funcao |
|---|---|
| [[50_Registros/Decisoes/Constituicao_Operacional_FabioOS]] | Constituicao operacional |
| [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]] | Modelo formal do FabioOS/MEGATRON |
| [[60_Sistemas/Governanca/Matriz_de_Permissoes_FabioOS]] | Permissoes por ator/ferramenta |
| [[60_Sistemas/Governanca/Contratos/Contrato_Resultado_MEGATRON]] | Contrato congelado de saida do orquestrador |
| [[60_Sistemas/Governanca/Contratos/Contrato_Agente_Run_MEGATRON]] | Padrao documental para agentes `run()` |
| [[60_Sistemas/Governanca/Contratos/Handoff_Paralelo_MEGATRON_Claude_Cursor_Codex_2026-06-29]] | Divisao de zonas do sprint paralelo |

## Regra de ouro

Ferramenta nenhuma entra no FabioOS so por existir.

Ela precisa ter:

- vocacao clara;
- permissao clara;
- contrato claro;
- teste minimo;
- criterio de permanencia;
- registro no vault.

## Relacoes

- [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]]
- [[60_Sistemas/FabioOS/Ordens_Coordenacao_Paralela_MEGATRON_2026-06-29]]
- [[60_Sistemas/FabioOS/specs/2026-06-29_megatron-coordenador]]
- [[60_Sistemas/MEGATRON/agentes/Registro_Agentes]]
