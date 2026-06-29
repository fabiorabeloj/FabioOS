---
tipo: revisao
area: 60_Sistemas
projeto: FabioOS
sistema: MEGATRON
status: rascunho
tags: [megatron, agentes, revisao, implementacao-minima, codex]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Revisão da Implementação Mínima dos Agentes MEGATRON

## Função

Registrar revisão técnica preliminar da implementação mínima criada em:

```text
60_Sistemas/MEGATRON/agentes/implementacao/claude/
```

Esta revisão não promove agentes para `piloto`. Ela apenas identifica o que está adequado, o que precisa ajuste e quais critérios devem ser cumpridos antes da promoção.

## Escopo revisado

| Arquivo | Papel |
|---|---|
| `_common.py` | Utilitários comuns, raiz do vault, log e UTF-8 |
| `safecommit.py` | Diagnóstico de commit e scan de segredos |
| `arquivista.py` | Criação de nota rascunho em `00_Inbox/` |
| `inbox.py` | Triagem report-only de `00_Inbox/` |
| `rag_agent.py` | Wrapper da Fase 12 RAG |
| `dashboard.py` | Geração de `STATUS_Agentes.md` |

---

## 1. Síntese executiva

A implementação mínima está coerente com a direção das specs: usa biblioteca padrão, evita push, evita commit automático, registra logs e falha de forma segura no RAG quando dependências estão ausentes.

 Após os commits temáticos do Claude, os dois achados P1 foram corrigidos pelo Codex em working tree:

- SafeCommit deixou de sugerir `git add -A` e agora orienta stage explícito por grupo temático.
- Arquivista passou a recusar `--dest` fora da raiz do vault.

Ainda assim, os agentes devem permanecer como:

```text
status: especificado
implementacao_minima: criada
promocao: pendente de revisao humana
```

Não recomendo promover para `piloto` antes dos ajustes listados abaixo.

---

## 2. Pontos fortes

- SafeCommit é advisor-only: não commita, não faz stage e não faz push.
- SafeCommit respeita `.gitignore` usando `git ls-files --modified --others --exclude-standard`.
- Valores de possíveis segredos não são armazenados nem exibidos.
- Arquivista evita sobrescrever arquivo existente.
- Inbox é report-only e não move/apaga arquivos.
- RAG falha de forma controlada quando dependências estão ausentes.
- Dashboard gera painel Markdown legível e rastreável.
- Logs ficam em `agentes/logs/`, que está ignorado pelo Git pela regra global `logs/`.

---

## 3. Achados por severidade

## 3.1 P1 — SafeCommit sugere `git add -A` genérico

**Status:** corrigido em working tree após o commit `32ae46c`.

**Arquivo:** `safecommit.py`

**Problema:** a saída final sugere:

```bash
git add -A && git commit -m "..."
```

Isso conflita com a estratégia atual de commits temáticos. Se o usuário copiar o comando, todos os grupos pendentes entram juntos: integração Codex, modelo formal, specs, implementação, RAG e arquivos paralelos do Codex.

**Impacto:** commit grande, mistura de escopos e possível inclusão de arquivos que deveriam ficar para commit separado.

**Recomendação:** SafeCommit deve sugerir commit por lista explícita de arquivos ou aceitar modo por grupo:

```text
python safecommit.py --paths <arquivos...>
```

Enquanto isso, usar SafeCommit apenas como diagnóstico, não como comando final de stage.

## 3.2 P1 — Arquivista aceita `--dest` sem restringir ao vault

**Status:** corrigido em working tree após o commit `32ae46c`.

**Arquivo:** `arquivista.py`

**Problema:** `dest_dir = ROOT / (args.dest or "00_Inbox")` pode permitir destino fora do vault se `--dest` usar caminho absoluto ou segmentos `..`, dependendo da forma como o usuário chamar.

**Impacto:** escrita fora da estrutura FabioOS.

**Recomendação:** resolver o caminho e validar que ele permanece dentro de `ROOT` antes de escrever.

Critério:

```text
dest_dir.resolve().is_relative_to(ROOT.resolve())
```

ou equivalente compatível.

## 3.3 P2 — SafeCommit usa scan de alto sinal, mas não cobre todo o contrato da spec

**Arquivo:** `safecommit.py`

**Problema:** a spec do agente menciona padrões amplos como `Authorization`, `anthropic`, `.env` e strings longas. A implementação atual usa padrões de alto sinal, o que reduz falso positivo, mas pode deixar passar casos que a spec mandaria revisar.

**Impacto:** falsa sensação de segurança se for tratado como scan final.

**Recomendação:** declarar explicitamente no output:

```text
scan de alto sinal, não substitui revisão completa
```

ou adicionar modo `--strict` com padrões mais amplos.

## 3.4 P2 — Inbox classifica domínio apenas pelo nome do arquivo

**Arquivo:** `inbox.py`

**Problema:** a função `dominio_por_nome` usa apenas o nome do arquivo, não o conteúdo.

**Impacto:** entradas com nome genérico podem ser classificadas como `indefinido` mesmo quando o conteúdo aponta para Escola, PietraOS ou PrimusOS.

**Recomendação:** para arquivos `.md` e `.txt`, ler amostra inicial do conteúdo e classificar por nome + texto.

## 3.5 P2 — Dashboard depende de log local ignorado pelo Git

**Arquivo:** `dashboard.py`

**Problema:** `STATUS_Agentes.md` é versionável, mas sua base principal de última execução (`agentes/logs/agentes_log.md`) é local e ignorada pelo Git.

**Impacto:** outro ambiente pode abrir o dashboard e ver status desatualizado ou sem histórico.

**Recomendação:** manter logs runtime ignorados, mas registrar execuções relevantes em changelog ou relatório versionável quando promover agente para piloto.

## 3.6 P3 — `_common.py` possui fallback frágil de raiz

**Arquivo:** `_common.py`

**Problema:** `return p.parents[5]` funciona na estrutura atual, mas é frágil se o arquivo mudar de profundidade.

**Impacto:** baixo agora; pode quebrar se a implementação for movida.

**Recomendação:** se `60_Sistemas/FabioOS/bootstrap/CLAUDE.md` não for encontrado, falhar explicitamente com erro claro em vez de inferir por índice fixo.

---

## 4. Avaliação por agente

| Agente | Estado recomendado | Motivo |
|---|---|---|
| SafeCommit | manter especificado | Bom advisor, mas precisa evitar sugestão `git add -A` em ambiente multi-commit |
| Arquivista | manter especificado | Útil, mas precisa restringir destino ao vault |
| Inbox | manter especificado | Seguro por ser report-only, mas classificação ainda superficial |
| RAG | manter especificado | Wrapper correto, mas depende da Fase 12 instalada e indexada |
| Dashboard | manter especificado | Útil, mas status depende de log local ignorado |

---

## 5. Critérios antes de promover para piloto

- [ ] SafeCommit suporta execução por grupo de arquivos ou deixa de sugerir `git add -A`.
- [ ] Arquivista valida que `--dest` permanece dentro do vault.
- [ ] Inbox classifica por nome + conteúdo para `.md` e `.txt`.
- [ ] RAG é testado após instalação das dependências e ingestão da primeira leva.
- [ ] Dashboard diferencia status local gerado de status versionado.
- [ ] Uma revisão humana lê os scripts alterados.
- [ ] SafeCommit/check-secrets roda antes do commit.

---

## 6. Recomendação para o Claude

Antes de commitar a implementação mínima dos agentes:

1. manter os agentes como `especificado`;
2. não promover para `piloto`;
3. commitar as correções P1 em commit próprio;
4. revisar depois os achados P2 antes de promover para piloto;
5. não fazer push sem aprovação humana.

Mensagem curta sugerida:

```text
Os dois P1 foram corrigidos após os commits temáticos:
1. SafeCommit não sugere mais `git add -A`.
2. Arquivista bloqueia `--dest` fora do vault.

Recomendação: commitar essas correções em commit próprio antes de qualquer promoção dos agentes.
```

## Relações

- [[60_Sistemas/MEGATRON/agentes/Revisao_Agentes_Checklist]]
- [[60_Sistemas/MEGATRON/agentes/specs/Agente_SafeCommit]]
- [[60_Sistemas/MEGATRON/agentes/specs/Agente_Arquivista]]
- [[60_Sistemas/FabioOS/Matriz_Frentes_Paralelas]]
- [[60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente]]
