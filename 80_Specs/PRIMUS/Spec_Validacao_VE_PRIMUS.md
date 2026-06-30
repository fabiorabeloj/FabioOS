---
tipo: spec
area: 80_Specs
projeto: PRIMUS
status: rascunho
fonte: [[80_Specs/PRIMUS/Spec_CatalogEntry_PRIMUS]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, spec, validacao, ve, enciclopedia]
---

# SPEC - Validacao V(E) PRIMUS

## Objetivo

Validar se uma entrada da Enciclopedia Funcional pode avancar para CatalogPool.

## Checklist V(E)

| Campo | Pergunta |
|---|---|
| Type | A entrada tem tipo canonico? |
| Class Base | A entrada e Entity, Event, State, Agent, Relation, Boundary ou Value? |
| Source | A origem esta identificada? |
| Page/Snippet | Ha pagina/trecho ou justificativa manual? |
| Box/Subbox | O endereco editorial esta definido? |
| Affects | O que pode afetar esta claro? |
| NeverAffects | O limite esta claro? |
| Instancing Hint | Como vira jogo esta claro? |
| Portability | Portable, persistent ou local? |
| Precedence | Canon, setting, homebrew ou framework? |

## Resultado

| Resultado | Significado |
|---|---|
| `VE-pass` | pode ir ao CatalogPool |
| `VE-pass-com-pendencia` | estrutura ok, mas falta pagina/trecho |
| `VE-fail` | nao pode avancar |
| `VE-blocked` | exige decisao humana |

## Regra

Entrada sem pagina/trecho nao deve virar canon. Pode existir como bootstrap, mas nao pode gerar missao final.
