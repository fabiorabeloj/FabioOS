---
tipo: quadro-operacional
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, ias, agentes, subagentes, mcp, rag, grafo, orquestracao]
criado_em: 2026-06-28
atualizado_em: 2026-06-28
---

# Quadro de Comando - IAs e Agentes do FabioOS

## Funcao

Definir quais inteligencias, agentes, conectores e ferramentas existem no FabioOS, quais sao acionaveis agora e qual papel cada uma deve cumprir.

## Regra governante

O FabioOS nao deve virar uma colecao de IAs soltas. Cada IA deve ter papel, limite, custo e modo de acionamento.

Documentos normativos complementares:

- [[40_Repertorio/IA/Modelos_e_IAs/Matriz_de_Aptidao_das_IAs_FabioOS]]
- [[30_Projetos/FabioOS/LLM_Wiki_FabioOS]]
- [[10_Dashboard/RAG_MCP_Control_Plane]]

Ordem de decisao:

1. Usar contexto local: vault, RAG, Grafo e MCP FabioOS.
2. Verificar a Matriz de Aptidao antes de escolher IA/modelo/ferramenta.
3. Verificar `index.md`, `log.md` e schema LLM Wiki antes de criar ou alterar conhecimento.
4. Usar skills/agentes especializados quando o escopo for claro.
5. Usar conectores e MCPs externos apenas com objetivo definido.
6. Usar API/modelo pago apenas quando a camada local nao bastar.
7. Nunca permitir acao externa sensivel sem aprovacao humana.

## Inventario operacional

| IA / capacidade | Acionavel agora? | Papel correto | Controle atual | Proxima ordem |
|---|---|---|---|---|
| Codex | Sim | Operador auxiliar/interino; edicao local, auditoria, scripts, docs | Direto nesta sessao | Continuar frentes seguras e versionaveis |
| Claude Code | Parcial | Lider estrutural e executor tecnico principal | Handoff por arquivo/prompt; app ativo | Aguardar retorno e entregar estado limpo |
| ChatGPT | Manual | Planejamento, estrategia, sintese conceitual | Conversa/manual | Registrar decisoes no vault |
| Claude Web/Desktop | Parcial | Interlocutor analitico complementar | Manual/handoff | Usar com prompt claro e sem colisao |
| MEGATRON v0 | Sim | Interface minima read-only/propose-only sobre RAG/Grafo/MCP | Script local | Usar para consulta com fontes e roteamento |
| RAG local | Sim | Memoria semantica com fontes | Script/MCP FabioOS | Consultar antes de responder sobre conhecimento ja documentado |
| Grafo local | Sim | Relacoes entre sistemas, notas, decisoes e agentes | Script/MCP FabioOS | Usar para dependencias e navegacao relacional |
| MCP FabioOS | Parcial | Porta padronizada read-only para RAG, Grafo e vault | Configurado; nativo apos reload | Recarregar Codex e retestar ferramentas nativas |
| MCP n8n-docs | Sim | Documentacao de nos n8n | Ferramenta MCP ativa | Usar antes de desenhar workflows |
| Gmail connector | Sim com cuidado | Busca/leitura de e-mails autorizados | Ferramenta conectada | Usar por escopo pequeno; sem envio/arquivo sem OK |
| Google Drive connector | Sim com cuidado | Buscar/ler Docs, Sheets, Slides e Drive | Ferramenta conectada | Usar por consulta especifica |
| n8n | Parcial | Automacao previsivel | Docs/MCP; workflows locais pendentes | Reconciliar workflows e testar inbox |
| OpenClaw | Parcial | Gateway conversacional externo | App ativo; instavel/ponte pendente | Nao usar para acoes sensiveis ate estabilizar |
| OpenRouter | Parcial | Modelos por API para sintese/geracao | Token nao necessario para MCP v0 | Ativar so com variavel local e teto de custo |
| Cursor | Manual | Oficina de desenvolvimento de software | App instalado; sem CLI no PATH | Usar para MCP robusto, testes e dashboard |
| Hermes Agent | Nao integrado | Agente autonomo opcional/persistente | App instalado; CLI/API nao confirmada | Descobrir interface antes de integrar |
| Manus | Manual/pendente | Pesquisa longa externa | Sem controle direto nesta sessao | Usar apenas para relatorios que virem fonte |
| Docker/MCP Docker | Sim com cuidado | Infra local, containers e gateway MCP | Processo ativo | Usar com escopo; nao destruir containers sem OK |

## Subagentes e skills

| Agente / skill | Status | Papel | Ordem atual |
|---|---|---|---|
| `explorer` | Funcionou nesta sessao | Auditoria read-only rapida | Usar para perguntas especificas |
| `vault-architect` | Disponivel | Estrutura do vault, mapas e coerencia | Usar antes de reorganizar Obsidian |
| `security-reviewer` | Instavel como spawn; skill existe | Scan de segredos e risco | Usar antes de commits/push |
| `wiki-curator` | Disponivel | Transformar fonte em wiki | Usar apos fonte preservada |
| `school-assistant` | Disponivel | Escola: provas, revisoes, gabaritos, comunicados | Usar sob demanda escolar |
| SafeCommit | Especificado/minimo | Commit seguro, changelog, scan | Manter como guardiao de Git |
| Arquivista | Especificado/minimo | Conteudo bruto -> nota organizada | Usar em Inbox/sources |
| Inbox | Especificado/minimo | Monitorar entradas e rotear | Ativar rotina manual antes de automacao |
| RAG Agent | Especificado/minimo | Consulta/indexacao controlada | Consultar; reindexar so com lock |
| Dashboard | Especificado/minimo | Status, tarefas e pendencias | Atualizar apos frentes importantes |

## Ordens operacionais por frente

### 1. Codex

- Continuar como executor interino ate retorno do Claude.
- Usar RAG/Grafo/MCP antes de responder quando a pergunta for sobre FabioOS.
- Registrar decisoes no vault.
- Nao fazer push.
- Nao tocar em RAG DB, OpenClaw runtime ou contas externas sem OK.

### 2. Claude

- Receber handoff com:
  - commits locais acumulados;
  - MCP FabioOS configurado no Codex;
  - subagente `explorer` funcionando;
  - Hermes instalado mas nao integrado;
  - Cursor como oficina, nao agente autonomo.

### 3. OpenClaw

- Papel: canal externo/visualizacao.
- Nao usar como cerebro central.
- So liberar acoes externas com autorizacao humana.
- Proxima acao: estabilizar autenticacao, QR e workboard antes de WhatsApp real.

### 4. Hermes

- Papel futuro: autonomia persistente.
- Proibido assumir controle de contas, Git, WhatsApp ou vault sem escopo.
- Proxima acao: descobrir se existe CLI, API local, webhooks ou apenas app visual.

### 5. Cursor

- Papel: desenvolvimento profissional.
- Proxima acao: usar para testes do MCP FabioOS e futura interface visual do MEGATRON.
- Nao tratar Cursor como agente autonomo enquanto nao houver workflow documentado.

### 6. Gmail / Google / n8n

- Gmail deve usar conectores ou n8n core nodes, nao login improvisado por Hermes.
- MCP n8n-docs confirmou os nos core:
  - `Gmail`;
  - `Gmail Tool`;
  - `Gmail Trigger`.
- Proxima acao: desenhar workflow de triagem com dry-run, limite e aprovacao.

## Riscos principais

- Dois agentes editarem os mesmos arquivos sem lock.
- Confundir app instalado com agente integrado.
- Enviar dados sensiveis para API externa sem triagem.
- Usar OpenRouter sem teto de custo.
- Deixar OpenClaw/Hermes fazerem acoes externas sem aprovacao.
- Versionar config real com Bearer/token.

## Proxima sequencia recomendada

1. Recarregar Codex para ativar MCP FabioOS como ferramenta nativa.
2. Retestar `fabioos.consultar_rag`, `fabioos.consultar_grafo`, `fabioos.buscar_nota`.
3. Criar handoff para Claude com este quadro.
4. Estabilizar subagentes: `explorer`, `vault-architect`, `security-reviewer`.
5. Depois disso, iniciar frente Google/n8n com Gmail Trigger em modo dry-run.
