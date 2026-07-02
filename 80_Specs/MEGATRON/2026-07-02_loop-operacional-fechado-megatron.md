---
tipo: spec
area: 80_Specs
projeto: MEGATRON
status: especificado
classe_dado: interno
criado_em: 2026-07-02
atualizado_em: 2026-07-02
tags: [megatron, intake, agentarium, obsidian, loop-operacional]
---

# SPEC - Loop Operacional Fechado do MEGATRON

## Objetivo

Provar que o [[10_Dashboard/MEGATRON|MEGATRON]] executa uma tarefa pequena de ponta a ponta:

```text
comando -> Universal Intake -> Mesa de Despacho -> aprovacao -> Arquivista -> Obsidian -> log -> painel
```

## Contexto

Relatorios existentes indicam que a espinha cognitiva ja funciona, mas o valor do sistema depende do ciclo fechado:

- [[50_Registros/Relatorios/Diagnostico_Operacional_Intake_Universal_2026-07-01_Claude]]
- [[50_Registros/Relatorios/Contrato_Mesa_Despacho_Intake_Codex_2026-07-01]]
- [[50_Registros/Relatorios/Bugbot_Mesa_Despacho_Intake_v0.9.0_Cursor]]

## Entrada de teste

```text
Criar tarefa ficticia: preparar prova do 8o ano sobre Africa para amanha.
```

## Saida esperada

- Card criado no [[60_Sistemas/FabioOS/schemas/universal_intake_schema|Universal Intake]].
- Card visivel na [[50_Registros/Relatorios/Bugbot_Mesa_Despacho_Intake_v0.9.0_Cursor|Mesa de Despacho]].
- Botao ou comando de aprovacao muda estado.
- [[60_Sistemas/Agentes/Arquivista_FabioOS|Arquivista]] grava nota em `00_Inbox/Triagem/` ou area definida.
- Log registra origem, aprovador, agente e caminho da nota.
- [[60_Sistemas/OpenClaw/Agentarium|Agentarium]] exibe estado final.

## Fora de escopo

- Envio externo.
- WhatsApp real.
- E-mail real.
- Chamada paga de API.
- RAG reindex.
- Alteracao de tokens.
- Push.

## Criterios de aceite

- [ ] Comando gera card valido.
- [ ] Validador do intake passa.
- [ ] Card aparece em fila de aprovacao.
- [ ] Aprovacao gera nota Markdown.
- [ ] Nota possui frontmatter e wikilinks minimos.
- [ ] Log aponta para a nota.
- [ ] Painel mostra `done` ou equivalente.
- [ ] Rejeicao tambem funciona e nao gera nota.

## Gargalos resolvidos

- [[40_Wiki/FabioOS/Gargalos_Sistemicos_FabioOS_MEGATRON|Loop operacional fechado]]
- [[50_Registros/Relatorios/Bugbot_Mesa_Despacho_Intake_v0.9.0_Cursor|Aprovacao humana]]
- [[60_Sistemas/Agentes/Arquivista_FabioOS|Escrita em memoria]]
- [[60_Sistemas/OpenClaw/Agentarium|Observabilidade real]]

## Proxima implementacao recomendada

1. Rodar o smoke test existente da Mesa de Despacho.
2. Confirmar se a nota aprovada aparece no Obsidian.
3. Confirmar se o Agentarium mostra o card final.
4. Registrar relatorio de evidencia em `50_Registros/Relatorios/`.
5. So depois conectar OpenClaw, n8n, Gmail ou WhatsApp real.

## Relacoes

- [[40_Wiki/FabioOS/Gargalos_Sistemicos_FabioOS_MEGATRON]]
- [[60_Sistemas/Obsidian/Protocolo_Revisao_Links_Nos_Obsidian]]
- [[10_Dashboard/MEGATRON]]
- [[10_Dashboard/Governanca_FabioOS]]
