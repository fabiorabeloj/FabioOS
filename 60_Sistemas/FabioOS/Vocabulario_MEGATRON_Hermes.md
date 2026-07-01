---
tipo: guia
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [megatron, whatsapp, vocabulario, hermes, canal]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
---

# Vocabulário: MEGATRON vs Hermes (sem confusão)

## Regra de ouro

| Nome que você usa | O que é | Fala com você no WPP? |
|---|---|---|
| **MEGATRON** | Assistente / voz do FabioOS | **Sim** — é quem responde |
| **Canal WPP pessoal** | Integração Evolution + n8n + Agentarium | Infraestrutura (não é um produto) |
| **Hermes IA** | App `.exe` instalado no PC (`Hermes.exe`) | **Não** — produto externo, não integrado |
| **`hermes` no Agentarium** | ID interno legado do agente no mapa | Só visual; persona = MEGATRON |

**Quando disser "falar com o MEGATRON no WhatsApp"** → canal pessoal `fabioos-pessoal`, respostas assinadas `[MEGATRON]`.

**Quando disser "Hermes" sem qualificar** → ambíguo. Prefira **MEGATRON** (assistente) ou **Hermes IA** (app).

---

## Um número só (seu pessoal)

Com **apenas** o seu número:

- O WhatsApp mostra o chat **"Você"** (mensagem para si mesmo).
- **Não dá** ter outro contato com foto separada sem um **segundo número** (futuro).
- Melhorias possíveis hoje:
  1. Respostas em **linguagem natural** (MEGATRON conversacional).
  2. Prefixo `[MEGATRON]` em toda resposta.
  3. Fixar o chat "Você" no topo do WhatsApp.
  4. (Opcional) Salvar seu número nos contatos como **MEGATRON** + foto — ajuda na lista, mas o thread continua "Você".

---

## Conversa natural (implementado)

| Modo | Como |
|---|---|
| **Com OpenRouter** | Coloque a chave em `%USERPROFILE%\.fabioos\secrets\openrouter_api_key.txt` |
| **Sem chave** | Respostas fallback humanizadas (limitadas) |
| **Comandos** | `/oi`, `/status`, `/help` — sempre funcionam |

Variáveis (já no `start_agentarium.ps1`):

- `WHATSAPP_CONVERSATIONAL=true`
- `MEGATRON_OPENROUTER_MODEL=openrouter/free`

---

## Fluxo (número pessoal)

```
Fabio (chat "Você")
  → Evolution fabioos-pessoal
  → n8n
  → Agentarium (canal pessoal)
  → MEGATRON responde (IA ou fallback)
  → inbox Cursor (mensagens não-comando)
```

Terceiros que mandarem no seu número: **aviso para você** no WPP; resposta ao contato continua `draft_only`.

---

## Futuro: contato com foto

Quando tiver **segundo número** (chip virtual, linha Business):

- Instância Evolution `megatron-assistente`
- Contato "MEGATRON" de verdade no WhatsApp
- Seu número pessoal volta a ser só fallback/comandos

---

## Relações

- [[60_Sistemas/FabioOS/Hermes_Canal_FabioOS]] — ponte inbox + Cursor
- [[60_Sistemas/Agentes/Hermes_Agent]] — app Hermes IA (externo)
- [[60_Sistemas/FabioOS/WhatsApp_Operations_Guide]]
