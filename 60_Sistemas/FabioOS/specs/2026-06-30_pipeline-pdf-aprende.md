---
tipo: spec
area: 60_Sistemas
projeto: FabioOS
status: rascunho
fase: 18.2
dominio: FabioOS
classe_dado: interno
permissao: leitura_e_proposta
autor: Claude (arquiteto-chefe)
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [fabios, spec, pdf, stirling, rag, ingestao, drop-folder, documentalista, multiagente]
---

# SPEC - Pipeline "Drop PDF → o sistema aprende"

## 1. Visão (do Fabio)

Uma **pasta (ou nuvem) onde o Fabio deposita qualquer PDF** — prova, edital,
artigo, contrato — e o sistema **processa → aprende → indexa → registra no
Obsidian**, sozinho. O conhecimento do documento entra na memória pesquisável.

## 2. Arquitetura (com zonas claras)

```text
Fabio deposita PDF
  • pasta local 00_Inbox/pdfs/   (drop folder)
  • OU nuvem: Google Drive sync / Mobile Gateway :8787 / webhook n8n
        ↓
[PORTA DE ENTRADA — zona CODEX]
  watcher de pasta OU fluxo n8n detecta PDF novo → chama o pipeline
        ↓
[PIPELINE COGNITIVO — zona CLAUDE/MEGATRON]
  1. documentalista (Stirling PDF): OCR + extrai texto → markdown limpo
  2. classificar_dado_fabioos.py: gate de dado sensível (bloqueia se preciso)
  3. Arquivista: cria nota-fonte em 05_Raw_Sources/pdfs/<slug>.md
     (frontmatter, domínio classificado, status: rascunho, fonte_pdf)
        ↓
[CURADORIA HUMANA opcional] → Fabio aprova/promove
        ↓
  4. RAG: reindexa COM LOCK → o sistema "aprende"
  5. Registro: a nota É o registro no Obsidian + changelog
```

## 3. Divisão de trabalho

| Parte | Dono | O quê |
|---|---|---|
| **Porta de entrada** | **Codex** | `00_Inbox/pdfs/` watcher e/ou fluxo n8n e/ou Mobile Gateway; detecta PDF novo e dispara o pipeline (subprocess do documentalista ou endpoint). É a zona n8n/gateway do Codex. |
| **Extração** | Claude (documentalista) | Stirling PDF: OCR + texto → markdown |
| **Classificação/Nota** | Claude (Arquivista + classificador) | gate sensível + nota-fonte no Obsidian |
| **Aprendizado** | Claude (RAG) | reindex com lock após curadoria |
| **Credencial Stirling** | **Fabio** | `STIRLING_USERNAME/PASSWORD` ou desabilitar login (HOJE dá HTTP 401) |

## 4. Fora de escopo (v0)

- Auto-promover ao RAG sem curadoria (começa com revisão humana).
- PDFs com dado pessoal de terceiros sem consentimento (gate bloqueia).
- Nuvem externa sem o Fabio configurar (Drive/n8n são frentes gated).
- Execução real de OCR enquanto o Stirling exigir auth não configurada.

## 5. Bloqueio atual (resolver primeiro)

**Stirling exige autenticação (HTTP 401).** Sem credencial, o documentalista
detecta o Stirling mas não executa OCR. **Ação do Fabio:** definir
`STIRLING_USERNAME`/`STIRLING_PASSWORD` no container ou desabilitar o login
(`SECURITY_ENABLELOGIN=false`). Depois disso, o documentalista passa de
"requer auth" para operacional.

## 6. Plano de tarefas

**Codex (porta de entrada):**
- [ ] Criar `00_Inbox/pdfs/` como drop folder oficial.
- [ ] Watcher (Python/n8n) que detecta PDF novo e chama o pipeline.
- [ ] (opcional) Conectar Mobile Gateway :8787 e/ou webhook n8n p/ depósito remoto.

**Claude (pipeline):**
- [ ] documentalista: implementar OCR/extração real via Stirling (após auth).
- [ ] Encadear documentalista → classificador → Arquivista (nota em `05_Raw_Sources/pdfs/`).
- [ ] Política de reindex com lock após curadoria.
- [ ] ReasoningBank: registrar cada ingestão (funcionou? tipo de PDF?).

**Fabio:**
- [ ] Configurar auth do Stirling.
- [ ] Decidir: curadoria humana antes do RAG (recomendado) vs auto-aprender.

## 7. Critérios de aceite

- [ ] PDF na pasta → nota-fonte limpa em `05_Raw_Sources/pdfs/` (rascunho).
- [ ] Dado sensível é detectado e bloqueia auto-promção.
- [ ] Após curadoria, conteúdo entra no RAG (reindex com lock) e é recuperável.
- [ ] Nada é executado sem o Stirling autenticado; sem push automático.

## 8. Relações
- [[60_Sistemas/MEGATRON/agentes/implementacao/claude/documentalista]]
- [[60_Sistemas/FabioOS/Stack_Tier2_Provisionamento_2026-06-29]]
- [[60_Sistemas/FabioOS/scripts/classificar_dado_fabioos]]
- [[60_Sistemas/RAG/scripts/ingest_vault]]
- [[50_Registros/Barramento_Multiagente]]
