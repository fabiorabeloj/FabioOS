#!/usr/bin/env python3
"""
FabioOS — RAG Fase 12: ingestão mínima do vault.

Lê a 1a leva de pastas, faz chunking consciente de cabeçalhos, gera embeddings
LOCAIS (bge-m3) e armazena no Chroma. Versão mínima funcional — não perfeita.

Segurança: NUNCA indexa logs sensíveis (sources/_inbox/, PIETRA*_LOG, etc.).
Embeddings 100% locais — nada sai da máquina.

Uso:
    python ingest_vault.py
"""
from pathlib import Path
import re
import sys

# Console do Windows usa cp1252; força UTF-8 no stdout/stderr (emojis/acentos).
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

import chromadb
import frontmatter
from sentence_transformers import SentenceTransformer

# --- Configuração ---------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = SCRIPT_DIR.parents[2]          # .../FabioOs/FabioOs
DB_PATH = SCRIPT_DIR.parent / "fabioos_db"  # 60_Sistemas/RAG/fabioos_db
COLLECTION = "fabioos"
MODEL_NAME = "BAAI/bge-m3"                   # multilíngue, forte em PT-BR, local

# 1a leva de pastas (alto sinal, estável)
INCLUDE_DIRS = ["00_Arquitetura", "wiki", "60_Sistemas", "30_Conhecimento", "40_Decisoes", "10_Mapas"]

# Exclusões de segurança/ruído (defesa em profundidade)
EXCLUDE_SUBSTRINGS = ["_inbox", ".obsidian", ".claude", "90_Arquivo",
                      "00_Inbox", "node_modules", ".git", "fabioos_db",
                      "/logs/", "agentes/logs", "agentes_log",
                      ".venv", "site-packages"]  # logs runtime + venv/libs
EXCLUDE_FILENAME_RE = re.compile(r"PIETRA.*LOG", re.IGNORECASE)  # logs Pietra

MAX_CHARS = 1500      # tamanho-alvo do chunk
META_KEYS = ["tipo", "area", "projeto", "status", "tags"]  # do frontmatter


def is_safe(path: Path) -> bool:
    """Garante que o arquivo não é sensível nem ruído."""
    rel = str(path.relative_to(VAULT_ROOT)).replace("\\", "/")
    if any(s in rel for s in EXCLUDE_SUBSTRINGS):
        return False
    if EXCLUDE_FILENAME_RE.search(path.name):
        return False
    return True


def collect_files():
    files = []
    for d in INCLUDE_DIRS:
        base = VAULT_ROOT / d
        if not base.exists():
            continue
        for md in base.rglob("*.md"):
            if is_safe(md):
                files.append(md)
    return files


def chunk_markdown(text: str, max_chars: int = MAX_CHARS):
    """Divide por cabeçalhos, prefixando cada chunk com a hierarquia (header_path)."""
    headers = {1: "", 2: "", 3: ""}
    chunks = []
    buf = []

    def header_path():
        return " > ".join(h for h in (headers[1], headers[2], headers[3]) if h)

    def flush():
        body = "\n".join(buf).strip()
        if body:
            hp = header_path()
            chunks.append((f"{hp}\n{body}" if hp else body, hp))
        buf.clear()

    for line in text.split("\n"):
        m = re.match(r"^(#{1,3})\s+(.*)", line)
        if m:
            flush()
            level = len(m.group(1))
            headers[level] = m.group(2).strip()
            for lower in range(level + 1, 4):
                headers[lower] = ""
            continue
        buf.append(line)
        if sum(len(x) for x in buf) >= max_chars:
            flush()
    flush()
    return chunks


def extract_wikilinks(text: str) -> str:
    return ", ".join(re.findall(r"\[\[([^\]]+)\]\]", text))


def clean_meta(value):
    if isinstance(value, list):
        return ", ".join(str(v) for v in value)
    if value is None:
        return ""
    if isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


def main():
    files = collect_files()
    print(f"📖 Arquivos encontrados (seguros): {len(files)}")
    if not files:
        print("Nada para indexar.")
        return

    print(f"🧠 Carregando modelo de embedding local: {MODEL_NAME} ...")
    print("   (primeira execução baixa ~2GB do modelo)")
    model = SentenceTransformer(MODEL_NAME)

    client = chromadb.PersistentClient(path=str(DB_PATH))
    print(f"🧹 Reindexação limpa: a coleção anterior '{COLLECTION}' será apagada se existir.")
    try:
        client.delete_collection(COLLECTION)  # reindex limpo (v1)
    except Exception:
        pass
    collection = client.create_collection(COLLECTION, metadata={"hnsw:space": "cosine"})

    ids, docs, metas = [], [], []
    skipped = 0
    for f in files:
        try:
            post = frontmatter.load(f)
        except Exception as e:
            skipped += 1
            print(f"   ⚠️  pulado (frontmatter inválido): "
                  f"{f.relative_to(VAULT_ROOT).as_posix()} — {e}")
            continue
        rel = str(f.relative_to(VAULT_ROOT)).replace("\\", "/")
        section = rel.split("/")[0]
        base_meta = {k: clean_meta(post.get(k, "")) for k in META_KEYS}
        for i, (chunk, hpath) in enumerate(chunk_markdown(post.content)):
            ids.append(f"{rel}::{i}")
            docs.append(chunk)
            metas.append({**base_meta,
                          "source_path": rel,
                          "filename": f.stem,
                          "header_path": hpath,
                          "chunk_index": i,
                          "vault_section": section,
                          "wikilinks": extract_wikilinks(chunk)})

    print(f"✂️  Total de chunks: {len(docs)}")
    print("📊 Gerando embeddings e gravando no Chroma (em lotes)...")
    BATCH = 64
    for start in range(0, len(docs), BATCH):
        sl = slice(start, start + BATCH)
        emb = model.encode(docs[sl], normalize_embeddings=True).tolist()
        collection.add(ids=ids[sl], embeddings=emb, documents=docs[sl], metadatas=metas[sl])
        print(f"   {min(start + BATCH, len(docs))}/{len(docs)}")

    print(f"\n✅ Ingestão completa: {len(docs)} chunks em {DB_PATH}")
    if skipped:
        print(f"   ⚠️  {skipped} arquivo(s) pulado(s) por frontmatter inválido.")


if __name__ == "__main__":
    sys.exit(main())
