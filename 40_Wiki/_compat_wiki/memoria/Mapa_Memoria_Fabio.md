---
tipo: mapa
area: wiki
projeto: FabioOS
status: rascunho
tags: [fabios, memoria, mapa, pessoal, profissional]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Mapa da Memoria Fabio

## Objetivo

Organizar a memoria pessoal e profissional absorvida pelo FabioOS sem misturar fonte bruta, privacidade e conhecimento consolidado.

## Categorias

| Categoria | Destino | Entra no RAG por padrao? |
|---|---|---|
| Projetos | `wiki/memoria/projetos/` | sim, apos revisao |
| Decisoes | `wiki/memoria/decisoes/` | sim, apos revisao |
| Ideias | `wiki/memoria/ideias/` | sim, apos revisao |
| Pessoas | `wiki/memoria/pessoas/` | nao; revisar caso a caso |
| Compromissos | `wiki/memoria/compromissos/` | nao; pode conter dados pessoais |
| Fontes sensiveis | `sources/*/_restrito/` | nao |

## Fontes planejadas

- ChatGPT: exportacao oficial e processamento por conversa.
- Gmail pessoal: `fabiorabelo.j@gmail.com`, por filtros pequenos e revisaveis.
- Gmail trabalho: `fabiofilosofia@colegiopietra.com.br`, pendente de autorizacao/conector.
- Changelogs Claude/Codex/OpenClaw: ja disponiveis no vault.

## Primeiro ciclo sugerido

1. [x] Ingerir uma amostra pequena de e-mails relacionados a FabioOS/MEGATRON.
2. [x] Criar fonte restrita em `sources/email/_restrito/` com `status: nao-indexar`.
3. [x] Consolidar decisoes relevantes em `wiki/memoria/decisoes/`.
4. [ ] So depois liberar para RAG/Grafo.

## Decisoes registradas

- [[wiki/memoria/decisoes/2026-06-27_Piloto_Email_Protocolos_FabioOS]]
- [[wiki/memoria/decisoes/2026-06-27_Email_Anthropic_Privacidade_Claude]]

## Projetos/tarefas registrados

- [[wiki/memoria/projetos/2026-06-27_GitHub_Actions_Auto_Changelog_Falhas]]
