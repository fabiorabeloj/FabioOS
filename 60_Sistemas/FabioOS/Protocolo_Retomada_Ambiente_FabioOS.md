---
tipo: protocolo
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, retomada, ambiente, automacao, start]
criado_em: 2026-06-27
atualizado_em: 2026-06-29
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
.\start_megatron.ps1
```

Compatibilidade (script legado):

```powershell
.\60_Sistemas\Scripts\start_fabioos.ps1
```

O nucleo do launcher vive em:

```text
60_Sistemas/Scripts/megatron_launcher.ps1
```

## Variantes seguras

Diagnostico (sem abrir apps, Docker ou browser):

```powershell
.\start_megatron.ps1 -Diagnostico
```

Sem Agentarium (so cockpit + n8n):

```powershell
.\start_megatron.ps1 -NoAgentarium
```

Abrir apenas diagnostico via script legado:

```powershell
.\60_Sistemas\Scripts\start_fabioos.ps1 -Diagnostico -NoOpenApps -SkipBrowser
```

Nao tentar iniciar Docker ou containers:

```powershell
.\start_megatron.ps1 -SkipDocker
```

Nao iniciar containers parados:

```powershell
.\start_megatron.ps1 -SkipContainers
```

## Atalho na Area de Trabalho

```powershell
.\60_Sistemas\Scripts\install_megatron_shortcut.ps1
```

Cria `MEGATRON.lnk` apontando para `start_megatron.ps1`. Este e o passo atual em direcao ao futuro `MEGATRON.exe`.

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

- Agentarium (interface MEGATRON): `http://127.0.0.1:5174`
- n8n local: `http://localhost:5678`
- GitHub do repositorio, se houver remote `origin`
- Dashboard Obsidian: `10_Dashboard/MEGATRON.md`

## Relacao com MEGATRON

Este protocolo e o ritual de "ligar o cockpit" do MEGATRON. **Orquestrador formal:** `60_Sistemas/FabioOS/specs/2026-06-29_MEGATRON_Orchestrator_v1.0.md`.

**Roadmap:** `MEGATRON.cmd` -> atalho `MEGATRON.lnk` -> `MEGATRON.exe` (binario unico).

## Criterio de sucesso

O usuario nao precisa lembrar manualmente quais programas, pastas, containers, paginas ou arquivos abrir para continuar o projeto.

## Proximas acoes

- [x] Validar o script apos um reinicio real do PC.
- [ ] Ajustar nomes de containers n8n se o ambiente Docker mudar.
- [ ] Decidir se OpenClaw deve entrar no roteiro de retomada automatica.
- [x] Painel local MEGATRON: Agentarium + megatron_runtime.json + megatron_health.ps1.
- [ ] Empacotar MEGATRON.exe (requer .NET SDK ou PS2EXE) embutindo MEGATRON.cmd.
