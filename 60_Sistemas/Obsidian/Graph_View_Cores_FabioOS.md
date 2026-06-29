---
tipo: documentacao
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [obsidian, graph-view, cores, organizacao-visual, fabios]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Graph View - Cores do FabioOS

## Funcao

Documenta a paleta de cores aplicada aos grupos do Graph View do Obsidian no vault FabioOS.

A configuracao foi salva em `.obsidian/graph.json`, no campo `colorGroups`. Cada consulta foi registrada como um grupo individual, para que os nos do grafo recebam cores tematicas sem depender de uma consulta gigante.

Tambem foram adicionadas consultas de compatibilidade para a estrutura real atual do vault, porque parte do FabioOS ainda usa nomes historicos como `10_Mapas`, `20_Projetos`, `30_Conhecimento`, `40_Decisoes` e `50_Fontes`, enquanto a estrutura alvo usa `10_Dashboard`, `20_Areas`, `30_Projetos`, `40_Repertorio` e `50_Registros`.

## Principio de cores

As cores seguem uma leitura operacional do FabioOS:

| Cor | Sentido | Uso no grafo |
|---|---|---|
| Cinza | Entrada, arquivo, neutro | Materiais brutos, arquivados ou infraestrutura GitHub |
| Amarelo | Painel, atencao, avaliacao | Dashboards, provas, avaliacoes e itens que pedem foco |
| Azul | Escola, organizacao, rotina | Areas continuas, escola, estudos e aulas |
| Roxo | Projetos, IA, criacao abstrata | Projetos, agentes, RAG, MCP, MEGATRON e sistemas de IA |
| Verde | Conhecimento, crescimento, financas | Repertorio, geografia, trader, bancos vetoriais e financas |
| Laranja | Decisoes, registros, movimento | Changelogs, decisoes, reunioes e OpenRouter |
| Vermelho | Sistemas, automacao, infraestrutura critica | Sistemas tecnicos, automacao, tecnologia e saude |
| Vinho / roxo escuro | Filosofia e vida pessoal | Filosofia, vida pessoal e reflexao |

## Consultas aplicadas

### Cinza - entrada, arquivo, neutro

Cor usada: `#8A8F98` (`rgb`: `9080728`).

- `path:"00_Inbox"`
- `path:"90_Arquivo"`
- `path:"50_Fontes"`
- `path:"sources"`
- `file:GitHub`
- `path:"60_Sistemas/GitHub"`

### Amarelo - painel, atencao, avaliacao

Cor usada: `#E0B852` (`rgb`: `14727250`).

- `path:"10_Dashboard"`
- `path:"10_Mapas"`
- `path:"20_Areas/Escola/Avaliacoes"`
- `tag:#avaliacao`
- `tag:#prova`

### Azul - escola, organizacao, rotina

Cor usada: `#4A90E2` (`rgb`: `4886754`).

- `path:"20_Areas"`
- `path:"20_Areas/Escola"`
- `path:"20_Areas/Estudos"`
- `path:"20_Areas/Escola/Aulas"`
- `tag:#aula`

### Roxo - projetos, IA, criacao abstrata

Cor usada: `#8E44AD` (`rgb`: `9323693`).

- `path:"30_Projetos"`
- `path:"20_Projetos"`
- `path:"90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/PRIMUS"`
- `path:"30_Projetos/FabioOS"`
- `path:"30_Projetos/PRIMUS"`
- `path:"30_Projetos/Atendimento_Pietra"`
- `path:"30_Projetos/IA"`
- `path:"90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Repertorio/IA"`
- `path:"60_Sistemas/Claude_Code"`
- `path:"60_Sistemas/ChatGPT"`
- `file:MEGATRON`
- `file:RAG`
- `file:MCP`
- `file:"Grafos de conhecimento"`
- `tag:#ia`
- `tag:#megatron`
- `tag:#rag`
- `tag:#mcp`
- `tag:#agente`
- `tag:#agentes`

### Verde - conhecimento, crescimento, financas

Cor usada: `#2ECC71` (`rgb`: `3066993`).

- `path:"40_Repertorio"`
- `path:"30_Conhecimento"`
- `path:"90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Repertorio/Geografia"`
- `path:"20_Areas/Financas"`
- `path:"30_Projetos/Trader"`
- `file:Supabase`
- `file:Pinecone`
- `file:"Banco Vetorial"`
- `tag:#geografia`
- `tag:#trader`

### Laranja - decisoes, registros, movimento

Cor usada: `#E67E22` (`rgb`: `15105570`).

- `path:"50_Registros"`
- `path:"40_Decisoes"`
- `path:"50_Registros/Decisoes"`
- `path:"50_Registros/Changelog"`
- `path:"50_Registros/Reunioes"`
- `path:"60_Sistemas/OpenRouter"`
- `tag:#decisao`
- `tag:#changelog`
- `tag:#reuniao`

### Vermelho - sistemas, automacao, infraestrutura critica

Cor usada: `#E74C3C` (`rgb`: `15158332`).

- `path:"60_Sistemas"`
- `path:"00_Arquitetura"`
- `path:"60_Sistemas/n8n"`
- `path:"60_Sistemas/OpenClaw"`
- `path:"60_Sistemas/Obsidian"`
- `path:"60_Sistemas/Agentes"`
- `path:"90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Repertorio/Automacao"`
- `path:"90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Repertorio/Tecnologia"`
- `path:"90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/30_Conhecimento/Tecnologia"`
- `path:"20_Areas/Saude"`
- `tag:#automacao`
- `tag:#tecnologia`

### Vinho / roxo escuro - filosofia e vida pessoal

Cor usada: `#7B1E3A` (`rgb`: `8068666`).

- `path:"90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Repertorio/Filosofia"`
- `path:"20_Areas/Vida_Pessoal"`
- `tag:#filosofia`

## Observacao sobre ordem dos grupos

Algumas consultas sao amplas e podem englobar consultas mais especificas. Exemplos:

- `path:"20_Areas"` tambem inclui `path:"20_Areas/Saude"` e `path:"20_Areas/Financas"`.
- `path:"60_Sistemas"` tambem inclui `path:"60_Sistemas/OpenRouter"`, `path:"60_Sistemas/Claude_Code"` e `path:"60_Sistemas/ChatGPT"`.
- `path:"40_Repertorio"` tambem inclui `path:"90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Repertorio/Filosofia"`, `path:"90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Repertorio/IA"` e `path:"90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Repertorio/Tecnologia"`.
- `path:"30_Conhecimento"` tambem inclui `path:"90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/30_Conhecimento/Tecnologia"`.
- `path:"20_Projetos"` tambem inclui `path:"90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/PRIMUS"`.

Por isso, as consultas mais especificas foram colocadas antes das consultas amplas no JSON. Se o Obsidian aplicar prioridade visual de forma diferente em alguma versao, ajuste manualmente a ordem dos grupos pela interface.

## Como alterar manualmente no Obsidian

1. Abra o Obsidian no vault FabioOS.
2. Abra o Graph View.
3. Clique no icone de engrenagem do Graph View.
4. Abra a secao de grupos.
5. Para alterar uma cor, edite o grupo correspondente e escolha uma nova cor.
6. Para ajustar prioridade, arraste os grupos deixando consultas especificas antes das consultas amplas.
7. Feche e reabra o Graph View se a visualizacao nao atualizar imediatamente.

## Backup

Antes da alteracao, foi criado o backup:

`C:\Users\user\Desktop\FabioOs\FabioOs\.obsidian\graph.json.backup-2026-06-27-graph-colors-fabios.json`

## Relacoes

- [[wiki/sistemas/obsidian]]
- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]
- [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]]

## Proximas acoes

- [ ] Abrir o Graph View no Obsidian e verificar se a ordem dos grupos produz a prioridade visual esperada.
- [ ] Ajustar manualmente tons ou prioridade se alguma categoria ficar visualmente ambigua.
