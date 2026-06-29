---
tipo: sistema
area: 60_Sistemas
projeto: FabioOS
sistema: Pietra
aliases: [PietraOS]
status: ativo
versao: 1.0
tags: [pietra, atendimento, classificacao, whatsapp, escola, camada-5]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Sistema Pietra

## Função

Atendimento Inteligente Pietra — classifica mensagens recebidas de pais, alunos e responsáveis, sugere respostas padronizadas e encaminha para aprovação humana antes de qualquer envio externo.

**Critério de sucesso da Fase 9:**

> Uma mensagem simulada é classificada corretamente e recebe resposta sugerida.

## Contexto

Mensagens escolares chegam por WhatsApp, e-mail e presencialmente. Sem sistema, a triagem é manual, inconsistente e lenta. O Pietra padroniza, documenta e acelera o atendimento — sem eliminar o julgamento humano em nenhuma etapa crítica.

**O Pietra nunca responde sozinho. Sempre prepara para aprovação.**

---

## 1. Módulos do Sistema

| Módulo | Função | Status |
|---|---|---|
| **intents/** | Catálogo de intenções por categoria | ativo |
| **respostas-modelo/** | Respostas padronizadas por tipo de mensagem | ativo |
| **regras/** | Regras de classificação e escalonamento | ativo |
| **fluxos/** | Fluxos de atendimento por categoria | pendente |
| **escalonamento/** | Registro de casos escalados | pendente |
| **logs/** | Histórico de atendimentos | pendente |
| **n8n-workflows/** | Automações do Pietra via n8n | futuro (Fase 10/11) |

---

## 2. Categorias de atendimento

| Categoria | Tipo | Nível de sensibilidade |
|---|---|---|
| **financeiro** | Informação / redirecionamento | Alto — redirecionar à secretaria |
| **secretaria** | Informação / documentos | Médio |
| **coordenação** | Reunião / comunicado | Médio |
| **professor** | Contato / horário | Baixo |
| **material** | Lista / apostila / livro | Baixo |
| **horário** | Aula / prova / atividade | Baixo |
| **prova** | Data / conteúdo / nota | Médio — nota exige cuidado |
| **matrícula** | Rematrícula / transferência | Médio |
| **segunda chamada** | Justificativa / formulário | Médio |
| **ocorrência** | Disciplinar / comunicação | Alto — sempre escalonar |
| **dúvida pedagógica** | Recuperação / acompanhamento | Médio |

---

## 3. Fluxo de atendimento

```
MENSAGEM RECEBIDA
(WhatsApp / email / presencial)
        ↓
REGISTRO
  salvar em logs/ com: data, canal, remetente (anonimizado), texto
        ↓
CLASSIFICAÇÃO
  identificar: categoria + nível de sensibilidade
        ↓
TRIAGEM
  Baixa sensibilidade → sugerir resposta-modelo
  Média sensibilidade → sugerir resposta + alertar para revisar
  Alta sensibilidade → escalonar diretamente (financeiro em disputa, ocorrência)
        ↓
RESPOSTA SUGERIDA
  Pietra prepara rascunho baseado na categoria e resposta-modelo
        ↓
APROVAÇÃO HUMANA (obrigatória)
  Professor ou responsável revisa, ajusta e aprova
        ↓
ENVIO
  Feito pelo humano — Pietra nunca envia autonomamente
        ↓
REGISTRO DE RESOLUÇÃO
  Marcar como resolvido, com data e canal
```

---

## 4. Regras operacionais

### O que o Pietra pode fazer
- Classificar mensagens por categoria
- Sugerir resposta baseada em modelo existente
- Alertar sobre sensibilidade e risco
- Registrar histórico de atendimentos
- Identificar padrões recorrentes

### O que o Pietra nunca faz
- Enviar mensagens a pais, alunos ou equipe sem aprovação
- Informar notas, situação financeira ou registros disciplinares automaticamente
- Tomar decisões pedagógicas ou administrativas
- Comprometer a escola em respostas automáticas

### Dados que nunca entram em respostas automáticas
- Notas individuais de alunos
- Situação financeira de famílias
- Registros de ocorrências disciplinares
- Informações de saúde
- Dados de outros alunos

---

## 5. Integração futura

| Sistema | Integração | Fase |
|---|---|---|
| **OpenClaw** | Gateway WhatsApp → Pietra | Fase 11 |
| **n8n** | Webhook → classificação → log automático | Fase 10 |
| **Claude Code** | Geração de respostas personalizadas | Fase 9 (atual) |
| **RAG** | Busca em respostas anteriores para sugestão | Fase 12 |

**Fluxo futuro completo:**
```
WhatsApp (pai/aluno)
  → OpenClaw (gateway)
  → n8n (webhook + classificação)
  → Pietra (resposta sugerida)
  → Aprovação do professor
  → OpenClaw (envio)
  → n8n (log)
```

---

## 6. Estrutura de arquivos

```
60_Sistemas/Pietra/
├── Sistema_Pietra.md               ← este arquivo
├── intents/
│   └── INTENTS_CATALOGO.md         ← todas as intenções por categoria
├── respostas-modelo/
│   └── RESPOSTAS_MODELO.md         ← respostas padronizadas editáveis
├── regras/
│   └── REGRAS_CLASSIFICACAO.md     ← como classificar e escalar
├── fluxos/                         ← (pendente)
├── escalonamento/                  ← (pendente)
├── logs/                           ← (pendente — nunca commitado se tiver dados reais)
└── n8n-workflows/                  ← (futuro)
```

**Atenção:** a pasta `logs/` deve conter apenas dados anonimizados. Nunca commitar logs com nomes de alunos, responsáveis ou dados financeiros reais.

---

## 7. Nomenclatura

```
PIETRA_[YYYY-MM]_[TIPO].md

PIETRA_2026-06_INTENT-FINANCEIRO.md
PIETRA_2026-06_RESPOSTA-HORARIO.md
PIETRA_2026-06_FLUXO-MATRICULA.md
```

---

## Relações

- [[40_Wiki/_compat_wiki/projetos/pietra]]
- [[60_Sistemas/Escola/Sistema_Escola]]
- [[40_Wiki/_compat_wiki/sistemas/openclaw]]
- [[40_Wiki/_compat_wiki/sistemas/n8n]]
- [[60_Sistemas/FabioOS/Protocolo_Operacional_FabioOS]]
- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]

## Próximas ações

- [ ] Testar classificação com 5 mensagens simuladas (critério de sucesso Fase 9)
- [ ] Criar fluxo n8n: webhook → classificação → log (Fase 10)
- [ ] Integrar com OpenClaw quando disponível (Fase 11)
- [ ] Expandir catálogo de intents com mensagens reais recebidas
