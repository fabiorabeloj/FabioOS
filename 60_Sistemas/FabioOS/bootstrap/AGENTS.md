# AGENTS.md — FabioOS

> **Ponteiro.** As regras de operação do FabioOS são únicas e vivem em **[`CLAUDE.md`](CLAUDE.md)**.
> Este arquivo existe porque o Codex (e outros agentes que seguem o padrão `AGENTS.md`) procuram por ele.
> **Não duplicar regras aqui** — para evitar divergência, há uma só fonte de verdade.

## Para qualquer agente (Codex, Claude, etc.)

1. **Leia `CLAUDE.md`** — é o documento canônico de regras, estrutura, segurança e leitura obrigatória de início de sessão.
2. Onde o `CLAUDE.md` disser "Claude", aplique as mesmas regras a si mesmo (ex.: o Codex assume os mesmos papéis: arquiteto, organizador do vault, revisor antes de commits).
3. Siga a **leitura obrigatória** listada no `CLAUDE.md`, incluindo o modelo formal em [`00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON.md`](00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON.md), que governa o sistema no nível conceitual.

**Frase padrão de início de sessão:** `Leia o contexto do FabioOS e continue a partir do último changelog.`

## Configuração específica do Codex

- `.codex/config.toml` — configuração do Codex neste repositório.
- `.codex/agents/*.toml` — definições dos agentes para o Codex (espelham `.claude/agents/`).
- `.agents/skills/` — espelho dos comandos do FabioOS no formato de skills do Codex.
