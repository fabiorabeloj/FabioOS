---
tipo: wiki
area: 40_Wiki
projeto: PRIMUS
status: ativo
fonte: [[05_Raw_Sources/PRIMUS/2026-06-30_google-doc_primus_contexto_completo_final]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, pipeline, eip, templates, processo]
---

# Pipeline PRIMUS

## Funcao

Definir como uma fonte vira conteudo jogavel sem virar texto solto.

## Fluxo Base

```text
Fonte
-> T1 Captura
-> T2 Materializacao
-> T3 Integracao
-> T4 Instanciamento
-> DeltaP
```

## Unidades de Processamento

| Unidade | Papel |
|---|---|
| CPU-E | Transforma fonte em entrada de Enciclopedia Funcional. |
| CPU-I | Transforma entradas em instancia jogavel fechada. |
| CPU-P | Transforma resultado de instancia em persistencia registravel. |

## Camadas Editoriais

Cada secao importante deve ter tres camadas:

| Camada | Pergunta |
|---|---|
| Registro | O que existe e de onde veio? |
| Exposicao | Como o humano entende isso? |
| Uso | Como isso entra no jogo ou no motor? |

## Ordem Minima de Preenchimento

1. Nome e Type.
2. Rastreabilidade.
3. Encaixe.
4. Portabilidade.
5. Uso.

## Modos de Expansao

| Modo | Uso |
|---|---|
| Profundidade | Detalhar um item ja aceito. |
| Lateralidade | Criar pares do mesmo nivel. |
| Ramificacao | Gerar subitens dependentes. |

## Resultado Esperado

PRIMUS deve transformar:

```text
PDF ou fonte
-> entries tipadas em E
-> conflitos/instancias em I
-> consequencias em P
-> WorldState atualizado
```

## Relacoes

- [[Circuito_EIP]]
- [[Leis_do_PRIMUS]]
- [[Tipagem_Universal_PRIMUS]]
- [[Motor_Causal_PRIMUS]]
