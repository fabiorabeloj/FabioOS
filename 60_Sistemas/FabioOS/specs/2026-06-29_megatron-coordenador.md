---
tipo: spec
area: 60_Sistemas
projeto: FabioOS
status: rascunho
fase: 16.1
dominio: FabioOS
classe_dado: interno
permissao: leitura_e_proposta
autor: Claude (arquiteto-chefe)
criado_em: 2026-06-29
atualizado_em: 2026-06-29
tags: [fabios, spec, megatron, coordenador, orquestrador, agentes, multiagente]
---

# SPEC - MEGATRON coordenador (CLI -> orquestrador)

## 1. Problema

MEGATRON v1 existe, mas e um **CLI de disparo unico**: classifica a intencao,
consulta RAG/Grafo e, quando detecta uma acao, apenas **nomeia** o agente que
deveria agir (`SafeCommit`/`Arquivista`) — nao despacha. Os agentes
(`arquivista.py`, `inbox.py`, `safecommit.py`, `dashboard.py`, `rag_agent.py`)
sao scripts soltos, sem interface comum. O sistema parece um buscador, nao um
organismo. Falta a camada de **coordenacao**.

## 2. Objetivo

Evoluir o MEGATRON de CLI para **orquestrador** que despacha agentes por um
contrato uniforme, mantendo read-only/propose-only. Entregue em fatias, cada uma
fechavel sozinha:

- **Fatia 1 - Briefing proativo:** `python megatron.py` sem argumento entrega
  estado (STATUS/NEXT_ACTIONS) + pendencias-topo + sugestao de proxima acao.
- **Fatia 2 - Esqueleto orquestrador:** `registry.py` (tabela capacidade->agente)
  + contrato `run()` no Arquivista + despacho dry-run de 1 agente.
- **Fatia 3 - Despacho real:** "registre pendencia X" -> dry-run mostra a nota;
  `--confirmar` -> Arquivista cria rascunho (`status: rascunho`).
- **Fatia 4 - Cadeia multi-passo:** consulta -> RAG -> grafo -> sintese ->
  sugestao encadeados numa resposta.

## 3. Fora de escopo

- Modo conversacional / estado de sessao (adiado — YAGNI por ora).
- Interface visual/web final (zona Cursor; consome a saida estruturada).
- LLM/API externa (recuperacao, custo zero — como na v1).
- Acao externa (push, WhatsApp, email, n8n) e sensivel (apagar, reindex, token):
  permanecem **bloqueadas**, so nomeadas/propostas.
- Reindex do RAG ou edicao do `fabioos_db`.

## 4. Dominio, dados e permissoes

| Campo | Valor |
|---|---|
| Dominio | FabioOS |
| Classe de dado | interno |
| RAG | permitido, read-only (via MCP, como hoje) |
| Grafo | permitido, read-only (via MCP) |
| Escrita | apenas **escrita segura** (rascunho em `00_Inbox` via Arquivista) e so com `--confirmar` |
| Modelo externo/API | proibido por padrao |
| Aprovacao humana | obrigatoria para qualquer acao externa/sensivel; dry-run por padrao |

## 5. Arquitetura proposta

```text
Entrada (pergunta OU pedido OU vazio)
  -> Orquestrador (megatron.py): classifica intencao + monta plano
  -> Registro (registry.py): resolve capacidade -> agente
  -> Agente.run(pedido) -> Resultado(ok, artefato, resumo, fontes)   [dry-run por padrao]
  -> Orquestrador compoe RESPOSTA estruturada (dict/dataclass)
  -> Apresentacao (camada fina) renderiza p/ terminal  [seam p/ Cursor renderizar visual]
  -> Log
```

**Costura anti-colisao (chave do trabalho paralelo):** o orquestrador devolve um
**Resultado estruturado** (dados), nao apenas texto impresso. Claude possui o
nucleo + o formato do Resultado; Cursor consome esse formato para a apresentacao
(CLI bonito, dashboard, futura UI) sem editar `megatron.py`; Codex documenta e
governa em volta sem tocar codigo. O contrato do Resultado e o ponto de acordo.

### Contrato uniforme do agente
Cada agente passa a expor uma funcao pura `run(...) -> Resultado` (a logica que
hoje vive no `main()`); o `main()` CLI vira casca fina que chama `run()`. Sem
mudar comportamento — so torna chamavel e testavel.

O **`Resultado` e o contrato congelado** (fonte unica:
[[60_Sistemas/FabioOS/Ordens_Coordenacao_Paralela_MEGATRON_2026-06-29]]):

```python
Resultado = {
    "tipo": str,        # "briefing" | "resposta" | "abstencao" | "proposta" | "bloqueio"
    "ok": bool,
    "titulo": str,
    "corpo": str,       # markdown
    "fontes": list,     # [{"source_path": str, "header_path": str}]
    "sugestao": str,
    "artefato": str | None,  # caminho do rascunho gerado, se houver
}
```

Claude e dono do formato; Cursor renderiza; Codex documenta. Mudanca so via arquiteto.

## 6. Plano de tarefas (Claude — zona nucleo)

- [ ] Fatia 1: modo briefing (sem args) reusando `_ler_estado` + RAG; corrigir o
      bug do caminho de log em `megatron.py:40` (`megatron_v1_log.md`).
- [ ] Fatia 2: criar `registry.py`; extrair `arquivista.run()`; orquestrador
      despacha em dry-run.
- [ ] Fatia 3: pedido de escrita -> dry-run + `--confirmar` -> rascunho.
- [ ] Fatia 4: cadeia RAG->grafo->sintese->sugestao.
- [ ] Definir `Resultado` estruturado e publicar o formato p/ Cursor.
- [ ] A cada fatia: +1-2 golden questions em `v1/tests/golden_questions.py`.

## 7. Criterios de aceite

- [ ] `megatron.py` sem args entrega briefing com estado real (nao inventa).
- [ ] Orquestrador despacha agente por contrato uniforme, nao por nome solto.
- [ ] Dry-run e padrao; escrita so com `--confirmar`, e so escrita segura.
- [ ] Acao externa/sensivel continua bloqueada.
- [ ] Saida estruturada disponivel para a apresentacao (Cursor).
- [ ] Passa a bateria `golden_questions.py` a cada fatia.
- [ ] Bug do caminho de log corrigido.

## 8. Testes minimos

- [ ] Briefing sem args (estado conhecido).
- [ ] Pergunta que exige RAG (resposta com fontes).
- [ ] Pergunta ambigua -> abstencao (ignorancia explicita preservada).
- [ ] Pedido de escrita em dry-run (nao cria arquivo).
- [ ] Pedido de escrita com `--confirmar` (cria rascunho, nao sobrescreve).
- [ ] Pedido de acao externa -> bloqueio.

## 9. Riscos

| Risco | Mitigacao |
|---|---|
| Colisao entre Claude/Cursor no `megatron.py` | costura por Resultado estruturado; Cursor so na apresentacao |
| Over-build (repetir o loop da Fase 12) | fatias fechaveis; YAGNI na conversacional |
| Escrita acidental | dry-run padrao; `--confirmar` explicito; so escrita segura |
| Quebra da v1 | v0/v1 atuais preservados; golden questions a cada fatia |
| Acao externa acidental | bloqueio mantido da v1 |

## 10. Rollback

Se uma fatia falhar: reverter o commit da fatia (atomico); v1 atual volta a ser o
estado bom. v0 segue como rollback final. Nenhuma fatia toca RAG DB nem runtime
externo, entao rollback e local e seguro.

## 11. Changelog esperado

`50_Registros/Changelog/2026-06-29_megatron-coordenador-fatia1.md` (e por fatia).

## Relacoes

- [[60_Sistemas/FabioOS/specs/2026-06-29_megatron-v1-ignorancia-explicita]]
- [[50_Registros/Decisoes/ADR_2026-06-29_Auditoria_Arquitetura_Claude]]
- [[60_Sistemas/FabioOS/Integracao_Cursor_e_Coordenacao_Multiagente_2026-06-29]]
- [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]]
- [[60_Sistemas/MEGATRON/v1/megatron]]
