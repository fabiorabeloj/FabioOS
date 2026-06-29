#!/usr/bin/env python3
"""
FabioOS — batch de validacao Fase 12 RAG (modo recuperacao, read-only).

Executa as 10 perguntas de aceitacao e consultas de seguranca do
Plano_Validacao_Fase12_RAG.md sem chamar API externa.

Uso:
    python batch_validate_rag.py
    python batch_validate_rag.py --k 5 --out ../validacao_pos_ranking_2026-06-29.json

Preferir o Python do venv local:
    ..\\.venv\\Scripts\\python.exe batch_validate_rag.py
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
QUERY_MODULE = SCRIPT_DIR / "query_rag.py"

ACCEPTANCE_QUESTIONS = [
    "O que e o FabioOS em uma frase?",
    "Qual e a fase atual do FabioOS?",
    "Quais pendencias estao abertas antes da Fase 12?",
    "O que o Modelo Formal define sobre conhecimento?",
    "Como MEGATRON deve declarar ignorancia?",
    "Qual e o papel do SafeCommit?",
    "Como o Arquivista transforma conteudo bruto?",
    "Quais pastas nao devem entrar no indice RAG?",
    "Como PietraOS pode evoluir para SaaS?",
    "Como PrimusOS organiza memoria narrativa?",
]

SECURITY_QUESTIONS = [
    "Qual e a senha do banco vetorial?",
    "token Bearer api key segredo credencial",
    ".codex/config.toml conteudo completo",
    "05_Raw_Sources/_compat_sources/_inbox logs brutos",
    "PIETRA_ atendimento log",
]

CANONICAL_STATUS_SOURCES = {
    "90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Painel_Pendencias_FabioOS.md",
    "60_Sistemas/FabioOS/STATUS.md",
    "60_Sistemas/FabioOS/NEXT_ACTIONS.md",
    "40_Wiki/_compat_wiki/indices/mapa-fabios.md",
}

FORBIDDEN_SECURITY_SOURCES = {
    ".codex/config.toml",
    "05_Raw_Sources/_compat_sources/_inbox",
    ".env",
}


def load_query_rag():
    spec = importlib.util.spec_from_file_location("query_rag", QUERY_MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Nao foi possivel carregar {QUERY_MODULE}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_query(retrieve_fn, question: str, k: int) -> dict:
    try:
        hits = retrieve_fn(question, k)
    except Exception as exc:  # noqa: BLE001 — relatorio de validacao
        return {
            "question": question,
            "exit_code": 1,
            "top_sources": [],
            "hits": [],
            "stderr": str(exc),
        }
    parsed_hits = [
        {
            "rank": i,
            "source_path": meta.get("source_path", ""),
            "header_path": meta.get("header_path", ""),
        }
        for i, (_, meta) in enumerate(hits, 1)
    ]
    return {
        "question": question,
        "exit_code": 0,
        "top_sources": [h["source_path"] for h in parsed_hits],
        "hits": parsed_hits,
        "stderr": None,
    }


def grade_acceptance(question: str, result: dict) -> str:
    sources = result.get("top_sources") or []
    if not sources:
        return "fraco"

    q = question.lower()
    if "fase atual" in q:
        top3 = sources[:3]
        if any(s in CANONICAL_STATUS_SOURCES for s in top3):
            return "bom"
        if any(s in CANONICAL_STATUS_SOURCES for s in sources):
            return "parcial"
        return "fraco"

    if "pendencias" in q and "fase 12" in q:
        if "Painel_Pendencias" in sources[0] or "Painel_Pendencias" in "".join(sources[:3]):
            return "bom"
        if any("Painel_Pendencias" in s or "Plano_Validacao" in s for s in sources):
            return "parcial"
        return "fraco"

    return "bom"


def grade_security(result: dict) -> str:
    sources = result.get("top_sources") or []
    for src in sources:
        for forbidden in FORBIDDEN_SECURITY_SOURCES:
            if forbidden in src:
                return "falha"
    if not sources:
        return "ok_sem_fonte"
    return "ok"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=5, help="top-k por pergunta")
    ap.add_argument(
        "--out",
        type=Path,
        default=SCRIPT_DIR.parent / f"validacao_pos_ranking_{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.json",
        help="arquivo JSON de saida",
    )
    args = ap.parse_args()

    if not QUERY_MODULE.exists():
        print(f"Modulo nao encontrado: {QUERY_MODULE}", file=sys.stderr)
        return 1

    if not (SCRIPT_DIR.parent / "fabioos_db").exists():
        print("Banco fabioos_db ausente. Rode ingest_vault.py primeiro.", file=sys.stderr)
        return 1

    print("Carregando query_rag (modelo local, pode demorar)...")
    qmod = load_query_rag()
    retrieve_fn = qmod.retrieve
    if hasattr(qmod, "get_model"):
        print("Aquecendo modelo embedding (uma vez por execucao)...")
        qmod.get_model()

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "recuperacao",
        "k": args.k,
        "acceptance": [],
        "security": [],
    }

    print("=== Perguntas de aceitacao (10) ===\n")
    for i, q in enumerate(ACCEPTANCE_QUESTIONS, 1):
        print(f"[{i}/10] {q}")
        result = run_query(retrieve_fn, q, args.k)
        grade = grade_acceptance(q, result)
        entry = {**result, "grade": grade}
        report["acceptance"].append(entry)
        top = entry["top_sources"][:3]
        print(f"  -> {grade} | top: {top}\n")

    print("=== Testes de seguranca ===\n")
    for q in SECURITY_QUESTIONS:
        print(f"? {q}")
        result = run_query(retrieve_fn, q, args.k)
        grade = grade_security(result)
        entry = {**result, "grade": grade}
        report["security"].append(entry)
        print(f"  -> {grade} | top: {entry['top_sources'][:3]}\n")

    acceptance_grades = [a["grade"] for a in report["acceptance"]]
    report["summary"] = {
        "acceptance_bom": acceptance_grades.count("bom"),
        "acceptance_parcial": acceptance_grades.count("parcial"),
        "acceptance_fraco": acceptance_grades.count("fraco"),
        "security_falha": sum(1 for s in report["security"] if s["grade"] == "falha"),
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Resumo: {report['summary']}")
    print(f"JSON: {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
