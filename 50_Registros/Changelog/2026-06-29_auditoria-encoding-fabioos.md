---
tipo: changelog
area: 50_Registros
projeto: FabioOS
status: registrado
tags: [encoding, utf-8, codex, auditoria, windows]
criado_em: 2026-06-29
agente: Cursor
---

# Changelog — Auditoria encoding FabioOS

## Resumo

Diagnosticados erros de encoding do Codex: causa principal e runtime Windows (cp1252), nao corrupcao massiva do vault. Um arquivo inbox corrigido; `.gitattributes` e script de auditoria criados.

## Entregas

- `50_Registros/Auditoria/Auditoria_Encoding_FabioOS_2026-06-29.md`
- `60_Sistemas/FabioOS/scripts/auditar_encoding_fabioos.py`
- `.gitattributes` (UTF-8 para md/py/ps1/json)
- Correcao `00_Inbox/Triagem/Teste_MCP_Obsidian.md`
- `batch_validate_rag.py` — reconfigure UTF-8

## Limites

- Nenhum commit ou push
- Config real `.codex/config.toml` nao alterada (gitignored)
