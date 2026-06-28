---
tipo: changelog
area: 50_Registros
projeto: FabioOS
status: concluido
tags: [changelog, mcp, codex, rag, grafo, agentes, cursor, hermes]
criado_em: 2026-06-28
atualizado_em: 2026-06-28
---

# Changelog - configuracao MCP FabioOS no Codex

## O que foi feito

- Configurado o servidor MCP `fabioos` no config global local do Codex.
- Validado que o TOML global continua parseavel.
- Validado que o servidor MCP FabioOS importa corretamente.
- Validado que o servidor encontra o vault e o banco RAG local.
- Testadas funcoes internas de busca no vault/wiki.
- Usado RAG local para recuperar contexto sobre Hermes, Cursor e fases.
- Usado Grafo local para localizar nos ligados ao MEGATRON.
- Usado MCP `n8n-docs` para confirmar os nos core relacionados a Gmail.
- Registrado plano de encaixe para subagentes, Cursor, Hermes, RAG, Grafo e MCP.

## Instalado/configurado

- Nenhum token foi usado.
- Nenhuma chave OpenRouter foi necessaria.
- Config local alterado: `C:\Users\user\.codex\config.toml`.
- Exemplo versionavel atualizado: `.codex/config.toml.example`.

## Criado/modificado no vault

- `.codex/config.toml.example`
- `60_Sistemas/FabioOS/Plano_Capacidades_Agentes_Cursor_Hermes_2026-06-28.md`
- `50_Registros/Changelog/2026-06-28_configuracao-mcp-fabioos-codex.md`

## Pendente

- Reiniciar/recarregar Codex para o MCP `fabioos` aparecer como ferramenta nativa.
- Retestar subagentes Codex apos reload.
- Avaliar Hermes apenas depois que houver caso de uso persistente claro.
