---
tipo: sistema
area: 60_Sistemas
projeto: FabioOS
sistema: Pietra
status: ativo
tags: [pietra, intents, classificacao, atendimento]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Catálogo de Intents — Pietra

## Como usar

Cada intent define:
- **Gatilhos** — frases ou palavras que identificam esta intenção
- **Classificação** — categoria + nível de sensibilidade
- **Ação** — o que Pietra deve fazer
- **Resposta** — qual modelo usar (ver RESPOSTAS_MODELO.md)
- **Escalonar se** — condições que exigem encaminhamento humano imediato

---

## 1. FINANCEIRO

**Nível:** Alto

**Gatilhos:**
- "mensalidade", "boleto", "pagamento", "atraso", "débito", "vencimento"
- "quanto é", "valor da mensalidade", "preciso pagar", "está em atraso"
- "desconto", "bolsa", "isenção", "inadimplente"

**Ação:** redirecionar à secretaria financeira — nunca informar valores, situação de débito ou histórico de pagamentos automaticamente.

**Resposta-modelo:** `FINANCEIRO_REDIRECIONAMENTO`

**Escalonar se:**
- Mensagem mencionar ameaça, advogado ou PROCON
- Pai/responsável relata erro de cobrança
- Situação envolve negociação ou parcelamento

---

## 2. SECRETARIA

**Nível:** Médio

**Gatilhos:**
- "declaração", "histórico", "documento", "certidão", "transferência"
- "preciso de um documento", "atestado de matrícula", "ficha do aluno"
- "horário de atendimento", "o que preciso trazer"

**Ação:** informar horários de atendimento e documentos necessários, ou redirecionar.

**Resposta-modelo:** `SECRETARIA_DOCUMENTOS`

**Escalonar se:**
- Solicitação envolve dado cadastral para alterar
- Transferência para outra escola

---

## 3. COORDENAÇÃO

**Nível:** Médio

**Gatilhos:**
- "coordenação", "reunião", "conversar com a coordenadora", "agendar"
- "reclamação", "problema com professor", "situação do meu filho"
- "comunicado", "conselho de classe", "representante"

**Ação:** registrar solicitação de contato e informar como agendar.

**Resposta-modelo:** `COORDENACAO_AGENDAMENTO`

**Escalonar se:**
- Relato de agressão, bullying ou situação de risco
- Reclamação formal sobre professor ou funcionário

---

## 4. PROFESSOR

**Nível:** Baixo

**Gatilhos:**
- "professor", "prof", "quero falar com o professor", "contato do professor"
- "o professor de [disciplina]", "quem é o professor"

**Ação:** informar canal oficial de contato com professor (sem expor dados pessoais).

**Resposta-modelo:** `PROFESSOR_CONTATO`

**Escalonar se:**
- Reclamação sobre conduta do professor

---

## 5. MATERIAL

**Nível:** Baixo

**Gatilhos:**
- "lista de material", "livro", "apostila", "caderno", "uniforme"
- "o que precisa comprar", "material escolar", "lista do [ano]"

**Ação:** informar onde encontrar a lista ou encaminhar o documento.

**Resposta-modelo:** `MATERIAL_LISTA`

**Escalonar se:**
- Reclamação sobre cobrança de material não informado

---

## 6. HORÁRIO

**Nível:** Baixo

**Gatilhos:**
- "horário", "que horas começa", "que horas termina", "entrada", "saída"
- "horário das aulas", "grade horária", "período"
- "feriado", "recesso", "aula amanhã"

**Ação:** informar horários ou confirmar funcionamento.

**Resposta-modelo:** `HORARIO_INFO`

**Escalonar se:**
- Nenhuma condição especial

---

## 7. PROVA

**Nível:** Médio

**Gatilhos:**
- "prova", "avaliação", "simulado", "recuperação", "nota"
- "quando é a prova de", "qual o conteúdo", "meu filho tirou"
- "resultado", "gabarito", "média"

**Ação (conteúdo/data):** informar data e conteúdo geral se disponível.
**Ação (nota individual):** nunca informar nota automaticamente — redirecionar ao professor ou secretaria.

**Resposta-modelo:** `PROVA_DATA_CONTEUDO` ou `PROVA_NOTA_REDIRECIONAMENTO`

**Escalonar se:**
- Pedido de nota individual específica
- Contestação de resultado

---

## 8. MATRÍCULA

**Nível:** Médio

**Gatilhos:**
- "matrícula", "rematrícula", "renovar matrícula", "prazo de matrícula"
- "inscrição", "vaga", "novo aluno", "transferência"
- "documentos para matricular"

**Ação:** informar prazo, documentos necessários e procedimento.

**Resposta-modelo:** `MATRICULA_INFO`

**Escalonar se:**
- Pedido de vaga quando há lista de espera
- Transferência de outra cidade com situação especial

---

## 9. SEGUNDA CHAMADA

**Nível:** Médio

**Gatilhos:**
- "segunda chamada", "faltou na prova", "não pôde fazer a prova"
- "atestado", "justificativa de falta", "falta na avaliação"
- "pode refazer"

**Ação:** informar prazo e procedimento para solicitação de segunda chamada.

**Resposta-modelo:** `SEGUNDA_CHAMADA_PROCEDIMENTO`

**Escalonar se:**
- Atestado médico ou situação excepcional que exige análise individual

---

## 10. OCORRÊNCIA

**Nível:** Alto — escalonar sempre

**Gatilhos:**
- "ocorrência", "suspensão", "expulsão", "disciplinar"
- "meu filho foi chamado", "aconteceu um problema", "briga", "conflito"
- "bullying", "agressão", "ameaça", "assédio"

**Ação:** nunca tentar resolver automaticamente. Registrar e escalonar para coordenação imediatamente.

**Resposta-modelo:** `OCORRENCIA_ESCALONAMENTO`

**Escalonar se:** sempre — sem exceção.

---

## 11. DÚVIDA PEDAGÓGICA

**Nível:** Médio

**Gatilhos:**
- "recuperação", "reforço", "está com dificuldade", "não está entendendo"
- "acompanhamento", "precisa de ajuda", "laudo", "necessidade especial"
- "como posso ajudar em casa", "atividade extra"

**Ação:** acolher e redirecionar ao professor da disciplina ou à coordenação pedagógica.

**Resposta-modelo:** `PEDAGOGICO_REDIRECIONAMENTO`

**Escalonar se:**
- Menção a laudo médico ou necessidade especial documentada
- Solicitação de adaptação curricular

---

## Categoria desconhecida

Quando nenhum intent for identificado com confiança:

**Ação:** registrar como "não classificado", alertar o professor e aguardar triagem manual.

**Resposta-modelo:** `NAO_CLASSIFICADO`
