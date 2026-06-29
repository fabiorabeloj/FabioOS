---
tipo: protocolo
area: 60_Sistemas
projeto: FabioOS
status: rascunho
tags: [fabios, ia, contexto, modelos, limites, multiagente]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Protocolo de Gestao de Contexto das IAs

## Funcao

Reduzir perda de contexto, chats longos demais, retrabalho e dependencia da memoria humana nas interacoes entre Claude, Codex, ChatGPT, MEGATRON e futuros agentes.

## Principio

O usuario nao deve atuar como mensageiro entre IAs. A troca de contexto deve ocorrer preferencialmente por artefatos do FabioOS: changelogs, status, protocolos, roteiros, decisoes e relatorios.

## Sinais de transicao de contexto

Um agente deve preparar transicao quando perceber:

- conversa longa demais;
- degradacao de qualidade;
- repeticao de informacoes;
- dificuldade para localizar decisoes anteriores;
- perda de precisao sobre arquivos tocados;
- aumento de risco de conflito com outro agente;
- limite de uso proximo;
- necessidade de trocar de modelo ou chat.

## Procedimento de transicao

Antes de encerrar ou migrar para outro chat, o agente deve:

1. registrar estado atual;
2. registrar arquivos tocados;
3. registrar arquivos que nao devem ser tocados;
4. registrar pendencias;
5. registrar decisoes em aberto;
6. atualizar changelog quando houver entrega real;
7. gerar prompt de continuidade;
8. indicar arquivos obrigatorios para leitura no novo ciclo.

## Prompt minimo de continuidade

```text
Leia o contexto do FabioOS e continue a partir do ultimo changelog.

Antes de agir, leia:
- AGENTS.md ou CLAUDE.md
- 90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Painel_Pendencias_FabioOS.md
- ultimo arquivo em 50_Registros/Changelog/
- protocolo/relatorio especifico da frente atual

Estado:
[resumo curto]

Arquivos tocados:
[lista]

Arquivos a evitar:
[lista]

Proxima acao:
[acao objetiva]

Nao fazer push. Nao expor tokens. Nao apagar arquivos.
```

## Gestao de limites de uso

Limites de Claude, Codex, ChatGPT e outros modelos devem ser tratados como recurso computacional.

Regras:

- reservar modelos fortes para arquitetura, revisao critica e decisoes;
- usar agentes/scripts para diagnosticos mecanicos;
- preparar backlog quando um agente estiver indisponivel;
- evitar rodadas de confirmacao repetitiva quando ja houver politica segura;
- nao gastar contexto com conteudo que pode ser salvo em arquivo.

## Matriz inicial de modelos

| Tarefa | Modelo/agente preferencial | Motivo |
|---|---|---|
| Arquitetura constitucional | Claude/Codex forte | exige raciocinio profundo e consistencia |
| Edicao de scripts locais | Codex/Claude Code | exige ferramenta e verificacao local |
| Resumo de estado | agente leve ou script | tarefa mecanica |
| Revisao de seguranca | SafeCommit + agente revisor | criterio objetivo |
| Atendimento externo | n8n + agente especializado | precisa logs, aprovacao e rastreabilidade |
| Consulta semantica | RAG | evita depender de memoria do chat |

## Relacao com MEGATRON

MEGATRON deve evoluir para orquestrar contexto entre agentes, mantendo o usuario como estrategista e nao como operador manual de mensagens entre IAs.

## Proximas acoes

- [ ] Integrar este protocolo ao Dashboard dos agentes.
- [ ] Criar modelo de `STATUS.md` por frente.
- [ ] Criar modelo de prompt de continuidade por fase.
- [ ] Definir criterio objetivo para quando abrir novo chat.
