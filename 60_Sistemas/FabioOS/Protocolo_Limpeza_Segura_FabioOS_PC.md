---
tipo: protocolo
area: 60_Sistemas
projeto: FabioOS
status: rascunho
tags: [fabios, limpeza, pc, seguranca, quarentena]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Protocolo de Limpeza Segura FabioOS / PC / IA

## Funcao

Reduzir sobrecarga, duplicacoes, arquivos inuteis, processos pesados e confusao operacional sem apagar nada importante.

## Regra zero

Nao deletar nada definitivamente sem antes mover para quarentena e registrar o que foi feito.

## Diagnostico inicial

Antes de qualquer limpeza, produzir relatorio com:

- espaco livre em disco;
- pastas mais pesadas;
- arquivos duplicados;
- arquivos temporarios;
- repositorios Git com arquivos grandes;
- `node_modules`, caches, builds, logs e pastas geradas;
- containers Docker parados;
- imagens Docker antigas;
- processos com alto consumo de CPU/RAM;
- estado do Obsidian vault;
- estado do Git;
- estado do n8n;
- estado do Claude/Codex/OpenClaw, quando aplicavel.

## Classificacao

| Classe | Destino | Regra |
|---|---|---|
| A - Manter | local atual | notas, documentos importantes, workflows, scripts ativos, configuracoes |
| B - Arquivar | `90_Arquivo/` ou `_Arquivo_FabioOS/` | antigo, util, concluido ou historico |
| C - Quarentena | `_QUARENTENA_LIMPEZA/AAAA-MM-DD/` | suspeito, duplicado ou sem funcao clara |
| D - Remover apos confirmacao | descarte controlado | caches, temporarios, builds, logs descartaveis, containers/imagens sem uso |

## Limpeza segura

Acoes permitidas sem destruicao:

- criar backup do estado atual;
- criar pasta de quarentena;
- listar candidatos a limpeza;
- mover duplicados obvios para quarentena;
- registrar tudo em changelog;
- atualizar `.gitignore` quando houver lixo recorrente.

Acoes que exigem confirmacao explicita:

- apagar arquivos;
- apagar volumes Docker;
- apagar imagens Docker;
- remover containers;
- limpar lixeira;
- desinstalar programas;
- alterar workflows n8n ativos;
- renomear notas centrais do Obsidian.

## Obsidian

Regras:

- nao quebrar links `[[ ]]`;
- nao renomear notas centrais sem atualizar backlinks;
- mover notas soltas para `00_Inbox/` ou area correta;
- mover material antigo para `90_Arquivo/`;
- registrar limpeza em `50_Registros/Changelog/`.

## Docker / n8n

Nunca apagar volumes do n8n sem backup.

Limpezas Docker destrutivas devem ser apresentadas como plano antes de qualquer execucao.

## Resultado obrigatorio

Todo ciclo de limpeza deve entregar:

```md
# Relatorio de Limpeza FabioOS

## Estado inicial
- Disco:
- RAM:
- Pastas pesadas:
- Processos pesados:

## Acoes realizadas
- ...

## Arquivos movidos para quarentena
- ...

## Arquivos arquivados
- ...

## Riscos encontrados
- ...

## Proximas decisoes humanas
- ...

## Comandos seguros para proxima etapa
- ...
```

## Proximas acoes

- [ ] Criar script de diagnostico somente leitura.
- [ ] Definir local padrao da quarentena fora do vault.
- [ ] Mapear caches seguros para limpeza no Windows.
- [ ] Criar rotina mensal de limpeza assistida.
