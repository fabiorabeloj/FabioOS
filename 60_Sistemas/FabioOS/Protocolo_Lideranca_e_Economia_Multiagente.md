---
tipo: protocolo
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, multiagente, lideranca, economia, tokens, codex, claude, custos]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Protocolo de Liderança e Economia Multiagente

## Função

Definir quem lidera as frentes e como Claude e Codex operam de forma econômica (custo/tokens), evitando trabalho redundante, colisão e gasto desnecessário do agente mais caro.

## Contexto

Foram observados **custos operacionais altos no Codex**. Decisão do Fabio: **Claude assume a liderança das frentes**; Codex passa a operar em **modo auxiliar e econômico**, principalmente quando Claude estiver ausente (limite de uso/tokens).

Complementa: [[60_Sistemas/FabioOS/Protocolo_Roteamento_Capacidades_IA]], [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]], [[60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente]].

## 1. Regra de liderança (vigente)

- **Claude lidera** as frentes: arquitetura, decisões, código, commits temáticos, revisão, subagentes.
- **Codex é auxiliar**: só frentes seguras, sem colisão, sem ações irreversíveis.
- O usuário atua como **estrategista**, não como mensageiro entre IAs — o estado passa pelos artefatos (`STATUS.md`, `NEXT_ACTIONS.md`, `Registro_Frentes_Ativas.md`).

## 2. Divisão de trabalho por custo

| Tipo de tarefa | Agente preferido | Por quê |
|---|---|---|
| Arquitetura, ontologia, decisões de fase | **Claude** | Raciocínio profundo; reservar o modelo forte para o que importa |
| Código novo, fixes, scripts, commits temáticos | **Claude** | Stage explícito + scan + commit já validados |
| Revisão de segurança / consistência | **Claude** (subagentes funcionam) | `security-reviewer`, `vault-architect` |
| Embeddings, OCR, classificação, busca | **Modelos locais** (RAG/Grafo) | Custo zero, privacidade |
| Validação read-only, varredura, contagem | **Codex** (econômico) | Tarefa barata, sem decisão cara |
| Preparação de backlog/relatórios para Claude executar | **Codex** | Deixa pronto; Claude executa quando voltar |
| Estratégia/síntese textual longa | ChatGPT/Codex | Quando não exige operar o repositório |

> **Economia:** não gastar o agente caro em tarefa trivial; não gastar dois agentes na mesma frente; reservar raciocínio pesado para Claude.

## 3. Como o Codex deve operar na ausência de Claude (token-econômico)

Quando Claude estiver indisponível (limite/tokens), o Codex deve:

1. **Só frentes seguras e sem colisão:** leitura, validação, varredura, coordenação, documentação simples, preparação de backlog.
2. **Registrar a frente** em `Registro_Frentes_Ativas.md` antes de tocar qualquer artefato compartilhado.
3. **Nunca** operação destrutiva (apagar, recriar, reindexar RAG, mover, matar processo) sem lock **e** OK humano.
4. **Não fazer push.** Não enviar nada externo (n8n/WhatsApp/e-mail).
5. **Não improvisar:** seguir o [[60_Sistemas/FabioOS/Protocolo_Roteamento_Capacidades_IA]] (skill → comando → agente → script → MCP → RAG/Grafo → manual).
6. **Preparar, não decidir o caro:** deixar grupos de commit, relatórios e perguntas prontos para Claude revisar/executar; evitar decisões de arquitetura sozinho.
7. **Subagentes Codex:** suspensos até reteste em sessão limpa (falha registrada: `spawn_agent could not resolve the child model`). Enquanto isso, subagentes ficam com o Claude.
8. **Handoff obrigatório:** ao parar, atualizar `STATUS.md`, `NEXT_ACTIONS.md` e o registro de frentes, e gerar prompt de retomada para Claude.

## 4. Quando Claude está presente (modo normal)

- Claude conduz; Codex faz verificações read-only paralelas e prepara material, **sem commit/push**.
- Operações destrutivas/compartilhadas: um agente por vez, com lock no registro de frentes.
- Push e ações externas: sempre exigem OK humano.

## 5. Política de modelos e limites

- Tratar limite de uso (mensagens/cotas) como **recurso computacional**.
- Reservar o modelo mais forte para **decisões arquiteturais**; tarefas repetitivas vão para modelos locais.
- Modelos pagos só com **ganho claro**.
- Distribuir trabalho entre agentes; preparar backlog para os períodos de indisponibilidade de um deles.

## Relações

- [[60_Sistemas/FabioOS/Protocolo_Roteamento_Capacidades_IA]]
- [[60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente]]
- [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]]
- [[60_Sistemas/FabioOS/Protocolo_Gestao_Contexto_IA]]
- [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]]

## Próximas ações

- [ ] Reteste de subagentes Codex em sessão limpa
- [ ] Avaliar matriz de seleção de modelo automatizável (Fase futura)
- [ ] Revisar esta divisão conforme os custos reais observados
