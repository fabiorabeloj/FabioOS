---
tipo: sistema
area: 60_Sistemas
projeto: FabioOS
sistema: MEGATRON
status: piloto
fase: capstone-v0
tags: [megatron, interface, capstone, mcp, rag, grafo, roteamento, ignorancia-explicita]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# MEGATRON v0 — Interface cognitiva mínima

## Função

Primeira versão funcional do **capstone** (bloco B5): a interface única que recebe a mensagem do Fabio, **roteia pelas capacidades** (MCP FabioOS → RAG/Grafo/vault), responde **com fontes** e respeita os limites de segurança. É a "face" que se senta sobre RAG (B1), Agentes (B2), Grafo (B3) e MCP (B4).

## Princípios (v0)

- **Read-only e propose-only.** Não escreve, não commita, não envia, não apaga.
- **Sem LLM/API.** Responde por **recuperação** (custo zero); a síntese gerada fica para v1 com `--generate` + aprovação.
- **Sempre com fontes.** Cita o caminho de cada trecho.
- **Reaproveita, não duplica.** Consome o [[60_Sistemas/MCP_FabioOS/README_MCP_FabioOS|MCP FabioOS]] in-memory (cliente FastMCP).

## Roteamento (classificador)

| Intent | Gatilho | Ação |
|---|---|---|
| `acao` | commit, push, criar, apagar, enviar, instalar… | **Não executa** — propõe + "requer aprovação humana" + indica agente |
| `status` | "fase atual", "pendência", "próximo passo"… | `consultar_rag` (ranking operacional) |
| `relacao` | "relaciona", "conectado", "depende"… | `consultar_rag` + `consultar_grafo` |
| `consulta` | (demais) | `consultar_rag` |

## Como usar

```powershell
60_Sistemas\RAG\.venv\Scripts\python.exe 60_Sistemas\MEGATRON\v0\megatron.py "Qual e a fase atual do FabioOS?"
```

Log das interações: `60_Sistemas/MEGATRON/v0/logs/megatron_log.md` (gitignored, runtime).

## Estado do teste (2026-06-27)

- ✅ status → recuperou Painel/Modelo Formal/Visão com fontes
- ✅ relação ("PietraOS") → RAG + grafo (23 nós)
- ✅ ação ("commit/push") → propose-only, não executou
- ✅ pergunta sem evidência → **dispara Ignorância Explícita** (melhor dist > 0.5) — resolvido na v1

## Limitações conhecidas → backlog

1. ✅ **Ignorância Explícita por limiar de relevância — RESOLVIDO (v1, 2026-06-27).** `consultar_rag` passou a expor `dist=`; o MEGATRON declara ignorância quando a melhor distância **> 0.5** (calibrado: relevantes ~0.28–0.36, sem sentido ~0.60–0.64).
2. **Sem síntese.** v0 só recupera; a resposta sintetizada (LLM) exige `--generate` + aprovação (v1).
3. **Sem execução de ação.** Por design; v1 conecta a SafeCommit/Arquivista com aprovação humana.
4. **CLI apenas.** Interface visual (PWA/dashboard) é fase futura.

## Relações

- [[60_Sistemas/MCP_FabioOS/README_MCP_FabioOS]]
- [[60_Sistemas/FabioOS/Visao_Interface_FabioOS]]
- [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]]
- [[60_Sistemas/FabioOS/Protocolo_Roteamento_Capacidades_IA]]
- [[60_Sistemas/MEGATRON/agentes/README_Agentes]]

## Próximas ações

- [ ] v1: limiar de relevância para Ignorância Explícita (expor distância no `consultar_rag`)
- [ ] v1: síntese opcional com `--generate` + aprovação humana
- [ ] Conectar ação → agentes MEGATRON (SafeCommit/Arquivista) com aprovação
- [ ] Avaliar interface visual (PWA) como fase posterior
