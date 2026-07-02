---
tipo: wiki
area: 40_Wiki
projeto: FabioOS
status: sprout
classe_dado: interno
aliases: [PietraOS, Sistema Pietra, Atendimento Pietra]
criado_em: 2026-07-02
atualizado_em: 2026-07-02
tags: [pietraos, escolaos, atendimento, whatsapp, governanca]
---

# PietraOS

## Definicao

PietraOS e o dominio institucional/escolar do [[10_Dashboard/FabioOS|FabioOS]].

Ele organiza atendimento, mensagens, classificacao, aprovacao humana e processos ligados ao Colegio Pietra.

## Nota canonica

- [[60_Sistemas/Pietra/Sistema_Pietra]]

## Papel no MEGATRON

PietraOS nao deve enviar mensagens externas sozinho. Ele recebe eventos de canais como [[60_Sistemas/n8n/README|n8n]], [[60_Sistemas/OpenClaw/OpenClaw|OpenClaw]] ou Evolution API, classifica a situacao e prepara rascunhos para aprovacao.

## Relacoes

- [[10_Dashboard/Governanca_FabioOS]]
- [[60_Sistemas/OpenClaw/Sistema_OpenClaw]]
- [[60_Sistemas/n8n/README]]
- [[40_Wiki/FabioOS/Gargalos_Sistemicos_FabioOS_MEGATRON]]
