---
tipo: matriz
area: 40_Repertorio/IA
projeto: FabioOS
status: ativo
classe_dado: Interno
tags: [fabios, ia, matriz, aptidao, megatron, governanca, rag, mcp, skills, specs]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Matriz de Aptidao das IAs - FabioOS

## Funcao

Definir por que cada IA, modelo, agente ou ferramenta existe dentro do FabioOS.

Esta matriz impede que o sistema vire uma colecao de IAs. Cada item precisa ter vocacao, tarefa adequada, limite, risco, teste e criterio de permanencia.

## Regra central

> Cada IA so deve existir no FabioOS por competencia especifica, nao por acumulo.

Uma IA entra no FabioOS somente se cumprir pelo menos uma destas condicoes:

- ser a melhor opcao para uma classe de tarefa;
- reduzir custo sem reduzir seguranca;
- oferecer redundancia estrategica para uma funcao critica;
- permitir uma capacidade que nenhuma outra peca oferece;
- melhorar privacidade, contexto, execucao local ou multimodalidade.

Se uma IA nao tiver especialidade, contrato, teste e criterio de uso, ela fica em `observacao` e nao participa da operacao.

## Papéis operacionais

| Papel | Definicao |
|---|---|
| Orquestrador | Escolhe rota, agente, memoria, ferramenta e criterio de aceite |
| Planejador | Estrutura estrategia, fases, trade-offs e decisoes |
| Executor | Altera arquivos, cria scripts, roda testes ou opera ferramenta |
| Revisor | Audita qualidade, seguranca, coerencia e risco |
| Leitor | Processa documentos, PDFs, fontes, notas e contexto longo |
| Multimodal | Trabalha com voz, video, imagem, personagem ou interfaces ricas |
| Ferramenta operacional | Integra sistemas, aciona fluxos, agenda, monitora ou executa jobs |
| Redundancia | Substituto controlado para custo, fornecedor, contexto ou disponibilidade |

## Categorias de status

| Status | Criterio |
|---|---|
| ativo | ja usado no FabioOS com funcao clara |
| piloto | pode ser testado em caso pequeno e reversivel |
| experimental | precisa de prova tecnica, custo ou integracao |
| observacao | acompanhar como tecnologia, sem acionar operacionalmente |
| bloqueado | nao usar ate resolver risco, custo, credencial, privacidade ou integracao |
| descontinuar | remover da arquitetura se nao provar utilidade |

## Gate antes de acionar uma IA

Antes de usar qualquer IA/modelo/ferramenta, MEGATRON, Claude ou Codex deve responder:

1. Qual tarefa precisa ser resolvida?
2. Qual memoria precisa ser consultada: LLM Wiki, RAG, Grafo, Specs, Skills ou protocolo?
3. A tarefa exige escrita, execucao local, acao externa ou custo?
4. Qual item desta matriz tem melhor aptidao para a tarefa?
5. Existe risco de dado pessoal, escolar, financeiro, credencial ou envio externo?
6. Existe criterio de teste e criterio de concluido?
7. O resultado sera persistido no FabioOS?

## Matriz de escolha por tarefa

| Tarefa | Principal | Secundaria | Motivo | Criterio de sucesso |
|---|---|---|---|---|
| Arquitetura do FabioOS | ChatGPT | Claude | planejamento, sintese e trade-offs | decisao clara, ADR ou protocolo |
| Documento longo formal | Claude | ChatGPT | coerencia textual e contexto extenso | documento consistente e linkado |
| Implementacao local | Codex | Claude Code | edicao, testes e scripts no repositorio | arquivos alterados, teste e scan |
| Refatoracao grande | Claude Code | Codex | leitura ampla de codebase e execucao | diff coerente e reversivel |
| Script pontual | Codex | DeepSeek | velocidade tecnica e validacao | script executavel com teste |
| Revisao tecnica | Claude | DeepSeek | critica, coerencia e codigo | achados acionaveis |
| PDF/documento longo | Kimi | Claude / NotebookLM | contexto longo e sintese documental | resumo fiel com fontes |
| Ingest na LLM Wiki | Claude | Codex / Kimi | integracao textual e manutencao wiki | paginas atualizadas, index/log/changelog |
| Consulta de memoria | RAG | Claude / ChatGPT | recuperar contexto com fontes | fontes corretas e resposta ancorada |
| Acao em ferramenta | MCP | n8n / OpenClaw | execucao controlada e logavel | log, resultado e permissao correta |
| Automacao recorrente | n8n | Hermes / OpenClaw | fluxo repetivel e credenciais | execucao repetivel, logs e fallback |
| Monitoramento/watchers | Hermes | n8n | persistencia e alertas | alerta correto, baixo ruido |
| Produto/MVP | Lovable | Cursor / Codex | prototipagem rapida | MVP navegavel e exportavel |
| Conteudo audiovisual | Seedance / MiniMax | ElevenLabs | video, voz e personagem | midia gerada com uso definido |
| PRIMUS narrativo | ChatGPT / Claude | MiniMax / ElevenLabs | lore, continuidade e multimodalidade | continuidade preservada |
| Interface visual | Cursor | Codex | desenvolvimento assistido e revisao humana | interface testada localmente |

## Matriz detalhada

### ChatGPT

| Campo | Definicao |
|---|---|
| Vocacao principal | Planejamento, sintese, ensino, arquitetura conceitual e raciocinio multidisciplinar |
| Tarefas recomendadas | definir fases, comparar alternativas, criar prompts para outras IAs, estruturar decisoes, explicar conceitos |
| Tarefas proibidas/inadequadas | operar arquivos locais sem ferramenta, fazer commit, enviar mensagem externa, tratar resposta como entrega final sem persistencia |
| Papel no FabioOS | cerebro estrategico e planejador |
| Categoria | planejador, revisor, redundancia estrategica |
| Integracao possivel | conversa manual, OpenRouter, futuras APIs com teto de custo |
| Risco | decisoes ficarem no chat sem registro; alucinacao sem consulta ao vault |
| Criterio de teste | produzir plano que vire ADR, SPEC ou tarefa verificavel |
| Criterio de permanencia | continuar gerando decisoes melhores que conversa solta e sempre registrar saidas relevantes no vault |

### Claude

| Campo | Definicao |
|---|---|
| Vocacao principal | Documentacao longa, arquitetura textual, revisao tecnica e coerencia de contexto |
| Tarefas recomendadas | protocolos, ADRs, specs extensas, revisao de arquitetura, consolidacao de conversas e documentos |
| Tarefas proibidas/inadequadas | executar sem verificar lock, sobrescrever frente ativa, enviar externo sem aprovacao |
| Papel no FabioOS | lider estrutural e arquiteto tecnico-documental |
| Categoria | planejador, revisor, leitor |
| Integracao possivel | Claude Code, Claude Desktop/Web, handoffs por Markdown |
| Risco | produzir documentos demais sem fechamento operacional |
| Criterio de teste | documento vira regra operacional linkada em STATUS/NEXT_ACTIONS/changelog |
| Criterio de permanencia | manter qualidade superior em textos longos e governanca |

### Claude Code

| Campo | Definicao |
|---|---|
| Vocacao principal | Engenharia agentiva em repositorio, leitura ampla de codebase, edicao e comandos |
| Tarefas recomendadas | refatoracoes, specs para implementacao, commits tematicos, testes, revisoes de codigo |
| Tarefas proibidas/inadequadas | usar `git add -A` em commits tematicos, push sem OK, apagar ou reindexar sem lock |
| Papel no FabioOS | executor tecnico principal quando disponivel |
| Categoria | executor, revisor, ferramenta operacional |
| Integracao possivel | CLI/app local, agentes Claude, skills, hooks, MCPs |
| Risco | colisao com Codex ou outras frentes se ignorar `Registro_Frentes_Ativas` |
| Criterio de teste | altera arquivos com diff claro, testes e scan |
| Criterio de permanencia | continuar fechando ciclos com changelog, status e verificacao |

### Codex

| Campo | Definicao |
|---|---|
| Vocacao principal | Implementacao local, scripts, testes, automacao, conectores e verificacao |
| Tarefas recomendadas | criar scripts pequenos, editar Markdown, validar com shell, usar Gmail/Drive conectores, criar dashboards locais |
| Tarefas proibidas/inadequadas | assumir lideranca estrutural se Claude estiver ativo sem handoff, expor tokens, tocar runtime externo sem lock |
| Papel no FabioOS | executor/engenheiro e operador auxiliar |
| Categoria | executor, revisor, ferramenta operacional |
| Integracao possivel | Codex app, skills `.agents`, conectores Gmail/Drive, MCPs |
| Risco | custo operacional, colisao multiagente e execucao sem registrar contexto |
| Criterio de teste | entrega persistida, verificada e sem arquivos fora de escopo |
| Criterio de permanencia | manter capacidade de executar com seguranca e documentar handoffs |

### Cursor

| Campo | Definicao |
|---|---|
| Vocacao principal | IDE assistida para desenvolvimento visual e revisao humana de codigo |
| Tarefas recomendadas | dashboards, interface MEGATRON, MCP robusto, refactors com acompanhamento visual |
| Tarefas proibidas/inadequadas | operar como agente autonomo sem fluxo documentado, mexer em credenciais ou runtime sem revisao |
| Papel no FabioOS | oficina de desenvolvimento |
| Categoria | executor assistido, ferramenta operacional |
| Integracao possivel | app local; CLI ainda nao detectada no PATH pelo inventario |
| Risco | ser confundido com agente operacional quando e ambiente de edicao |
| Criterio de teste | abrir projeto, editar branch/arquivo de teste e gerar diff revisavel |
| Criterio de permanencia | ser usado em software maior onde Codex/Claude Code sozinhos fiquem menos visuais |

### DeepSeek

| Campo | Definicao |
|---|---|
| Vocacao principal | Codigo, matematica, raciocinio tecnico e revisao de algoritmos |
| Tarefas recomendadas | debug, revisao tecnica, scripts, algoritmos, alternativas de baixo custo |
| Tarefas proibidas/inadequadas | decisoes sensiveis sem revisor, dados privados sem politica, acao externa direta |
| Papel no FabioOS | motor auxiliar tecnico |
| Categoria | executor, revisor, redundancia |
| Integracao possivel | OpenRouter ou API/provedor futuro com teto de custo |
| Risco | privacidade, variacao de qualidade e dependencia de provedor externo |
| Criterio de teste | resolver problema tecnico comparado com Codex/Claude em tarefa controlada |
| Criterio de permanencia | permanecer se reduzir custo ou melhorar qualidade tecnica em casos reais |

### Qwen

| Campo | Definicao |
|---|---|
| Vocacao principal | Agentes, RAG, multimodalidade, modelos alternativos e possivel execucao local |
| Tarefas recomendadas | laboratorio local, agentes especializados, RAG alternativo, tarefas multimodais controladas |
| Tarefas proibidas/inadequadas | assumir como modelo principal sem avaliacao, tratar saida como fonte sem verificacao |
| Papel no FabioOS | redundancia tecnica e laboratorio de agentes |
| Categoria | leitor, executor, multimodal, redundancia |
| Integracao possivel | OpenRouter, modelos locais, futuras APIs |
| Risco | maturidade operacional e variacao entre versoes |
| Criterio de teste | consulta RAG/agentica com fontes e custo menor que alternativa |
| Criterio de permanencia | manter se oferecer bom custo, contexto ou integracao local |

### Kimi

| Campo | Definicao |
|---|---|
| Vocacao principal | Contexto longo e leitura de documentos extensos |
| Tarefas recomendadas | PDFs longos, cursos, livros, transcricoes, comparacao de documentos |
| Tarefas proibidas/inadequadas | executar arquivos, alterar vault, decidir sem integracao com wiki |
| Papel no FabioOS | scanner/leitor documental |
| Categoria | leitor, redundancia |
| Integracao possivel | uso manual, OpenRouter/API futura |
| Risco | resumo fiel sem aplicar protocolo da LLM Wiki |
| Criterio de teste | processar documento grande e gerar sintese com lacunas e aplicacoes |
| Criterio de permanencia | permanecer se superar Claude/ChatGPT em contexto longo real |

### GLM / ChatGLM

| Campo | Definicao |
|---|---|
| Vocacao principal | LLM geral, codigo, agentes e alternativa aberta |
| Tarefas recomendadas | redundancia geral, testes locais, agentes secundarios, RAG experimental |
| Tarefas proibidas/inadequadas | substituir modelos principais sem benchmark |
| Papel no FabioOS | redundancia geral e laboratorio local |
| Categoria | redundancia, executor experimental |
| Integracao possivel | OpenRouter, modelos locais, API futura |
| Risco | manutencao de mais um modelo sem utilidade comprovada |
| Criterio de teste | comparar com Qwen/DeepSeek em tarefa tecnica e RAG |
| Criterio de permanencia | ficar apenas se vencer um nicho ou reduzir custo |

### ERNIE

| Campo | Definicao |
|---|---|
| Vocacao principal | IA empresarial, busca e multimodalidade como referencia de mercado |
| Tarefas recomendadas | observacao estrategica, benchmark de mercado, estudo de arquitetura corporativa |
| Tarefas proibidas/inadequadas | dados sensiveis ou producao sem integracao formal |
| Papel no FabioOS | referencia empresarial |
| Categoria | observacao, multimodal, redundancia futura |
| Integracao possivel | API/provedor futuro se houver caso real |
| Risco | entrar por curiosidade sem uso operacional |
| Criterio de teste | demonstrar ganho em busca/multimodalidade corporativa |
| Criterio de permanencia | permanecer em observacao ate haver uso claro |

### Hunyuan

| Campo | Definicao |
|---|---|
| Vocacao principal | IA corporativa, agentes e integracao empresarial |
| Tarefas recomendadas | estudo de agentes empresariais, arquitetura corporativa, redundancia futura |
| Tarefas proibidas/inadequadas | ser usado em producao sem prova de privacidade e custo |
| Papel no FabioOS | referencia corporativa |
| Categoria | observacao, redundancia |
| Integracao possivel | API/provedor futuro |
| Risco | baixa utilidade imediata no vault local |
| Criterio de teste | caso empresarial pequeno com comparacao a Claude/ChatGPT |
| Criterio de permanencia | manter se houver vantagem corporativa mensuravel |

### Doubao

| Campo | Definicao |
|---|---|
| Vocacao principal | Conteudo, multimodalidade e assistente geral |
| Tarefas recomendadas | marketing, conteudo rapido, experimentos criativos |
| Tarefas proibidas/inadequadas | governanca, codigo critico, dados sensiveis |
| Papel no FabioOS | motor de conteudo futuro |
| Categoria | multimodal, redundancia criativa |
| Integracao possivel | API/provedor futuro |
| Risco | conteudo generico sem rastreabilidade |
| Criterio de teste | produzir peca de marketing melhor/mais barata que alternativa |
| Criterio de permanencia | manter apenas se houver ProdutoOS ou PRIMUS com demanda real |

### MiniMax

| Campo | Definicao |
|---|---|
| Vocacao principal | Voz, video, personagens e interacao multimodal |
| Tarefas recomendadas | PRIMUS, personagens, agentes narrativos, materiais audiovisuais |
| Tarefas proibidas/inadequadas | decisao operacional, dados privados, governanca |
| Papel no FabioOS | modulo criativo multimodal |
| Categoria | multimodal |
| Integracao possivel | API/provedor futuro |
| Risco | custo, direitos de midia e saida dificil de auditar |
| Criterio de teste | gerar personagem/video/voz com criterio de qualidade e uso |
| Criterio de permanencia | permanecer se PRIMUS/ProdutoOS exigir midia recorrente |

### Yi

| Campo | Definicao |
|---|---|
| Vocacao principal | Modelos open-weight, execucao local e personalizacao |
| Tarefas recomendadas | laboratorio local, independencia de fornecedor, testes offline |
| Tarefas proibidas/inadequadas | producao sem benchmark, dados sensiveis sem isolamento |
| Papel no FabioOS | laboratorio de IA local |
| Categoria | redundancia, executor local experimental |
| Integracao possivel | runtime local futuro |
| Risco | hardware, manutencao e qualidade inferior a modelos gerenciados |
| Criterio de teste | rodar tarefa local com privacidade/custo favoravel |
| Criterio de permanencia | manter se hardware local justificar e qualidade for suficiente |

### SenseNova

| Campo | Definicao |
|---|---|
| Vocacao principal | Visao computacional e analise visual |
| Tarefas recomendadas | analise de imagens, OCR/visao futura, material visual |
| Tarefas proibidas/inadequadas | texto longo, codigo, decisoes sensiveis |
| Papel no FabioOS | modulo de visao em observacao |
| Categoria | multimodal, observacao |
| Integracao possivel | API/provedor futuro |
| Risco | privacidade de imagens e baixa prioridade imediata |
| Criterio de teste | analisar imagem relevante com ganho sobre alternativas ja disponiveis |
| Criterio de permanencia | permanecer se houver fluxo visual recorrente |

### Xiaomi MiMo

| Campo | Definicao |
|---|---|
| Vocacao principal | Eficiencia, modelos abertos e inferencia otimizada como sinal de mercado |
| Tarefas recomendadas | radar tecnologico, estudo de IA local e eficiencia |
| Tarefas proibidas/inadequadas | producao sem maturidade e benchmark local |
| Papel no FabioOS | tecnologia em observacao |
| Categoria | observacao, redundancia futura |
| Integracao possivel | laboratorio local futuro |
| Risco | hype sem aplicacao atual |
| Criterio de teste | demonstrar melhor relacao custo/desempenho em tarefa local |
| Criterio de permanencia | manter em observacao ate haver runtime e caso de uso |

### StepFun

| Campo | Definicao |
|---|---|
| Vocacao principal | Contexto longo e modelos alternativos emergentes |
| Tarefas recomendadas | leitura longa experimental, comparacao com Kimi/Claude |
| Tarefas proibidas/inadequadas | operacao critica sem benchmark |
| Papel no FabioOS | redundancia de contexto longo |
| Categoria | leitor, observacao |
| Integracao possivel | API/provedor futuro |
| Risco | pouco uso imediato e informacao instavel |
| Criterio de teste | ler documento longo com melhor custo/qualidade que Kimi/Claude |
| Criterio de permanencia | manter apenas se vencer nicho de contexto longo |

### OpenClaw

| Campo | Definicao |
|---|---|
| Vocacao principal | Gateway conversacional, painel/companion e visualizacao de agentes |
| Tarefas recomendadas | interface externa, workboard, ponte de mensagens, visualizacao de agentes trabalhando |
| Tarefas proibidas/inadequadas | acao sensivel, envio WhatsApp/e-mail, auth/runtime sem lock e aprovacao |
| Papel no FabioOS | atuador/canal externo, nao cerebro central |
| Categoria | ferramenta operacional |
| Integracao possivel | gateway local, OpenClaw Companion, n8n, futuro WhatsApp/Telegram |
| Risco | instabilidade de auth, custo de chamadas e exposicao externa |
| Criterio de teste | receber mensagem teste e criar nota local sem envio externo |
| Criterio de permanencia | permanecer se estabilizar auth, logs, custo e escopo |

### n8n

| Campo | Definicao |
|---|---|
| Vocacao principal | Automacao previsivel, webhooks, credenciais e workflows repetiveis |
| Tarefas recomendadas | Gmail/Drive/Calendar, WhatsApp via webhook, rotinas, integracoes e dry-runs |
| Tarefas proibidas/inadequadas | raciocinio livre, envio externo sem aprovacao, workflow critico sem log |
| Papel no FabioOS | orquestrador de borda e atuador confiavel |
| Categoria | ferramenta operacional |
| Integracao possivel | n8n local/cloud, MCP n8n-docs, workflows versionados |
| Risco | acao externa incorreta em escala |
| Criterio de teste | workflow dry-run com entrada, saida, log e rollback |
| Criterio de permanencia | permanecer como camada de automacao se logs e credenciais forem controlados |

### NotebookLM

| Campo | Definicao |
|---|---|
| Vocacao principal | Estudo de fontes fechadas e cadernos de pesquisa |
| Tarefas recomendadas | PDFs, apostilas, cursos, analise de fonte restrita e perguntas sobre material fechado |
| Tarefas proibidas/inadequadas | manutencao direta do vault, acao externa, decisao sem registro |
| Papel no FabioOS | cerebro auxiliar de aprendizagem |
| Categoria | leitor |
| Integracao possivel | uso manual; resumos entram como fontes/notes no FabioOS |
| Risco | conhecimento ficar preso fora do Obsidian |
| Criterio de teste | produzir sintese que vire nota LLM Wiki com fonte |
| Criterio de permanencia | manter se acelerar estudo sem criar silo |

### Lovable

| Campo | Definicao |
|---|---|
| Vocacao principal | Criacao rapida de apps, MVPs e prototipos |
| Tarefas recomendadas | ProductOS, landing/app inicial, prototipo de dashboard |
| Tarefas proibidas/inadequadas | backend sensivel, credenciais, dados escolares/financeiros sem arquitetura |
| Papel no FabioOS | ferramenta de ProdutoOS |
| Categoria | executor/prototipador |
| Integracao possivel | export/import para repo, Vercel/Supabase futuro |
| Risco | gerar app bonito sem governanca, testes ou controle de dados |
| Criterio de teste | MVP navegavel, exportavel e documentado |
| Criterio de permanencia | permanecer se acelerar produto real sem perder controle do codigo |

### Manus

| Campo | Definicao |
|---|---|
| Vocacao principal | Agente autonomo de pesquisa, navegacao e tarefas longas |
| Tarefas recomendadas | pesquisas externas, comparativos, relatorios, coleta de referencias |
| Tarefas proibidas/inadequadas | alterar vault diretamente, agir em contas sensiveis, executar sem fonte preservada |
| Papel no FabioOS | executor externo de pesquisa |
| Categoria | leitor, executor externo |
| Integracao possivel | relatorios entram em `sources/research/` e depois LLM Wiki |
| Risco | resultado nao rastreavel ou fonte nao preservada |
| Criterio de teste | entregar relatorio com links/fontes que vire nota no FabioOS |
| Criterio de permanencia | manter se economizar tempo em pesquisa longa com fontes confiaveis |

### Hermes

| Campo | Definicao |
|---|---|
| Vocacao principal | Assistente persistente, agendamento, watchers, briefings e automacoes permanentes |
| Tarefas recomendadas | monitoramento, lembretes, relatorios periodicos, watchers de baixa criticidade |
| Tarefas proibidas/inadequadas | mexer em Git, Gmail, WhatsApp, credenciais ou arquivos sensiveis sem protocolo |
| Papel no FabioOS | agente persistente opcional |
| Categoria | ferramenta operacional, observacao |
| Integracao possivel | app local; CLI/API ainda precisa confirmacao |
| Risco | autonomia sem log e sem escopo claro |
| Criterio de teste | watcher simples que gera nota local e log, sem acao externa |
| Criterio de permanencia | permanecer se fizer recorrencia melhor que n8n com menos risco |

### Antigravity

| Campo | Definicao |
|---|---|
| Vocacao principal | Referencia de plataforma para agentes, fluxos e automacoes sem codigo |
| Tarefas recomendadas | estudo de arquitetura de agentes, inspiracao de workflows e product design |
| Tarefas proibidas/inadequadas | producao sem integracao, credenciais, acao externa |
| Papel no FabioOS | referencia arquitetural |
| Categoria | observacao |
| Integracao possivel | Radar Tecnologico; eventual piloto se houver caso claro |
| Risco | virar ferramenta de moda sem necessidade |
| Criterio de teste | demonstrar fluxo que n8n/OpenClaw/Hermes nao resolvem melhor |
| Criterio de permanencia | manter apenas se houver capacidade diferenciada comprovada |

### ElevenLabs

| Campo | Definicao |
|---|---|
| Vocacao principal | Voz sintetica e interfaces faladas |
| Tarefas recomendadas | PRIMUS, aulas, narracao, assistente com voz e prototipos audio |
| Tarefas proibidas/inadequadas | decisoes, dados sensiveis, voz de terceiros sem cuidado etico |
| Papel no FabioOS | modulo de voz |
| Categoria | multimodal |
| Integracao possivel | API futura com teto de custo e aprovacao |
| Risco | custo, direitos de voz e uso indevido |
| Criterio de teste | gerar audio curto com utilidade pedagogica/criativa |
| Criterio de permanencia | manter se voz virar canal real de uso ou produto |

### Seedance

| Campo | Definicao |
|---|---|
| Vocacao principal | Video generativo e midia dinamica |
| Tarefas recomendadas | PRIMUS, aulas, apresentacoes e conteudo visual de produto |
| Tarefas proibidas/inadequadas | informacao sensivel, decisao operacional, midia sem finalidade |
| Papel no FabioOS | modulo de video |
| Categoria | multimodal |
| Integracao possivel | API/provedor futuro, pipeline criativo |
| Risco | custo, direitos de imagem e baixa auditabilidade |
| Criterio de teste | gerar clipe curto com roteiro, objetivo e avaliacao |
| Criterio de permanencia | manter se houver demanda recorrente por video |

## Regras de proibicao geral

- Nenhuma IA envia e-mail, WhatsApp, publicacao ou mensagem externa sem aprovacao humana.
- Nenhuma IA apaga arquivo, move estrutura grande ou executa comando destrutivo sem aprovacao.
- Nenhuma IA mexe em credenciais, `.env`, tokens, secrets ou variaveis locais sensiveis.
- Nenhuma IA altera regra de trade, dado financeiro ou decisao de risco sem registro e aprovacao.
- Nenhuma IA usa modelo/API paga sem teto de custo e classificacao de dado.
- Nenhuma IA entra em RAG/Grafo/LLM Wiki sem fonte, status, escopo e permissao.

## Validacao empirica

Esta matriz nao e dogma. Ela deve ser validada com tarefas reais.

Para cada IA/ferramenta promovida a `ativo` ou `piloto`, registrar:

| Campo | Obrigatorio |
|---|---|
| Tarefa-teste | simples, media ou complexa |
| Fonte/contexto usado | link, nota, SPEC ou issue |
| Resultado | arquivo, resposta, log, midia ou workflow |
| Custo | zero, estimado ou real |
| Tempo | manual ou medido |
| Erros | falhas, alucinacoes, duplicacoes |
| Revisao humana | aprovada, reprovada, ajustes |
| Decisao | manter, rebaixar, testar novamente, descartar |

## Relacoes obrigatorias

- LLM Wiki: [[30_Conhecimento/LLM_Wiki_Pattern]] e [[30_Projetos/FabioOS/LLM_Wiki_FabioOS]]
- MEGATRON: [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]] e [[60_Sistemas/MEGATRON/v0/README_MEGATRON_v0]]
- RAG/MCP Control Plane: [[10_Dashboard/RAG_MCP_Control_Plane]]
- Governanca: [[60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente]] e [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]]
- Skills: [[60_Sistemas/Skills/Inventario_Skills]]
- Specs: [[60_Sistemas/FabioOS/Protocolo_Spec_Driven_FabioOS]]
- Contratos de agentes: [[60_Sistemas/MEGATRON/agentes/README_Agentes]]
- STATUS: [[60_Sistemas/FabioOS/STATUS]]
- NEXT_ACTIONS: [[60_Sistemas/FabioOS/NEXT_ACTIONS]]
- Roteamento de capacidades: [[60_Sistemas/FabioOS/Protocolo_Roteamento_Capacidades_IA]]

## Proxima evolucao

- Criar testes reais para 5 classes: documentacao longa, implementacao, PDF longo, automacao recorrente e multimodalidade.
- Transformar resultados em `Relatorio_Aptidao_IAs_YYYY-MM-DD.md`.
- Atualizar status das IAs conforme evidencia, nao impressao.
