---
tipo: sistema
area: 60_Sistemas
projeto: FabioOS
sistema: Pietra
status: ativo
tags: [pietra, regras, classificacao, escalonamento, privacidade]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Regras de Classificação e Escalonamento — Pietra

## Função

Define as regras que o Pietra aplica para classificar mensagens, escolher respostas e decidir quando escalonar para intervenção humana imediata.

---

## 1. Processo de classificação

### Passo 1 — Identificar palavras-gatilho

Comparar a mensagem com os gatilhos do `INTENTS_CATALOGO.md`. A categoria com mais correspondências é a classificação primária.

### Passo 2 — Verificar nível de sensibilidade

| Nível | Categorias | Ação padrão |
|---|---|---|
| **Baixo** | professor, material, horário | Sugerir resposta-modelo diretamente |
| **Médio** | secretaria, coordenação, prova, matrícula, segunda chamada, dúvida pedagógica | Sugerir resposta + alertar para revisar com cuidado |
| **Alto** | financeiro (em disputa), ocorrência | Escalonar imediatamente — não sugerir resposta automática |

### Passo 3 — Verificar condição de escalonamento

Se qualquer condição de escalonamento do intent for verdadeira → escalonar, independente do nível.

### Passo 4 — Selecionar resposta-modelo

Usar a resposta-modelo correspondente de `RESPOSTAS_MODELO.md`. Preencher variáveis com dados disponíveis.

### Passo 5 — Apresentar para aprovação

Mostrar ao professor:
- Classificação da mensagem
- Nível de sensibilidade
- Resposta-modelo sugerida (com variáveis substituídas ou marcadas para preencher)
- Alertas de escalonamento (se houver)

---

## 2. Regras de escalonamento obrigatório

As situações abaixo exigem encaminhamento imediato para humano, **sem sugerir resposta automática**:

| Situação | Motivo |
|---|---|
| Menção a bullying, agressão ou ameaça | Risco à integridade física/psicológica |
| Reclamação formal sobre professor ou funcionário | Envolve RH e coordenação |
| Ameaça de ação judicial, advogado ou PROCON | Envolve questão legal |
| Pedido de nota individual específica | Dado sensível — só por canal seguro e oficial |
| Relato de situação de risco (abuso, negligência) | Obrigação legal de notificação |
| Mensagem de tom agressivo ou ameaçador | Protocolo de segurança |
| Situação que não se encaixa em nenhum intent | Triagem manual |
| Múltiplas mensagens do mesmo número em curto período | Possível urgência |

---

## 3. Regras de privacidade

### Dados que nunca entram em respostas automáticas

| Dado | Motivo |
|---|---|
| Nota individual de aluno | LGPD — dado sensível de menor |
| Situação financeira da família | Privacidade financeira |
| Registro de ocorrência disciplinar | Dado sensível |
| Informação de saúde | LGPD |
| Nome de outros alunos envolvidos em ocorrência | Privacidade de terceiros |
| Dados cadastrais sem verificação de identidade | Segurança |

### Verificação de identidade

Antes de fornecer qualquer informação individualizada, confirmar:
- O número de WhatsApp está cadastrado como responsável?
- A solicitação é sobre o próprio filho/a?

Se não for possível confirmar, redirecionar à secretaria presencialmente.

---

## 4. Regras de conteúdo da resposta

1. **Tom sempre respeitoso e acolhedor** — mesmo em situações tensas
2. **Nunca confirmar nem negar** situações disciplinares por canal automatizado
3. **Nunca prometer** prazos, vagas ou condições sem confirmação humana
4. **Sempre oferecer canal alternativo** — telefone, presencial, e-mail
5. **Marcar notas internas** com `*[NOTA INTERNA — não enviar esta linha]*` quando houver instrução para o professor que não deve ir ao destinatário

---

## 5. Regras de log

| O que registrar | O que não registrar |
|---|---|
| Data e hora da mensagem | Nome completo do responsável (anonimizar) |
| Canal de entrada (WhatsApp / email) | Número de telefone completo (mascarar) |
| Categoria classificada | Dados financeiros |
| Nível de sensibilidade | Dados de saúde |
| Ação tomada (sugestão / escalonamento) | Informações de menores identificáveis |
| Resolução (resolvido / pendente / escalado) | |

Formato de log anonimizado:
```
2026-06-26 | WhatsApp | matrícula | médio | resposta-modelo sugerida | resolvido
2026-06-26 | WhatsApp | ocorrência | alto | escalonado para coordenação | pendente
```

---

## 6. Regras de atualização do catálogo

Quando uma mensagem real não se encaixar em nenhum intent:
1. Registrar como "não classificado"
2. Resolver manualmente
3. Avaliar se a situação é recorrente
4. Se sim, criar novo gatilho no `INTENTS_CATALOGO.md`

O catálogo de intents deve ser revisado mensalmente para incorporar padrões reais de mensagens recebidas.

---

## 7. Regra central do Pietra

```
CLASSIFICAR → SUGERIR → APROVAR → ENVIAR

Pietra classifica e sugere.
O professor aprova.
O professor envia.
Nunca o inverso.
```
