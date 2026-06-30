---
tipo: protocolo
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [concluido, governanca, fechamento, qualidade]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Definicao de Concluido FabioOS

## Regra central

Resposta de IA nao e entrega. Entrega e persistencia verificavel no sistema.

## Uma tarefa esta concluida quando

1. O arquivo foi criado ou atualizado.
2. A decisao foi registrada, se houver decisao.
3. A tarefa foi marcada ou criada.
4. O changelog foi atualizado, se houver mudanca relevante.
5. O status do projeto foi atualizado.
6. O Git foi verificado.
7. O resumo final foi produzido.
8. A proxima acao esta clara.

## Estados permitidos

| Estado | Significado |
|---|---|
| rascunho | existe, mas nao validado |
| especificado | requisitos claros, sem execucao |
| piloto | testado em caso pequeno |
| ativo | usado de forma recorrente |
| operacional | testado, logado e confiavel |
| suspenso | pausado por risco/custo/falha |
| concluido | entregue e registrado |

## Checklist final

- [ ] Arquivos alterados listados.
- [ ] Links internos criados.
- [ ] STATUS/NEXT_ACTIONS atualizados quando necessario.
- [ ] Changelog criado ou atualizado.
- [ ] Segredos verificados.
- [ ] Git status revisado.
- [ ] Risco residual informado.

## Relacoes

- [[50_Registros/Decisoes/Constituicao_Operacional_FabioOS]]
- [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]]
- [[50_Registros/Changelog/CHANGELOG_FabioOS]]
