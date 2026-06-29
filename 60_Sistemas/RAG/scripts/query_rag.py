#!/usr/bin/env python3
"""
FabioOS — RAG Fase 12: consulta mínima.

pergunta -> embedding local (bge-m3) -> busca no Chroma -> Claude (com fontes).

Por padrão opera em MODO RECUPERAÇÃO (só mostra os trechos encontrados). O Claude
SÓ é chamado com a flag explícita --generate (e exige ANTHROPIC_API_KEY) — evita
envio de contexto/custo não intencional.

Uso:
    python query_rag.py "O que é o FabioOS?"              # modo recuperação
    python query_rag.py "Qual a fase atual?" --k 5
    python query_rag.py "Explique o RAG" --generate       # chama o Claude
"""
from pathlib import Path
import argparse
import os
import sys

# Console do Windows usa cp1252; força UTF-8 no stdout/stderr (emojis/acentos).
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

import chromadb
from sentence_transformers import SentenceTransformer

SCRIPT_DIR = Path(__file__).resolve().parent
DB_PATH = SCRIPT_DIR.parent / "fabioos_db"
COLLECTION = "fabioos"
MODEL_NAME = "BAAI/bge-m3"
CLAUDE_MODEL = os.getenv("FABIOOS_RAG_CLAUDE_MODEL", "claude-sonnet-4-6")
_MODEL = None


def get_model():
    global _MODEL
    if _MODEL is None:
        _MODEL = SentenceTransformer(MODEL_NAME)
    return _MODEL

OPERATIONAL_TERMS = (
    "fase atual", "status", "pendência", "pendencias", "pendências",
    "próxima ação", "proxima acao", "próximo passo", "proximo passo",
    "roadmap", "o que continua", "onde estamos",
)
OPERATIONAL_QUERY_SUFFIX = (
    " Painel de Pendências FabioOS próximo passo de execução confirmado "
    "roadmap por trilho fase atual pendências abertas status operacional "
    "STATUS Estado atual prioridade atual Fase 12 validação parcial"
)
CANONICAL_OPERATIONAL_SOURCES = {
    "90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Painel_Pendencias_FabioOS.md": 0.12,
    "40_Wiki/_compat_wiki/indices/mapa-fabios.md": 0.07,
    "60_Sistemas/FabioOS/STATUS.md": 0.10,
    "60_Sistemas/FabioOS/NEXT_ACTIONS.md": 0.09,
}

SYSTEM = (
    "Você é o assistente do FabioOS. Responda APENAS com base no contexto "
    "fornecido. Se a informação não estiver no contexto, diga que não encontrou "
    "no vault. Cite as fontes (caminhos) que usou. Responda em português do Brasil."
)


def is_operational_query(question: str) -> bool:
    q = question.lower()
    return any(term in q for term in OPERATIONAL_TERMS)


def retrieve(question: str, k: int):
    operational = is_operational_query(question)
    retrieval_question = question + OPERATIONAL_QUERY_SUFFIX if operational else question
    pool_k = max(k, 40) if operational else k

    model = get_model()
    client = chromadb.PersistentClient(path=str(DB_PATH))
    collection = client.get_collection(COLLECTION)
    q_emb = model.encode([retrieval_question], normalize_embeddings=True).tolist()
    res = collection.query(query_embeddings=q_emb, n_results=pool_k)
    docs = res["documents"][0]
    metas = res["metadatas"][0]
    distances = res.get("distances", [[]])[0]
    hits = list(zip(docs, metas, distances or [0.0] * len(docs)))

    if operational:
        def score(hit):
            doc, meta, distance = hit
            source_path = meta.get("source_path", "")
            header_path = meta.get("header_path", "").lower()
            text = f"{header_path}\n{doc[:700]}".lower()
            boost = CANONICAL_OPERATIONAL_SOURCES.get(source_path, 0.0)
            if "trilho pessoal" in header_path or "prioridade atual" in header_path:
                boost += 0.16
            if "fase 12" in text:
                boost += 0.08
            if "validacao parcial" in text or "validação parcial" in text:
                boost += 0.08
            if source_path == "60_Sistemas/FabioOS/STATUS.md":
                boost += 0.08
            if "pendências abertas" in header_path or "pendencias abertas" in header_path:
                boost += 0.05
            if "próximas ações" in header_path or "proximas ações" in header_path:
                boost += 0.04
            if "documento de referência mestre" in header_path:
                boost += 0.03
            return distance - boost

        hits.sort(key=score)

    return [(doc, meta) for doc, meta, _ in hits[:k]]


def build_context(hits):
    parts = []
    for i, (doc, meta) in enumerate(hits, 1):
        parts.append(f"[{i}] (fonte: {meta['source_path']})\n{doc}")
    return "\n\n".join(parts)


def answer_with_claude(question: str, context: str):
    import anthropic
    client = anthropic.Anthropic()
    msg = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=1024,
        system=SYSTEM,
        messages=[{"role": "user",
                   "content": f"Contexto do FabioOS:\n\n{context}\n\nPergunta: {question}"}],
    )
    return "".join(b.text for b in msg.content if b.type == "text")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("question", nargs="+", help="pergunta")
    ap.add_argument("--k", type=int, default=4, help="nº de trechos (top-k)")
    ap.add_argument("--generate", action="store_true",
                    help="chamar o Claude para gerar resposta; sem a flag, modo recuperação")
    args = ap.parse_args()
    question = " ".join(args.question)

    if not DB_PATH.exists():
        print("⚠️  Banco vetorial não encontrado. Rode ingest_vault.py primeiro.")
        return 1

    print(f"🔍 Busca: {question!r}\n")
    hits = retrieve(question, args.k)
    if not hits:
        print("Nenhum trecho relevante encontrado.")
        return 0

    def mostrar_recuperacao():
        for i, (doc, meta) in enumerate(hits, 1):
            print(f"[{i}] {meta['source_path']}  ({meta.get('header_path', '')})")
            print(f"    {doc[:240].strip()}...\n")

    # Claude SÓ é chamado com --generate explícito (evita custo/envio não intencional).
    if not args.generate:
        print("ℹ️  MODO RECUPERAÇÃO (use --generate para resposta do Claude).\n")
        mostrar_recuperacao()
        return 0

    if not os.getenv("ANTHROPIC_API_KEY"):
        print("⚠️  --generate pedido, mas ANTHROPIC_API_KEY ausente. "
              "Caindo para MODO RECUPERAÇÃO.\n")
        mostrar_recuperacao()
        return 0

    context = build_context(hits)
    print(f"🤖 Resposta ({CLAUDE_MODEL}):\n")
    print(answer_with_claude(question, context))
    print("\n📚 Fontes:")
    for _, meta in hits:
        print(f"   - {meta['source_path']}  [[{meta['filename']}]]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
