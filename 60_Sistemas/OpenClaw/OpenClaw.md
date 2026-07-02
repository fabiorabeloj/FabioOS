
# OpenClaw

## Decisao operacional - 2026-07-02

OpenClaw fica reposicionado como **gateway de borda opcional** do MEGATRON.

Ele nao e mais tratado como nucleo, memoria, orquestrador soberano ou solucao
automatica para mobile/WhatsApp. O papel correto e receber ou exibir eventos,
encaminhar para o MEGATRON/Universal Intake e respeitar aprovacao humana.

Documentos de recuperacao:

- [[50_Registros/Auditoria/Diagnostico_OpenClaw_Recuperacao_2026-07-02]]
- [[50_Registros/Decisoes/ADR_2026-07-02_OpenClaw_Gateway_De_Borda]]
- [[80_Specs/OpenClaw/2026-07-02_recuperacao-openclaw-gateway-borda]]
- [[60_Sistemas/OpenClaw/Plano_Recuperacao_OpenClaw_FabioOS_2026-07-02]]

## Função

Gateway de borda conversacional e operacional do MEGATRON.

## Objetivo

Receber ou exibir eventos, encaminhar ao `Universal Intake` e tornar a acao visivel para aprovacao humana.

## O que ele NÃO é

- Não é a memória principal.
    
- Não é o sistema de automação principal.
    
- Não é o sistema de versionamento.
    
- Não é o repositório de conhecimento.
    

## O que ele É

Uma borda operacional capaz de conversar, encaminhar eventos e acionar fluxos controlados. A decisao continua no MEGATRON.

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
