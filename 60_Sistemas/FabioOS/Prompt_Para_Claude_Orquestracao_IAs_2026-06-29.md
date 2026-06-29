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
- 90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Repertorio/IA/Modelos_e_IAs/Matriz_de_Aptidao_das_IAs_FabioOS.md
- 30_Projetos/FabioOS/LLM_Wiki_FabioOS.md
- index.md
- log.md
- 60_Sistemas/Wiki/Schema_Wiki_FabioOS.md
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
2. Aplicar a Matriz de Aptidao antes de decidir quais frentes ficam com Claude, Codex, n8n, OpenClaw, Cursor, Hermes ou modelos via OpenRouter.
3. Aplicar a LLM Wiki operacional antes de criar novas notas, fontes, specs, skills ou protocolos.
4. Retestar MCP FabioOS nativo se estiver disponivel.
5. Retestar subagentes.
6. Preparar a frente Google/n8n em modo dry-run, sem envio externo e sem ler e-mail em massa.

Regras:
- Nao fazer push sem OK do Fabio.
- Nao reindexar RAG sem lock.
- Nao usar Hermes/OpenClaw para acoes externas sem aprovacao.
- Nao copiar tokens ou config real para o vault.
```
