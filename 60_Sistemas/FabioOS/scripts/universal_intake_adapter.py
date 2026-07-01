#!/usr/bin/env python3
"""
Universal Intake Adapter - FabioOS / MEGATRON Core.

Converte payloads fake ou exportados por conectores autorizados no contrato de
fila que o Cursor/Agentarium consome. Deterministico, sem LLM e sem efeitos
externos.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
MEGATRON_V1 = ROOT / "60_Sistemas" / "MEGATRON" / "v1"
# A fila viva `intake_queue.json` e atualizada pelo intake_flow/arquivista.
# O adapter escreve em uma fila propria por padrao para evitar corrida entre agentes.
DEFAULT_QUEUE = MEGATRON_V1 / "state" / "intake_queue.codex_adapter.json"
DEFAULT_LOG_NAME = "intake_log.jsonl"
CONTRACT = "MEGATRON Core Spec v0.1"
REDACTED_PLACEHOLDER = "[REDIGIDO - credencial/segredo detectado; corpo retido fora da fila]"

if str(MEGATRON_V1) not in sys.path:
    sys.path.insert(0, str(MEGATRON_V1))

from megatron_core import classificar_intake  # noqa: E402


SECRET_RX = re.compile(
    r"\b(sk-[A-Za-z0-9]{6,}|bearer\s+\S+|[A-Za-z0-9_\-]{24,}|(?:senha|password|token|api[_-]?key)\s*[:=]?\s*\S+)",
    re.IGNORECASE,
)


def load_payload(path: Path | None) -> list[dict[str, Any]]:
    raw = sys.stdin.read() if path is None else path.read_text(encoding="utf-8-sig")
    raw = raw.strip()
    if not raw:
        return []
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        data = [json.loads(line) for line in raw.splitlines() if line.strip()]

    if isinstance(data, dict):
        if isinstance(data.get("items"), list):
            return data["items"]
        if isinstance(data.get("emails"), list):
            return [email_to_item(email) for email in data["emails"]]
        return [data]
    if isinstance(data, list):
        return data
    raise ValueError("Payload deve ser objeto JSON, lista JSON ou JSONL.")


def email_to_item(raw: dict[str, Any]) -> dict[str, Any]:
    labels = raw.get("labels") or raw.get("label_ids") or []
    label_text = " ".join(str(x) for x in labels)
    text = str(raw.get("snippet") or raw.get("body_preview") or raw.get("text") or "")
    if label_text:
        text = f"{text}\nlabels: {label_text}"
    return {
        "source": "gmail",
        "sender": str(raw.get("from_") or raw.get("from") or raw.get("sender") or ""),
        "subject": str(raw.get("subject") or ""),
        "texto": text,
        "received_at": str(raw.get("email_ts") or raw.get("timestamp") or raw.get("date") or ""),
        "connector_id": str(raw.get("id") or raw.get("message_id") or raw.get("gmail_id") or ""),
    }


def item_text(item: dict[str, Any]) -> str:
    return str(item.get("texto") or item.get("text") or item.get("content") or item.get("snippet") or "")


def stable_hash(item: dict[str, Any]) -> str:
    seed = "|".join(
        [
            str(item.get("source", "")),
            str(item.get("sender", "")),
            str(item.get("subject", "")),
            str(item.get("received_at", "")),
            item_text(item),
        ]
    )
    return hashlib.sha256(seed.encode("utf-8")).hexdigest()[:12]


def timestamp_for_id(item: dict[str, Any]) -> str:
    raw = str(item.get("received_at") or "")
    digits = re.sub(r"[^0-9]", "", raw)
    if len(digits) >= 14:
        return f"{digits[:8]}T{digits[8:14]}"
    return datetime.now().strftime("%Y%m%dT%H%M%S")


def redact_summary(text: str, sensitivity: str) -> str:
    if sensitivity == "forbidden_external":
        return REDACTED_PLACEHOLDER
    return SECRET_RX.sub("[REDIGIDO]", text or "")[:180]


def normalize_source(source: str) -> str:
    source = (source or "manual").lower().strip()
    allowed = {"gmail", "whatsapp", "pdf", "drive", "mobile", "manual", "obsidian", "github"}
    return source if source in allowed else "manual"


def status_for(classification: dict[str, Any]) -> str:
    if classification["suggested_action"] == "descartar":
        return "archived"
    if classification["requires_human_approval"]:
        return "waiting_approval"
    return "classified"


def to_card(item: dict[str, Any], log_name: str = DEFAULT_LOG_NAME) -> dict[str, Any]:
    text = item_text(item)
    source = normalize_source(str(item.get("source") or "manual"))
    sender = str(item.get("sender") or "")
    subject = str(item.get("subject") or "")
    c = classificar_intake(text, source, sender, subject)
    intake_id = f"intake_{timestamp_for_id(item)}_{stable_hash(item)}"
    raw_ref = f"60_Sistemas/MEGATRON/v1/state/_raw/{intake_id}.txt (gitignored, nao versionado)"
    status = status_for(c)

    return {
        "id": intake_id,
        "source": source,
        "received_at": str(item.get("received_at") or c["received_at"]),
        "sender": sender,
        "subject": subject,
        "raw_content_ref": raw_ref,
        "summary": redact_summary(text, c["sensitivity"]),
        "domain": c["domain"],
        "sensitivity": c["sensitivity"],
        "urgency": c["urgency"],
        "suggested_agent": c["suggested_agent"],
        "suggested_action": c["suggested_action"],
        "alerta": bool(c["alerta"]),
        "requires_human_approval": bool(c["requires_human_approval"]),
        "rag_permitido": bool(c["rag_permitido"]),
        "status": status,
        "log_ref": log_name,
    }


def build_queue(
    items: list[dict[str, Any]],
    gerado_por: str = "universal_intake_adapter.py",
    generated_at: str | None = None,
) -> dict[str, Any]:
    cards = [to_card(item) for item in items]
    aguardando = sum(1 for card in cards if card["status"] == "waiting_approval")
    sensiveis = sum(1 for card in cards if card["sensitivity"] in {"private", "restricted", "no_rag", "forbidden_external"})
    return {
        "generated_at": generated_at or datetime.now().isoformat(timespec="seconds"),
        "gerado_por": gerado_por,
        "contrato": CONTRACT,
        "resumo": {
            "total": len(cards),
            "aguardando_fabio": aguardando,
            "sensiveis": sensiveis,
        },
        "cores_status": {
            "waiting_approval": "amarelo",
            "archived": "cinza",
            "blocked": "vermelho",
            "classified": "azul",
        },
        "fila": cards,
    }


def write_json(path: Path, payload: dict[str, Any]) -> Path:
    resolved_root = ROOT.resolve()
    resolved_target = path.resolve()
    if resolved_root not in [resolved_target, *resolved_target.parents]:
        raise ValueError("Destino deve permanecer dentro do vault FabioOS.")
    resolved_target.parent.mkdir(parents=True, exist_ok=True)
    resolved_target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return resolved_target


def main() -> int:
    parser = argparse.ArgumentParser(description="Gera fila do Intake Universal sem efeitos externos.")
    parser.add_argument("--input", type=Path, help="JSON, JSONL, {items:[...]} ou {emails:[...]}.")
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_QUEUE,
        help="Destino da fila JSON (por padrao, fila dedicada do Codex; gitignored).",
    )
    parser.add_argument("--stdout", action="store_true", help="Imprime JSON no stdout em vez de gravar arquivo.")
    parser.add_argument("--generated-at", help="Timestamp fixo para samples versionaveis.")
    args = parser.parse_args()

    items = load_payload(args.input)
    if not items:
        print(json.dumps({"ok": False, "error": "Payload vazio ou sem entradas."}, ensure_ascii=False), file=sys.stderr)
        return 1

    queue = build_queue(items, generated_at=args.generated_at)
    if args.stdout:
        print(json.dumps(queue, ensure_ascii=False, indent=2))
    else:
        target = write_json(args.output, queue)
        print(
            json.dumps(
                {"ok": True, "cards": len(queue["fila"]), "queue": target.relative_to(ROOT.resolve()).as_posix()},
                ensure_ascii=False,
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
