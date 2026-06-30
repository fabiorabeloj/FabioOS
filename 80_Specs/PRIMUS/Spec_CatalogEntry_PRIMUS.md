---
tipo: spec
area: 80_Specs
projeto: PRIMUS
status: rascunho
fonte: [[40_Wiki/PRIMUS/Tipagem_Universal_PRIMUS]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, spec, catalogentry, catalogo, enciclopedia]
---

# SPEC - CatalogEntry PRIMUS

## Objetivo

Definir a unidade minima da Enciclopedia Funcional.

## Schema

```yaml
entry_id:
type:
name:
class_base:
source_id:
source_layer:
page:
snippet_ref:
box:
subbox:
affects:
never_affects:
instancing_hint:
portability:
confidence:
status:
notes:
```

## Regras

- Sem `type`, nao entra.
- Sem `source_id`, fica como rascunho.
- Sem `affects` e `never_affects`, nao pode ir para CatalogPool.
- Sem `instancing_hint`, nao pode gerar instancia.
- Fonte externa nunca altera regra D&D sem decisao de precedencia.

## Estados

| Status | Significado |
|---|---|
| `bootstrap` | entrada criada para estruturar o motor |
| `fonte-pendente` | precisa de pagina/trecho |
| `validada` | fonte e encaixe verificados |
| `pool-ready` | pode entrar no CatalogPool |
| `bloqueada` | nao pode ser usada em instancia |

## Proxima Entrega

Validar o lote inicial em [[30_Projetos/PRIMUS/CatalogEntries_Lote_0001_PRIMUS]].
