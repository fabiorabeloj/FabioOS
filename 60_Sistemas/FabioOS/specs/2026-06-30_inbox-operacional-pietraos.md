---
tipo: spec
area: 60_Sistemas
projeto: FabioOS
status: rascunho
fase: 19
dominio: PietraOS
classe_dado: sensivel
permissao: leitura_e_proposta
autor: Claude (arquiteto-chefe)
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [fabios, pietraos, spec, inbox-operacional, whatsapp, escola, produto, multivertical]
---

# SPEC - Inbox Operacional (PietraOS) — motor genérico, escola como vertical #1

## 1. Problema

Negócios que vivem no WhatsApp (escola, clínica, imobiliária, contábil, pet…)
recebem texto/foto/PDF/áudio que **não viram processo**: sem triagem, histórico,
responsável claro nem rastreabilidade. Mensagem perdida = retrabalho, erro e, em
alguns nichos, dinheiro perdido. Dois documentos estratégicos do Fabio convergem:
o produto **não é escolar — é uma infraestrutura de operação por mensagens**.

## 2. Objetivo

Construir o **motor "Inbox Operacional"**: entrada informal → interpretação →
classificação → próxima ação → resposta sugerida → encaminhamento → registro →
relatório. **Genérico por design**, com uma **camada de vertical** (categorias,
matriz de risco, matriz de roteamento, templates) por nicho. **Escola = vertical #1**
(laboratório onde o Fabio tem domínio real). Frase-âncora: **toda mensagem vira uma
próxima ação**.

## 3. Tese de mercado (resumo, ver docs do Fabio)

- **Laboratório:** escola (domínio, acesso, dor vivida).
- **Dinheiro:** odonto/estética premium, imobiliário, contábil, clínicas, pet/vet.
- **Mesmo motor; muda vocabulário, risco, ticket, urgência.**
- **Decisão do arquiteto (diverge levemente do doc):** o **vertical #2 ideal para o
  FabioOS é Contábil ou Pet/Vet**, NÃO odonto — porque reusa o **pipeline documental
  que já existe** e tem **risco regulatório menor** que saúde humana. Odonto vem
  depois, com case e (idealmente) parceiro do nicho.

## 4. Arquitetura: motor + camada de vertical

```text
[MOTOR — genérico, já existe no FabioOS]
  Entrada (WhatsApp) -> Classificador -> Documental -> Risco/Segurança ->
  Roteador -> Atendimento(proposta) -> Registro -> Relatório
        ^                                   |
        +------- camada de VERTICAL --------+
  (config: categorias, matriz de risco, matriz de roteamento, templates, FAQ)
```

O motor é **agnóstico de domínio** (Maestro/barramento/agentes); cada vertical é
**dados/config**, não código novo. Isso é o que torna o produto replicável — e o
moat real é a **biblioteca de configs por vertical** (não o código).

## 5. Mapa de agentes → REUSO vs CONSTRUIR

| Agente (doc do Fabio) | Componente FabioOS | Estado |
|---|---|---|
| Entrada (texto/foto/PDF/áudio) | Evolution API + n8n + Hermes (RODANDO) | ♻️ reuso + add mídia |
| Classificador | MEGATRON `classificar()` | ♻️ reuso (keyword agora; LLM depois) |
| Documental | **documentalista** (Stirling/PyMuPDF) | ✅ **construído nesta sessão** |
| Segurança (bloqueia sensível) | risk-gate (read-only/propose-only, ação sensível BLOQUEADA) | ✅ **já existe** |
| Roteador | `registry.rotear()` + matriz de roteamento (config) | ♻️ reuso padrão + config |
| Registro | barramento + nota Obsidian (Arquivista) | ♻️ reuso |
| Pedagógico (vertical escola) | skill `school-assistant` (provas/revisões/comunicados) | ♻️ reuso |
| Atendimento (resposta sugerida) | templates + LLM | 🔨 **construir** |
| Relatório (semanal) | agregador sobre o registro | 🔨 **construir** (é o produto-chave) |

**~6 de 9 agentes são reuso.** O trabalho é **domínio + config + 2 agentes novos
(atendimento/relatório)**, não o motor.

## 6. Fluxo (cartão de atendimento)

Mensagem → ID único → remetente/mídia → categoria → extração → **risco** → consulta
base → decisão (responder/sugerir/pedir dados/encaminhar/abrir tarefa/bloquear+escalar)
→ registro → relatório. A escola vê só **cartões simples** (categoria, responsável,
prioridade, risco, sugestão, ações). RAG/n8n/agentes ficam no bastidor.

## 7. Restrições inegociáveis

- **LGPD é pilar, não rodapé.** Menores + saúde + financeiro: consentimento,
  minimização, retenção, dados sensíveis nunca em log/Git/RAG cru (mesmo padrão
  copyright-safe do pipeline PDF). Promessa de venda: *"os dados do aluno não saem
  da escola"*.
- **Risco sensível NUNCA responde sozinho** (saúde, bullying, conflito, jurídico,
  ameaça) — bloqueia + escala humano. (já é o comportamento do MEGATRON).
- **WhatsApp oficial p/ escalar.** Evolution API (não-oficial) serve o piloto Pietra;
  vender comercialmente exige a **WhatsApp Business API oficial (Meta)** — custo +
  compliance antes do 3º cliente.
- Sem emissão de documento oficial, diagnóstico, decisão disciplinar ou jurídica.

## 8. MVP — vertical Escola (piloto Pietra)

1. WhatsApp Pietra conectado (infra já roda).
2. ID único por atendimento; remetente/mídia/conteúdo.
3. Classificação em ~13 categorias escolares.
4. Risco baixo/médio/alto/crítico.
5. Resposta sugerida (risco baixo/médio) com aprovação.
6. Bloqueio automático de sensível.
7. Encaminhamento por setor (matriz).
8. Registro consultável + **relatório semanal**.

**Fora do MVP:** SaaS multi-escola, GPU obrigatória, dashboard sofisticado,
autonomia total, emissão de documento, resposta automática a sensível, capinhas
como centro.

## 9. Roadmap de verticais

1. **Escola (Pietra)** — laboratório + **estudo de caso antes/depois** (o ativo nº1).
2. **Contábil ou Pet/Vet** — reusa o pipeline documental; menor risco regulatório.
3. **Imobiliário** — alto valor por lead; precisa integração CRM.
4. **Odonto/estética premium** — maior ticket; entrar com case + parceiro do nicho.

## 10. Métricas do piloto (metas)

Classificação correta ≥80%; encaminhamento ≥85%; resposta aproveitável ≥60%;
**sensível bloqueado 100%**; atendimentos registrados ≥90%; -40% tempo de triagem;
-50% mensagens perdidas; relatório útil p/ direção ≥7/10.

## 11. Entregáveis (da Seção 29 do doc)

Arquitetura técnica; fluxograma; matriz de roteamento; matriz de risco; modelo de
cartão; exemplos de mensagens; checklist de testes; manual operacional; backlog;
**política de dados/LGPD** + checklist; modelo de relatório semanal.

## 12. Relações
- [[60_Sistemas/Pietra/Sistema_Pietra]]
- [[60_Sistemas/MEGATRON/v1/megatron]]
- [[60_Sistemas/MEGATRON/agentes/implementacao/claude/documentalista]]
- [[60_Sistemas/FabioOS/specs/2026-06-30_pipeline-pdf-aprende]]
- [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]] (separação FabioOS/PietraOS/PrimusOS)
