---
tipo: documentação
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [claude-desktop, claude-code, operação, workflow, sessão]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Operação do FabioOS no Claude Desktop

## Função

Define como continuar o trabalho diário do FabioOS a partir do Claude Desktop (app nativo), sem depender do PowerShell como interface principal. Inclui o fluxo de início de sessão, diferenças entre ambientes e quando cada ferramenta deve ser usada.

## Contexto

O FabioOS foi desenvolvido inicialmente via PowerShell + Claude Code CLI. A partir da Fase 11, a operação migra para o **Claude Desktop** como interface padrão — mais fluida, com suporte a MCPs, skills, agentes e comandos slash, sem necessidade de abrir terminal.

**Documento de referência:** [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]

---

## Como abrir o FabioOS no Claude Desktop

### Pré-requisito: projeto configurado

O Claude Desktop deve ter o projeto `FabioOs` apontando para:

```
C:\Users\user\Desktop\FabioOs\FabioOs
```

Para verificar: abra o Claude Desktop → menu lateral → "Projects" → confirme que `FabioOs` aparece na lista e está apontando para o diretório correto.

Se ainda não estiver configurado:
1. Abra o Claude Desktop
2. Clique em **"Add Project"** (ou equivalente na versão atual)
3. Selecione a pasta `C:\Users\user\Desktop\FabioOs\FabioOs`
4. O Claude lerá automaticamente o `CLAUDE.md` e registrará a configuração

### Início de sessão

Ao abrir uma conversa neste projeto, use a frase padrão:

> **`Leia o contexto do FabioOS e continue a partir do último changelog.`**

Isso instrui o Claude a:
1. Ler `CLAUDE.md`
2. Ler `60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS.md`
3. Ler `wiki/indices/mapa-fabios.md`
4. Ler `60_Sistemas/FabioOS/Protocolo_Operacional_FabioOS.md`
5. Ler o último arquivo em `50_Registros/Changelog/`
6. Informar fase atual, próxima ação e lacunas detectadas

---

## Arquivos que o Claude deve ler no início

| Ordem | Arquivo | Por que |
|---|---|---|
| 1 | `CLAUDE.md` | Regras de operação, papel do Claude, estrutura do vault |
| 2 | `60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS.md` | Arquitetura completa e fases 0–23 |
| 3 | `wiki/indices/mapa-fabios.md` | Mapa navegável de todos os sistemas |
| 4 | `60_Sistemas/FabioOS/Protocolo_Operacional_FabioOS.md` | Fluxo operacional e convenções |
| 5 | Último arquivo em `50_Registros/Changelog/` | Estado atual do projeto |

O CLAUDE.md já define essa ordem obrigatória. O Claude seguirá automaticamente se a frase padrão de início for usada.

---

## Como continuar o trabalho sem usar PowerShell

### O que você pode fazer diretamente no Claude Desktop

| Ação | Como fazer |
|---|---|
| Criar e editar notas do vault | Peça ao Claude diretamente ("crie uma nota sobre X") |
| Executar comandos FabioOS | Digite `/nome-do-comando` na conversa |
| Acionar agentes especializados | Peça ao Claude ("use o agente vault-architect") |
| Commitar com segurança | Use `/safe-commit` |
| Gerar materiais escolares | Use `/criar-prova`, `/criar-revisao`, `/criar-gabarito` |
| Ingerir fontes externas | Use `/ingest-url`, `/ingest-pdf`, `/ingest-doc` |
| Simular mensagens Pietra | Use `/simular-mensagem-pietra "mensagem"` |
| Verificar segredos antes de commit | Use `/check-secrets` |
| Gerar changelog da sessão | Use `/session-changelog` |

### Comandos disponíveis (`.claude/commands/`)

| Comando | Função |
|---|---|
| `/archive-source` | Arquiva fonte bruta em `sources/` |
| `/source-to-wiki` | Transforma fonte em página `wiki/` |
| `/update-index` | Atualiza índices de sources e wiki |
| `/check-secrets` | Escaneia por credenciais antes do commit |
| `/session-changelog` | Gera changelog da sessão |
| `/safe-commit` | Fluxo completo de commit com segurança |
| `/criar-prova` | Gera prova escolar (GEO/FIL) |
| `/criar-revisao` | Gera revisão de conteúdo escolar |
| `/criar-gabarito` | Gera gabarito estruturado |
| `/criar-comunicado` | Gera comunicado escolar |
| `/ingest-url` | Ingere conteúdo de URL |
| `/ingest-pdf` | Ingere conteúdo de PDF |
| `/ingest-doc` | Ingere documento genérico |
| `/normalize-source` | Normaliza metadados de fonte |
| `/check-source-quality` | Avalia qualidade de fonte |
| `/simular-mensagem-pietra` | Testa classificação Pietra sem infraestrutura |

### Agentes disponíveis (`.claude/agents/`)

| Agente | Quando usar |
|---|---|
| `vault-architect` | Auditar ou reorganizar estrutura do vault |
| `wiki-curator` | Transformar sources/ em wiki/ com revisão humana |
| `security-reviewer` | Detectar tokens e credenciais antes de commits |
| `school-assistant` | Criar e organizar materiais pedagógicos (GEO/FIL) |

---

## Quando ainda será necessário usar PowerShell

O PowerShell continua necessário para operações de infraestrutura que o Claude Desktop não executa diretamente:

| Situação | Motivo |
|---|---|
| Subir/parar containers Docker (n8n, Evolution API) | Operações de sistema fora do vault |
| Instalar dependências globais (Bun, Node, etc.) | Administração do sistema operacional |
| Criar junctions para skills (`mklink /J`) | Operação de sistema de arquivos NTFS |
| Configurar variáveis de ambiente globais | Requer shell administrativo |
| Rodar scripts de setup de infraestrutura | Scripts `.ps1` ou `.bat` do FabioOS |
| Verificar status de processos em background | `Get-Process`, `netstat`, etc. |

**Regra prática:** se a ação mexe com Docker, PATH, arquivos fora do vault ou permissões do sistema → use PowerShell. Se a ação é sobre o vault, conhecimento, código ou automações do FabioOS → use Claude Desktop.

---

## Diferença entre os ambientes

| Ambiente | O que é | Quando usar |
|---|---|---|
| **Claude Desktop** | App nativo com projeto FabioOS carregado | Operação diária, criação de conteúdo, execução de comandos, agentes |
| **Claude Code CLI** | Claude no terminal PowerShell/Bash | Quando precisa de terminal + Claude integrados (debugging de scripts, execução shell) |
| **VS Code** | Editor de código com extensão Claude | Edição de código pesado, multi-arquivo, com diff visual |
| **Cursor** | IDE com IA integrada nativamente | Desenvolvimento de software novo (projetos de código, MCPs customizados) |
| **OpenClaw** | Gateway WhatsApp/Telegram via Evolution API + n8n | Receber e responder mensagens externas (Pietra, alunos, pais) |
| **n8n** | Orquestrador de automações (localhost:5678) | Criar e monitorar workflows automáticos entre sistemas |

### Qual usar para cada tarefa comum

| Tarefa | Ambiente recomendado |
|---|---|
| Organizar vault / criar notas | Claude Desktop |
| Criar materiais escolares | Claude Desktop (`/criar-prova`, `/school-assistant`) |
| Ingerir PDF, URL ou doc | Claude Desktop (`/ingest-pdf`, `/ingest-url`) |
| Commitar mudanças | Claude Desktop (`/safe-commit`) |
| Desenvolver novo MCP | Cursor |
| Criar workflow n8n | n8n (localhost:5678) + Claude Desktop para doc |
| Testar workflow n8n com MCP | Claude Desktop (mcp__n8n-mcp__*) |
| Subir n8n container | PowerShell (`docker start n8n`) |
| Receber mensagem WhatsApp (escola) | OpenClaw (Evolution API → n8n → Pietra) |
| Depurar script `.ps1` | Claude Code CLI no PowerShell |

---

## Frase padrão de início de sessão

```
Leia o contexto do FabioOS e continue a partir do último changelog.
```

Use essa frase ao abrir qualquer nova sessão no Claude Desktop. Ela ativa a leitura obrigatória dos quatro documentos centrais e informa a fase atual do projeto antes de qualquer ação.

Variação útil quando há uma tarefa específica já em mente:

```
Leia o contexto do FabioOS e continue a partir do último changelog. Em seguida, [sua tarefa aqui].
```

---

## Relações

- [[60_Sistemas/Claude_Code/Claude_Project_Config]]
- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]
- [[60_Sistemas/FabioOS/Protocolo_Operacional_FabioOS]]
- [[wiki/sistemas/claude-code]]
- [[wiki/indices/mapa-fabios]]

## Próximas ações

- [ ] Confirmar que o projeto FabioOs aparece corretamente no Claude Desktop
- [ ] Testar a frase padrão de início em nova sessão
- [ ] Documentar qualquer diferença de comportamento entre Claude Desktop e CLI
- [ ] Avaliar se algum comando precisa de ajuste para funcionar melhor no Desktop
