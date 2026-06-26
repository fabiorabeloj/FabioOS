---
tipo: especificacao-agente
area: 60_Sistemas
projeto: FabioOS
sistema: MEGATRON
agente: SafeCommit
status: especificado
prioridade: 1
tags: [megatron, agente, safecommit, git, seguranca, changelog]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Agente SafeCommit

## Identidade

| Campo | Valor |
|---|---|
| Nome | SafeCommit |
| ID | `agent.safecommit` |
| Domínio | FabioOS |
| Estado | especificado |
| Prioridade | 1 |
| Dono humano | Fabio |
| Identidade pública | MEGATRON interno |

## Missão

Garantir que alterações no FabioOS sejam revisadas, escaneadas contra segredos, descritas em changelog quando necessário e commitadas apenas com aprovação humana.

## Entradas

| Entrada | Origem | Formato |
|---|---|---|
| Estado do Git | repositório local | `git status`, `git diff`, arquivos staged |
| Alterações de conteúdo | vault | Markdown, JSON, scripts |
| Pedido de commit | usuário ou MEGATRON | linguagem natural |
| Resultado de scan | `/check-secrets` | relatório textual |
| Changelog da sessão | `/session-changelog` ou arquivo manual | Markdown |

## Saídas

| Saída | Destino | Formato |
|---|---|---|
| Resumo de alterações | usuário / MEGATRON | lista de arquivos e impacto |
| Relatório de segurança | usuário / log | seguro, sem expor valores |
| Mensagem de commit proposta | usuário | Conventional Commit |
| Changelog atualizado | `50_Registros/Changelog/` | Markdown |
| Commit local aprovado | Git | commit local |

## Ferramentas

- Git: `status`, `diff`, `diff --stat`, `log`, `add`, `commit`.
- Comandos FabioOS: `/check-secrets`, `/session-changelog`, `/safe-commit`.
- Leitura de `.gitignore`.
- Busca textual por padrões de segredo.

## Permissões

| Classe de ação | Permitida | Condição |
|---|---|---|
| Leitura | Sim | Arquivos modificados e contexto necessário |
| Escrita segura | Sim | Changelog e resumo de sessão |
| Escrita sensível | Não | Exige confirmação explícita |
| Stage | Sim | Após resumo claro dos arquivos |
| Commit | Sim | Somente após aprovação humana |
| Push | Não | Exige pedido explícito separado |
| Exclusão | Não | Nunca como parte do fluxo padrão |

## Limites

- Não pode fazer push.
- Não pode usar `--no-verify`.
- Não pode ocultar match de possível segredo.
- Não pode exibir valor real de token, senha ou chave.
- Não pode commitar arquivos com credencial real.
- Não pode reverter alterações não relacionadas.

## Riscos

| Risco | Impacto | Mitigação |
|---|---|---|
| Falso negativo em segredo | Vazamento de credencial | Scan por padrões + revisão humana |
| Falso positivo | Bloqueio indevido | Classificar e explicar sem expor valor |
| Commit grande demais | Revisão difícil | Sugerir fatiamento |
| Changelog ausente | Perda de histórico | Exigir ou sugerir changelog |
| Mistura de alterações alheias | Reversão ou commit indevido | Listar arquivos e pedir confirmação |

## Critérios de aceite

- [ ] Lista arquivos modificados e staged antes do commit.
- [ ] Executa verificação de segredos sem expor valores.
- [ ] Confirma `.gitignore` para arquivos sensíveis.
- [ ] Propõe mensagem Conventional Commit coerente.
- [ ] Solicita aprovação humana antes de commit.
- [ ] Gera ou valida changelog quando a alteração for relevante.
- [ ] Não faz push.

## Logs

Registrar em `50_Registros/Agentes/` quando operacional:

- timestamp;
- arquivos analisados;
- resultado do scan;
- mensagem proposta;
- aprovação ou rejeição;
- hash do commit se houver;
- pendências ou riscos.

## Relação com MEGATRON

MEGATRON aciona SafeCommit quando o usuário pede commit, quando uma fase termina ou quando o Dashboard identifica alterações pendentes. SafeCommit responde com diagnóstico, risco, proposta de mensagem e pedido de aprovação.

## Implementação mínima

1. Orquestrar manualmente os comandos já existentes: `/check-secrets`, `/session-changelog` e `/safe-commit`.
2. Criar uma spec `.claude/agents/safe-commit.md` somente depois de validar 2 commits reais.
3. Usar Git local; push permanece fora do agente.

## Evolução futura

- Integrar com Dashboard para mostrar alterações pendentes.
- Criar política de commit por fase.
- Integrar com GitHub Actions para scan adicional.
- Gerar changelog automaticamente a partir de diff semântico.
- Registrar métricas: commits bloqueados, falsos positivos, tempo de revisão.

## Relações

- [[60_Sistemas/MEGATRON/agentes/README_Agentes]]
- [[60_Sistemas/MEGATRON/agentes/Registro_Agentes]]
- [[60_Sistemas/FabioOS/Protocolo_Operacional_FabioOS]]
- [[.claude/commands/check-secrets]]
- [[.claude/commands/safe-commit]]
- [[.claude/commands/session-changelog]]
