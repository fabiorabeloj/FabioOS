#!/usr/bin/env python3
"""
Agente Documentalista — extração de PDF para o pipeline "Drop PDF → aprende".

Dois backends de extração:
  • LOCAL (pypdf): texto de PDFs digitais — funciona já, sem auth. (padrão)
  • Stirling PDF (Docker :8081): OCR pesado / PDFs escaneados — quando a auth
    estiver configurada (hoje HTTP 401).

Governança copyright (Restricted): o texto bruto vai para `00_Inbox/pdfs/_extracted/`
(**gitignored**); o Resultado só devolve metadados + prévia curta. Nada de dump
integral de conteúdo com copyright no Git/RAG/Obsidian — curadoria humana decide
o que vira resumo/metadado/CatalogEntry e só então entra no RAG (com lock).

Uso:
    python documentalista.py status
    python documentalista.py --pdf "00_Inbox/pdfs/arquivo.pdf"            # dry-run
    python documentalista.py --pdf "00_Inbox/pdfs/arquivo.pdf" --confirmar
"""
import argparse
import json
import os
import re
import sys
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path

from _common import resultado, log_event, vault_root

ROOT = vault_root()
STIRLING = os.environ.get("STIRLING_URL", "http://localhost:8081")
EXTRACT_DIR = ROOT / "00_Inbox" / "pdfs" / "_extracted"   # gitignored
EVENTS_DIR = ROOT / "00_Inbox" / "pdfs" / "_events"        # eventos do Codex (front door)
PREVIEW = 400


def _atualizar_evento(pdf_name: str, **campos) -> str:
    """Avança o evento do PDF (contrato com Cursor): atualiza status/safety/extraction
    para a aba PDF Pipeline progredir DETECTADO→OCR→INDEXADO. Chaves 'safety.x' vão
    para o bloco safety; demais no topo. Retorna o nome do arquivo ou ''."""
    if not EVENTS_DIR.exists():
        return ""
    for jf in EVENTS_DIR.glob("*.json"):
        try:
            ev = json.loads(jf.read_text(encoding="utf-8"))
        except Exception:
            continue
        if ev.get("file_name") == pdf_name:
            ev.setdefault("safety", {})
            for k, v in campos.items():
                if k.startswith("safety."):
                    ev["safety"][k.split(".", 1)[1]] = v
                else:
                    ev[k] = v
            jf.write_text(json.dumps(ev, ensure_ascii=False, indent=2), encoding="utf-8")
            return jf.name
    return ""


def _slug(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s[:70] or "pdf"


def _http_status(path: str = "/"):
    try:
        with urllib.request.urlopen(urllib.request.Request(STIRLING + path), timeout=5) as r:
            return r.status, ""
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return None, str(e)


def status() -> dict:
    code, err = _http_status("/")
    if code is None:
        return resultado("proposta", False, "Stirling indisponível",
                         f"Sem resposta de {STIRLING}: {err}. Extração local (pypdf) segue ok.",
                         sugestao="Use extração local; suba Stirling p/ OCR de escaneados.")
    if code == 401:
        return resultado("proposta", True, "Stirling no ar (requer auth)",
                         corpo=(f"{STIRLING} responde (HTTP 401). OCR pesado precisa de "
                                "`STIRLING_USERNAME`/`STIRLING_PASSWORD`. Extração local (pypdf) "
                                "já funciona sem isso."),
                         sugestao="Configurar auth do Stirling só p/ PDFs escaneados/imagem.")
    return resultado("proposta", True, "Stirling operacional",
                     corpo=f"{STIRLING} responde (HTTP {code}). OCR/merge/split disponíveis.")


def _extrair_local(pdf_path: str):
    """Extrai texto de PDF digital. PyMuPDF (rápido p/ livros); pypdf como fallback.
    Devolve (texto, n_paginas)."""
    try:
        import fitz                              # PyMuPDF — ~10x mais rápido
        doc = fitz.open(pdf_path)
        try:
            texto = "\n\n".join(pg.get_text() for pg in doc)
            return texto, doc.page_count
        finally:
            doc.close()
    except ImportError:
        import pypdf
        reader = pypdf.PdfReader(pdf_path)
        partes = []
        for pg in reader.pages:
            try:
                partes.append(pg.extract_text() or "")
            except Exception:
                pass
        return "\n\n".join(partes), len(reader.pages)


def run(pdf_path: str = None, op: str = "extrair", dry_run: bool = True) -> dict:
    """Contrato uniforme. op=status -> estado do Stirling. op=extrair + pdf_path ->
    extração local (pypdf), texto bruto em pasta gitignored (Restricted-safe)."""
    if op == "status" or not pdf_path:
        return status()
    p = Path(pdf_path)
    if not p.is_absolute():
        p = ROOT / pdf_path
    if not p.exists():
        return resultado("proposta", False, "PDF não encontrado", f"`{pdf_path}` não existe.")
    try:
        texto, n = _extrair_local(str(p))
    except Exception as e:
        return resultado("proposta", False, "Falha na extração local",
                         f"pypdf não leu `{p.name}`: {e}. Pode ser escaneado/imagem → "
                         "precisa OCR (Stirling, após auth).",
                         sugestao="Configurar auth do Stirling para OCR.")
    chars = len(texto.strip())
    if chars < 30:
        return resultado("proposta", False, "Sem texto extraível",
                         f"`{p.name}`: {n} páginas, ~0 texto → provavelmente escaneado. "
                         "Precisa OCR (Stirling).",
                         sugestao="Configurar auth do Stirling para OCR de imagem.")
    out = EXTRACT_DIR / f"{_slug(p.stem)}.txt"
    rel = out.relative_to(ROOT).as_posix()
    if not dry_run:
        EXTRACT_DIR.mkdir(parents=True, exist_ok=True)
        out.write_text(texto, encoding="utf-8")
        log_event("Documentalista", "extraido_local", f"{rel} {n}pg {chars}c")
        # contrato Cursor: avança o evento (painel PDF Pipeline DETECTADO→OCR→…)
        _atualizar_evento(p.name, status="extracted",
                          **{"safety.ocr_executed": True},
                          extraction={"method": "pymupdf-local", "pages": n,
                                      "chars": chars, "output_gitignored": rel,
                                      "rag_reindexed": False})
    return resultado(
        "proposta", True, f"Extraído (local): {p.name}",
        corpo=(f"{n} páginas, {chars} chars. "
               f"{'Salvo em' if not dry_run else 'Salvaria em'} `{rel}` "
               f"(gitignored, Restricted-safe). Prévia:\n\n{texto.strip()[:PREVIEW]}..."),
        sugestao=("Curadoria humana: classificar (Restricted?) → resumo/metadados/"
                  "CatalogEntries → RAG com lock. Não versionar conteúdo copyright."),
        artefato=None)        # não expõe caminho versionável de conteúdo copyright


def main() -> int:
    ap = argparse.ArgumentParser(description="Documentalista (PDF: pypdf local + Stirling)")
    ap.add_argument("op", nargs="?", default="status")
    ap.add_argument("--pdf")
    ap.add_argument("--confirmar", action="store_true",
                    help="salva o texto extraído (sem isto, dry-run / só prévia)")
    args = ap.parse_args()
    op = "extrair" if (args.pdf and args.op == "status") else args.op
    r = run(args.pdf, op, dry_run=not args.confirmar)
    print(f"{'✅' if r['ok'] else '🛑'} {r['titulo']}\n{r['corpo']}")
    if r["sugestao"]:
        print(f"💡 {r['sugestao']}")
    return 0 if r["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
