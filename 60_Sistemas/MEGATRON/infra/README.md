---
tipo: sistema
area: 60_Sistemas
projeto: MEGATRON
status: ativo
tags: [fabios, megatron, infraestrutura, hardware, nos, distribuido]
criado_em: 2026-07-02
atualizado_em: 2026-07-02
---

# Infraestrutura MEGATRON

## Funcao

Esta pasta define o MEGATRON como infraestrutura distribuida, nao como um unico computador.

O objetivo e permitir que o FabioOS evolua de uma maquina local para um conjunto de nos:

- Core;
- GPU;
- NAS;
- workers;
- interfaces;
- automacoes;
- memoria.

## Arquivos

| Arquivo | Funcao |
|---|---|
| [[60_Sistemas/MEGATRON/infra/Arquitetura_Hardware_MEGATRON_FabioOS_v1]] | arquitetura fisica e logica do MEGATRON |
| [[60_Sistemas/MEGATRON/infra/Roadmap_Hardware_Software_MEGATRON]] | fases de expansao de hardware e software |
| `nodes.megatron.example.json` | registro configuravel de nos e capacidades |
| `node_registry.schema.json` | schema minimo do registro de nos |
| `node_registry.py` | utilitario local para validar, listar e rotear capacidades por no |
| `docker-compose.megatron.example.yml` | exemplo de perfis Docker por camada, sem segredos |

## Como usar

Validar o registro de nos:

```powershell
python 60_Sistemas/MEGATRON/infra/node_registry.py validate
```

Listar nos:

```powershell
python 60_Sistemas/MEGATRON/infra/node_registry.py list
```

Roteamento por capacidade:

```powershell
python 60_Sistemas/MEGATRON/infra/node_registry.py route --capability vector_search
python 60_Sistemas/MEGATRON/infra/node_registry.py route --capability local_llm_inference
```

## Regra

Codigo do MEGATRON nao deve depender de um modelo especifico de hardware.

O hardware entra como capacidade declarada:

```text
capacidade -> no elegivel -> servico -> politica de permissao
```

Nao como:

```text
if maquina == AOOSTAR
```
