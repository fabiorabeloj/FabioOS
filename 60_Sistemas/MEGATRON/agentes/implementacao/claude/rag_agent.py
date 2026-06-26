#!/usr/bin/env python3
"""
Agente RAG (agent.rag) — implementação mínima (wrapper da Fase 12).

Conforme specs/Agente_RAG.md. NÃO duplica lógica: delega ao
60_Sistemas/RAG/scripts/query_rag.py (Chroma + bge-m3 local, exclui dados
sensíveis, responde com fontes). Aqui só orquestra e registra log.

Uso:
    python rag_agent.py "O que é o FabioOS?"
"""
import importlib.util
import subprocess
import sys
from pathlib import Path

from _common import vault_root, log_event

ROOT = vault_root()
QUERY_SCRIPT = ROOT / "60_Sistemas" / "RAG" / "scripts" / "query_rag.py"
DB_PATH = ROOT / "60_Sistemas" / "RAG" / "fabioos_db"


def deps_ok() -> bool:
    return all(importlib.util.find_spec(m) for m in ("chromadb", "sentence_transformers"))


def main():
    pergunta = " ".join(sys.argv[1:]).strip()
    if not pergunta:
        print('Uso: python rag_agent.py "sua pergunta"')
        return 1

    if not deps_ok():
        print("⚠️  Dependências da Fase 12 ausentes (chromadb, sentence-transformers).")
        print("   Instale conforme 60_Sistemas/RAG/requirements.txt e rode ingest_vault.py.")
        log_event("RAG", "consulta", "bloqueado: deps ausentes")
        return 2
    if not DB_PATH.exists():
        print("⚠️  Índice vetorial não encontrado. Rode primeiro:")
        print("   python 60_Sistemas/RAG/scripts/ingest_vault.py")
        log_event("RAG", "consulta", "bloqueado: indice ausente")
        return 2

    print(f"🔎 RAG → {pergunta!r}\n")
    res = subprocess.run([sys.executable, str(QUERY_SCRIPT), pergunta],
                         cwd=ROOT, text=True)
    log_event("RAG", "consulta", f"pergunta respondida (rc={res.returncode})")
    return res.returncode


if __name__ == "__main__":
    sys.exit(main())
