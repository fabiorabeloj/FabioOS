---
tipo: politica-operacional
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, codex, configuracao, seguranca, vault, mcp]
criado_em: 2026-06-28
atualizado_em: 2026-06-28
---

# Politica Codex - Vault vs Config Local

## Decisao

O FabioOS deve ser a fonte de verdade para tudo que e estrutural, versionavel e reaproveitavel do Codex.

O diretorio global `C:\Users\user\.codex` deve continuar existindo apenas como runtime local do aplicativo Codex.

## O que fica dentro do vault FabioOS

Dentro de `C:\Users\user\Desktop\FabioOs\FabioOs` devem ficar:

- `.codex/config.toml.example`;
- `.codex/agents/*.toml`;
- `.agents/skills/`;
- documentacao de MCPs, agentes, protocolos e capacidades;
- changelogs;
- planos de configuracao;
- templates de config sem segredo;
- scripts versionaveis do FabioOS.

Motivo: isso e conhecimento do projeto, precisa ser auditavel, versionavel, recuperavel e visivel no Obsidian/Git.

## O que nao deve ir para o vault

Nao mover nem versionar:

- `C:\Users\user\.codex\auth.json`;
- bancos sqlite do Codex;
- logs internos do app;
- caches;
- anexos temporarios;
- estado de sessoes;
- tokens;
- credenciais;
- arquivos com `Authorization`, `Bearer`, API keys ou senhas reais.

Motivo: isso e estado local, sensivel, grande ou descartavel. Versionar isso aumenta risco e polui o FabioOS.

## Regra pratica

Se uma configuracao ajuda outro agente a reconstruir o ambiente, ela deve existir no vault como exemplo ou protocolo.

Se uma configuracao autentica uma conta, guarda estado do app ou contem segredo, ela fica fora do Git e fora do vault versionado.

## Config MCP FabioOS

O MCP `fabioos` foi registrado no config global local:

`C:\Users\user\.codex\config.toml`

O espelho versionavel fica em:

`.codex/config.toml.example`

Essa e a forma correta: o Codex le o arquivo global, mas o FabioOS guarda o molde auditavel.

## Politica de sincronizacao

Ao alterar o config global do Codex:

1. Nao imprimir valores sensiveis.
2. Atualizar apenas o `.example` dentro do vault.
3. Registrar changelog.
4. Rodar scan de segredos antes de commit.
5. Nunca copiar `auth.json`, sqlite, logs ou caches para dentro do repositorio.

## Proxima melhoria

Criar futuramente um script auxiliar seguro que valide se o config global possui os servidores MCP esperados sem copiar segredos para o vault.
