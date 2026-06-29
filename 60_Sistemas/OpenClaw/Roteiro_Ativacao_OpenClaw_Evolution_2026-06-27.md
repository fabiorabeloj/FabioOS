---
tipo: roteiro
area: 60_Sistemas
projeto: FabioOS
sistema: OpenClaw
status: pronto-para-aprovacao
tags: [openclaw, evolution-api, n8n, whatsapp, pietra, roteiro]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Roteiro de Ativação OpenClaw/Evolution

## Função

Definir a ordem segura para ativar a camada conversacional do FabioOS sem expor tokens, sem envio autônomo e sem misturar o OpenClaw local com o gateway WhatsApp.

## Contexto

O diagnóstico local confirmou:

- OpenClaw Tray instalado, mas gateway WSL não operacional;
- Evolution API ainda não instalada em Docker;
- n8n rodando em `localhost:5678`;
- workflow `FabioOS - WhatsApp para Pietra` válido, com 8 nós e estado inativo;
- porta `8080` livre para Evolution API;
- Hermes Agent documentado, mas não implantado.

## Decisão operacional

Para uso real no FabioOS, priorizar esta ordem:

1. Evolution API + n8n + Pietra para mensagens WhatsApp.
2. OpenClaw local apenas depois de corrigir WSL e confirmar utilidade como gateway/MCP/agente local.
3. Hermes Agent apenas em fase futura, se houver caso de uso que exija autonomia contínua.

## Trilha A — WhatsApp/Pietra via Evolution API

### Objetivo

Receber uma mensagem WhatsApp de teste, classificar pelo Pietra, salvar log anonimizado e devolver confirmação ao webhook, sem envio automático ao responsável.

### Pré-requisitos

- Docker ativo.
- n8n ativo na porta `5678`.
- Workflow `FabioOS - WhatsApp para Pietra` importado e ativado.
- Obsidian aberto com Local REST API disponível em `https://localhost:27124`.
- Credencial `httpHeaderAuth` configurada no n8n para a Obsidian API.
- Chave da Evolution API gerada localmente e nunca salva no repositório.

### Execução mínima

1. Criar volume Docker `evolution_data`.
2. Subir container `evolution-api` na porta `8080`.
3. Criar instância de teste `escola`.
4. Escanear QR Code com número de teste.
5. Configurar webhook para `http://host.docker.internal:5678/webhook/whatsapp-pietra-v2`.
6. Enviar mensagem controlada de teste.
7. Verificar resposta do webhook.
8. Verificar log anonimizado em `05_Raw_Sources/_compat_sources/_inbox/PIETRA_YYYY-MM_LOG.md`.

### Critérios de aceite

- [ ] `docker ps` mostra `evolution-api` ativo.
- [ ] `curl http://localhost:8080/manager` responde.
- [ ] Instância `escola` fica com estado `open`.
- [ ] Workflow n8n recebe evento `messages.upsert`.
- [ ] Mensagem é classificada como uma categoria Pietra.
- [ ] Log salvo contém número anonimizado, sem nome completo e sem telefone completo.
- [ ] Nenhuma resposta externa é enviada automaticamente.

## Trilha B — OpenClaw local

### Objetivo

Descobrir se o OpenClaw local agrega valor ao MEGATRON como agente de desktop, MCP, voz, tela, browser ou executor controlado.

### Pré-requisitos

- Atualizar WSL.
- Reexecutar setup do OpenClaw.
- Confirmar criação da distro `OpenClawGateway`.
- Confirmar porta `18789` ouvindo em `localhost`.
- Manter `SystemRunSandboxEnabled: true`.
- Não habilitar capacidades sensíveis sem escopo e revisão.

### Critérios de aceite

- [ ] `wsl -l -v` mostra `OpenClawGateway`.
- [ ] `Get-NetTCPConnection -LocalPort 18789` mostra listener.
- [ ] OpenClaw Tray conecta no gateway.
- [ ] `EnableMcpServer` só é ativado se houver uso definido.
- [ ] Permissões de tela, câmera, localização e execução ficam documentadas antes de habilitar.

## Trilha C — Hermes Agent

### Objetivo

Manter Hermes como hipótese futura, não como instalação imediata.

### Critério de entrada

Hermes só deve ser avaliado se houver uma tarefa que:

- exija autonomia real e prolongada;
- não seja melhor resolvida por Codex, Claude Code, n8n, RAG ou OpenClaw;
- tenha limite claro de permissões;
- possa ser interrompida sem dano ao FabioOS.

## Não fazer agora

- Não fazer push.
- Não salvar API key no repositório.
- Não ativar envio automático de WhatsApp.
- Não conectar número real de atendimento antes de teste com número controlado.
- Não habilitar Hermes sem especificação formal.
- Não habilitar execução local irrestrita no OpenClaw.

## Prompt operacional para Claude

```text
O Codex diagnosticou o OpenClaw local e criou:

60_Sistemas/OpenClaw/Diagnostico_OpenClaw_Local_2026-06-27.md
60_Sistemas/OpenClaw/Roteiro_Ativacao_OpenClaw_Evolution_2026-06-27.md

Achados principais:
- OpenClaw Tray está instalado e rodando, versão 0.6.0.
- O gateway OpenClaw não está operacional: sem WSL OpenClawGateway e sem listener na porta 18789.
- O setup falhou em preflight-wsl; precisa atualizar WSL antes de tentar de novo.
- Evolution API ainda não está instalada; Docker só tem n8n rodando.
- n8n está ativo em 5678 e o workflow FabioOS - WhatsApp para Pietra é válido, mas inativo.
- Hermes Agent permanece apenas documentado e não deve ser ativado agora.

Por favor, não mexa nesses arquivos enquanto estiver fechando a frente RAG.
Quando concluir RAG, revise o roteiro e proponha o próximo passo seguro para ativar Evolution API sem expor tokens e sem envio automático.
```

## Relações

- [[60_Sistemas/OpenClaw/Diagnostico_OpenClaw_Local_2026-06-27]]
- [[60_Sistemas/OpenClaw/Sistema_OpenClaw]]
- [[60_Sistemas/OpenClaw/setup/EVOLUTION_API_SETUP]]
- [[60_Sistemas/n8n/Workflows/FabioOS_WhatsApp_Pietra]]
- [[60_Sistemas/Pietra/Sistema_Pietra]]
- [[60_Sistemas/Hermes_Agent]]
