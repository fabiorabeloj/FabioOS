#!/usr/bin/env python3
"""
Agente Pesquisador (agent.pesquisador) — ingestão web limpa via Crawl4AI.

Conforme `60_Sistemas/FabioOS/specs/2026-06-29_crawl4ai-ingestao-rag.md`. Recebe
uma URL, coleta markdown limpo (Crawl4AI, local) e salva como **fonte rascunho**
em `05_Raw_Sources/web/` para curadoria humana antes de promover ao RAG.

Governança: dry_run por padrão (só prévia); não reindexa o RAG; não coleta dados
pessoais/login/paywall. Devolve o contrato `Resultado`.

Uso:
    python pesquisador.py https://exemplo.com/doc
    python pesquisador.py https://exemplo.com/doc --confirmar
"""
import argparse
import asyncio
import re
import sys
import unicodedata
from datetime import date
from urllib.parse import urlparse
from pathlib import Path

from _common import vault_root, log_event, resultado

ROOT = vault_root()


def _slug_url(url: str) -> str:
    p = urlparse(url)
    base = (p.netloc + p.path).strip("/")
    base = unicodedata.normalize("NFKD", base).encode("ascii", "ignore").decode()
    base = re.sub(r"[^a-zA-Z0-9]+", "-", base).strip("-").lower()
    return base[:70] or "web"


async def _coletar(url: str):
    """Coleta a página com Crawl4AI (import lazy). Devolve (markdown, sucesso)."""
    from crawl4ai import AsyncWebCrawler
    async with AsyncWebCrawler() as crawler:
        r = await crawler.arun(url=url)
        md = getattr(r, "markdown", "") or ""
        if hasattr(md, "raw_markdown"):     # MarkdownGenerationResult
            md = md.raw_markdown
        return str(md), bool(getattr(r, "success", True))


def _montar(url: str, md: str, hoje: str) -> str:
    return f"""---
tipo: fonte
area: 05_Raw_Sources
projeto: FabioOS
dominio: web
status: rascunho
origem: pesquisador
fonte_url: {url}
coletado_em: {hoje}
tags: [fonte, web, rascunho, crawl4ai]
---

# Fonte web: {url}

> Coletado por Crawl4AI. Rascunho para curadoria humana antes de promover a wiki/RAG.

{md}
"""


def run(url: str, dest: str = "05_Raw_Sources/web", dry_run: bool = True,
        max_preview: int = 1200) -> dict:
    """Contrato uniforme. dry_run=True: só prévia. dry_run=False: salva rascunho."""
    hoje = date.today().isoformat()
    try:
        md, ok = asyncio.run(_coletar(url))
    except Exception as e:
        log_event("Pesquisador", "erro", f"{url}: {e}")
        return resultado("proposta", False, "Falha na coleta",
                         f"Erro ao coletar {url}: {e}")
    if not ok or len(md.strip()) < 20:
        return resultado("proposta", False, "Conteúdo insuficiente",
                         f"{url} não retornou conteúdo útil.")
    rel = f"{dest}/{hoje}_{_slug_url(url)}.md"
    if dry_run:
        return resultado("proposta", True, f"Proposta de fonte: {url}",
                         corpo=(f"Coletado {len(md)} chars. Salvaria em `{rel}`. "
                                f"Prévia:\n\n{md.strip()[:max_preview]}..."),
                         sugestao="Para salvar de fato, confirme (--confirmar).")
    destino = ROOT / rel
    if destino.exists():
        return resultado("proposta", False, "Já existe",
                         f"`{rel}` já existe — não sobrescrevo.")
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(_montar(url, md, hoje), encoding="utf-8")
    log_event("Pesquisador", "fonte_criada", rel)
    return resultado("proposta", True, f"Fonte salva: {url}",
                     corpo=f"Salvo em `{rel}` ({len(md)} chars).",
                     sugestao="Curar e promover a wiki/RAG (reindex com lock).",
                     artefato=rel)


def main() -> int:
    ap = argparse.ArgumentParser(description="Pesquisador (Crawl4AI -> fonte rascunho)")
    ap.add_argument("url")
    ap.add_argument("--confirmar", action="store_true",
                    help="salva o rascunho (sem isto, dry-run / só prévia)")
    args = ap.parse_args()
    r = run(args.url, dry_run=not args.confirmar)
    print(f"{'✅' if r['ok'] else '🛑'} {r['titulo']}")
    print(r["corpo"][:2000])
    if r["sugestao"]:
        print(f"💡 {r['sugestao']}")
    return 0 if r["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
