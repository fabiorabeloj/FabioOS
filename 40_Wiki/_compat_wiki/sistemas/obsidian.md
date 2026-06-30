---
tipo: wiki
area: sistemas
projeto: FabioOS
status: ativo
camada: camada-1
tags: [obsidian, vault, memória, notas, camada-1]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Obsidian

## Função no FabioOS

[DECISÃO] O Obsidian é o **território central do FabioOS** — a memória humana e navegável do sistema. Todos os outros sistemas orbitam este núcleo. Nenhuma IA ou automação deve substituí-lo como repositório principal de conhecimento.

## O que essa ferramenta faz

[FATO] Editor de Markdown com grafo de conhecimento local. Armazena arquivos `.md` em disco, sem dependência de nuvem. Suporta links internos (`[[wiki]]`), tags, templates, plugins e visualização em grafo.

No FabioOS, o Obsidian cumpre:

- Guardar notas, fontes, decisões e changelogs
- Organizar projetos, áreas e repertório por pastas
- Manter a wiki (`wiki/`) e as fontes (`sources/`)
- Permitir navegação por links internos entre sistemas
- Servir como interface humana de leitura e edição
- Hospedar o schema de regras (`schema/`)

[FATO] Instância atual: vault em `C:\Users\user\Desktop\FabioOs\FabioOs\`. Plugin REST API ativo na porta `27124` (HTTPS, SSL auto-assinado).

## O que essa ferramenta não deve fazer

- Ser usada como único ponto de backup (o GitHub cumpre essa função)
- Receber conteúdo sem frontmatter (quebra o fluxo LLM-Wiki)
- Armazenar credenciais, tokens ou dados sensíveis em notas
- Ser reorganizada automaticamente por IA sem aprovação humana

## Relação com outras ferramentas

| Ferramenta | Relação |
|---|---|
| [[wiki/sistemas/github]] | GitHub versiona o vault do Obsidian |
| [[wiki/sistemas/claude-code]] | Claude Code lê, cria e edita arquivos do vault |
| [[wiki/sistemas/n8n]] | n8n pode salvar notas via REST API ou filesystem |
| [[wiki/conceitos/mcp]] | MCP `obsidian` e `filesystem` expõem o vault a agentes |

## Uso atual

- [x] Vault ativo e versionado no GitHub
- [x] Estrutura de pastas definida (`00_Inbox/` a `90_Arquivo/` + `sources/wiki/schema/`)
- [x] Plugin REST API ativo (porta 27124) — MCP `obsidian` configurado
- [x] Plugin Minimal Settings configurado
- [x] Claude Code opera no vault com leitura e escrita de arquivos

## Uso futuro

- [ ] MCP `obsidian` testado e confirmado funcional (SSL cosmético a validar)
- [ ] Ingestão automática via n8n: webhook → nota no vault
- [ ] Dashboards em `10_Dashboard/` com Dataview ou Canvas
- [ ] RAG sobre o vault (Fase 12)

## Riscos e cuidados

- **SSL auto-assinado**: o MCP `obsidian` falha no health check mas a porta está aberta — comportamento cosmético, não bloqueante; confirmar com teste real antes de depender
- **Reorganização por IA**: nunca mover ou renomear pastas em batch sem revisão humana
- **Conflitos de sync**: se o Obsidian estiver aberto e o Claude Code editar o mesmo arquivo, pode haver conflito — fechar o Obsidian ou usar o vault somente-leitura durante sessões intensas de edição

## Próximas ações

- [ ] Testar MCP `obsidian` com leitura real de uma nota — confirmar se SSL é apenas cosmético
- [ ] Criar `10_Dashboard/` com visão geral do FabioOS
- [ ] Definir template de nota padrão para `00_Inbox/`

## Links internos

- [[wiki/indices/mapa-fabios]]
- [[wiki/sistemas/github]]
- [[wiki/sistemas/claude-code]]
- [[wiki/conceitos/mcp]]
- [[schema/fluxo-wiki]]
- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]
