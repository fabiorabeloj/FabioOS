---
tipo: spec
area: 60_Sistemas
projeto: FabioOS
status: rascunho
fase: 16
dominio: FabioOS
classe_dado: interno
permissao: leitura_e_proposta
criado_em: 2026-06-29
atualizado_em: 2026-06-29
tags: [fabios, spec, megatron, rag, grafo, mcp, governanca]
---

# SPEC - MEGATRON v1 com Ignorancia Explicita

## 1. Problema

MEGATRON v0 existe como interface minima, mas ainda precisa operar com criterio claro de confianca.

Sem ignorancia explicita, o sistema pode responder com aparente certeza mesmo quando RAG/Grafo/MCP nao recuperam fontes suficientes.

## 2. Objetivo

Criar MEGATRON v1 como camada de roteamento e resposta controlada que:

- consulta memoria antes de responder;
- informa quando nao sabe;
- cita fontes internas;
- diferencia resposta, sugestao e acao;
- registra logs;
- respeita a Fase 17 Governanca Operacional.

## 3. Fora de escopo

Nao entra nesta SPEC:

- envio de email;
- envio de WhatsApp;
- escrita via MCP;
- alteracao de workflows n8n;
- uso obrigatorio de API externa;
- acao financeira/trading;
- automacao persistente;
- interface web final.

## 4. Dominio, dados e permissoes

| Campo | Valor |
|---|---|
| Dominio | FabioOS |
| Classe de dado | interno; pode tocar privado apenas em modo leitura local e minimizado |
| RAG | permitido, read-only |
| Grafo | permitido, read-only |
| Modelo externo/API | proibido por padrao; so com aprovacao e teto de custo |
| Aprovacao humana | obrigatoria para qualquer acao externa ou sensivel |

## 5. Arquitetura proposta

```text
Pergunta do Fabio
  -> classificar dominio e risco
  -> consultar index/log/STATUS/NEXT_ACTIONS
  -> consultar RAG se precisar de memoria semantica
  -> consultar Grafo se precisar de relacoes
  -> consultar MCP FabioOS read-only se disponivel
  -> avaliar confianca
  -> responder com fontes OU declarar ignorancia
  -> propor proxima acao
  -> registrar log/changelog quando relevante
```

## 6. Plano de tarefas

- [ ] Definir limiar de confianca por tipo de consulta.
- [ ] Definir formato de resposta com fontes.
- [ ] Definir formato de "nao sei ainda".
- [ ] Criar log de consultas MEGATRON v1.
- [ ] Integrar leitura de `10_Dashboard/_entrada/index.md`, `50_Registros/Logs_Agentes/log.md`, `STATUS.md` e `NEXT_ACTIONS.md`.
- [ ] Integrar consulta RAG read-only.
- [ ] Integrar consulta Grafo read-only.
- [ ] Integrar MCP FabioOS read-only quando ferramenta nativa estiver disponivel.
- [ ] Criar bateria de perguntas golden.
- [ ] Atualizar dashboard MEGATRON.

## 7. Criterios de aceite

- [ ] Responde com fontes quando ha evidencia suficiente.
- [ ] Diz explicitamente que nao encontrou base quando a recuperacao falha.
- [ ] Nao inventa status operacional.
- [ ] Nao executa acao externa.
- [ ] Diferencia "posso fazer", "posso sugerir" e "precisa de aprovacao".
- [ ] Registra log de consulta relevante.
- [ ] Usa matriz de permissoes para classificar acao.
- [ ] Passa em pelo menos 10 perguntas golden.

## 8. Testes minimos

- [ ] Pergunta com resposta conhecida no vault.
- [ ] Pergunta ambigua que exige abstencao.
- [ ] Pergunta que tenta acao externa.
- [ ] Pergunta sobre dado sensivel.
- [ ] Pergunta que exige RAG.
- [ ] Pergunta que exige Grafo.
- [ ] Pergunta que exige protocolo de governanca.

## 9. Riscos

| Risco | Mitigacao |
|---|---|
| Falsa certeza | limiar de confianca e resposta "nao encontrei no vault" |
| Acao externa acidental | permissao read-only por padrao |
| Custo de API | API externa proibida por padrao |
| Dados sensiveis | aplicar matriz de dominios/dados/permissoes |
| Confusao entre plano e estado real | consultar STATUS/NEXT_ACTIONS e changelog |

## 10. Rollback

Se MEGATRON v1 falhar:

- manter MEGATRON v0 como read-only/propose-only;
- desativar qualquer chamada nova;
- usar scripts RAG/Grafo manualmente;
- registrar incidente em `50_Registros/Auditoria/`.

## 11. Changelog esperado

Arquivo esperado:

`50_Registros/Changelog/2026-06-29_spec-megatron-v1-ignorancia-explicita.md`

## Relacoes

- [[60_Sistemas/FabioOS/Roadmap_Fases_FabioOS_v2_2026-06-29]]
- [[50_Registros/Decisoes/Constituicao_Operacional_FabioOS]]
- [[60_Sistemas/Governanca/Matriz_de_Permissoes_FabioOS]]
- [[10_Dashboard/RAG_MCP_Control_Plane]]
- [[60_Sistemas/MEGATRON/v0/README_MEGATRON_v0]]
