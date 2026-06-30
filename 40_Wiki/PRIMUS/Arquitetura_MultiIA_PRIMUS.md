---
tipo: wiki
area: 40_Wiki
projeto: PRIMUS
status: ativo
fonte: [[05_Raw_Sources/PRIMUS/2026-06-30_chatgpt_project_primus_inventario_logs]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, ia, n8n, openclaw, steward, automacao]
---

# Arquitetura MultiIA PRIMUS

## Tese

As IAs do PRIMUS nao devem conversar livremente. Elas devem operar como modulos especializados de um pipeline, com saidas estruturadas e registro permanente.

## Papeis

| Componente | Papel | Limite |
|---|---|---|
| ChatGPT / GPT | cerebro arquitetural, schemas, ontologia, instanciamento | nao arquiva sozinho sem integracao |
| Claude | auditor/editor de contexto longo | nao deve executar runtime sem protocolo |
| Codex | executor documental/codigo local | nao deve liderar se Claude estiver como lead |
| Cursor | engenharia de UI/codigo | nao deve editar governanca sem handoff |
| Gemini | extracao massiva, OCR, multimodal | nao decide canon |
| Perplexity | pesquisa canonica | nao altera ontologia |
| NotebookLM | consulta sobre biblioteca propria | nao e fonte de verdade sem export |
| n8n | esteira de automacao | nao e cerebro |
| OpenClaw | operador/agente por mensagem | precisa de permissoes e logs |
| Drive/GitHub/Obsidian | memoria permanente | nao decide |

## Fluxo Ideal

```text
Fontes
-> extracao
-> normalizacao
-> validacao
-> banco PRIMUS
-> instanciamento
-> DeltaP
-> WorldState
-> Player View / Cantina
```

## Regra de Seguranca

- Agente pode sugerir e preparar.
- Agente so altera Stable com validacao.
- Acao destrutiva exige confirmacao humana.
- Log nunca e apagado.
- Documento mestre nunca e sobrescrito sem changelog.

## Proxima Acao

Formalizar [[80_Specs/PRIMUS/Spec_PRIMUS_Steward]] como camada de governanca executiva do PRIMUS.
