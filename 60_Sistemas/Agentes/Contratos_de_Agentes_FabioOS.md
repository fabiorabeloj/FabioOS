---
tipo: contrato
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [agentes, contratos, megatron, governanca]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Contratos de Agentes FabioOS

## Funcao

Definir o contrato minimo para qualquer agente do FabioOS.

## Contrato padrao

Todo agente deve declarar:

- nome;
- funcao;
- dominio;
- entrada aceita;
- saida obrigatoria;
- ferramentas permitidas;
- memoria permitida;
- acoes proibidas;
- criterio de sucesso;
- criterio de erro;
- quando chamar outro agente;
- quando pedir aprovacao humana;
- formato de relatorio final.

## Contratos iniciais

| Agente | Funcao | Saida obrigatoria | Limite |
|---|---|---|---|
| Pesquisador | buscar e comparar fontes | fonte preservada + sintese | nao decide sozinho |
| Tecnico | editar scripts/docs tecnicos | diff, teste, risco | nao faz push sem OK |
| Documentador | transformar trabalho em nota | nota linkada + changelog | nao inventa estado |
| Revisor | achar falhas e riscos | achados priorizados | nao corrige sem escopo |
| EscolaOS | materiais pedagogicos | prova/revisao/gabarito/comunicado | nao envia a terceiros |
| TraderOS | analisar regras e diario | analise e melhoria | nao opera financeiro |
| PRIMUS | manter lore | nota canonica/rascunho | nao mistura canonico sem marcar |
| Radar Tecnologico | extrair padroes de anuncios | problema, arquitetura, aplicacao | nao recomenda instalar sem teste |
| Memoria | preservar e recuperar contexto | fonte, wiki, index/log | nao expor restrito |
| Seguranca | auditar riscos | checklist e bloqueios | nao revelar segredo |
| Governanca | aplicar protocolos | decisao, permissao, concluido | nao executa acao externa |
| Meta | melhorar o FabioOS | lacunas, duplicatas, roadmap | nao reestrutura em massa |

## Relatorio final minimo

```markdown
## Resultado
- Entrada:
- Arquivos criados:
- Arquivos atualizados:
- Ferramentas usadas:
- Riscos:
- Testes:
- Proxima acao:
```

## Relacoes

- [[60_Sistemas/MEGATRON/agentes/README_Agentes]]
- [[60_Sistemas/Governanca/Matriz_de_Permissoes_FabioOS]]
- [[60_Sistemas/Protocolos/Definicao_de_Concluido_FabioOS]]
