
# OpenClaw

## Função

Secretário Executivo Digital do FabioOS.

## Objetivo

Coordenar ferramentas, agentes e automações para reduzir a necessidade de supervisão manual.

## O que ele NÃO é

- Não é a memória principal.
    
- Não é o sistema de automação principal.
    
- Não é o sistema de versionamento.
    
- Não é o repositório de conhecimento.
    

## O que ele É

Um coordenador operacional capaz de utilizar ferramentas e agentes para executar tarefas complexas.

## Relação com os outros sistemas

### Obsidian

Função:  
Memória e Segundo Cérebro.

Responsabilidade:  
Armazenar conhecimento, decisões e contexto.

### GitHub

Função:  
Versionamento e preservação.

Responsabilidade:  
Guardar workflows, documentação e código.

### n8n

Função:  
Execução e automação.

Responsabilidade:  
Executar processos repetitivos.

### Claude / GPT

Função:  
Inteligência.

Responsabilidade:  
Analisar, planejar e produzir conteúdo.

### OpenClaw

Função:  
Coordenação.

Responsabilidade:  
Decidir qual ferramenta utilizar para atingir um objetivo.

## Exemplo

Objetivo:

"Organizar minha próxima semana."

Fluxo:

Usuário  
↓  
OpenClaw  
↓  
Consulta Agenda  
↓  
Consulta Obsidian  
↓  
Consulta tarefas  
↓  
Solicita análise da IA  
↓  
Aciona automações necessárias  
↓  
Entrega plano consolidado

## Status Atual

OpenClaw Companion/Tray ativo no Windows.

Gateway local ativo via WSL: distro `OpenClawGateway`, porta `18789` em loopback, health HTTP `200`, node mode habilitado.

O Companion e a Evolution API são frentes diferentes: o Companion é o nó local do computador; a Evolution API continua sendo a ponte WhatsApp/n8n.

Diagnóstico detalhado: [[60_Sistemas/OpenClaw/Diagnostico_OpenClaw_Local_2026-06-27]]

Relatório de ativação: [[60_Sistemas/OpenClaw/Relatorio_Ativacao_OpenClaw_Companion_2026-06-27]]

Não faz parte da Fase 1 do FabioOS.

## Prioridade

Fase 1:  
Obsidian

Fase 2:  
GitHub

Fase 3:  
n8n

Fase 4:  
Integrações

Fase 5:  
OpenClaw

## Decisão

O OpenClaw somente será integrado após a consolidação da memória (Obsidian), versionamento (GitHub) e automação (n8n).
