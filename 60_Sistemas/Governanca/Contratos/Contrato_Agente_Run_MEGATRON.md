---
tipo: contrato
area: 60_Sistemas
projeto: FabioOS
status: ativo
responsavel_formato: Claude
criado_em: 2026-06-29
atualizado_em: 2026-06-29
tags: [fabios, megatron, agentes, contrato, run]
---

# Contrato - Agente `run()` MEGATRON

## Funcao

Padronizar a chamada dos agentes funcionais sem obrigar Cursor ou Codex a tocar no codigo do MEGATRON.

Este documento e governanca/documentacao. A implementacao pertence ao Claude.

## Principio

Cada agente deve ter uma casca CLI e uma funcao chamavel:

```python
def run(pedido: dict) -> dict:
    ...
```

O retorno deve ser compativel com [[60_Sistemas/Governanca/Contratos/Contrato_Resultado_MEGATRON]].

## Pedido minimo

```python
Pedido = {
    "id": str,
    "origem": str,
    "intencao": str,
    "conteudo": str,
    "modo": str,        # "dry_run" | "confirmado"
    "permissao": str,   # "read_only" | "propose_only" | "write_draft" | "blocked"
    "contexto": dict,
}
```

## Regras por modo

| Modo | Pode fazer | Nao pode |
|---|---|---|
| `dry_run` | validar, simular, propor artefato | escrever, enviar, apagar |
| `confirmado` | executar escrita segura prevista no contrato | acao externa/sensivel |

## Agentes iniciais

| Agente | Vocacao | Permissao padrao | Saida esperada |
|---|---|---|---|
| SafeCommit | revisar diff/segredos/commit | propose_only | `proposta` ou `bloqueio` |
| Arquivista | transformar bruto em nota | write_draft com confirmacao | `proposta` ou `artefato` |
| Inbox | triagem de entradas | propose_only | `proposta` |
| RAG | consulta semantica com fontes | read_only | `resposta` ou `abstencao` |
| Dashboard | consolidar status | propose_only | `briefing` |

## Invariantes

- `dry_run` e padrao.
- Escrita so pode gerar rascunho, nunca sobrescrever conhecimento canonico sem aprovacao.
- Acao externa deve retornar `bloqueio`.
- Falta de fonte deve retornar `abstencao`, nao resposta inventada.
- Segredo detectado deve retornar `bloqueio`.

## Criterios de aceite

- O agente pode ser chamado por Python sem depender de stdin.
- O CLI continua funcionando como casca fina.
- O retorno tem os campos do contrato `Resultado`.
- Teste golden cobre caso feliz e caso bloqueado.

## Relacoes

- [[60_Sistemas/MEGATRON/agentes/Registro_Agentes]]
- [[60_Sistemas/FabioOS/specs/2026-06-29_megatron-coordenador]]
- [[60_Sistemas/Governanca/Matriz_de_Permissoes_FabioOS]]
