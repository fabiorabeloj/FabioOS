---
tipo: catalogo
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, megatron, arquitetura, ferramentas, assimilacao, roadmap]
criado_em: 2026-06-28
atualizado_em: 2026-06-28
fonte: [[sources/docs/2026-06-28_anuncios-ia-roadmap-fabioos]]
---

# Catalogo - Caminhos e Ferramentas Demonstradas

## Funcao

Registrar o que o prompt ensina em termos de caminhos, demonstracoes e ferramentas, separando:

- o padrao arquitetural;
- a ferramenta citada;
- onde ela entra no FabioOS;
- como testar sem risco;
- quando promover para parte oficial da estrutura.

Este catalogo aplica o metodo do [[30_Conhecimento/Tecnologia/Arquiteturas_de_Mercado_Radar_Tecnologico]] ao FabioOS.

## Principio

Fabio pode possuir muitos recursos. O FabioOS precisa transformar esses recursos em arquitetura.

Toda ferramenta deve ocupar um lugar claro:

```text
entrada -> memoria/fonte -> processamento -> ferramenta/agente -> log -> dashboard -> decisao
```

Se uma ferramenta nao encaixa nesse fluxo, ela fica em observacao.

## Processo de extracao do radar

Para cada imagem, video, propaganda, artigo, demo ou ferramenta, registrar:

| Etapa | Pergunta |
|---|---|
| Problema | Qual problema esta sendo resolvido? |
| Arquitetura | Como o sistema funciona do usuario ate o resultado? |
| Tecnologias | Quais linguagens, frameworks, bancos, APIs, clouds, IAs e ferramentas aparecem? |
| Conceitos | Quais conceitos estruturais aparecem: MCP, RAG, agentes, eventos, contexto, observabilidade? |
| Padrao recorrente | Isso aparece em varias empresas ou e caso isolado? |
| Aplicacao no FabioOS | Entra imediatamente, futuramente ou deve ser descartado? |
| Prioridade | 5/5 essencial, 4/5 muito importante, 3/5 importante, 2/5 opcional, 1/5 referencia |

## Caminhos demonstrados pelo prompt

| Caminho demonstrado | O que ensina | Encaixe no FabioOS | Teste minimo |
|---|---|---|---|
| IA gera notas Markdown -> Obsidian | Conteudo produzido por IA deve virar fonte estruturada, nao conversa perdida | Inbox, Arquivista, Obsidian, RAG | Capturar uma nota MD, salvar em `sources/`, gerar wiki e consultar no RAG |
| OpenClaw/WhatsApp -> agente -> tarefa/email/banco | Canal conversacional precisa de escopo e permissao | Fase 11, n8n, agente Inbox, OpenClaw | Receber mensagem de teste, criar nota local sem envio externo |
| MEGATRON -> MCP Gateway -> ferramentas | IAs nao devem acessar sistemas diretamente; devem passar por ferramentas padronizadas | Fases 14-15, MCP FabioOS | Consultar RAG/Grafo via MCP read-only |
| Spec -> plano -> tarefas -> codigo -> testes -> docs | O futuro do desenvolvimento e especificacao antes da implementacao | Metodo transversal, Cursor, Claude, Codex | Criar uma SPEC pequena e gerar checklist/teste antes do codigo |
| Agentes especializados -> dominios especializados | A escala vem de papeis e memorias separadas | FabioOS, PietraOS, TraderOS, PrimusOS, IAOS | Matriz de dominios/dados/permissoes |
| Dashboard unico -> agentes/projetos/custos/logs | Sistema profissional precisa ser visivel | Fase 21 e 21.5 | Dashboard textual ja existe; evoluir para painel visual |
| Obsidian + Supabase + MongoDB + Vector DB + Grafo | Cada tipo de dado precisa de armazenamento apropriado | Data Platform 20.5 | Definir o que fica em Markdown, SQL, documento, vetor e grafo |
| Linux/Docker/VPS -> producao | Servicos permanentes precisam de ambiente reprodutivel | Fase 23 e 23.5 | Rodar um servico em Docker com backup e rollback documentado |
| Vercel/Cloudflare -> app publico | Deploy moderno exige borda, dominio e CI/CD | Fase 23.5 / 25 | So usar quando houver interface/app externo |
| Stripe/Resend/PostHog -> produto | Produto real exige pagamento, e-mail e metricas | Fase 25 ProductOS | Aguardar produto/usuario externo |
| LLM local/hardware -> privacidade/custo | Infra local pode proteger dados, mas so depois de medir uso | Fase 26 | Avaliar apenas apos mapa de custo e privacidade |

## Ferramentas e papel correto

| Ferramenta / recurso | Papel correto no FabioOS | Status recomendado |
|---|---|---|
| Claude | lider estrutural, specs, arquitetura e revisao | usar continuamente |
| Codex | execucao, patch, testes, automacao e verificacao local | usar continuamente |
| ChatGPT / GPT | dialogo, ideacao e sintese quando util | usar com registro quando gerar decisao |
| Gemini | util para ecossistema Google e comparacao | avaliar na Fase 20 |
| Cursor | oficina de software para MCP, dashboards, testes e interface | usar em tarefas de desenvolvimento maior |
| Hermes | executor opcional se tiver CLI/API/logs claros | nao promover sem prova |
| OpenClaw | canal conversacional/gateway, nao memoria principal | estabilizar auth, logs e escopo |
| n8n | workflows externos, gatilhos, credenciais e integrações | alta prioridade |
| Python | automacao local, validadores, workers e scripts | linguagem principal |
| MCP | contrato padrao entre agentes e ferramentas | prioridade maxima |
| RAG | memoria semantica com fontes | ja operacional, evoluir limiar |
| Grafo | relacoes, dependencias e navegacao | ja operacional, evoluir ontologia |
| Supabase/PostgreSQL | estados, metadados, tarefas, custos, usuarios | subfase 20.5 |
| MongoDB | sessoes, logs de agentes, documentos flexiveis | complementar, nao agora |
| Vercel | deploy de frontend/app | futuro |
| Cloudflare | dominio, DNS, borda e protecao | futuro |
| Stripe | pagamentos | apenas ProductOS |
| Resend | e-mail transacional | apenas ProductOS |
| PostHog | analytics e produto | quando houver usuarios |
| Docker | ambiente reprodutivel | alto valor |
| Linux/VPS | producao e agentes permanentes | alto valor, gradual |
| Kubernetes/Kafka | escala avancada | futuro distante |

## Demonstracoes que viram requisitos

### 1. Notas de IA entram no Obsidian

Requisito:

- toda nota produzida fora do FabioOS deve entrar como fonte;
- deve ter origem, data, autor, status e tag;
- so vira wiki depois de avaliacao;
- so entra no RAG depois de privacidade validada.

### 2. Multiplas IAs nao sao o centro

Requisito:

- IAs sao substituiveis;
- memoria, permissoes e logs sao permanentes;
- MEGATRON deve rotear por capacidade, nao por preferencia de modelo.

### 3. Varios cerebros especializados

Requisito:

- FabioOS central nao deve misturar tudo;
- dominios devem ter fronteiras;
- cada dominio pode ter RAG, grafo, permissoes e dashboard proprios quando justificar.

### 4. MCP Gateway

Requisito:

- nenhum agente deve operar ferramenta critica diretamente;
- toda ferramenta oficial deve ter contrato;
- ferramentas de escrita devem ser separadas das ferramentas read-only;
- logs devem indicar agente, ferramenta, entrada, saida e decisao humana.

### 5. Spec-Driven Development

Requisito:

- antes de software grande, criar SPEC;
- SPEC gera tarefas;
- tarefas geram implementacao;
- implementacao gera teste;
- teste gera changelog;
- changelog atualiza mapa/dashboard.

### 6. Observabilidade

Requisito:

- todo agente relevante deve ter status;
- todo workflow relevante deve ter ultimo teste;
- todo custo de API deve ser estimado;
- erros devem aparecer no dashboard;
- automacao sem log nao e profissional.

## Arquitetura consolidada sugerida

```text
Fabio
  -> MEGATRON
      -> Context Engineering
      -> Spec-Driven Development
      -> Roteador de capacidades
      -> Agentes especializados
      -> MCP Gateway
          -> Obsidian / GitHub
          -> RAG / Grafo
          -> n8n / OpenClaw
          -> Google / Gmail / Drive / Calendar
          -> Data Platform
          -> Deploy Stack
          -> Observability Stack
      -> Dashboard unico
```

## Como usar este catalogo

Ao Fabio enviar um novo anuncio, print, ferramenta ou ideia:

1. identificar qual caminho ele demonstra;
2. verificar se ja existe capacidade equivalente no FabioOS;
3. mapear para fase/subfase;
4. registrar risco, custo e teste minimo;
5. criar SPEC antes de implementar;
6. atualizar o dashboard e o changelog.

## Implementacao v0

O primeiro mecanismo operacional desta frente e:

`60_Sistemas/FabioOS/scripts/radar_tecnologico.py`

Uso:

```powershell
python 60_Sistemas/FabioOS/scripts/radar_tecnologico.py caminho\para\material.txt --title "Titulo do material"
```

Ele gera uma nota em `30_Conhecimento/Tecnologia/Radar/` com:

- problema;
- arquitetura;
- tecnologias detectadas;
- conceitos;
- padroes recorrentes;
- aplicacao no FabioOS;
- prioridade;
- decisao operacional sugerida.

Limite: o v0 usa deteccao local por sinais/palavras-chave. Nao substitui revisao humana nem validacao em fontes primarias.
