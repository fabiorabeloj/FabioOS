---
tipo: protocolo
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, retomada, ambiente, automacao, start]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Protocolo de Retomada do Ambiente FabioOS

## Funcao

Definir como o FabioOS deve voltar ao estado operacional apos reinicio do computador, com o menor numero possivel de passos manuais.

## Objetivo

Ao ligar o PC, o usuario deve conseguir executar um unico comando ou atalho para restaurar o ambiente minimo de trabalho:

- Obsidian aberto no vault FabioOS;
- Cursor ou VS Code aberto na pasta do projeto;
- Docker Desktop verificado ou iniciado;
- containers locais relevantes verificados, especialmente n8n;
- Git verificado;
- terminal aberto no diretorio correto;
- paginas essenciais abertas no navegador;
- pendencias resumidas;
- retomada registrada no changelog.

## Comando padrao

Executar na raiz do vault:

```powershell
.\start_fabioos.ps1
```

O script fica em:

```text
start_fabioos.ps1
```

## Variantes seguras

Abrir apenas diagnostico, sem aplicativos:

```powershell
.\start_fabioos.ps1 -NoOpenApps -SkipBrowser
```

Nao tentar iniciar Docker ou containers:

```powershell
.\start_fabioos.ps1 -SkipDocker
```

Nao iniciar containers parados:

```powershell
.\start_fabioos.ps1 -SkipContainers
```

## O que o script pode fazer

- Abrir aplicativos locais.
- Abrir paginas essenciais.
- Verificar Git.
- Verificar Docker.
- Iniciar Docker Desktop, se instalado.
- Iniciar containers n8n parados ja existentes.
- Criar ou atualizar changelog de retomada.
- Exibir resumo operacional baseado no painel de pendencias.

## O que o script nao deve fazer

- Nao fazer commit.
- Nao fazer push.
- Nao apagar arquivos.
- Nao criar credenciais.
- Nao expor tokens.
- Nao alterar workflows n8n.
- Nao executar automacoes externas com efeito sobre terceiros.

## Paginas essenciais

- n8n local: `http://localhost:5678`
- GitHub do repositorio, se houver remote `origin`
- Claude: `https://claude.ai/`
- ChatGPT/Codex: `https://chatgpt.com/`

## Relacao com MEGATRON

Este protocolo e o ritual de "ligar o cockpit" do MEGATRON. Ele nao substitui agentes, RAG, n8n, OpenClaw ou Obsidian; apenas restaura o ambiente minimo para que esses sistemas possam operar juntos.

## Criterio de sucesso

O usuario nao precisa lembrar manualmente quais programas, pastas, containers, paginas ou arquivos abrir para continuar o projeto.

## Proximas acoes

- [ ] Validar o script apos um reinicio real do PC.
- [ ] Ajustar nomes de containers n8n se o ambiente Docker mudar.
- [ ] Decidir se OpenClaw deve entrar no roteiro de retomada automatica.
- [ ] Decidir se o script deve abrir tambem um painel local do MEGATRON no futuro.
