---
tipo: sistema
area: tecnologia
status: ativo
tags: [tecnico, Obsidian, vault]
criado_em: 2026-06-25
atualizado_em: 2026-06-25
---

# Obsidian

## O que é?

Obsidian é aplicativo de notas baseado em markdown que permite criar um vault conectado (conhecimento em rede). Suporta plugins, temas e sincronização.

## Para que serve?

- Armazenar e organizar [[30_Conhecimento|conhecimento]] do FabioOS
- Criar links bidirecionais entre notas
- Visualizar grafos de conceitos
- Usar templates e automações via plugins
- Interface local e rápida

## Plugins essenciais

- **Obsidian Git**: Sincronizar com [[GitHub]]
- **Dataview**: Queries estruturadas em MD
- **Templater**: Templates dinâmicos
- **Tasks**: Gerenciar tarefas e checkboxes
- **Sodalite Theme**: Tema integrado

## Onde entra no FabioOS?

[[60_Sistemas|Sistemas]] > [[Obsidian]] → core:
- Interface principal de edição
- Armazenamento do vault
- Visualização de links
- Execução de automações via plugins

## Fluxo de sincronização

```
Local editing (Obsidian)
    ↓ [Obsidian Git plugin]
GitHub commit
    ↓ [GitHub webhook]
n8n trigger
    ↓ [Processing]
Sync back to Obsidian
```

## Relações

- ↔ [[GitHub]] — sincronização bidirecional
- ↔ [[n8n]] — automações
- ↔ [[MCP]] — integração com Claude
- → [[30_Conhecimento|Conhecimento]] — storage

## Próximas ações

- [ ] Atualizar plugins
- [ ] Revisar tema Sodalite
- [ ] Testar sincronização GitHub
- [ ] Documentar atalhos principais
