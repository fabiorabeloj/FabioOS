---
tipo: adr
area: FabioOS
projeto: FabioOS
status: aprovado
tags: [adr, governanca, seguranca, agentes, automacao]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# ADR - Governanca Operacional FabioOS

## Contexto

O FabioOS ja possui vault, wiki, RAG, Grafo, agentes, MCPs, n8n, OpenClaw, Google connectors catalogados, matriz de IAs e roadmap v2.

O risco deixou de ser falta de ferramentas. O risco passou a ser crescimento sem regime.

## Problema

Sem governanca operacional, o FabioOS pode:

- duplicar notas;
- perder decisoes;
- acionar ferramentas sensiveis sem aprovacao;
- misturar dominios;
- enviar dados a modelos externos sem criterio;
- automatizar erro;
- confundir resposta com entrega.

## Alternativas consideradas

| Alternativa | Avaliacao |
|---|---|
| Continuar implementando automacoes | rapido, mas aumenta risco |
| Criar governanca depois | posterga o controle para quando o sistema ja estiver caotico |
| Criar governanca agora | reduz velocidade momentanea, mas aumenta seguranca e profissionalismo |

## Decisao

O FabioOS adotara uma camada de governanca operacional antes de expandir automacoes e agentes, para evitar caos, duplicacao, acoes inseguras e perda de controle.

## Consequencias

Positivas:

- agentes ganham limites;
- automacoes ganham aprovacao e log;
- dados sensiveis ganham classificacao;
- tarefas passam a ter criterio de concluido;
- o sistema fica mais profissional.

Negativas:

- mais documentacao para manter;
- algumas automacoes ficam mais lentas ate haver permissao;
- exige disciplina operacional.

## Proximos passos

1. Revisar esta camada com Claude/Fabio.
2. Aplicar a Matriz de Permissoes em RAG/MCP/n8n/OpenClaw.
3. Criar checklist de release das proximas fases.
4. Iniciar MEGATRON v1 somente com limites de acao.
