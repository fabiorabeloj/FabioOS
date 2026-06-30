#!/usr/bin/env python3
"""
FabioOS — RAG Fase 12: ingestão mínima do vault.

Lê a 1a leva de pastas, faz chunking consciente de cabeçalhos, gera embeddings
LOCAIS (bge-m3) e armazena no Chroma. Versão mínima funcional — não perfeita.

Segurança: NUNCA indexa logs sensíveis (05_Raw_Sources/_compat_sources/_inbox/, PIETRA*_LOG, etc.).
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

# 1a leva de pastas (alto sinal, estável), já na estrutura LLM Wiki.
INCLUDE_DIRS = [
    "00_Arquitetura",
    "10_Dashboard",
    "20_Areas",
    "30_Projetos",
    "40_Wiki",
    "50_Registros/Decisoes",
    "60_Sistemas/FabioOS/specs",
    "60_Sistemas/Governanca",
    "60_Sistemas/Agentes",
    "60_Sistemas/Protocolos",
    "60_Sistemas/Seguranca",
    "60_Sistemas/Memoria",
    "60_Sistemas/Conhecimento",
    "60_Sistemas/Padroes",
    "60_Sistemas/Observabilidade",
    "60_Sistemas/MEGATRON/agentes/specs",
    "60_Sistemas/RAG",
    "60_Sistemas/Grafo",
    "60_Sistemas/MCP_FabioOS",
    "60_Sistemas/Pietra",
    "70_Skills",
    "80_Specs",
    "40_Wiki/_compat_wiki",
    "90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Decisoes",
]

INCLUDE_FILES = [
    "60_Sistemas/FabioOS/STATUS.md",
    "60_Sistemas/FabioOS/NEXT_ACTIONS.md",
    "60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS.md",
    "60_Sistemas/FabioOS/Roadmap_Fases_FabioOS_v2_2026-06-29.md",
    "60_Sistemas/FabioOS/Registro_Frentes_Ativas.md",
    "60_Sistemas/FabioOS/Protocolo_Operacional_FabioOS.md",
    "60_Sistemas/FabioOS/Protocolo_Roteamento_Capacidades_IA.md",
    "60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente.md",
    "60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG.md",
    "60_Sistemas/FabioOS/Roteiro_Execucao_Fase12_RAG.md",
    "60_Sistemas/FabioOS/Mapa_Canonico_Pastas_Obsidian_v2_2026-06-29.md",
    "60_Sistemas/FabioOS/Plano_Normalizacao_Pastas_Obsidian_2026-06-29.md",
    "60_Sistemas/FabioOS/Plano_Capacidades_Agentes_Cursor_Hermes_2026-06-28.md",
    "60_Sistemas/FabioOS/Visao_Interface_FabioOS.md",
    "90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Painel_Pendencias_FabioOS.md",
    "90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Painel_Memoria_FabioOS.md",
    "90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/INDEX.md",
    "90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Mapa_Mestre_Fabio.md",
]

# Exclusões de segurança/ruído (defesa em profundidade)
EXCLUDE_SUBSTRINGS = ["_inbox", ".obsidian", ".claude",
                      "90_Arquivo/Descartes_Visuais",
                      "90_Arquivo/Antigo",
                      "90_Arquivo/Superseded",
                      "90_Arquivo/Projetos_Encerrados",
                      "90_Arquivo/Referencias_Mortas",
                      "00_Inbox", "node_modules", ".git", "fabioos_db",
                      "/logs/", "agentes/logs", "agentes_log",
                      ".venv", "site-packages"]  # logs runtime + venv/libs
EXCLUDE_FILENAME_RE = re.compile(r"PIETRA.*LOG", re.IGNORECASE)  # logs Pietra

MAX_CHARS = 6000      # Fase 12.1 (1200) adiada: reindex pesado em máquina carregada;
#                       fazer em janela de manutenção (CPU livre) — ver barramento/changelog
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
    for f in INCLUDE_FILES:
        path = VAULT_ROOT / f
        if path.exists() and is_safe(path):
            files.append(path)
    files = sorted(set(files), key=lambda p: p.as_posix())
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
    BATCH = 256
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
