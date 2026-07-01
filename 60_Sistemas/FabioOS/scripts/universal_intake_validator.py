#!/usr/bin/env python3
"""Validador local do contrato Universal Intake Queue."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


REQUIRED_TOP = {"generated_at", "gerado_por", "contrato", "resumo", "cores_status", "fila"}
REQUIRED_CARD = {
    "id",
    "source",
    "received_at",
    "sender",
    "subject",
    "raw_content_ref",
    "summary",
    "domain",
    "sensitivity",
    "urgency",
    "suggested_agent",
    "suggested_action",
    "alerta",
    "requires_human_approval",
    "rag_permitido",
    "status",
    "log_ref",
}
SOURCES = {"gmail", "whatsapp", "pdf", "drive", "mobile", "manual", "obsidian", "github"}
DOMAINS = {"fabios", "pietraos", "escolaos", "primus", "financeiro", "pessoal", "tecnico", "juridico", "saude", "spam", "seguranca"}
SENSITIVITY = {"public", "internal", "private", "restricted", "no_rag", "forbidden_external"}
URGENCY = {"none", "low", "medium", "high", "critical"}
STATUS = {"captured", "classified", "waiting_approval", "approved", "executing", "executed", "archived", "blocked", "failed"}
SECRET_RX = re.compile(r"(sk-[A-Za-z0-9]{6,}|bearer\s+\S+|(?:senha|password|token|api[_-]?key)\s*[:=]?\s*\S+)", re.IGNORECASE)


def load_json(path: Path | None) -> dict[str, Any]:
    raw = sys.stdin.read() if path is None else path.read_text(encoding="utf-8-sig")
    return json.loads(raw)


def add(errors: list[str], message: str) -> None:
    errors.append(message)


def validate_card(card: dict[str, Any], idx: int, errors: list[str]) -> None:
    missing = REQUIRED_CARD - set(card)
    extra = set(card) - REQUIRED_CARD
    if missing:
        add(errors, f"fila[{idx}] faltando campos: {sorted(missing)}")
    if extra:
        add(errors, f"fila[{idx}] contem campos nao permitidos: {sorted(extra)}")
    if missing:
        return

    prefix = f"fila[{idx}] {card.get('id')}"
    if not re.match(r"^intake_[0-9]{8}T[0-9]{6}(_[a-f0-9]{10,16})?$", str(card["id"])):
        add(errors, f"{prefix}: id fora do padrao intake_<ts>[_<hash>]")
    if card["source"] not in SOURCES:
        add(errors, f"{prefix}: source invalido {card['source']}")
    if card["domain"] not in DOMAINS:
        add(errors, f"{prefix}: domain invalido {card['domain']}")
    if card["sensitivity"] not in SENSITIVITY:
        add(errors, f"{prefix}: sensitivity invalida {card['sensitivity']}")
    if card["urgency"] not in URGENCY:
        add(errors, f"{prefix}: urgency invalida {card['urgency']}")
    if card["status"] not in STATUS:
        add(errors, f"{prefix}: status invalido {card['status']}")
    if not isinstance(card["requires_human_approval"], bool):
        add(errors, f"{prefix}: requires_human_approval deve ser boolean")
    if not isinstance(card["rag_permitido"], bool):
        add(errors, f"{prefix}: rag_permitido deve ser boolean")
    if card["sensitivity"] in {"private", "restricted", "no_rag", "forbidden_external"} and card["rag_permitido"]:
        add(errors, f"{prefix}: dado sensivel nao pode permitir RAG automaticamente")
    if card["requires_human_approval"] and card["status"] not in {"waiting_approval", "blocked", "failed"}:
        add(errors, f"{prefix}: item que exige humano deve aguardar aprovacao/bloqueio/falha")
    if SECRET_RX.search(str(card["summary"])):
        add(errors, f"{prefix}: summary parece conter segredo")
    if card["sensitivity"] == "forbidden_external" and "[REDIGIDO" not in str(card["summary"]):
        add(errors, f"{prefix}: forbidden_external deve ter summary redigido")
    for forbidden in ("texto", "text", "body", "content", "snippet"):
        if forbidden in card:
            add(errors, f"{prefix}: corpo bruto proibido no card ({forbidden})")


def validate_queue(queue: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED_TOP - set(queue)
    if missing:
        add(errors, f"top-level faltando campos: {sorted(missing)}")
        return errors
    if queue["contrato"] != "MEGATRON Core Spec v0.1":
        add(errors, "contrato deve ser MEGATRON Core Spec v0.1")
    if not isinstance(queue["fila"], list):
        add(errors, "fila deve ser array")
        return errors
    for idx, card in enumerate(queue["fila"]):
        if not isinstance(card, dict):
            add(errors, f"fila[{idx}] nao e objeto")
            continue
        validate_card(card, idx, errors)
    total = len(queue["fila"])
    resumo = queue.get("resumo") or {}
    if resumo.get("total") != total:
        add(errors, f"resumo.total={resumo.get('total')} mas fila tem {total}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida fila do Intake Universal.")
    parser.add_argument("--input", type=Path, help="Arquivo JSON; omita para stdin.")
    args = parser.parse_args()
    queue = load_json(args.input)
    errors = validate_queue(queue)
    if errors:
        print(json.dumps({"ok": False, "errors": errors}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1
    print(json.dumps({"ok": True, "cards": len(queue["fila"])}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
