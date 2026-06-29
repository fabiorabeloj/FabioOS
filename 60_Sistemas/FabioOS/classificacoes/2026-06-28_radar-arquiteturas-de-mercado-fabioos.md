---
tipo: classificacao-dado
area: 60_Sistemas
projeto: FabioOS
status: gerado
gerado_por: classificar_dado_fabioos.py
fonte_original: 30_Conhecimento/Tecnologia/Radar/2026-06-28_prompt-arquiteturas-de-mercado-fabioos.md
dominio: IAOS
classe_dado: Interno
criado_em: 2026-06-28
atualizado_em: 2026-06-28
tags: [fabios, classificacao, dominios, permissoes, privacidade]
---

# Classificacao de dado - Radar Arquiteturas de Mercado FabioOS

> Gerado por `60_Sistemas/FabioOS/scripts/classificar_dado_fabioos.py`.
> Leitura local, sem API, sem envio de dados e sem alteracao de RAG/Grafo.

## Resultado

| Campo | Valor |
|---|---|
| Dominio provavel | IAOS |
| Classe de dado | Interno |
| Permissao RAG | Permitido |
| Permissao Grafo | Permitido |
| Modelo externo/API | Permitido com criterio |

## Dominios detectados

| Dominio | Sinais | Descricao |
| --- | --- | --- |
| IAOS | 42 | Dominio tecnico de IA e automacao |
| FabioOS | 14 | Plataforma base e dominio pessoal/operacional |
| ProductOS | 9 | Dominio futuro de produto/negocio |
| TraderOS | 2 | Dominio de trading e desempenho financeiro |

## Sensibilidade detectada

| Classe | Sinais | Motivo |
| --- | --- | --- |
| Interno | 35 | Operacao interna sem indicio forte de dado sensivel |

## Decisao recomendada

Pode entrar no fluxo normal se nao houver dados pessoais.

## Politica aplicada

- Se a classificacao parecer duvidosa, usar a classe mais restritiva.
- Conteudo restrito nao deve ir bruto para RAG/Grafo.
- Conteudo critico nao deve entrar no vault.
- Acoes externas exigem aprovacao humana registrada.

## Fonte

- Arquivo analisado: `30_Conhecimento/Tecnologia/Radar/2026-06-28_prompt-arquiteturas-de-mercado-fabioos.md`
- Tamanho aproximado: 892 palavras
