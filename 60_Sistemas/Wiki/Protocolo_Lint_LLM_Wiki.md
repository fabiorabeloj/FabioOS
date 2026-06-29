---
tipo: protocolo
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [llm-wiki, lint, manutencao, anti-caos, obsidian]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Protocolo de Lint - LLM Wiki FabioOS

## Funcao

Definir a revisao periodica de saude da wiki.

## Frequencia

Recomendacao inicial: semanal para areas ativas e mensal para areas estaveis.

## Checklist

Verificar:

- paginas sem frontmatter;
- paginas sem links internos;
- paginas sem link de entrada;
- paginas duplicadas;
- conceitos importantes sem pagina;
- decisoes sem consequencia;
- fontes sem processamento;
- protocolos sem criterio de uso;
- specs sem status;
- agentes sem contrato;
- links quebrados;
- claims obsoletos;
- documentos planejados confundidos com ativos.

## Criterios de problema

| Problema | Criterio |
|---|---|
| nota orfa | nao possui link de entrada nem aparece em index/dashboard |
| duplicata | duas paginas tratam do mesmo objeto sem relacao clara |
| contradicao | paginas afirmam regras diferentes sem ADR ou decisao |
| obsolescencia | estado operacional antigo contradiz STATUS atual |
| promessa vaga | documento anuncia automacao sem criterio de teste |
| fonte solta | fonte bruta sem resumo, destino ou proxima acao |

## Saida do lint

Cada lint deve gerar relatorio com:

- data;
- escopo;
- paginas revisadas;
- achados P1/P2/P3;
- sugestoes de fusao;
- links quebrados;
- decisoes pendentes;
- proxima acao.

## Regras

- Nao mover em massa durante lint.
- Nao apagar paginas sem aprovacao.
- Preferir marcar `status: revisar` ou `status: superseded`.
- Alteracoes estruturais exigem changelog.

## Piloto recomendado

Executar primeiro em `40_Wiki/_compat_wiki/sistemas/` e `40_Wiki/_compat_wiki/conceitos/`, pois ja possuem paginas suficientes para detectar duplicacao e lacunas sem tocar dados sensiveis.
