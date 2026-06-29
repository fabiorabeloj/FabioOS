---
tipo: wiki
area: wiki
projeto: FabioOS
status: ativo
fonte: [[sources/fabios/2026-06-29_governanca-operacional-pontos-cegos]]
tags: [fabios, governanca, megatron, agentes, seguranca, llm-wiki]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Governanca Operacional do FabioOS

## Funcao

Definir o conceito de governanca operacional como camada que transforma multiplos cerebros, agentes, RAG, MCP, Obsidian, n8n e OpenClaw em um sistema controlado, auditavel e seguro.

## Sintese

[FATO] A fonte afirma que o FabioOS nao falha por falta de IA, mas pode falhar por falta de regime, limite, auditoria e fechamento de ciclo.

[INTERPRETACAO] A principal ameaca arquitetural do FabioOS e entropia operacional: muitas ferramentas, muitos agentes e muitos documentos sem uma instituicao interna que defina permissao, criterio de concluido, logs e revisao.

[DECISAO] Governanca operacional passa a ser pre-condicao para expandir automacoes externas, agentes autonomos e conectores sensiveis.

## Problema que resolve

Sem governanca, o FabioOS tende a acumular:

- notas duplicadas;
- decisoes sem consequencia;
- agentes redundantes;
- automacoes inseguras;
- workflows sem dono;
- respostas que morrem no chat;
- credenciais mal posicionadas;
- tarefas sem fechamento.

## Componentes minimos

| Componente | Papel |
|---|---|
| Constituicao operacional | Define leis do sistema e hierarquia de decisao |
| Matriz de permissoes | Define quem pode ler, sugerir, escrever, executar e acionar externos |
| Contratos de agentes | Define entrada, saida, ferramentas, limites e criterios |
| Definicao de concluido | Impede confundir resposta com entrega |
| Protocolo anti-caos | Rotina de revisao, limpeza e consolidacao |
| Protocolo de seguranca | Protege tokens, credenciais, dados escolares, financeiros e externos |
| Separacao de memorias | Diferencia Obsidian, GitHub, RAG, banco estruturado, logs e grafo |
| Observabilidade | Mede custo, erro, tarefas, agentes, automacoes e revisoes |

## Relacao com MEGATRON

MEGATRON deve coordenar, nao executar tudo.

Na governanca operacional, MEGATRON decide:

- qual cerebro acionar;
- se a tarefa exige RAG;
- se a tarefa exige MCP;
- se ha necessidade de aprovacao humana;
- onde registrar o resultado;
- quando uma resposta vira nota, decisao, tarefa, Skill ou Spec;
- quando encerrar o ciclo.

## Relacao com LLM Wiki

A LLM Wiki e o corpo de conhecimento mantido por LLMs.

Governanca operacional e o conjunto de regras que impede essa wiki de virar deposito.

Todo conhecimento importante deve responder:

1. o que e;
2. de onde veio;
3. por que importa;
4. onde entra no FabioOS;
5. o que muda;
6. qual acao ou decisao exige;
7. onde sera encontrado depois.

## Relacao com RAG e MCP

[FATO] RAG recupera memoria. MCP aciona ferramentas.

[DECISAO] RAG e MCP precisam de catalogo, escopo, permissao, teste, log, metrica e revisao.

Sem RAG, o FabioOS nao consulta bem sua memoria.
Sem MCP, o FabioOS nao opera ferramentas reais.
Sem governanca, ambos viram risco.

## Regras praticas

- Nenhum agente envia email ou WhatsApp sem aprovacao humana.
- Nenhum agente apaga arquivo sem aprovacao.
- Nenhum agente mexe em credenciais.
- Nenhum agente altera regra financeira ou de trade sem aprovacao.
- Nenhum agente publica conteudo externo sem autorizacao.
- Nenhuma resposta de IA e entrega ate virar persistencia verificavel.
- Toda frente relevante deve atualizar STATUS, NEXT_ACTIONS ou changelog.

## Aplicacao imediata

1. Usar [[30_Projetos/FabioOS/LLM_Wiki_FabioOS]] antes de novas ingestoes.
2. Usar [[10_Dashboard/RAG_MCP_Control_Plane]] antes de acionar RAG/MCP.
3. Usar [[90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Repertorio/IA/Modelos_e_IAs/Matriz_de_Aptidao_das_IAs_FabioOS]] antes de escolher IA ou ferramenta.
4. Criar a camada completa de governanca operacional como proxima frente documental.
5. Testar tudo primeiro em piloto pequeno antes de escala.

## Fontes

- [[sources/fabios/2026-06-29_governanca-operacional-pontos-cegos]]

## Relacoes

- [[30_Projetos/FabioOS/LLM_Wiki_FabioOS]]
- [[10_Dashboard/RAG_MCP_Control_Plane]]
- [[60_Sistemas/Wiki/Schema_Wiki_FabioOS]]
- [[60_Sistemas/FabioOS/Protocolo_Roteamento_Capacidades_IA]]
- [[60_Sistemas/MEGATRON/agentes/README_Agentes]]
- [[90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Repertorio/IA/Modelos_e_IAs/Matriz_de_Aptidao_das_IAs_FabioOS]]

## Proximas acoes

- [ ] Criar Constituicao Operacional do FabioOS.
- [ ] Criar Matriz de Permissoes.
- [ ] Criar Contratos de Agentes.
- [ ] Criar Definicao de Concluido.
- [ ] Criar Protocolo Anti-Caos.
- [ ] Criar Protocolo de Seguranca.
