#!/usr/bin/env python3
"""
FabioOS — auditoria de encoding (vault + runtime Windows).

Testa hipoteses de falha comuns no Codex/Windows e grava relatorio JSON + log NDJSON.

Uso:
    60_Sistemas\\RAG\\.venv\\Scripts\\python.exe 60_Sistemas\\FabioOS\\scripts\\auditar_encoding_fabioos.py
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

# #region agent log
DEBUG_LOG = Path(__file__).resolve().parents[3] / "debug-e23183.log"
SESSION_ID = "e23183"


def _dbg(hypothesis_id: str, location: str, message: str, data: dict | None = None) -> None:
    payload = {
        "sessionId": SESSION_ID,
        "runId": os.environ.get("FABIOOS_ENCODING_RUN", "pre-fix"),
        "hypothesisId": hypothesis_id,
        "location": location,
        "message": message,
        "data": data or {},
        "timestamp": int(time.time() * 1000),
    }
    try:
        with DEBUG_LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps(payload, ensure_ascii=False) + "\n")
    except OSError:
        pass


# #endregion

ROOT = Path(__file__).resolve().parents[3]
SKIP = {".git", "node_modules", ".venv", "fabioos_db", "__pycache__", ".obsidian", ".claude", ".codex", ".agents", ".cursor"}
EXTS = {".md", ".py", ".ps1", ".json", ".toml", ".txt"}


def scan_vault() -> dict:
    invalid_utf8: list[str] = []
    u_fffd: list[dict] = []
    for p in ROOT.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in EXTS:
            continue
        if any(x in SKIP for x in p.parts):
            continue
        raw = p.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            invalid_utf8.append(str(p.relative_to(ROOT)))
            continue
        n = text.count("\ufffd")
        if n:
            u_fffd.append({"path": str(p.relative_to(ROOT)), "count": n})
    return {"invalid_utf8": invalid_utf8, "u_fffd": u_fffd}


def test_stdout_emoji() -> dict:
    code = (
        "import sys\n"
        "enc = sys.stdout.encoding\n"
        "try:\n"
        "    print('probe:' + enc)\n"
        "    print('\\U0001f50d emoji')\n"
        "    ok = True\n"
        "except UnicodeEncodeError as e:\n"
        "    ok = False\n"
        "    err = str(e)\n"
        "print('OK' if ok else 'FAIL')\n"
    )
    proc = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        cwd=str(ROOT),
    )
    return {
        "python": sys.executable,
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip()[:500],
        "PYTHONIOENCODING": os.environ.get("PYTHONIOENCODING"),
    }


def test_query_rag_probe() -> dict:
    script = ROOT / "60_Sistemas" / "RAG" / "scripts" / "query_rag.py"
    venv_py = ROOT / "60_Sistemas" / "RAG" / ".venv" / "Scripts" / "python.exe"
    py = str(venv_py if venv_py.exists() else sys.executable)
    if not script.exists():
        return {"skipped": True, "reason": "query_rag ausente"}
    proc = subprocess.run(
        [py, str(script), "probe encoding", "--k", "1"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        cwd=str(script.parent),
        timeout=180,
    )
    combined = (proc.stdout or "") + (proc.stderr or "")
    return {
        "python": py,
        "returncode": proc.returncode,
        "has_unicode_error": "UnicodeEncodeError" in combined,
        "has_search_emoji": "🔍" in combined or "Busca" in combined,
        "tail": combined[-400:],
    }


def main() -> int:
    # #region agent log
    _dbg("H1", "auditar_encoding:main", "start", {"python": sys.executable, "stdout_encoding": sys.stdout.encoding})
    # #endregion

    vault = scan_vault()
    # #region agent log
    _dbg("H2", "auditar_encoding:scan_vault", "vault scan done", vault)
    # #endregion

    stdout_probe = test_stdout_emoji()
    # #region agent log
    _dbg("H1", "auditar_encoding:test_stdout_emoji", "stdout probe", stdout_probe)
    # #endregion

    rag_probe = {"skipped": True}
    try:
        rag_probe = test_query_rag_probe()
    except subprocess.TimeoutExpired:
        rag_probe = {"timeout": True}
    # #region agent log
    _dbg("H3", "auditar_encoding:test_query_rag", "query_rag probe", rag_probe)
    # #endregion

    gitattributes = (ROOT / ".gitattributes").exists()
    # #region agent log
    _dbg("H4", "auditar_encoding:gitattributes", "gitattributes check", {"exists": gitattributes})
    # #endregion

    codex_example = ROOT / ".codex" / "config.toml.example"
    has_pyio = False
    if codex_example.exists():
        has_pyio = "PYTHONIOENCODING" in codex_example.read_text(encoding="utf-8")
    # #region agent log
    _dbg("H5", "auditar_encoding:codex_config", "codex PYTHONIOENCODING", {"example_has_pyio": has_pyio})
    # #endregion

    report = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "vault": vault,
        "stdout_probe": stdout_probe,
        "query_rag_probe": rag_probe,
        "gitattributes_exists": gitattributes,
        "codex_example_has_PYTHONIOENCODING": has_pyio,
    }

    out = ROOT / "60_Sistemas" / "FabioOS" / "classificacoes" / "auditoria_encoding_fabioos.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print("Auditoria encoding FabioOS")
    print(f"  invalid_utf8: {len(vault['invalid_utf8'])}")
    print(f"  u_fffd files: {len(vault['u_fffd'])}")
    print(f"  stdout_probe: {stdout_probe.get('stdout', '')}")
    print(f"  JSON: {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
