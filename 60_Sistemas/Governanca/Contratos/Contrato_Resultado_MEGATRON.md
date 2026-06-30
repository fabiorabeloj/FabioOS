---
tipo: contrato
area: 60_Sistemas
projeto: FabioOS
status: ativo
responsavel_formato: Claude
consumidores: [Cursor, Codex, OpenClaw, n8n]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
tags: [fabios, megatron, contrato, resultado, multiagente]
---

# Contrato - Resultado MEGATRON

## Funcao

Definir a costura entre:

- Claude: nucleo do orquestrador;
- Cursor: apresentacao/interface;
- Codex: governanca/documentacao;
- futuros canais: OpenClaw, n8n, mobile.

O orquestrador deve devolver dados estruturados, nao apenas texto impresso.

## Contrato congelado

Fonte de autoridade: [[60_Sistemas/FabioOS/Ordens_Coordenacao_Paralela_MEGATRON_2026-06-29]].

```python
Resultado = {
    "tipo": str,        # "briefing" | "resposta" | "abstencao" | "proposta" | "bloqueio"
    "ok": bool,
    "titulo": str,      # 1 linha
    "corpo": str,       # markdown
    "fontes": list,     # [{"source_path": str, "header_path": str}]
    "sugestao": str,    # proxima acao sugerida (pode ser "")
    "artefato": str | None,
}
```

## Campos

| Campo | Tipo | Obrigatorio | Regra |
|---|---|---:|---|
| `tipo` | string | sim | Um dos tipos permitidos |
| `ok` | boolean | sim | `true` apenas quando a resposta tem base suficiente ou a operacao proposta e segura |
| `titulo` | string | sim | Uma linha, sem markdown complexo |
| `corpo` | string | sim | Markdown legivel; deve declarar ignorancia quando faltar base |
| `fontes` | lista | sim | Lista vazia apenas em `abstencao`, `bloqueio` ou resposta operacional sem fonte |
| `sugestao` | string | sim | Proxima acao recomendada ou string vazia |
| `artefato` | string/null | sim | Caminho de rascunho gerado, quando houver |

## Tipos permitidos

| Tipo | Uso |
|---|---|
| `briefing` | Estado proativo do FabioOS |
| `resposta` | Resposta fundamentada com fontes |
| `abstencao` | Sistema nao encontrou base suficiente |
| `proposta` | Plano, rascunho, diff ou proxima acao sem executar externo |
| `bloqueio` | Pedido proibido, sensivel ou sem permissao |

## Regras de qualidade

- Nao inventar status operacional.
- Nao esconder incerteza.
- Nao transformar sugestao em acao.
- Nao executar WhatsApp, email, push, trade ou delecao.
- Citar fontes internas quando houver consulta ao vault/RAG/Grafo/MCP.
- Preservar `artefato` como caminho relativo ao vault quando existir.

## Consumidores

| Consumidor | Como usa |
|---|---|
| Cursor | renderiza terminal/UI sem alterar logica |
| Codex | documenta governanca e audita aderencia |
| OpenClaw | pode exibir resultado no chat, sem executar |
| n8n | pode rotear por `tipo`, `ok` e `artefato` |

## Criterios de aceite

- Um `Resultado` de exemplo renderiza sem precisar importar `megatron.py`.
- Cursor consegue montar `render(resultado: dict) -> str`.
- Codex consegue auditar campos obrigatorios.
- n8n consegue decidir rota por `tipo` e `ok`.
- OpenClaw consegue exibir `titulo`, `corpo`, `fontes` e `sugestao`.

## Mudanca de contrato

Qualquer mudanca exige:

1. decisao do Claude;
2. changelog;
3. atualizacao deste documento;
4. ajuste dos consumidores.
