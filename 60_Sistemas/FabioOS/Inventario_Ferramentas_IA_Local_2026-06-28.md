---
tipo: inventario
area: 60_Sistemas
projeto: FabioOS
status: gerado
classe_dado: Interno
gerado_por: inventario_ferramentas_ia.py
atualizado_em: 2026-06-28 23:57:38
tags: [fabios, ia, ferramentas, cursor, hermes, openclaw, n8n, openrouter]
---

# Inventario Local de Ferramentas IA - FabioOS

> Este arquivo nao exibe valores de tokens. Ele mostra apenas presenca/ausencia e estado operacional local.

## Comandos no PATH

| Comando | Estado |
| --- | --- |
| openclaw | nao encontrado no PATH |
| cursor | nao encontrado no PATH |
| cursor.cmd | nao encontrado no PATH |
| hermes | nao encontrado no PATH |
| hermes-agent | nao encontrado no PATH |
| n8n | nao encontrado no PATH |
| node | C:\Program Files\nodejs\node.EXE |
| python | C:\Users\user\AppData\Local\Programs\Python\Python312\python.EXE |
| uv | C:\Users\user\AppData\Local\Microsoft\WinGet\Packages\astral-sh.uv_Microsoft.Winget.Source_8wekyb3d8bbwe\uv.EXE |
| git | C:\Program Files\Git\cmd\git.EXE |
| claude | C:\Users\user\.local\bin\claude.EXE |

## Variaveis de ambiente

| Variavel | Estado |
| --- | --- |
| OPENROUTER_API_KEY | ausente |
| OPENAI_API_KEY | ausente |
| ANTHROPIC_API_KEY | ausente |
| GEMINI_API_KEY | ausente |
| GOOGLE_API_KEY | ausente |
| OPENCLAW_GATEWAY_TOKEN | ausente |

## Diretorios conhecidos

| Item | Estado |
| --- | --- |
| OpenClaw Tray local | existe |
| OpenClaw usuario | nao encontrado |
| Cursor Local Programs | existe |
| Cursor AppData | nao encontrado |
| Hermes AppData | existe |
| n8n FabioOS | existe |
| OpenClaw FabioOS | existe |
| MCP FabioOS | existe |

## Processos detectados

| Processo | PID | Estado |
| --- | --- | --- |
| OpenClaw.Tray.WinUI.exe | 16160 | rodando |
| claude.exe | 13828 | rodando |
| claude.exe | 740 | rodando |
| claude.exe | 17544 | rodando |
| claude.exe | 5180 | rodando |
| claude.exe | 13744 | rodando |
| claude.exe | 10000 | rodando |
| claude.exe | 6208 | rodando |
| claude.exe | 17628 | rodando |
| claude.exe | 13796 | rodando |
| node_repl.exe | 21652 | rodando |
| node.exe | 20808 | rodando |
| node.exe | 17352 | rodando |
| node.exe | 13924 | rodando |
| claude.exe | 23660 | rodando |
| claude.exe | 23908 | rodando |
| claude.exe | 3752 | rodando |
| claude.exe | 4960 | rodando |
| node.exe | 23496 | rodando |
| node_repl.exe | 22244 | rodando |
| node.exe | 22940 | rodando |
| node.exe | 21152 | rodando |
| python.exe | 22320 | rodando |
| node_repl.exe | 25444 | rodando |
| python.exe | 15716 | rodando |
| node.exe | 18296 | rodando |
| node.exe | 23872 | rodando |
| node.exe | 7492 | rodando |
| python.exe | 23904 | rodando |
| node_repl.exe | 23256 | rodando |
| python.exe | 23100 | rodando |
| node.exe | 5224 | rodando |
| node.exe | 23596 | rodando |
| node.exe | 25420 | rodando |
| claude.exe | 20992 | rodando |
| node.exe | 21052 | rodando |
| node.exe | 6732 | rodando |
| node.exe | 7612 | rodando |
| node.exe | 1832 | rodando |
| node.exe | 24908 | rodando |
| node_repl.exe | 22036 | rodando |
| python.exe | 20800 | rodando |
| python.exe | 7540 | rodando |
| node.exe | 21488 | rodando |
| node.exe | 9352 | rodando |
| node.exe | 21112 | rodando |
| python.exe | 10496 | rodando |
| claude.exe | 21776 | rodando |
| python.exe | 23604 | rodando |

## Portas relevantes

| Porta | Estado | PID |
| --- | --- | --- |
| 18789 | ouvindo | 20448 |
| 5678 | livre/nao detectado | - |
| 8787 | ouvindo | 10496 |
| 3000 | livre/nao detectado | - |
| 5173 | livre/nao detectado | - |
| 8000 | livre/nao detectado | - |
| 8080 | livre/nao detectado | - |

## Papeis recomendados

| Ferramenta | Papel | Uso no FabioOS |
| --- | --- | --- |
| Claude | lider estrutural | arquitetura, revisao, commits tematicos e governanca |
| Codex | executor/engenheiro | implementacao local, testes, scripts, conectores e handoffs |
| Cursor | IDE aumentada | edicao visual, refactors, navegacao de codigo e pair programming |
| Hermes | pendente de confirmacao | avaliar como agente local se houver CLI/API utilizavel |
| OpenClaw | painel/companion | visualizar agentes e operar workboard quando auth/runtime estiver estavel |
| n8n | orquestrador de borda | webhooks, WhatsApp, email, Drive e automacoes com aprovacao |
| OpenRouter | broker de modelos | usar com teto de custo e por tarefas especificas, nunca por padrao |
| RAG FabioOS | memoria semantica | consulta com fontes; ingestao apenas apos triagem |
| Grafo FabioOS | mapa relacional | relacionar notas, fases, agentes e projetos |

## Leitura operacional

- Se `OpenClaw` estiver rodando mas `openclaw` nao estiver no PATH, o Companion existe, mas a automacao por CLI precisa de ajuste de ambiente.
- Se `n8n` nao estiver no PATH e a porta `5678` estiver livre, ha workflows versionados, mas nao ha servico n8n local ativo.
- Se `OPENROUTER_API_KEY` estiver ausente, nao ha base segura para chamadas pagas via OpenRouter nesta sessao.
- Cursor pode ser usado como IDE humana/visual, mesmo sem CLI detectada, se o aplicativo estiver instalado fora do PATH.
- Hermes precisa de confirmacao de caminho/CLI antes de virar agente operacional.
