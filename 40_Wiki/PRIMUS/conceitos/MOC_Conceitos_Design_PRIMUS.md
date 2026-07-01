---
tipo: moc
area: 40_Wiki
projeto: PRIMUS
autoria: derivado (conceitos de design abstratos)
criado_em: 2026-07-01
tags: [primus, moc, design, conceitos, sandbox]
---

# MOC — Conceitos de Design (PRIMUS)

> Hub dos conceitos de design derivados dos livros (Modo Catálogo, lei Nota vs Dado).
> Só ideias fortes e ligáveis — o dado dos livros vive no índice/SQLite.

## Conceitos (nós)
- [[faccoes-e-turnos-de-faccao]] — o mundo age sozinho por objetivos de facção.
- [[tags-de-aventura]] — tags que geram ganchos (aliados/inimigos/complicações).
- [[sandbox-e-jogo-por-regioes]] — mundo aberto por regiões × trilho linear.
- [[npc-rapido-motivacao-metodo-meios]] — NPC vivo em 3 eixos.
- [[aventura-como-situacao]] — situação carregada × enredo pré-escrito.

## Como eles se encaixam
```text
NPCs (motivação) ─┐
Facções (turnos) ─┼─> Tensões ─> Situações ─> Conflitos (Cantina) ─> ΔP ─> WorldState
Tags (ganchos) ───┘        (Tension Engine)        (Conflict Engine)      (DeltaP)
Sandbox por regiões = o palco onde o jogador escolhe
```

## Método
- [[80_Specs/PRIMUS/Metodo_Markdownizacao_Conceitos_de_Livro]] — como o Codex extrai
  conceitos de qualquer livro sem gerar stubs.

## Motor PRIMUS (destino dos links)
- [[WorldState_0001_PRIMUS]] · [[Spec_Tension_Engine_PRIMUS]] · [[Spec_DeltaP]] · [[Spec_Cantina_Conflict_Engine_PRIMUS]]
