---
tipo: protocolo
area: 60_Sistemas
projeto: FabioOS
status: ativo
versao: 1.0
tags: [fabios, protocolo, operação, rotina, fluxo, convenções]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Protocolo Operacional do FabioOS

## Função

Define como o FabioOS deve ser usado no dia a dia — como as informações entram, onde vão, quem decide o que e como o sistema é mantido vivo. Sem este protocolo, o FabioOS vira uma coleção de ferramentas.

## Contexto

Todo sistema de conhecimento morre de dois jeitos: ou ninguém alimenta, ou tudo entra mas nada é organizado. Este protocolo garante que cada informação que entra no FabioOS tem destino, forma e critério de transformação.

**Documento de referência:** [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]

---

## 1. Princípio central

> **Toda informação que entra no FabioOS deve virar uma destas cinco coisas — e apenas uma:**

| Destino final | O que é | Onde fica |
|---|---|---|
| **Fonte** | Conteúdo externo preservado, ainda bruto | `05_Raw_Sources/` |
| **Nota wiki** | Conhecimento tratado, conectado e navegável | `40_Wiki/` |
| **Tarefa** | Ação com responsável, prazo ou contexto | `30_Projetos/`, `20_Areas/` ou task de sessão |
| **Decisão** | Escolha documentada com motivo e data | `50_Registros/Decisoes/` |
| **Arquivo** | Material encerrado, preservado sem uso ativo | `90_Arquivo/` |

Se uma informação não se encaixa em nenhuma das cinco, ela vai para `00_Inbox/` até ser triada.

**Regra:** informação sem destino = ruído. Ruído suficiente = sistema morto.

---

## 2. Fluxo operacional

```
ENTRADA
  ↓
TRIAGEM
  (o que é isso? qual dos cinco destinos?)
  ↓
PRESERVAÇÃO
  (salvar na forma original antes de qualquer transformação)
  ↓
TRANSFORMAÇÃO
  (extrair, sintetizar, organizar, linkar)
  ↓
AÇÃO
  (usar, executar, responder, publicar — com aprovação quando necessário)
  ↓
REVISÃO
  (fechar loop: changelog, pendências, próximas ações)
```

Nenhuma etapa deve ser pulada. A transformação sem preservação perde a fonte. A ação sem revisão perde o histórico.

---

## 3. Tipos de entrada

| Tipo | Exemplo | Urgência padrão |
|---|---|---|
| Texto | rascunho, pensamento, trecho copiado | baixa |
| Áudio transcrito | gravação processada, nota de voz | média |
| Print | screenshot de conversa, aviso, post | baixa |
| PDF | artigo, edital, material de aula | média |
| Link | URL de página, vídeo, repositório | baixa |
| Google Docs | documento compartilhado, planilha | variável |
| Email | comunicado, solicitação, resposta | média/alta |
| Mensagem escolar | aviso de pais, comunicado da escola | alta |
| Ideia | pensamento criativo, hipótese, insight | baixa |
| Decisão | escolha operacional, mudança de rota | alta |
| Material de aula | conteúdo para ensinar, exercício, prova | alta |

---

## 4. Destino de cada tipo de entrada

| Tipo de entrada | Destino primário | Destino secundário (após triagem) |
|---|---|---|
| Texto bruto / pensamento | `00_Inbox/` | → `40_Wiki/` ou `30_Projetos/` |
| Áudio transcrito | `00_Inbox/` | → `05_Raw_Sources/Conversas/` ou `05_Raw_Sources/Videos_Transcricoes/` |
| Print | `00_Inbox/` | → `05_Raw_Sources/Prints/` ou descartado |
| PDF | `05_Raw_Sources/PDFs/` | → `40_Wiki/` (via extração) |
| Link / URL | `05_Raw_Sources/Radar_Tecnologico/` | → `40_Wiki/` |
| Google Docs | `05_Raw_Sources/Conversas/` ou compatibilidade `sources/drive/` | → `40_Wiki/` ou `60_Sistemas/Escola/` |
| Email | `00_Inbox/` | → `50_Registros/` ou `05_Raw_Sources/Conversas/` |
| Mensagem escolar | `00_Inbox/` | → `60_Sistemas/Escola/` |
| Ideia | `00_Inbox/` | → `30_Projetos/` ou `40_Wiki/` |
| Decisão operacional | `50_Registros/Decisoes/` | → `50_Registros/Changelog/` |
| Material de aula | `05_Raw_Sources/EscolaOS/` | → `60_Sistemas/Escola/` |

**Regra de ouro:** nenhum arquivo deve permanecer em `00_Inbox/` por mais de uma semana sem triagem.

---

## 5. Rotina diária

Tempo estimado: **5–15 minutos**.

```
CAPTURAR
  Qualquer informação nova vai para 00_Inbox/ imediatamente.
  Não organizar no momento da captura — só capturar.
  ↓
CLASSIFICAR (no fim do dia)
  Abrir 00_Inbox/ e perguntar para cada item:
  "Isso é fonte, wiki, tarefa, decisão ou arquivo?"
  ↓
ARQUIVAR
  Mover para o destino correto conforme tabela da seção 4.
  ↓
TRANSFORMAR O QUE FOR URGENTE
  Materiais escolares, mensagens de pais, decisões críticas.
  Não esperar a rotina semanal para processar urgências.
```

**Não é necessário processar tudo todo dia.** O objetivo é não deixar acumular mais de um dia sem classificação.

---

## 6. Rotina semanal

Tempo estimado: **30–60 minutos** (preferencialmente domingo ou segunda-feira).

```
1. PROCESSAR INBOX
   Zerar ou triagear tudo em 00_Inbox/.
   Mover, transformar ou descartar.

2. ATUALIZAR CHANGELOG
   Criar ou atualizar nota em 50_Registros/Changelog/
   com o que foi feito, decidido ou alterado na semana.

3. REVISAR PENDÊNCIAS
   Abrir notas com [ ] em aberto em 30_Projetos/ e wiki/.
   Mover para próxima semana ou executar.

4. ATUALIZAR MAPA
   Verificar se wiki/indices/mapa-fabios.md reflete o estado atual.
   Corrigir links quebrados, fases e status.

5. LIMPAR DUPLICAÇÕES
   Verificar se há notas duplicadas, versões antigas ou arquivos órfãos.
   Mover para 90_Arquivo/ ou apagar com confirmação.
```

---

## 7. Rotina mensal

Tempo estimado: **1–2 horas** (preferencialmente início do mês).

```
1. REVISAR FASES
   Abrir Plano_Mestre_Implantacao_FabioOS.md.
   Verificar quais fases avançaram, quais travaram, quais precisam mudar.
   Atualizar status de cada fase.

2. REVISAR SEGURANÇA
   Rodar /check-secrets no vault.
   Verificar se .gitignore está atualizado.
   Checar se algum arquivo sensível foi adicionado inadvertidamente.
   Verificar se credenciais em uso estão corretas e não expiradas.

3. ARQUIVAR PROJETOS MORTOS
   Identificar projetos em 30_Projetos/ sem atividade há mais de 30 dias.
   Decidir: retomar, suspender ou encerrar.
   Mover encerrados para 90_Arquivo/.

4. ATUALIZAR PLANO MESTRE
   Registrar mudanças de arquitetura, novos sistemas, decisões estratégicas.
   Atualizar a seção "Ordem prioritária" com as próximas fases.
```

---

## 7.1 Estrutura canonica de pastas

A estrutura de destino deve seguir:

`60_Sistemas/FabioOS/Mapa_Canonico_Pastas_Obsidian_v2_2026-06-29.md`

Pastas legadas como `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/`, `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/`, `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/30_Conhecimento/`, `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Decisoes/`, `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Repertorio/`, `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/50_Fontes/`, `sources/` e `wiki/` nao devem receber novos arquivos sem justificativa explicita. `sources/` e `wiki/` continuam como compatibilidade operacional ate migracao de links, RAG, MCP e scripts.

---

## 8. Regras de aprovação humana

> **A IA pode preparar. Só o humano pode executar.**

### O que a IA pode fazer sem aprovação

- Criar rascunhos, notas, listas e documentos locais
- Ler e organizar arquivos dentro do vault
- Rodar verificações de segurança
- Sugerir ações, estruturas e próximos passos
- Executar Git add e commit (com resumo antes de confirmar)
- Criar e editar arquivos Markdown no repositório local

### O que exige aprovação humana explícita

| Ação | Motivo |
|---|---|
| **Enviar** email, mensagem ou comunicado | Ação externa irreversível |
| **Publicar** conteúdo em plataformas externas | Visibilidade pública |
| **Apagar** arquivos ou pastas | Perda de dados |
| **Expor** dados sensíveis (alunos, finanças, credenciais) | Privacidade e segurança |
| **Executar** ações em APIs externas | Efeitos colaterais |
| **Push** para o GitHub | Versionamento público |
| **Fazer push --force** | Nunca fazer — exige justificativa crítica |
| **Acionar** automações n8n com efeito externo | Ações que afetam terceiros |

### Regra de verificação antes de commit

```
1. /check-secrets — verificar se há credenciais nos arquivos
2. Revisão do resumo de mudanças — o que foi alterado?
3. Confirmação do usuário — "pode commitar?"
4. git commit + push apenas após confirmação
```

---

## 9. Convenções de nomenclatura

### Regra geral

```
SISTEMA_CONTEXTO_TIPO.md
```

Datas no formato `YYYY-MM-DD`. Sem espaços — usar `-` ou `_`. Sem acentos no nome do arquivo.

---

### Escola

```
[ANO]_[TURMA]_[DISCIPLINA]_[BIMESTRE]_[TIPO].md
```

| Campo | Valores possíveis |
|---|---|
| ANO | `2026` |
| TURMA | `6A`, `7B`, `8C`, `9A` |
| DISCIPLINA | `GEO` (Geografia), `FIL` (Filosofia), `HIS`, `PORT` |
| BIMESTRE | `B1`, `B2`, `B3`, `B4` |
| TIPO | `PROVA`, `REVISAO`, `GABARITO`, `AULA`, `COMUNICADO`, `CRONOGRAMA` |

Exemplos:
```
2026_9A_GEO_B2_PROVA.md
2026_8B_FIL_B1_REVISAO.md
2026_7C_HIS_B3_GABARITO.md
```

---

### Pietra

```
PIETRA_[YYYY-MM]_[TIPO].md
```

| Campo | Valores possíveis |
|---|---|
| TIPO | `INTENT`, `RESPOSTA-PADRAO`, `FLUXO`, `LOG`, `ESCALONAMENTO` |

Exemplos:
```
PIETRA_2026-06_INTENT-FINANCEIRO.md
PIETRA_2026-06_RESPOSTA-PADRAO-HORARIO.md
PIETRA_2026-06_FLUXO-MATRICULA.md
```

---

### Trader

```
TRADER_[YYYY-MM-DD]_[TIPO].md   ← para entradas diárias
TRADER_[YYYY-MM]_[TIPO].md      ← para revisões mensais
```

| Campo | Valores possíveis |
|---|---|
| TIPO | `DIARIO`, `SETUP`, `REVISAO`, `ESTATISTICA`, `RISCO`, `METODO` |

Exemplos:
```
TRADER_2026-06-26_DIARIO.md
TRADER_2026-06_REVISAO.md
TRADER_2026-06_SETUP-IFR.md
```

---

### PRIMUS

```
PRIMUS_[SESSAO]_[TIPO].md
PRIMUS_[SESSAO]_[TIPO]-[SUBTIPO].md
```

| Campo | Valores possíveis |
|---|---|
| SESSAO | `S01`, `S02`, `S03` ... |
| TIPO | `EVENTO`, `PERSONAGEM`, `FACCAO`, `MISSAO`, `ITEM`, `WORLDFLAG`, `LORE` |

Exemplos:
```
PRIMUS_S01_EVENTO-ENCONTRO-FABIO.md
PRIMUS_S01_PERSONAGEM-ARIC.md
PRIMUS_S02_WORLDFLAG-GUERRA-DO-NORTE.md
```

---

### Fontes (`sources/`)

```
sources/[categoria]/[YYYY-MM-DD]_[slug].md
```

| Campo | Valores possíveis |
|---|---|
| categoria | `web`, `pdfs`, `docs`, `drive`, `repositorios`, `research` |
| slug | versão em kebab-case do título, sem acentos |

Exemplos:
```
sources/web/2026-06-26_fastmcp-framework-docs.md
sources/pdfs/2026-06-26_edital-concurso-xpto.md
sources/repositorios/2026-06-25_gsd-core.md
sources/research/2026-06-26_comparativo-bancos-vetoriais.md
```

---

### Changelogs (`50_Registros/Changelog/`)

```
YYYY-MM-DD_[slug-da-fase-ou-ação].md
```

Exemplos:
```
2026-06-26_fase7-consolidacao-camada1.md
2026-06-26_workstation-setup.md
2026-07-01_fase8-escola-inicial.md
```

---

### Notas estruturais e de sistemas

```
60_Sistemas/[Sistema]/[Nome_Em_Title_Case].md
```

Exemplos:
```
60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS.md
60_Sistemas/FabioOS/Protocolo_Operacional_FabioOS.md
60_Sistemas/Escola/Sistema_Escola.md
60_Sistemas/Claude_Code/Claude_Project_Config.md
```

---

## 10. Critérios de sucesso por fase

> Cada fase do FabioOS tem um teste objetivo — uma condição binária que pode ser verificada sem ambiguidade.

| Fase | Critério de sucesso verificável |
|---|---|
| 0 — Definição | "Consigo explicar o FabioOS em uma frase sem hesitar." |
| 1 — Vault | "Toda informação nova tem um lugar lógico para entrar." |
| 2 — GitHub | "O vault pode ser salvo, versionado e restaurado em outro computador." |
| 3 — Workstation | "O computador roda Claude Code, n8n e plugins sem erro." |
| 4 — Project-level | "Claude Code começa cada sessão com contexto do FabioOS, não de zero." |
| 5 — LLM-Wiki inicial | "O FabioOS começa a se explicar por dentro." |
| 6 — Bootstrap | "Digo 'leia o contexto e continue' — Claude Code sabe o que fazer." |
| 7 — Camada 1 | "Toda ferramenta principal tem função documentada e linkada." |
| **7.5 — Protocolo** | **"Qualquer entrada sabe onde vai e como será processada."** |
| 7.5 — Ingestão | "Um link externo vira fonte preservada + Markdown normalizado." |
| 8 — Escola | "Produzo uma prova do zero usando o FabioOS em menos de 30 min." |
| 9 — Pietra | "Uma mensagem simulada é classificada e recebe resposta sugerida." |
| 10 — n8n | "Um webhook gera uma nota em `sources/_inbox/`." |
| 11 — OpenClaw | "Uma mensagem externa aciona uma ação controlada no FabioOS." |
| 12 — RAG | "Perguntas recuperam notas relevantes do vault por semântica." |
| 13 — Grafo | "Projetos, ferramentas e decisões aparecem conectados visualmente." |
| 14 — MCPs | "Claude Code usa ferramenta externa com controle e log." |
| 15 — MCP FabioOS | "Qualquer IA autorizada consulta e opera o FabioOS por MCP." |
| 16 — Manus | "Manus entrega relatório que entra direto em `sources/research/`." |
| 17 — Hermes | "Hermes executa tarefa agendada sem supervisão contínua." |
| 18 — Trader | "Registro de operação gera cálculo de risco automaticamente." |
| 19 — PRIMUS | "IA lembra evento de sessão anterior sem precisar reler tudo." |

---

## Como usar

1. **Ao capturar:** pergunte "qual dos cinco destinos?" antes de salvar.
2. **Ao usar IA:** dê o contexto + peça o rascunho. Revise antes de qualquer ação externa.
3. **Ao commitar:** sempre rodar `/check-secrets` e mostrar resumo antes do push.
4. **Nas rotinas:** diária (5–15 min), semanal (30–60 min), mensal (1–2h).
5. **Ao avaliar uma fase:** use o critério de sucesso — passou ou não passou.

---

## Relações

- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]
- [[60_Sistemas/FabioOS/Mapa_Canonico_Pastas_Obsidian_v2_2026-06-29]]
- [[wiki/indices/mapa-fabios]]
- [[schema/fluxo-wiki]]
- [[schema/qualidade-wiki]]
- [[.claude/commands/check-secrets]]
- [[.claude/commands/safe-commit]]
- [[.claude/commands/session-changelog]]

## Próximas ações

- [ ] Testar rotina diária por 3 dias consecutivos
- [ ] Criar template de nota de inbox para `00_Inbox/`
- [ ] Avaliar se convenções de nome precisam de ajuste após uso real
- [ ] Revisar critérios de sucesso após Fase 8
