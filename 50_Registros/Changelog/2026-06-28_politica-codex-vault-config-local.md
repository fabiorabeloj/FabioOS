---
tipo: changelog
area: 50_Registros
projeto: FabioOS
status: concluido
tags: [changelog, codex, configuracao, seguranca, vault]
criado_em: 2026-06-28
atualizado_em: 2026-06-28
---

# Changelog - politica Codex vault vs config local

## O que foi feito

- Registrada a decisao de manter o FabioOS como fonte de verdade para configuracoes versionaveis do Codex.
- Definido que o diretorio global `C:\Users\user\.codex` continua sendo runtime local do app.
- Separado o que deve ir para o vault do que deve ficar fora por seguranca.
- Reforcada a regra de nao versionar tokens, auth, sqlite, logs, caches ou estado de sessoes.

## Criado/modificado no vault

- `60_Sistemas/FabioOS/Politica_Codex_Config_Local_vs_Vault_2026-06-28.md`
- `50_Registros/Changelog/2026-06-28_politica-codex-vault-config-local.md`

## Pendente

- Criar futuramente um validador seguro de config Codex que confira MCPs esperados sem copiar segredos.
