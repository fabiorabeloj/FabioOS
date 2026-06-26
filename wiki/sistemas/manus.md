---
tipo: wiki
area: sistemas
projeto: FabioOS
status: pendente
camada: camada-1
tags: [manus, pesquisa, executor-externo, ia, camada-1]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Manus

## Função no FabioOS

[DECISÃO] O Manus é o **executor externo de tarefas longas** do FabioOS — realiza pesquisas web, navega em sites, compara ferramentas e produz relatórios que o Claude Code não conseguiria executar eficientemente dentro do tempo de sessão.

## O que essa ferramenta faz

[FATO] Agente de IA com capacidade de navegação web autônoma, execução de tarefas prolongadas e produção de relatórios estruturados. Opera de forma assíncrona — recebe uma tarefa e entrega o resultado.

No FabioOS, o Manus deve cumprir:

- Pesquisar e comparar ferramentas, bibliotecas ou abordagens
- Navegar em documentações extensas e extrair informações relevantes
- Montar relatórios de pesquisa para embasar decisões
- Coletar referências externas para alimentar `sources/research/`
- Executar tarefas de coleta de dados que exigem muita navegação

Fluxo integrado:

```
Manus executa pesquisa externa
        ↓
Entrega relatório estruturado
        ↓
sources/research/<nome>.md
        ↓
Claude Code processa
        ↓
wiki/
```

[FATO] Status atual: **não integrado tecnicamente**. Mencionado no Plano Mestre e na estratégia do FabioOS. Nenhum workflow de importação de resultados definido ainda.

## O que essa ferramenta não deve fazer

- Substituir a curadoria humana — relatórios do Manus são fontes, não decisões
- Operar dados sensíveis (credenciais, dados pessoais, dados de alunos)
- Ser o repositório dos resultados — tudo que produz deve entrar no vault

## Relação com outras ferramentas

| Ferramenta | Relação |
|---|---|
| [[wiki/sistemas/obsidian]] | Destino dos relatórios: `sources/research/` |
| [[wiki/sistemas/claude-code]] | Claude Code transforma relatórios do Manus em wiki |
| [[wiki/sistemas/playwright-mcp]] | Para navegação web dentro do Claude Code, usar playwright-mcp primeiro |

## Uso atual

- [ ] Nenhum — **pendente de integração** (Fase 16)

## Uso futuro

- [ ] Pesquisa de ferramentas para novas fases do FabioOS
- [ ] Coleta de referências para `wiki/conceitos/`
- [ ] Relatórios de benchmark entre tecnologias
- [ ] Pesquisa de mercado para sistema Trader

## Riscos e cuidados

- **Confiabilidade da fonte**: resultados do Manus devem ser verificados antes de virar wiki — tratar como fonte bruta, não verdade
- **Injeção de prompt**: se o Manus navegar em sites maliciosos, pode receber conteúdo projetado para manipular IAs — revisar antes de processar
- **Custo de tarefas longas**: avaliar custo de cada tarefa antes de acionar

## Próximas ações

- [ ] Criar pasta `sources/research/` para receber outputs do Manus
- [ ] Definir template de relatório de pesquisa esperado do Manus
- [ ] Testar com uma pesquisa simples e comparar com resultado do playwright-mcp

## Links internos

- [[wiki/indices/mapa-fabios]]
- [[wiki/sistemas/obsidian]]
- [[wiki/sistemas/claude-code]]
- [[wiki/sistemas/playwright-mcp]]
- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]
