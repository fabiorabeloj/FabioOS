---
tipo: prompt-handoff
area: 60_Sistemas
projeto: FabioOS
status: pronto
tags: [claude, handoff, ias, agentes, mcp, codex]
criado_em: 2026-06-28
atualizado_em: 2026-06-28
---

# Prompt para Claude - Orquestracao de IAs e Agentes

Cole no Claude quando ele retornar:

```text
Leia o contexto do FabioOS e continue a partir do ultimo changelog.

Antes de agir, leia:
- CLAUDE.md
- 60_Sistemas/FabioOS/Registro_Frentes_Ativas.md
- 60_Sistemas/FabioOS/Quadro_Comando_IAs_Agentes_2026-06-28.md
- 60_Sistemas/FabioOS/Plano_Capacidades_Agentes_Cursor_Hermes_2026-06-28.md
- 60_Sistemas/FabioOS/Politica_Codex_Config_Local_vs_Vault_2026-06-28.md
- 60_Sistemas/MCP_FabioOS/README_MCP_FabioOS.md

Estado deixado pelo Codex:
- MCP FabioOS foi configurado no config global local do Codex como servidor `fabioos`.
- O exemplo versionavel `.codex/config.toml.example` foi atualizado sem segredos.
- RAG local e Grafo local foram usados com sucesso em modo read-only.
- Subagente Codex `explorer` funcionou; tentativa paralela de `security-reviewer` falhou por resolucao de modelo.
- Cursor esta instalado e deve ser tratado como oficina de desenvolvimento.
- Hermes esta instalado, mas nao integrado; nao usar como agente autonomo sem descobrir CLI/API e escopo.
- OpenRouter nao e necessario para MCP FabioOS v0; usar apenas com variavel local e teto de custo.
- Gmail/n8n: MCP n8n-docs confirmou os nodes core `Gmail`, `Gmail Tool` e `Gmail Trigger`.

Sua tarefa:
1. Revisar o quadro de comando das IAs.
2. Decidir quais frentes ficam com Claude, Codex, n8n, OpenClaw, Cursor e Hermes.
3. Retestar MCP FabioOS nativo se estiver disponivel.
4. Retestar subagentes.
5. Preparar a frente Google/n8n em modo dry-run, sem envio externo e sem ler e-mail em massa.

Regras:
- Nao fazer push sem OK do Fabio.
- Nao reindexar RAG sem lock.
- Nao usar Hermes/OpenClaw para acoes externas sem aprovacao.
- Nao copiar tokens ou config real para o vault.
```
