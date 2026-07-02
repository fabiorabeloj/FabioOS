---
tipo: adr
area: 50_Registros
projeto: FabioOS
sistema: OpenClaw
status: aceita
tags: [adr, openclaw, gateway, borda, governanca]
criado_em: 2026-07-02
atualizado_em: 2026-07-02
---

# ADR 2026-07-02 - OpenClaw como Gateway de Borda

## Contexto

O FabioOS ja possui OpenClaw instalado e com gateway local ativo, mas a experiencia pratica foi instavel: QR Code, token, companion, chat web, OpenRouter, Workboard, WhatsApp e Agentarium foram tratados como se fossem uma unica frente.

Ao mesmo tempo, fabricantes como Beelink ja vendem equipamentos com OpenClaw pre-instalado, o que cria a impressao de que comprar hardware poderia resolver a experiencia.

## Decisao

OpenClaw sera tratado como **gateway de borda opcional**, nao como nucleo do FabioOS.

Ele pode receber ou exibir mensagens, servir como companion local, mostrar sala visual/Workboard, encaminhar eventos para o MEGATRON e executar acoes locais somente quando houver permissao e teste.

Ele nao pode ser a memoria principal, a fonte da verdade de tarefas, o decisor soberano, um emissor externo autonomo, nem substituto de n8n, Agentarium, Obsidian, Git ou MEGATRON.

## Consequencias

### Positivas

- Reduz frustracao: OpenClaw nao precisa "ser tudo".
- A arquitetura continua funcionando mesmo se o Companion estiver instavel.
- O teste de sucesso fica objetivo.
- Hardware pre-instalado vira conveniencia, nao dependencia.

### Negativas

- O caminho mobile via OpenClaw deixa de ser prioridade maxima ate passar no aceite.
- Pode parecer menos ambicioso no curto prazo.
- Exige manter n8n/Evolution/Agentarium como trilhas separadas.

## Politica de compra

Nao comprar mini PC "OpenClaw edition" como solucao para governanca.

A compra de mini PC deve ser justificada por uptime 24/7, Docker permanente, n8n, Evolution, Open WebUI, RAG, MEGATRON, menor dependencia do notebook, consumo eletrico e manutencao.

OpenClaw pre-instalado e bonus, nao criterio principal.

## Criterio de reversao

A decisao pode ser revista se OpenClaw provar por 7 dias que recebe comandos pelo canal escolhido, gera item de intake rastreavel, respeita aprovacao humana, nao vaza token, sobrevive a reinicio e reduz trabalho real do usuario.

## Relacoes

- [[50_Registros/Auditoria/Diagnostico_OpenClaw_Recuperacao_2026-07-02]]
- [[80_Specs/OpenClaw/2026-07-02_recuperacao-openclaw-gateway-borda]]
- [[60_Sistemas/OpenClaw/Plano_Recuperacao_OpenClaw_FabioOS_2026-07-02]]
- [[60_Sistemas/MEGATRON/infra/Arquitetura_Hardware_MEGATRON_FabioOS_v1]]
- [[50_Registros/Decisoes/ADR_2026-07-02_Tokens_vs_Hardware_MEGATRON]]
