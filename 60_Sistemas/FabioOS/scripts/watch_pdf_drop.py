#!/usr/bin/env python3
"""Watcher local do pipeline "Drop PDF -> aprende".

Zona Codex: detectar PDFs novos e emitir um evento seguro para o Claude.
Nao executa OCR, nao chama RAG, nao copia conteudo do PDF e nao usa API externa.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


def find_root() -> Path:
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "60_Sistemas/FabioOS/bootstrap/CLAUDE.md").exists():
            return parent
    raise RuntimeError("Nao encontrei a raiz do FabioOS.")


ROOT = find_root()
DEFAULT_DROP_DIR = ROOT / "00_Inbox" / "pdfs"
DEFAULT_EVENTS_DIR = DEFAULT_DROP_DIR / "_events"
DEFAULT_LOG = ROOT / "60_Sistemas" / "FabioOS" / "logs" / "pdf_drop_events.jsonl"
DEFAULT_STATE = ROOT / "60_Sistemas" / "FabioOS" / "logs" / "pdf_drop_watcher_state.json"
SPEC_PATH = "60_Sistemas/FabioOS/specs/2026-06-30_pipeline-pdf-aprende.md"
TARGET_AGENT = "claude.documentalista"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return str(path.resolve())


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-")[:80] or "pdf"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"version": 1, "files": {}}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        backup = path.with_suffix(path.suffix + ".broken")
        path.replace(backup)
        return {"version": 1, "files": {}, "warning": f"state_corrupt_backup:{backup.name}"}


def save_state(path: Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def stable_enough(path: Path, min_age_seconds: int) -> bool:
    stat = path.stat()
    age = time.time() - stat.st_mtime
    return age >= min_age_seconds and stat.st_size > 0


def iter_pdfs(drop_dir: Path) -> list[Path]:
    if not drop_dir.exists():
        return []
    ignored_parts = {"_events", "_processed", "_failed"}
    pdfs: list[Path] = []
    for path in drop_dir.rglob("*.pdf"):
        if any(part in ignored_parts for part in path.parts):
            continue
        if path.is_file():
            pdfs.append(path)
    return sorted(pdfs)


def build_event(pdf: Path, digest: str, size: int) -> dict[str, Any]:
    ts = utc_now()
    event_id = f"pdf-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-{digest[:12]}"
    return {
        "event_id": event_id,
        "detected_at": ts,
        "status": "detected",
        "source": "00_Inbox/pdfs",
        "source_pdf": rel(pdf),
        "absolute_pdf": str(pdf.resolve()),
        "file_name": pdf.name,
        "size_bytes": size,
        "sha256": digest,
        "target_agent": TARGET_AGENT,
        "spec": SPEC_PATH,
        "next_action": "Claude/documentalista deve processar quando Stirling estiver autenticado.",
        "safety": {
            "ocr_executed": False,
            "rag_reindexed": False,
            "content_copied": False,
            "requires_sensitive_data_gate": True,
            "requires_human_curation_before_rag": True,
        },
    }


def render_markdown(event: dict[str, Any]) -> str:
    return f"""---
tipo: evento-pdf-drop
area: 00_Inbox
projeto: FabioOS
status: {event["status"]}
fase: 18.2
classe_dado: pendente-classificacao
permissao: proposta
evento_id: {event["event_id"]}
criado_em: {event["detected_at"][:10]}
tags: [fabios, pdf, drop-folder, documentalista, codex]
---

# PDF detectado - {event["file_name"]}

## Evento

| Campo | Valor |
|---|---|
| Evento | `{event["event_id"]}` |
| Detectado em | `{event["detected_at"]}` |
| PDF | `{event["source_pdf"]}` |
| Tamanho | `{event["size_bytes"]}` bytes |
| SHA256 | `{event["sha256"]}` |
| Agente alvo | `{event["target_agent"]}` |

## Proxima Acao

{event["next_action"]}

## Comando Sugerido ao Claude

```powershell
python 60_Sistemas/MEGATRON/agentes/implementacao/claude/documentalista.py info --pdf "{event["absolute_pdf"]}"
```

## Politica

- OCR executado: nao.
- RAG reindexado: nao.
- Conteudo copiado: nao.
- Gate sensivel: obrigatorio.
- Curadoria humana antes do RAG: obrigatoria.
"""


def write_event(event: dict[str, Any], events_dir: Path, log_path: Path) -> None:
    events_dir.mkdir(parents=True, exist_ok=True)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    event_base = f"{event['event_id']}_{slugify(event['file_name'])}"
    (events_dir / f"{event_base}.json").write_text(
        json.dumps(event, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (events_dir / f"{event_base}.md").write_text(render_markdown(event), encoding="utf-8")
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False) + "\n")


def scan_once(args: argparse.Namespace) -> int:
    drop_dir = Path(args.drop_dir)
    if not drop_dir.is_absolute():
        drop_dir = ROOT / drop_dir
    events_dir = Path(args.events_dir)
    if not events_dir.is_absolute():
        events_dir = ROOT / events_dir
    log_path = Path(args.log)
    if not log_path.is_absolute():
        log_path = ROOT / log_path
    state_path = Path(args.state)
    if not state_path.is_absolute():
        state_path = ROOT / state_path

    drop_dir.mkdir(parents=True, exist_ok=True)
    events_dir.mkdir(parents=True, exist_ok=True)
    state = load_state(state_path)
    files_state = state.setdefault("files", {})

    created = 0
    skipped = 0
    for pdf in iter_pdfs(drop_dir):
        if not stable_enough(pdf, args.min_age_seconds):
            skipped += 1
            continue
        stat = pdf.stat()
        digest = sha256_file(pdf)
        key = rel(pdf)
        previous = files_state.get(key)
        if previous and previous.get("sha256") == digest and previous.get("size_bytes") == stat.st_size:
            skipped += 1
            continue

        event = build_event(pdf, digest, stat.st_size)
        if not args.dry_run:
            write_event(event, events_dir, log_path)
            files_state[key] = {
                "sha256": digest,
                "size_bytes": stat.st_size,
                "last_event_id": event["event_id"],
                "detected_at": event["detected_at"],
            }
            save_state(state_path, state)
        created += 1
        print(json.dumps(event, ensure_ascii=False))

    print(json.dumps({"created": created, "skipped": skipped, "drop_dir": rel(drop_dir)}, ensure_ascii=False))
    return created


def main() -> int:
    parser = argparse.ArgumentParser(description="Detecta PDFs novos em 00_Inbox/pdfs e emite eventos para o documentalista.")
    parser.add_argument("--drop-dir", default=str(DEFAULT_DROP_DIR.relative_to(ROOT)))
    parser.add_argument("--events-dir", default=str(DEFAULT_EVENTS_DIR.relative_to(ROOT)))
    parser.add_argument("--log", default=str(DEFAULT_LOG.relative_to(ROOT)))
    parser.add_argument("--state", default=str(DEFAULT_STATE.relative_to(ROOT)))
    parser.add_argument("--interval", type=float, default=5.0)
    parser.add_argument("--min-age-seconds", type=int, default=3)
    parser.add_argument("--once", action="store_true", help="executa uma varredura e sai")
    parser.add_argument("--dry-run", action="store_true", help="mostra eventos sem gravar estado/log")
    args = parser.parse_args()

    if args.once:
        scan_once(args)
        return 0

    print(f"watching {args.drop_dir}; Ctrl+C para parar")
    try:
        while True:
            scan_once(args)
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("watcher encerrado")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
