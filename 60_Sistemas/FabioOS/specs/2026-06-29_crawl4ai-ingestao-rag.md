---
tipo: spec
area: 60_Sistemas
projeto: FabioOS
status: rascunho
fase: 18.1
dominio: FabioOS
classe_dado: interno
permissao: leitura_e_proposta
autor: Claude (arquiteto-chefe)
criado_em: 2026-06-29
atualizado_em: 2026-06-29
tags: [fabios, spec, crawl4ai, rag, ingestao, stack, matriz-aptidao]
---

# SPEC - Crawl4AI: ingestão web limpa para o RAG

> Primeiro tool da stack operacional a passar pelo portão de governança
> (ver [[50_Registros/Decisoes/ADR_2026-06-29_Stack_Operacional_e_Barramento_Capacidades]]).
> Esta SPEC **não autoriza instalação** — documenta a avaliação e o plano. Instalar
> exige OK explícito do Fabio.

## 1. Problema

O RAG (Fase 12, piloto) só indexa o vault local. Conhecimento da web (documentação
técnica, artigos, editais) entra de forma manual e pontual (skill `ingest-url`).
Falta um pipeline confiável que transforme páginas — inclusive sites em JavaScript —
em **markdown limpo e estruturado** pronto para virar fonte e alimentar o RAG.

## 2. Objetivo

Pipeline local e governado: `URL -> Crawl4AI -> markdown limpo -> 05_Raw_Sources/web/
-> revisão humana -> RAG`. Ativa o agente `pesquisador` (hoje `planejado` no
registry) com a capacidade `coletar_web` / `alimentar_rag`.

## 3. Matriz de Aptidão (portão antes de instalar)

| Critério | Avaliação |
|---|---|
| **Vocação** | Crawler open-source feito p/ IA: devolve markdown/JSON estruturado, entende sites JS, extrai tabelas/links. Melhor da categoria p/ alimentar RAG. |
| **Encaixe FabioOS** | Camada Conhecimento/RAG; alimenta o Chroma+bge-m3 que já existe. Não substitui curadoria humana (sources/ → revisão → wiki/RAG). |
| **Limites** | Respeitar robots.txt/ToS; sem login/paywall; sem dados pessoais sem consentimento; não é curador (humano decide o que promove). |
| **Riscos** | Scraping de site proibido; conteúdo-lixo poluir o RAG; custo de runtime/tempo; sites que bloqueiam. |
| **Permanência** | Manter se reduzir o trabalho de ingestão e melhorar a recuperação; descartar se gerar ruído > sinal. |
| **Barreira de adoção** | **Baixa**: `pip install crawl4ai` (Python local), não exige Docker/servidor. Menor risco que Coolify/Supabase/Dify. |

## 4. Fora de escopo

- Instalar agora (precisa OK do Fabio).
- Scraping em massa / agendado (vem depois, gated).
- Sites com login, paywall ou dados pessoais.
- Reindex automático do RAG sem lock e sem revisão humana.
- Qualquer API externa paga.

## 5. Domínio, dados e permissões

| Campo | Valor |
|---|---|
| Domínio | FabioOS (conhecimento) |
| Classe de dado | público (web) → vira interno em `05_Raw_Sources/web/` |
| Escrita | só em `05_Raw_Sources/web/` (escrita segura; revisão antes de promover) |
| RAG | só após revisão humana + reindex **com lock** |
| Modelo externo/API | não usa |
| Aprovação humana | obrigatória p/ instalar e p/ promover fonte → RAG |

## 6. Arquitetura proposta

```text
URL (aprovada)
  -> Crawl4AI (local) -> markdown limpo + metadados
  -> Arquivista: salva em 05_Raw_Sources/web/<slug>.md (status: rascunho)
  -> revisão humana (curadoria)
  -> promover a fonte/wiki -> reindex RAG (com lock no Registro_Frentes_Ativas)
  -> MEGATRON 'pesquisador' passa de planejado a ativo
```

## 7. Plano de tarefas (após OK do Fabio)

- [x] `pip install crawl4ai` (0.9.0) no venv do RAG + `playwright install chromium` + smoke test (`example.com` → markdown limpo, dry-run). **Feito 2026-06-30.**
- [x] `pesquisador.py`: `run(url) -> Resultado` (markdown limpo; dry-run só prévia; `--confirmar` salva em `05_Raw_Sources/web/`).
- [x] Registrar agente `pesquisador` como `ativo` no `registry.py` (Maestro mostra 6 ativos).
- [ ] Golden de crawl real: 5 casos (doc técnica, artigo, página JS, tabela, página bloqueada → falha graciosa). [golden atual: import+rota ativa, sem rede]
- [ ] Registrar experiência no ReasoningBank (funcionou? que tipo de site?).
- [ ] (opcional) Wire `coletar_web` ao responder do MEGATRON (intent "pesquisar").

## 8. Testes mínimos

- [ ] URL de documentação técnica → markdown estruturado.
- [ ] Página JS pesada → conteúdo recuperado.
- [ ] Página com tabela → tabela preservada.
- [ ] Site que bloqueia / 404 → falha graciosa, sem travar.
- [ ] robots.txt proíbe → respeita e aborta com aviso.

## 9. Riscos e mitigação

| Risco | Mitigação |
|---|---|
| Scraping indevido | só URLs aprovadas; respeitar robots/ToS; sem login/paywall |
| Lixo no RAG | sources/ é rascunho; humano cura antes de promover; reindex com lock |
| Dados pessoais | bloquear; classificar com `classificar_dado_fabioos.py` antes do RAG |
| Runtime/custo | local, sob demanda; sem agendamento automático nesta fase |

## 10. Rollback

`pip uninstall crawl4ai`; agente `pesquisador` volta a `planejado`; nada no RAG é
tocado sem reindex explícito. Rollback local e seguro.

## 11. Changelog esperado

`50_Registros/Changelog/2026-06-29_crawl4ai-spec.md` (e na implementação).

## Relações
- [[50_Registros/Decisoes/ADR_2026-06-29_Stack_Operacional_e_Barramento_Capacidades]]
- [[60_Sistemas/MEGATRON/v1/registry]]
- [[60_Sistemas/RAG/scripts/ingest_vault]]
