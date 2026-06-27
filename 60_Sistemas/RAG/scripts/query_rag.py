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

import chromadb
from sentence_transformers import SentenceTransformer

SCRIPT_DIR = Path(__file__).resolve().parent
DB_PATH = SCRIPT_DIR.parent / "fabioos_db"
COLLECTION = "fabioos"
MODEL_NAME = "BAAI/bge-m3"
CLAUDE_MODEL = "claude-sonnet-4-6"   # padrão do passo de geração (Fase 12)

SYSTEM = (
    "Você é o assistente do FabioOS. Responda APENAS com base no contexto "
    "fornecido. Se a informação não estiver no contexto, diga que não encontrou "
    "no vault. Cite as fontes (caminhos) que usou. Responda em português do Brasil."
)


def retrieve(question: str, k: int):
    model = SentenceTransformer(MODEL_NAME)
    client = chromadb.PersistentClient(path=str(DB_PATH))
    collection = client.get_collection(COLLECTION)
    q_emb = model.encode([question], normalize_embeddings=True).tolist()
    res = collection.query(query_embeddings=q_emb, n_results=k)
    docs = res["documents"][0]
    metas = res["metadatas"][0]
    return list(zip(docs, metas))


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
    print("🤖 Resposta (Claude Sonnet 4.6):\n")
    print(answer_with_claude(question, context))
    print("\n📚 Fontes:")
    for _, meta in hits:
        print(f"   - {meta['source_path']}  [[{meta['filename']}]]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
