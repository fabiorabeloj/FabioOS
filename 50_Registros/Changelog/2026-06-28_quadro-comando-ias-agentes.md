---
tipo: changelog
area: 50_Registros
projeto: FabioOS
status: concluido
tags: [changelog, ias, agentes, subagentes, mcp, rag, grafo]
criado_em: 2026-06-28
atualizado_em: 2026-06-28
---

# Changelog - quadro de comando de IAs e agentes

## O que foi feito

- Inventariadas as IAs, agentes, subagentes, skills, MCPs e conectores disponiveis.
- Acionado subagente `explorer` em modo read-only para auditar papeis e riscos.
- Usado RAG local para recuperar contexto sobre Cursor, Hermes, OpenClaw e papeis.
- Usado MCP n8n-docs para confirmar os nos core de Gmail no n8n.
- Criado quadro de comando operacional das IAs do FabioOS.
- Criado prompt de handoff para Claude retomar a orquestracao sem colisao.

## Resultado

- Codex: acionavel agora como executor interino.
- Claude: lider estrutural, via handoff.
- RAG/Grafo: acionaveis agora e devem ser usados antes de responder sobre FabioOS.
- MCP FabioOS: configurado, nativo apos reload.
- Cursor: oficina de desenvolvimento.
- Hermes: instalado, nao integrado.
- OpenClaw: gateway externo, ainda cauteloso.
- Gmail/Drive/n8n: usar por conectores e nodes oficiais, com escopo e aprovacao.

## Pendente

- Recarregar Codex para testar MCP FabioOS nativo.
- Retestar subagentes em nova sessao.
- Iniciar frente Google/n8n em modo dry-run.
