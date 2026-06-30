---
tipo: ordem-coordenacao
area: 60_Sistemas
projeto: FabioOS
status: ativo
autor: Claude (arquiteto-chefe)
criado_em: 2026-06-29
atualizado_em: 2026-06-29
tags: [fabios, multiagente, coordenacao, ordens, megatron, anti-colisao, paralelo]
---

# Ordens de Coordenacao Paralela - Sprint MEGATRON coordenador

> Emitido por Claude (arquiteto-chefe). Os tres cerebros atuam **em paralelo**,
> cada um na sua especialidade, **sem colisao**. A regra unica e:
> **cada agente so edita os arquivos da sua zona**. A costura entre as zonas e o
> **Resultado estruturado** (contrato congelado abaixo).
> Base: [[60_Sistemas/FabioOS/specs/2026-06-29_megatron-coordenador]] e
> [[60_Sistemas/FabioOS/Integracao_Cursor_e_Coordenacao_Multiagente_2026-06-29]].

## Contrato congelado (a costura) — NAO mudar sem acordo do arquiteto

O orquestrador devolve um **Resultado estruturado** (dado, nao texto impresso):

```python
Resultado = {
    "tipo": str,        # "briefing" | "resposta" | "abstencao" | "proposta" | "bloqueio"
    "ok": bool,
    "titulo": str,      # 1 linha
    "corpo": str,       # markdown
    "fontes": list,     # [{"source_path": str, "header_path": str}]
    "sugestao": str,    # proxima acao sugerida (pode ser "")
    "artefato": str | None,  # caminho do rascunho gerado, se houver
}
```

Claude e dono deste formato. Cursor consome; Codex documenta. Mudanca so via
arquiteto.

---

## ZONA CLAUDE — nucleo do orquestrador (eu)

**Possui e edita:**
- `60_Sistemas/MEGATRON/v1/megatron.py`
- `60_Sistemas/MEGATRON/v1/registry.py` (novo)
- contrato `run()` dentro dos agentes em `60_Sistemas/MEGATRON/agentes/implementacao/claude/`
- `60_Sistemas/MEGATRON/v1/tests/golden_questions.py`
- `STATUS.md`, `NEXT_ACTIONS.md`, `Registro_Frentes_Ativas.md` (lideranca)

**Entrega:** Fatias 1-4 da spec; publica o `Resultado` congelado.

**Nao toca:** apresentacao visual, dashboards Obsidian, Painel de Pendencias,
Roadmap, wikilinks.

---

## ZONA CURSOR — oficina de apresentacao/interface

**Especialidade:** software de apresentacao, dashboards, empacotamento. Consome
o `Resultado`, **nao** mexe na logica.

**Possui e edita:**
- `60_Sistemas/MEGATRON/v1/apresentacao.py` (novo) — recebe um `Resultado` e
  renderiza bonito no terminal (secoes, realce, fontes legiveis). Funcao pura
  `render(resultado: dict) -> str`.
- `60_Sistemas/Cursor/` — mockup/prototipo visual do briefing "Bom dia, FabioOS"
  (HTML estatico ou protótipo), consumindo o mesmo `Resultado`.

**Como comecar JA sem me esperar:** use o **contrato congelado** acima como alvo.
Crie um `Resultado` de exemplo (fixture) e construa `render()` + o mockup contra
ele. Quando minha Fatia 1/2 cair, o `megatron.py` so passa a chamar `render()`.

**Nao toca:** `megatron.py`, `registry.py`, agentes, RAG/MCP, `fabioos_db`,
arquivos de governanca/roadmap.

**Lock a registrar:** `CURSOR_APRESENTACAO_MEGATRON` em Registro_Frentes_Ativas.

---

## ZONA CODEX — governanca, estrutura e documentacao (independente; pode iniciar agora)

**Especialidade:** estrutura do vault, migracao, links, governanca documental,
roadmap. **Zero codigo** do MEGATRON/RAG.

**Possui e edita:**
- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Painel_Pendencias_FabioOS.md`
  — **desatualizado**: corrigir `1795`->`1206`, marcar Fase 12 como **piloto/encerrada**,
  inserir "MEGATRON coordenador (16.1)" como frente ativa.
- `60_Sistemas/FabioOS/Roadmap_Fases_FabioOS_v2_2026-06-29.md` — refletir Fase 12
  fechada + MEGATRON coordenador (16.1) como fase tecnica corrente.
- `60_Sistemas/MEGATRON/agentes/Registro_Agentes.md` e
  `60_Sistemas/Governanca/` (INDEX) — documentar o **contrato de agente** (`run()`)
  como padrao (texto/doc, nao implementacao).
- wikilinks pendentes da migracao (zona Codex de sempre).

**Nao toca:** `60_Sistemas/MEGATRON/**` codigo, `60_Sistemas/RAG/` scripts/DB,
MCP, `apresentacao.py`/mockups do Cursor, `STATUS.md`/`NEXT_ACTIONS.md`
(propriedade Claude neste sprint — se precisar, pedir ao arquiteto).

**Lock a registrar:** `CODEX_GOVERNANCA_POS_FASE12` em Registro_Frentes_Ativas.

---

## Matriz anti-colisao (rapida)

| Arquivo/zona | Dono unico neste sprint |
|---|---|
| `MEGATRON/v1/megatron.py`, `registry.py`, agentes, golden_questions | Claude |
| `MEGATRON/v1/apresentacao.py`, `60_Sistemas/Cursor/` mockups | Cursor |
| Painel_Pendencias, Roadmap v2, Registro_Agentes (doc), wikilinks | Codex |
| `STATUS.md`, `NEXT_ACTIONS.md`, `Registro_Frentes_Ativas.md` | Claude (lider) |
| RAG scripts, `fabioos_db`, MCP | Claude (read-only; sem reindex) |
| `Resultado` (contrato) | Claude define; todos consomem |

## Regras gerais (valem para os tres)

1. Registrar lock em `Registro_Frentes_Ativas.md` antes de tocar artefato proprio.
2. Sem push, sem API externa, sem runtime (n8n/OpenClaw/WhatsApp): Fabio-gated.
3. Sem reindex do RAG, sem editar `fabioos_db`.
4. Ao concluir: marcar lock `concluida`, gerar changelog, apontar entrega.
5. Conflito de fronteira -> parar e escalar ao arquiteto (Claude), nao improvisar.

## Relacoes
- [[60_Sistemas/FabioOS/specs/2026-06-29_megatron-coordenador]]
- [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]]
- [[50_Registros/Decisoes/ADR_2026-06-29_Auditoria_Arquitetura_Claude]]
