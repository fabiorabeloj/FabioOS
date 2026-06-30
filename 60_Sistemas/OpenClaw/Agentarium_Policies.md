---
tipo: referencia
area: 60_Sistemas
sistema: OpenClaw
projeto: FabioOS
status: ativo
tags: [agentarium, politicas, sandbox, openclaw, seguranca]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
---

# Agentarium — Politicas padrao (FabioOS)

Referencia humana alinhada a **OpenClaw multi-agent sandbox and tools**.

## Pietra

| Campo | Valor |
|---|---|
| Funcao | Atendimento escolar |
| sandboxMode | all |
| workspaceAccess | ro |
| allowedTools | read, sessions_send, sessions_history |
| deniedTools | exec, write, edit, apply_patch, process, browser, gateway |
| elevated | disabled |
| riskLevel | safe |
| agentDir | `~/.openclaw/agents/pietra/agent` |

## Arquivista

| Campo | Valor |
|---|---|
| Funcao | Arquivamento Obsidian |
| sandboxMode | all |
| workspaceAccess | rw |
| allowedTools | read, write, edit |
| deniedTools | exec, process, browser, gateway |
| elevated | disabled |
| riskLevel | warning (filesystem mutation) |
| agentDir | `~/.openclaw/agents/arquivista/agent` |

## Codex

| Campo | Valor |
|---|---|
| Funcao | Programacao / GitHub |
| sandboxMode | all |
| workspaceAccess | rw |
| allowedTools | read, write, edit, apply_patch, exec, process |
| deniedTools | browser, gateway |
| elevated | restricted |
| riskLevel | warning |
| agentDir | `~/.openclaw/agents/codex/agent` |

Se `exec` permitido com `sandboxMode: off` → **danger** automatico.

## Pesquisador

| Campo | Valor |
|---|---|
| Funcao | RAG / pesquisa |
| sandboxMode | all |
| workspaceAccess | ro |
| allowedTools | read, browser |
| deniedTools | exec, write, edit, apply_patch, process |
| elevated | disabled |
| riskLevel | safe |
| agentDir | `~/.openclaw/agents/pesquisador/agent` |

## Supervisor

| Campo | Valor |
|---|---|
| Funcao | Auditoria / aprovacao |
| sandboxMode | off |
| workspaceAccess | ro |
| allowedTools | read, sessions_list, sessions_history, session_status |
| deniedTools | write, edit, apply_patch, exec, process |
| elevated | disabled |
| riskLevel | safe (sem exec/write) |
| agentDir | `~/.openclaw/agents/supervisor/agent` |

## Regras de alerta

1. **agentDir compartilhado** → danger (global)
2. **auth default-fallback** → warning
3. **exec + sandbox off** → danger
4. **process + rw** → warning
5. **write/edit/apply_patch** → warning
6. **elevated enabled** → danger

## Cadeia de filtros de ferramentas

1. Tool profile
2. Provider tool profile
3. Global tool policy
4. Provider tool policy (runtime)
5. Agent-specific tool policy
6. Agent provider policy
7. Sandbox tool policy
8. Subagent tool policy

## Relacoes

- [[60_Sistemas/OpenClaw/Agentarium]]
- [[60_Sistemas/OpenClaw/ponte/MAPA_Agentes_MEGATRON_OpenClaw]]
