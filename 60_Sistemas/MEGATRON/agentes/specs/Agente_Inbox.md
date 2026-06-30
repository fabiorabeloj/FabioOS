---
tipo: especificacao-agente
area: 60_Sistemas
projeto: FabioOS
sistema: MEGATRON
agente: Inbox
status: especificado
prioridade: 3
tags: [megatron, agente, inbox, triagem, roteamento]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Agente Inbox

## Identidade

| Campo | Valor |
|---|---|
| Nome | Inbox |
| ID | `agent.inbox` |
| Domínio | FabioOS |
| Estado | especificado |
| Prioridade | 3 |
| Dono humano | Fabio |
| Identidade pública | MEGATRON interno |

## Missão

Monitorar entradas novas, classificar destino operacional e encaminhar cada item para o agente, sistema ou revisão humana adequada.

## Entradas

| Entrada | Origem | Formato |
|---|---|---|
| Capturas manuais | `00_Inbox/` | Markdown, texto, imagem |
| Logs de captura | `05_Raw_Sources/_compat_sources/_inbox/` | Markdown |
| Mensagens externas | OpenClaw/n8n | JSON ou Markdown |
| Pendências soltas | usuário ou changelog | checklist |

## Saídas

| Saída | Destino | Formato |
|---|---|---|
| Roteamento para Arquivista | Agente Arquivista | caminho + tipo |
| Roteamento para Pietra | Sistema Pietra | mensagem classificada |
| Roteamento para Escola | Sistema Escola | material ou tarefa |
| Roteamento para humano | Fabio | alerta |
| Tarefa | `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Painel_Pendencias_FabioOS.md` ou projeto | checklist |
| Log de triagem | `50_Registros/Agentes/` | Markdown |

## Ferramentas

- Leitura de `00_Inbox/` e `05_Raw_Sources/_compat_sources/_inbox/`.
- `rg` para detectar padrões.
- Regras do [[60_Sistemas/FabioOS/Protocolo_Operacional_FabioOS]].
- Catálogo de intents do Pietra quando aplicável.
- Encaminhamento manual para Arquivista, SafeCommit, RAG ou Dashboard.

## Permissões

| Classe de ação | Permitida | Condição |
|---|---|---|
| Leitura | Sim | Pastas de entrada e contexto |
| Escrita segura | Sim | Criar triagem, tarefa e log |
| Mover arquivo | Não na v1 | Propor destino antes |
| Escrita sensível | Não | Encaminhar ao humano |
| Exclusão | Não | Nunca |
| Envio externo | Não | Fora do escopo |
| Commit | Não | Encaminhar para SafeCommit |

## Limites

- Não processa profundamente conteúdo; apenas classifica e encaminha.
- Não envia mensagens externas.
- Não decide sozinho sobre dados sensíveis.
- Não apaga itens antigos.
- Não indexa conteúdo no RAG diretamente; encaminha ao RAG após curadoria.

## Riscos

| Risco | Impacto | Mitigação |
|---|---|---|
| Roteamento errado | Perda ou atraso | Registrar categoria e confiança |
| Entrada sensível tratada como comum | Vazamento | Classificar sensibilidade |
| Acúmulo de inbox | Ruído operacional | Rotina diária/semanal |
| Duplicidade | Trabalho repetido | Buscar título e hash quando possível |

## Critérios de aceite

- [ ] Lista entradas novas.
- [ ] Classifica cada entrada em fonte, wiki, tarefa, decisão ou arquivo.
- [ ] Atribui domínio: FabioOS, PietraOS, PrimusOS, Escola ou indefinido.
- [ ] Indica agente recomendado.
- [ ] Marca sensibilidade.
- [ ] Não move nem apaga sem confirmação na v1.

## Logs

Registrar:

- itens encontrados;
- classificação;
- agente de destino;
- confiança;
- sensibilidade;
- itens que exigem decisão humana.

## Relação com MEGATRON

MEGATRON usa Inbox como sensor de entrada. Inbox informa "o que chegou" e "para onde deve ir". MEGATRON decide se aciona Arquivista, Pietra, Escola, RAG, Dashboard ou Fabio.

## Implementação mínima

1. Rotina manual: listar arquivos novos em `00_Inbox/` e `05_Raw_Sources/_compat_sources/_inbox/`.
2. Produzir relatório de triagem.
3. Para cada item, sugerir destino e agente.
4. Só mover ou transformar após confirmação.

## Evolução futura

- Monitor n8n ou automação recorrente.
- Classificação por modelo local.
- Detecção de duplicata por hash.
- Priorização por urgência.
- Integração com Dashboard.

## Relações

- [[60_Sistemas/MEGATRON/agentes/specs/Agente_Arquivista]]
- [[60_Sistemas/MEGATRON/agentes/specs/Agente_Dashboard]]
- [[60_Sistemas/FabioOS/Protocolo_Operacional_FabioOS]]
- [[60_Sistemas/Pietra/Sistema_Pietra]]
