---
tipo: moc
area: 40_Wiki
projeto: PRIMUS
autoria: derivado (conceitos de design abstratos)
criado_em: 2026-07-01
atualizado_em: 2026-07-01
tags: [primus, moc, design, conceitos, sandbox]
---

# MOC - Conceitos de Design (PRIMUS)

Hub dos conceitos de design derivados dos livros em Modo Catalogo. Aqui entram
apenas ideias fortes, reutilizaveis e ligaveis. Dado bruto, lista, tabela, item,
estatistica e texto protegido ficam no PRIMUS Index/SQLite ou em catalogos
restritos, nao como bolinhas soltas no Obsidian.

## Regra de admissao

Um candidato so entra aqui se passar nos tres testes:

- e uma ideia de design, nao uma linha de dado;
- possui pelo menos dois wikilinks reais para o motor PRIMUS ou outros conceitos;
- pode orientar uma decisao de jogo, mundo, missao, tensao ou DeltaP.

## Conceitos-base

- [[faccoes-e-turnos-de-faccao]] - o mundo age sozinho por objetivos de faccao.
- [[tags-de-aventura]] - tags que geram ganchos, aliados, inimigos e complicacoes.
- [[sandbox-e-jogo-por-regioes]] - mundo aberto por regioes, nao trilho linear.
- [[npc-rapido-motivacao-metodo-meios]] - NPC vivo em motivacao, metodo e meios.
- [[aventura-como-situacao]] - situacao carregada, nao enredo pre-escrito.

## Conceitos extraidos de SWN/WWN free

- [[frente-de-faccao-e-projetos]] - faccao como plano ativo no mundo.
- [[reacao-do-mundo-entre-sessoes]] - o mundo reage fora da cena.
- [[regiao-com-tags-e-problemas]] - regiao como maquina de situacoes.
- [[npc-com-agenda-e-alavancas]] - NPC como agente causal.
- [[site-com-proposito-e-perigo]] - local jogavel precisa de motivo e risco.
- [[rumor-com-fonte-e-incerteza]] - informacao como decisao, nao exposicao.
- [[missao-com-situacao-nao-trilho]] - missao como problema aberto.
- [[recompensa-com-consequencia]] - recompensa como causa de mudanca.

## Conceitos abstratos de D&D Core

Estes nos sao abstracoes de design. Nao contem texto integral, tabela,
estatistica, lista protegida ou reproducoes de regras.

- [[classe-como-fantasia-operacional]] - classe como promessa de papel e decisao.
- [[encontro-como-pressao-de-recursos]] - encontro como consumo e escolha.
- [[tesouro-como-vetor-de-decisao]] - recompensa que muda comportamento.
- [[monstro-como-funcao-dramatica]] - criatura pela funcao no conflito.
- [[premissa-de-mundo-como-gerador-de-tensao]] - lore que gera pressao recorrente.
- [[viagem-planar-como-custo-e-risco]] - deslocamento fantastico como decisao.

## Como eles se encaixam

```text
Premissa de mundo
  -> Regioes com tags/problemas
  -> Faccao + projeto + NPC com agenda
  -> Rumor / site / missao como situacao
  -> Encontro, recompensa, monstro, tesouro
  -> DeltaP
  -> WorldState atualizado
```

## Metodo

- [[80_Specs/PRIMUS/Metodo_Markdownizacao_Conceitos_de_Livro]] - metodo de
  extracao de conceitos sem stubs massivos.
- [[50_Registros/Decisoes/ADR_2026-07-01_Catalogo_DND_Core_Sem_Stubs_Massivos]] -
  decisao que baniu stubs massivos no 40_Wiki.
- [[40_Wiki/PRIMUS/Fontes_Oficiais_DND/Catalogo_DND_Core_Consolidado]] - catalogo
  seguro para os dados restritos.

## Motor PRIMUS

- [[WorldState_0001_PRIMUS]]
- [[Spec_Tension_Engine_PRIMUS]]
- [[Spec_DeltaP_PRIMUS]]
- [[Spec_Cantina_Conflict_Engine_PRIMUS]]
