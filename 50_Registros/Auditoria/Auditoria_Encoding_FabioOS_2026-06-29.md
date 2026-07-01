---
tipo: auditoria
area: 50_Registros
projeto: FabioOS
status: ativo
tags: [encoding, utf-8, codex, windows, cp1252, auditoria, obsidian]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
agente: Cursor
---

# Auditoria de Encoding — FabioOS 2026-06-29

## Funcao

Diagnosticar erros de encoding reportados pelo Codex no Windows: distinguir **corrupcao de arquivos** de **falha de runtime** (console Python cp1252 vs UTF-8).

## Contexto

No Windows, Python usa frequentemente `cp1252` em stdout/stderr. Scripts FabioOS que imprimem emoji ou acentos podem gerar `UnicodeEncodeError` se nao reconfigurarem UTF-8 ou se `PYTHONIOENCODING=utf-8` nao estiver definido.

O Codex executa muitos scripts via shell; erros repetidos costumam ser de **runtime**, nao de vault inteiro corrompido.

## Hipoteses testadas

| ID | Hipotese | Resultado |
|---|---|---|
| H1 | Python padrao (cp1252) quebra ao imprimir emoji | **CONFIRMADA** — `UnicodeEncodeError` sem `PYTHONIOENCODING` |
| H2 | Vault com arquivos UTF-8 invalidos ou U+FFFD | **PARCIAL** — 1 arquivo corrigido; resto valido |
| H3 | `query_rag.py` falha por emoji no print | **REJEITADA** — script ja faz `reconfigure(utf-8)` |
| H4 | Falta `.gitattributes` forçando UTF-8 | **CONFIRMADA** — criado `.gitattributes` na raiz |
| H5 | Codex MCP sem `PYTHONIOENCODING` | **MITIGADA** — `.codex/config.toml.example` ja define para MCP fabioos |

## Evidencia runtime (H1)

```
sys.stdout.encoding = cp1252
UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f50d'
```

## Evidencia vault (H2)

Scan excluindo plugins (`.claude`, `.codex`):

| Tipo | Quantidade |
|---|---|
| Arquivos UTF-8 invalidos | 0 (vault principal) |
| Arquivos com U+FFFD (substituicao) | 1 — corrigido |

**Arquivo corrigido:** `00_Inbox/Triagem/Teste_MCP_Obsidian.md` — `integração`, `Criação`, `Conclusão` estavam corrompidos (MCP Obsidian / cp1252).

## Mitigacoes aplicadas

1. **`.gitattributes`** — `*.md`, `*.py`, `*.ps1`, `*.json` como `text utf-8`.
2. **Script de auditoria:** `60_Sistemas/FabioOS/scripts/auditar_encoding_fabioos.py` — reproduz testes e gera JSON + log debug.
3. **`batch_validate_rag.py`** — adicionado `reconfigure(utf-8)` no inicio.
4. **Correcao** do unico `.md` corrompido encontrado no vault principal.

## O que ja existia (nao duplicar)

- Scripts RAG, Grafo, FabioOS, MEGATRON: padrao `reconfigure(encoding="utf-8")` no topo ou via `_common.py`.
- `60_Sistemas/Scripts/start_fabioos.ps1`: `[Console]::OutputEncoding = UTF8`.
- `.codex/config.toml.example`: `PYTHONIOENCODING = "utf-8"` no MCP fabioos.

## Recomendacoes para Codex

1. Preferir venv RAG para scripts Python: `60_Sistemas\RAG\.venv\Scripts\python.exe`.
2. Antes de sessao Codex no Windows:

```powershell
$env:PYTHONIOENCODING = 'utf-8'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
```

3. Rodar auditoria periodica:

```powershell
60_Sistemas\RAG\.venv\Scripts\python.exe 60_Sistemas\FabioOS\scripts\auditar_encoding_fabioos.py
```

4. Saida JSON: `60_Sistemas/FabioOS/classificacoes/auditoria_encoding_fabioos.json`.

## Como usar

- Leia este relatorio quando Codex reportar "encoding error".
- Execute o script de auditoria e compare JSON entre sessoes.
- Nao reindexar RAG por encoding sem novos arquivos corrompidos.

## Relacoes

- [[60_Sistemas/RAG/Relatorio_Validacao_Parcial_RAG_2026-06-26]] — menciona `PYTHONIOENCODING=utf-8`
- [[60_Sistemas/FabioOS/Politica_Codex_Config_Local_vs_Vault_2026-06-28]]
- [[50_Registros/Sessoes/2026-06-29_cursor-sessao-validacao-rag]]
- [[60_Sistemas/Cursor/README_Cursor_FabioOS]]

## Proximas acoes

- [ ] Codex confirmar se erros cessam com `PYTHONIOENCODING=utf-8`
- [ ] Validador Codex (pendente na politica config) incluir checagem de encoding
- [ ] Fabio autorizar commit de `.gitattributes` + auditoria + correcao inbox
