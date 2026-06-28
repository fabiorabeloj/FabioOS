---
tipo: matriz-operacional
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, automacao, python, n8n, megatron, mcp, rag, grafo]
criado_em: 2026-06-28
atualizado_em: 2026-06-28
---

# Matriz de Automatizacoes - Python, n8n e Hibrido

## Funcao

Classificar as automatizacoes candidatas do FabioOS pela ferramenta correta: Python, n8n ou arquitetura hibrida.

Esta matriz aplica a decisao registrada em [[2026-06-28_Decisao_Python_n8n_MEGATRON]].

## Regra de decisao

| Pergunta | Se sim | Se nao |
|---|---|---|
| Precisa de gatilho externo, credencial ou API de terceiro? | n8n ou hibrido | Python |
| Precisa enviar mensagem, email ou notificacao? | n8n com aprovacao humana | Python |
| E processamento local de arquivo/nota/dado? | Python | avaliar |
| Precisa ser testavel e versionavel como logica de sistema? | Python | n8n se for fluxo externo |
| Precisa de painel visual de aprovacao? | n8n ou futuro MEGATRON UI | Python para worker |

## Matriz principal

| Automacao candidata | Ferramenta | Motivo | Risco | Proxima acao |
|---|---|---|---|---|
| Triagem de `00_Inbox/` | Python | Leitura local, classificacao por regras e roteamento interno | mover/alterar nota errada | Criar dry-run que so sugere destino |
| Arquivamento de fonte bruta | Python | Preservar arquivo e frontmatter local | duplicacao ou perda de fonte | Usar skill `archive-source` e padronizar logs |
| Fonte bruta -> wiki | Python + revisao humana | Transformacao textual versionavel | alucinacao/sintese ruim | Usar `source-to-wiki` com diff antes de salvar |
| Validacao de frontmatter e links | Python | Regra deterministica, testavel e rapida | falsos positivos | Criar script de auditoria read-only |
| Atualizacao de indices Obsidian | Python | Operacao local e versionavel | remover links por engano | Fazer primeiro em modo diff |
| SafeCommit | Python/Git | Scan, stage explicito e changelog sao locais | segredo escapar ou commit amplo | Manter fluxo com scan antes de commit |
| Changelog de sessao | Python | Gera arquivo local com base em Git/status | registrar fato nao verificado | Usar `session-changelog` com revisao |
| Consulta RAG | Python/MCP FabioOS | Banco local, sem API, com fontes | ranking ruim | Usar antes de responder sobre FabioOS |
| Reindexacao RAG | Python com lock | Processo local pesado e sensivel | apagar/recriar base indevidamente | So com lock e backup/registro |
| Validacao RAG 10 perguntas | Python | Teste local repetivel | conclusao subjetiva | Rodar suite e registrar resultados |
| Build/auditoria do Grafo | Python | Extracao local de relacoes | relacionar entidade errada | Rodar audit antes de usar em decisao |
| Export Neo4j/Gephi | Python | CSV/JSON regeneraveis | churn no Git | Manter dados pesados gitignored |
| MCP FabioOS | Python/FastMCP | Expor ferramentas read-only para agentes | ferramenta escrever sem querer | Manter v0 read-only |
| MEGATRON v0 consulta/roteamento | Python | Orquestrador local sobre RAG/Grafo/MCP | parecer mais capaz do que e | Declarar ignorancia e pedir aprovacao |
| MEGATRON acao -> agente | Hibrido | Python decide rota; agente executa; n8n se externo | acao sensivel sem aprovacao | Implementar propose-only primeiro |
| Dashboard textual FabioOS | Python | Lê status, Git, changelogs, agentes | painel desatualizado | Gerar Markdown com fontes |
| Dashboard visual FabioOS | Python + Cursor/web | Precisa app/interface | complexidade prematura | Prototipo depois do MCP estabilizar |
| `start_fabioos.ps1` / retomada | PowerShell + Python | Ambiente Windows e checagens locais | iniciar servico indevido | Manter conservador e idempotente |
| Limpeza segura do PC/vault | Python | Auditoria local e quarentena | exclusao indevida | Somente read-only ate aprovacao |
| Gmail pessoal: triagem pontual | Conector Gmail + Python | Busca autorizada + resumo local | dados pessoais sensiveis | Escopo pequeno, sem envio/arquivo em massa |
| Gmail profissional | n8n/Gmail connector | Conta externa, credencial e fluxo institucional | privacidade/institucional | Solicitar autorizacao antes de ler |
| Gmail -> nota Obsidian | Hibrido | n8n/Gmail captura; Python normaliza; humano aprova | salvar dado sensivel | Comecar com dry-run e fonte restrita |
| Google Drive/Docs ingestao | Hibrido | Drive e credenciais externos; processamento local | copiar documento sensivel | Conector Drive + Python para normalizar |
| Calendar/lembretes | n8n | Gatilhos, agenda e notificacoes | notificar errado | Usar aprovacao e logs |
| WhatsApp Pietra | n8n + OpenClaw/Evolution + agente | Canal externo e webhook | resposta enviada indevidamente | Simular antes; envio sempre aprovado |
| OpenClaw Companion | OpenClaw + n8n + Python | Gateway conversacional | instabilidade e contexto excessivo | Estabilizar auth/QR antes de producao |
| Hermes Agent persistente | Futuro/hibrido | Autonomia real se houver CLI/API | autonomia sem escopo | Descobrir interface tecnica primeiro |
| Cursor como oficina | Manual + Python/tests | Desenvolvimento assistido | virar agente sem controle | Usar para MCP, testes e interface |
| GitHub Actions Auto Changelog | GitHub/MCP + Python | Logs e YAML podem ser auditados localmente | quebrar CI | Investigar read-only, depois patch pequeno |
| Matriz de privacidade por provedor IA | Python/docs | Documento e classificacao local | omitir risco | Criar tabela de dados permitidos/proibidos |
| Export ChatGPT -> memoria | Python | Processar export local em camadas | dados pessoais em massa | Inventario primeiro, ingestao por lote |
| Escola: provas/revisoes | Python/skills | Geracao local de documentos | misturar turma/disciplina | Usar templates e aprovacao humana |
| Escola: envio comunicado | n8n ou manual | Envio externo | mensagem errada a pais/alunos | Apenas rascunho ate aprovacao |

## Achados de consistencia

Auditoria read-only do subagente `explorer` apontou dois desalinhamentos que precisam ser tratados antes de automatizar mais:

1. **RAG:** documentos recentes tratam Fase 12 como validada 10/10, mas `NEXT_ACTIONS.md` e alguns roteiros antigos ainda pedem reexecucao/revalidacao. Decisao pratica: considerar RAG utilizavel para consulta, mas manter uma tarefa de saneamento documental para reconciliar status antigo vs status recente.
2. **n8n:** ha divergencia entre workflows documentados no vault e nomes/status observados no n8n real em rodadas anteriores. Decisao pratica: antes de ativar qualquer fluxo externo, criar auditoria read-only que compare `60_Sistemas/n8n/Workflows/*.json` com o estado real do n8n.

Esses achados reforcam que a proxima automacao deve ser local e read-only: um dashboard textual que mostre estado real, pendencias e inconsistencias.

## Prioridade de implementacao

### Prioridade 1 - local, segura e de alto retorno

1. Auditoria de frontmatter/links em Python.
2. Dashboard textual FabioOS em Python.
3. Validador de config Codex/MCP sem segredos.
4. Suite de validacao RAG por Python.
5. Rotina de Inbox dry-run.

### Prioridade 2 - hibrida, com credenciais controladas

1. Gmail pessoal -> nota restrita -> resumo seguro.
2. Google Drive/Docs -> fonte preservada -> wiki.
3. n8n Webhook Inbox com worker Python.
4. Gmail Trigger em n8n com dry-run e limite.

### Prioridade 3 - externa/sensivel

1. WhatsApp Pietra real.
2. Gmail profissional.
3. OpenClaw Companion em producao.
4. Hermes autonomo.
5. Envio automatico de mensagens.

## Desenho hibrido recomendado

```text
Evento externo
  -> n8n recebe gatilho
  -> salva payload bruto em area restrita ou passa trecho minimo
  -> Python normaliza, valida, classifica e gera proposta
  -> MEGATRON mostra proposta e pede aprovacao
  -> n8n executa envio/acao externa se aprovado
  -> Python registra log/changelog/nota
```

## Decisao pratica

O FabioOS deve priorizar Python para inteligencia operacional local e n8n para bordas externas.

MEGATRON fica acima dos dois:

- decide rota;
- consulta contexto;
- chama Python quando for trabalho local;
- chama n8n quando houver mundo externo;
- exige aprovacao humana quando houver risco.

## Proxima acao concreta

Implementar primeiro um **Dashboard textual FabioOS em Python**, porque ele:

- usa apenas dados locais;
- reduz confusao de estado;
- prepara a interface MEGATRON;
- nao depende de tokens;
- ajuda Claude, Codex e Fabio a enxergarem o sistema.
