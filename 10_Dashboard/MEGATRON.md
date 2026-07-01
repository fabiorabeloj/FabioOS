---
tipo: dashboard
area: 10_Dashboard
projeto: MEGATRON
status: ativo
tags: [fabios, megatron, dashboard, agentes]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# MEGATRON

Painel da interface/orquestrador unico do FabioOS.

## Documentos principais

- [[60_Sistemas/FabioOS/Protocolo_Retomada_Ambiente_FabioOS]]
- [[60_Sistemas/FabioOS/specs/2026-06-29_megatron-v1-ignorancia-explicita]]
- [[60_Sistemas/MEGATRON/agentes/README_Agentes]]
- [[60_Sistemas/MEGATRON/v0/README_MEGATRON_v0]]
- [[30_Projetos/MEGATRON/README]]

## Ligar o cockpit (Windows)

```powershell
.\MEGATRON.cmd
# ou
.\start_megatron.ps1
```

Atalho: `MEGATRON.lnk` na Area de Trabalho (`60_Sistemas/Scripts/install_megatron_shortcut.ps1`).

Config local: copie `megatron.env.example` para `megatron.local.env`.

Health rapido: `60_Sistemas/Scripts/megatron_health.ps1`

Estado runtime: `60_Sistemas/MEGATRON/v1/state/megatron_runtime.json`

Roadmap: `MEGATRON.cmd` -> `MEGATRON.exe` (binario unico).

Spec: [[60_Sistemas/FabioOS/specs/2026-06-29_MEGATRON_Orchestrator_v1.0]]

## Regras

- responder com fontes quando houver memoria;
- assumir ignorancia quando nao houver evidencia;
- propor antes de agir;
- nao executar acao externa sem aprovacao.
