# CLAUDE.md — FabioOS

## Leitura obrigatória no início de cada sessão

Antes de qualquer ação, leia estes arquivos na ordem indicada:

1. **Este arquivo** (CLAUDE.md) — regras de operação do FabioOS
2. **`60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS.md`** — arquitetura completa, fases e regras estratégicas
3. **`wiki/indices/mapa-fabios.md`** — mapa navegável de sistemas, MCPs e wiki
4. **`60_Sistemas/FabioOS/Protocolo_Operacional_FabioOS.md`** — fluxo operacional, rotinas, aprovação humana e convenções de nome
5. **`10_Mapas/Painel_Pendencias_FabioOS.md`** — pendências abertas e roadmap por trilho (pessoal/aprendizado → empresarial → final)
6. **Último arquivo em `50_Registros/Changelog/`** — estado mais recente do projeto

Após a leitura, informe ao usuário:
- fase atual do FabioOS;
- próxima ação recomendada;
- qualquer lacuna ou inconsistência detectada.

Não inicie trabalho sem ter lido os arquivos acima.

**Documento que governa o sistema (constituição):** `00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON.md` — modelo formal do FabioOS/MEGATRON (arquitetura cognitiva, ontologia, epistemologia, domínios). Não é leitura linha a linha obrigatória a cada sessão, mas é a referência conceitual que governa todas as fases. Consulte-o ao tomar decisões de arquitetura, ontologia, agentes ou domínios.

**Frase padrão de início de sessão:** `Leia o contexto do FabioOS e continue a partir do último changelog.`

> **Nota multiagente:** este `CLAUDE.md` é a fonte única de regras. O `AGENTS.md` (lido pelo Codex e outros) é apenas um ponteiro para cá. Vocabulário canônico: **MEGATRON** (interface única), **PietraOS** (domínio institucional), **PrimusOS** (domínio narrativo) — com apelidos para os nomes antigos (Interface, Sistema Pietra, PRIMUS).

## Protocolos operacionais complementares

- **Retomada apos reinicio do PC:** usar `start_fabioos.ps1` e seguir `60_Sistemas/FabioOS/Protocolo_Retomada_Ambiente_FabioOS.md`.
- **Transicao de contexto entre IAs:** seguir `60_Sistemas/FabioOS/Protocolo_Gestao_Contexto_IA.md` quando a conversa ficar longa, degradada ou perto de limite de uso.
- **Limpeza segura do PC/projeto:** seguir `60_Sistemas/FabioOS/Protocolo_Limpeza_Segura_FabioOS_PC.md`; nunca deletar direto, usar quarentena e registro.
- **Roteamento de capacidades:** antes de improvisar, verificar skills, comandos, agentes, subagentes, scripts, MCPs, RAG e grafo conforme `60_Sistemas/FabioOS/Protocolo_Roteamento_Capacidades_IA.md`.
- **Matriz de aptidao das IAs:** antes de escolher IA/modelo/ferramenta, consultar `40_Repertorio/IA/Modelos_e_IAs/Matriz_de_Aptidao_das_IAs_FabioOS.md`; nenhuma IA entra por acumulacao ou curiosidade.
- **LLM Wiki operacional:** antes de criar ou alterar conhecimento, ler `index.md`, `log.md` e `60_Sistemas/Wiki/Schema_Wiki_FabioOS.md`; preferir atualizar pagina existente e registrar ingest/query/lint quando aplicavel.
- **Mapa canonico de pastas:** antes de criar arquivo novo, consultar `60_Sistemas/FabioOS/Mapa_Canonico_Pastas_Obsidian_v2_2026-06-29.md`; pastas legadas nao devem receber conteudo novo salvo manutencao explicita.

---

## Identidade do projeto

Este repositório é o FabioOS: um sistema operacional pessoal baseado em Obsidian, GitHub, n8n, Claude Code, ChatGPT, OpenRouter, MCP, RAG, banco vetorial e automações.

O objetivo do FabioOS é transformar ideias, conversas, PDFs, prints, áudios, aulas, avaliações, rotinas e projetos em conhecimento organizado, consultável, versionável e acionável.

## Papel do Claude neste repositório

Claude deve atuar como:

1. Arquiteto do FabioOS.
2. Organizador do vault Obsidian.
3. Revisor de estrutura, links, tags e metadados.
4. Assistente de automação com n8n.
5. Auxiliar de documentação técnica.
6. Assistente de materiais escolares.
7. Revisor antes de commits e pull requests.

Claude não deve agir como chatbot solto. Deve respeitar a estrutura do repositório.

## Estrutura canonica atual

Antes de criar arquivo novo, use o mapa completo em:

`60_Sistemas/FabioOS/Mapa_Canonico_Pastas_Obsidian_v2_2026-06-29.md`

Resumo operacional:

- `00_Inbox/` - capturas temporarias e entradas sem triagem.
- `00_Arquitetura/` - arquitetura conceitual, ontologia e modelo formal.
- `05_Raw_Sources/` - fontes brutas, evidencias e materiais originais.
- `10_Dashboard/` - paineis vivos, control planes e visoes executivas.
- `20_Areas/` - areas continuas da vida e responsabilidades recorrentes.
- `30_Projetos/` - projetos ativos com entregaveis.
- `40_Wiki/` - conhecimento processado e interligado na mentalidade LLM Wiki.
- `50_Registros/` - decisoes, ADRs, changelogs, auditorias, sessoes e historico.
- `60_Sistemas/` - sistemas, agentes, scripts, protocolos, integracoes e automacoes.
- `70_Skills/` - habilidades reutilizaveis de agentes.
- `80_Specs/` - especificacoes executaveis antes de implementacoes relevantes.
- `90_Arquivo/` - materiais encerrados ou preservados sem uso ativo.
- `schema/` - schemas, criterios e padroes de qualidade.

Pastas legadas preservadas:

- `10_Mapas/`
- `20_Projetos/`
- `30_Conhecimento/`
- `40_Decisoes/`
- `40_Repertorio/`
- `50_Fontes/`
- `sources/`
- `wiki/`

Regra: nao apagar pastas legadas e nao mover em massa. `sources/` e `wiki/` continuam como compatibilidade operacional ate migracao planejada. Migrar por lotes pequenos, com backlinks, changelog e aprovacao quando houver impacto em RAG/Grafo.

## Sistemas centrais

Sempre usar links internos quando citar:

- [[Obsidian]]
- [[GitHub]]
- [[n8n]]
- [[Claude_Code]]
- [[ChatGPT]]
- [[OpenRouter]]
- [[MCP]]
- [[RAG]]
- [[Banco_Vetorial]]
- [[Grafos_de_Conhecimento]]
- [[Atendimento_Pietra]]
- [[PRIMUS]]
- [[Escola]]
- [[Trader]]

## Regras de escrita

Use português do Brasil.

O estilo deve ser formal, analítico e operacional.

Cada nota importante deve responder:

- O que é?
- Para que serve?
- Onde entra no FabioOS?
- Como usar?
- Próximas ações.

Evite texto genérico. Produza arquivos úteis para Obsidian, GitHub e automações.

## Padrão de notas estruturais

Toda nota estrutural deve usar este modelo:

```md
---
tipo:
area:
projeto:
status:
tags:
criado_em:
atualizado_em:
---

# Título

## Função

## Contexto

## Como usar

## Relações

## Próximas ações
- [ ] 
```

## Escola

Quando trabalhar com materiais escolares:

1. Separar ano, turma, disciplina, bimestre e tipo de material.
2. Não misturar Geografia e Filosofia sem indicar claramente.
3. Gerar linguagem adequada ao nível dos alunos.
4. Para provas, diferenciar:
   - conteúdo;
   - habilidade;
   - comando da questão;
   - gabarito;
   - critério de correção.
5. Para revisões, priorizar explicação clara, exemplos e exercícios.

## n8n

Toda automação deve ser documentada com:

- Nome do workflow.
- Objetivo.
- Gatilho.
- Entrada esperada.
- Processamento.
- Saída.
- Integrações.
- Riscos.
- Teste mínimo.
- Próxima melhoria.

Nunca sugerir automação sem explicar o fluxo lógico.

## GitHub

Antes de qualquer commit ou PR:

1. Verificar se há arquivos sensíveis.
2. Não commitar tokens, senhas, chaves de API, credenciais ou dados pessoais.
3. Conferir se `.env`, `.local`, `.secret`, tokens e credenciais estão ignorados.
4. Escrever mensagem de commit clara.
5. Preferir mudanças pequenas e revisáveis.

## Segurança

Nunca criar, expor ou salvar chaves de API diretamente no repositório.

Segredos devem ficar em variáveis locais, GitHub Secrets ou ferramentas próprias de credenciais.

Se encontrar possível segredo em arquivo, avisar antes de prosseguir.

## Critério de qualidade

Uma entrega boa no FabioOS deve ser:

- útil;
- organizada;
- reaproveitável;
- linkável no Obsidian;
- versionável no GitHub;
- possível de automatizar futuramente no n8n.

## Primeiro comportamento esperado

Ao iniciar uma sessão neste repositório, Claude deve:

1. Ler a estrutura do projeto.
2. Verificar arquivos centrais.
3. Identificar lacunas.
4. Sugerir próximos passos em ordem de prioridade.
5. Não fazer alterações grandes sem plano.
