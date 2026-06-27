---
tipo: changelog
area: 50_Registros
projeto: FabioOS
status: concluido
tags: [changelog, fabios, skills, agentes, roteamento, governanca]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Roteamento de Capacidades de IA - 2026-06-27

## O que foi feito

- Criado protocolo para usar capacidades ja instaladas antes de improvisar fluxo manual.
- Mapeadas skills, comandos Claude, agentes Claude/Codex, agentes MEGATRON, scripts locais, MCPs, RAG e grafo.
- Registrada a regra operacional: se ja existe capacidade instalada para a tarefa, ela deve ser usada ou a excecao deve ser justificada.
- Registrada lacuna tecnica: tentativa de spawn de subagente Codex falhou por resolucao de modelo.

## Criado/modificado no vault

- `60_Sistemas/FabioOS/Protocolo_Roteamento_Capacidades_IA.md`
- `CLAUDE.md`
- `60_Sistemas/Skills/Inventario_Skills.md`
- `60_Sistemas/FabioOS/Registro_Frentes_Ativas.md`

## Resultado

O FabioOS passa a ter uma camada explicita de roteamento:

```text
pedido -> skill/comando/agente/script/MCP/RAG/Grafo -> execucao manual apenas se necessario
```

## Pendente

- Retestar subagentes Codex em sessao limpa.
- Testar `taste-skill` e `huashu-design` em tarefa real.
- Criar uma skill/comando `route-capability` se o roteamento manual virar repetitivo.

## Proximas acoes

- Usar `security-reviewer` ou `/check-secrets` antes de push.
- Usar `vault-architect` para revisoes estruturais.
- Usar `wiki-curator` e comandos de ingestao para fontes.
- Usar RAG/Grafo antes de respostas sobre conhecimento interno do vault.
