---
tipo: spec
area: 60_Sistemas
projeto: FabioOS
status: rascunho
fase: 16.2
dominio: FabioOS
classe_dado: interno
permissao: leitura_e_proposta
autor: Claude (arquiteto-chefe)
criado_em: 2026-06-29
atualizado_em: 2026-06-29
tags: [fabios, spec, megatron, memoria, reasoningbank, aprendizado, ruflo]
---

# SPEC - ReasoningBank-lite (memória de experiências do MEGATRON)

## 1. Problema

O FabioOS tem RAG (memória semântica de **documentos**) e claude-mem
(observações de sessão), mas **não tem memória estruturada de experiências**: o
que foi tentado, qual abordagem funcionou, em que contexto. Cada decisão é
re-derivada do zero. O MEGATRON classifica e recupera, mas não **aprende com o
que deu certo**.

Padrão absorvido do **ReasoningBank** do ruflo (ver
[[50_Registros/Decisoes/ADR_2026-06-29_Avaliacao_Ruflo_e_Absorcao]]),
reimplementado local e governado — sem AgentDB, sem API, sem daemon.

## 2. Objetivo

Uma memória append-only de experiências que o MEGATRON consulta para **recomendar
estratégia** antes de propor um passo:

- registrar `experiência = {tarefa, abordagem, resultado, contexto, confiança}`;
- consultar por tarefa/contexto e recomendar a abordagem de maior sucesso;
- decaimento de confiança e consolidação simples (sinal, não verdade absoluta);
- alimentar-se do que já existe: ADRs, changelogs, golden tests, claude-mem.

## 3. Fora de escopo

- Treino neural / Q-learning real (o ruflo faz; aqui é heurística simples).
- Banco externo (AgentDB/SQLite vetorial) — começa em arquivo append-only.
- Auto-train autônomo via hooks/daemon — registro é explícito ou semi-explícito.
- Ação: continua propose-only; a memória **sugere**, não decide.

## 4. Domínio, dados e permissões

| Campo | Valor |
|---|---|
| Domínio | FabioOS |
| Classe de dado | interno |
| Escrita | append-only em arquivo do vault (escrita segura) |
| Modelo externo/API | proibido |
| Aprovação humana | a memória só **sugere**; agir exige aprovação |

## 5. Arquitetura proposta

```text
Tarefa + contexto
  -> ReasoningBank.recomendar(tarefa, contexto)
       -> lê experiencias.jsonl (ou .md append-only)
       -> filtra por tarefa/contexto similar
       -> ordena por confiança (com decaimento temporal)
       -> devolve abordagem sugerida + evidência (Resultado)
  -> MEGATRON propõe o passo citando a experiência
  -> após execução: ReasoningBank.registrar(resultado)  [explícito]
```

Armazenamento: `60_Sistemas/MEGATRON/v1/reasoningbank/experiencias.jsonl`
(uma experiência por linha — append-only, à prova de colisão). Devolve o contrato
`Resultado` congelado (tipo `sugestao`).

## 6. Plano de tarefas (fatia futura)

- [ ] Definir o registro de experiência e o JSONL append-only.
- [ ] `registrar(tarefa, abordagem, resultado, contexto, confianca)`.
- [ ] `recomendar(tarefa, contexto)` com decaimento + consolidação simples.
- [ ] Seed a partir de ADRs/changelogs reais (ex.: "validar RAG em modo
      recuperação funcionou 10/10"; "commit temático com scan funcionou").
- [ ] Integrar ao MEGATRON: ao propor ação, citar a experiência relevante.
- [ ] Golden: recomenda abordagem conhecida; abstém quando não há experiência.

## 7. Critérios de aceite

- [ ] Registra e recupera experiência sem API externa.
- [ ] Recomenda a abordagem de maior confiança para uma tarefa conhecida.
- [ ] Diz "sem experiência suficiente" quando o histórico é fraco (alinha com a
      Ignorância Explícita do MEGATRON).
- [ ] Append-only; não reescreve experiências antigas.
- [ ] Sugere, nunca executa.

## 8. Testes mínimos

- [ ] Registrar 1 experiência e recuperá-la.
- [ ] Recomendar entre 2 abordagens concorrentes.
- [ ] Abstenção quando não há histórico.
- [ ] Colisão: 2 appends concorrentes não corrompem o arquivo.

## 9. Riscos

| Risco | Mitigação |
|---|---|
| Falso aprendizado (amostra pequena) | limiar de confiança + rótulo "sinal fraco" |
| Memória crescer demais | consolidação + TTL para experiências antigas |
| Viés (só registra sucesso) | registrar também fracassos (best practice do ReasoningBank) |
| Sobreposição com RAG/claude-mem | RAG=documentos; claude-mem=narrativa; este=experiência tática |

## 10. Rollback

Arquivo append-only isolado; desligar = parar de consultar. Não toca RAG DB,
MCP, runtime. Rollback é local e seguro.

## 11. Changelog esperado

`50_Registros/Changelog/2026-06-29_reasoningbank-lite-spec.md` (e por implementação).

## Relações
- [[50_Registros/Decisoes/ADR_2026-06-29_Avaliacao_Ruflo_e_Absorcao]]
- [[60_Sistemas/FabioOS/specs/2026-06-29_megatron-coordenador]]
- [[50_Registros/Barramento_Multiagente]]
- [[60_Sistemas/MEGATRON/v1/megatron]]
