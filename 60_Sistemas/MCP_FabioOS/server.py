#!/usr/bin/env python3
"""
MCP FabioOS (Fase 15) — expõe RAG, Grafo e vault como ferramentas padronizadas.

v0: SOMENTE CONSULTA (read-only). Não escreve, não reindexa, não apaga.
Reaproveita capacidades já validadas:
  - RAG  : chromadb + bge-m3 (in-process, leitura do fabioos_db)
  - Grafo: subprocess do 60_Sistemas/Grafo/scripts/query_graph.py
  - Vault: filesystem (stdlib)

Rodar (após instalar fastmcp no venv do RAG — ver requirements.txt):
    60_Sistemas/RAG/.venv/Scripts/python.exe 60_Sistemas/MCP_FabioOS/server.py
"""
from pathlib import Path
import subprocess
import sys

from fastmcp import FastMCP


def _vault_root() -> Path:
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / "60_Sistemas/FabioOS/bootstrap/CLAUDE.md").exists():
            return parent
    return p.parents[2]


VAULT = _vault_root()
RAG_DB = VAULT / "60_Sistemas" / "RAG" / "fabioos_db"
QUERY_GRAPH = VAULT / "60_Sistemas" / "Grafo" / "scripts" / "query_graph.py"
RAG_MODEL = "BAAI/bge-m3"
EXCLUI = ("/.venv/", "/fabioos_db/", "/node_modules/", "/.git/",
          "/.obsidian/", "/.claude/", "/05_Raw_Sources/_compat_sources/_inbox/")

mcp = FastMCP("FabioOS")

# --- RAG: modelo carregado uma vez, mantido em memória ---
_model = None
_collection = None


def _rag():
    global _model, _collection
    if _collection is None:
        import chromadb
        from sentence_transformers import SentenceTransformer
        _model = SentenceTransformer(RAG_MODEL)
        _collection = chromadb.PersistentClient(
            path=str(RAG_DB)).get_collection("fabioos")
    return _model, _collection


@mcp.tool
def consultar_rag(pergunta: str, k: int = 5) -> str:
    """Busca semântica no conhecimento do vault (RAG, read-only).

    Retorna os trechos mais relevantes com a fonte. Use para perguntas do tipo
    'o que o FabioOS sabe/decidiu/definiu sobre X'. Não chama modelo externo.
    """
    if not RAG_DB.exists():
        return "Índice RAG ausente. Rode 60_Sistemas/RAG/scripts/ingest_vault.py."
    model, col = _rag()
    emb = model.encode([pergunta], normalize_embeddings=True).tolist()
    r = col.query(query_embeddings=emb, n_results=max(1, min(k, 20)))
    docs, metas = r["documents"][0], r["metadatas"][0]
    dists = (r.get("distances") or [[None] * len(docs)])[0]
    if not docs:
        return "Nenhum trecho relevante encontrado."
    linhas = []
    for d, m, dist in zip(docs, metas, dists):
        ds = f"dist={dist:.3f} " if isinstance(dist, (int, float)) else ""
        linhas.append(f"[{ds}{m.get('source_path', '?')}] "
                      f"({m.get('header_path', '')})\n{d[:400].strip()}")
    return "\n\n".join(linhas)


@mcp.tool
def consultar_grafo(termo: str = "", top: int = 10) -> str:
    """Consulta o grafo de conhecimento (read-only).

    Com 'termo', busca nós relacionados; sem termo, lista os hubs (nós mais
    conectados). Use para 'o que se relaciona com X' ou 'quais os centros do vault'.
    """
    if not QUERY_GRAPH.exists():
        return "Script do grafo ausente."
    args = [sys.executable, str(QUERY_GRAPH)]
    args += ["--search", termo, "--limit", str(top)] if termo else ["--top", str(top)]
    try:
        out = subprocess.run(args, cwd=str(VAULT), capture_output=True,
                             text=True, encoding="utf-8", timeout=60).stdout
    except Exception as e:
        return f"Erro ao consultar grafo: {e}"
    return out.strip() or "Sem resultado (talvez rodar build_graph.py primeiro)."


@mcp.tool
def buscar_nota(termo: str, limite: int = 15) -> str:
    """Busca arquivos .md no vault cujo nome OU conteúdo contenha o termo (read-only)."""
    termo_l = termo.lower()
    achados = []
    for md in VAULT.rglob("*.md"):
        rel = md.relative_to(VAULT).as_posix()
        if any(e in "/" + rel + "/" for e in EXCLUI):
            continue
        hit_nome = termo_l in md.name.lower()
        if not hit_nome:
            try:
                if termo_l not in md.read_text(encoding="utf-8", errors="ignore").lower():
                    continue
            except Exception:
                continue
        achados.append(rel + ("  (nome)" if hit_nome else "  (conteúdo)"))
        if len(achados) >= limite:
            break
    return "\n".join(achados) or "Nenhuma nota encontrada."


@mcp.tool
def consultar_wiki(termo: str, limite: int = 15) -> str:
    """Busca páginas em 40_Wiki/_compat_wiki/ cujo nome ou conteúdo contenha o termo (read-only)."""
    base = VAULT / "40_Wiki/_compat_wiki"
    if not base.exists():
        return "40_Wiki/_compat_wiki/ não existe."
    termo_l = termo.lower()
    achados = []
    for md in base.rglob("*.md"):
        rel = md.relative_to(VAULT).as_posix()
        try:
            txt = md.read_text(encoding="utf-8", errors="ignore").lower()
        except Exception:
            continue
        if termo_l in md.name.lower() or termo_l in txt:
            achados.append(rel)
            if len(achados) >= limite:
                break
    return "\n".join(achados) or "Nenhuma página wiki encontrada."


@mcp.tool
def listar_projetos() -> str:
    """Lista os projetos em 20_Projetos/ (read-only)."""
    base = VAULT / "20_Projetos"
    if not base.exists():
        return "20_Projetos/ não existe."
    itens = sorted({p.relative_to(base).parts[0]
                    for p in base.rglob("*") if p.is_file()})
    return "\n".join(itens) or "Sem projetos."


if __name__ == "__main__":
    mcp.run()
