#!/usr/bin/env python3
"""
PietraOS WhatsApp dry-run bridge.

Receives an Evolution/n8n-style WhatsApp payload, calls
60_Sistemas/Pietra/pietra_conversa.py, and returns a proposed response/card.

Safety contract:
- dry-run only;
- no WhatsApp send;
- no external API;
- no RAG;
- phone number is redacted in the response;
- Pietra runtime state stays under 60_Sistemas/Pietra/tenants/ (gitignored).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse


for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


ROOT = Path(__file__).resolve().parents[3]
PIETRA_DIR = ROOT / "60_Sistemas" / "Pietra"
sys.path.insert(0, str(PIETRA_DIR))

from pietra_conversa import conversar  # noqa: E402


SECRET_RE = re.compile(
    r"(sk-[A-Za-z0-9]{10,}|gh[pous]_[A-Za-z0-9_]{10,}|Bearer\s+[A-Za-z0-9._-]{10,}|"
    r"api[_-]?key\s*[:=]|password\s*[:=]|senha\s*[:=]|secret\s*[:=]|token\s*[:=])",
    re.IGNORECASE,
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _as_dict(value):
    if isinstance(value, dict):
        return value
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
            return parsed if isinstance(parsed, dict) else {}
        except json.JSONDecodeError:
            return {}
    return {}


def _text_from_message(message: dict) -> str:
    return (
        message.get("conversation")
        or _as_dict(message.get("extendedTextMessage")).get("text")
        or _as_dict(message.get("imageMessage")).get("caption")
        or _as_dict(message.get("documentMessage")).get("caption")
        or ""
    ).strip()


def normalize_payload(payload: dict, default_tenant: str) -> dict:
    body = _as_dict(payload.get("body", payload))
    data = _as_dict(body.get("data", body))
    key = _as_dict(data.get("key"))
    message = _as_dict(data.get("message"))

    remote_jid = str(key.get("remoteJid") or body.get("remoteJid") or "")
    raw_number = remote_jid.replace("@s.whatsapp.net", "").replace("@g.us", "")
    raw_number = re.sub(r"\D+", "", raw_number)
    sender = raw_number or str(body.get("from") or data.get("from") or "unknown")

    instance = str(body.get("instance") or data.get("instance") or "")
    tenant = str(body.get("tenant") or data.get("tenant") or default_tenant)
    text = _text_from_message(message) or str(body.get("text") or body.get("texto") or "").strip()
    timestamp = data.get("messageTimestamp") or body.get("timestamp")

    ignored_reason = None
    if remote_jid.endswith("@g.us"):
        ignored_reason = "grupo_nao_suportado"
    elif key.get("fromMe"):
        ignored_reason = "mensagem_do_proprio_numero"
    elif not text:
        ignored_reason = "sem_texto"

    message_id_seed = "|".join([str(timestamp or ""), sender, text[:80], instance])
    message_id = "wa_" + hashlib.sha256(message_id_seed.encode("utf-8")).hexdigest()[:16]

    return {
        "message_id": message_id,
        "tenant": tenant,
        "sender": sender,
        "sender_redacted": redact_sender(sender),
        "instance": instance or "unknown",
        "text": text,
        "timestamp": timestamp,
        "ignored_reason": ignored_reason,
    }


def redact_sender(sender: str) -> str:
    digits = re.sub(r"\D+", "", sender)
    if not digits:
        return "unknown"
    return "****" + digits[-4:]


def safe_card(card: dict | None) -> dict | None:
    if not card:
        return None
    clean = dict(card)
    clean["remetente"] = redact_sender(str(clean.get("remetente", "")))
    if "texto" in clean:
        text = str(clean["texto"])
        clean["texto_resumo"] = "[redigido: possivel dado pessoal]" if len(text) > 0 else ""
        clean.pop("texto", None)
    return clean


def run(payload: dict, tenant: str = "colegio-pietra", dentro_horario: bool = True) -> dict:
    item = normalize_payload(payload, tenant)

    base = {
        "ok": True,
        "dry_run": True,
        "send_allowed": False,
        "external_effects": False,
        "rag_used": False,
        "generated_at": _utc_now(),
        "message_id": item["message_id"],
        "tenant": item["tenant"],
        "instance": item["instance"],
        "sender": item["sender_redacted"],
        "source": "whatsapp/evolution",
    }

    if item["ignored_reason"]:
        return {
            **base,
            "status": "ignored",
            "ignored_reason": item["ignored_reason"],
            "respostas_sugeridas": [],
            "cartao": None,
        }

    if SECRET_RE.search(item["text"]):
        return {
            **base,
            "status": "blocked",
            "blocked_reason": "possivel_segredo_no_texto",
            "respostas_sugeridas": [
                "Mensagem bloqueada para revisao humana: possivel segredo ou credencial detectada."
            ],
            "cartao": None,
        }

    result = conversar(
        item["tenant"],
        item["sender"],
        item["text"],
        dentro_horario=dentro_horario,
    )

    return {
        **base,
        "status": "proposed",
        "estado": result.get("estado"),
        "requires_human_approval": True,
        "respostas_sugeridas": result.get("respostas", []),
        "cartao": safe_card(result.get("cartao")),
    }


class Handler(BaseHTTPRequestHandler):
    server_version = "PietraWhatsAppDryRun/0.1"

    def do_GET(self):  # noqa: N802
        if urlparse(self.path).path != "/health":
            self._json({"ok": False, "error": "not_found"}, status=404)
            return
        self._json({"ok": True, "service": "pietra-whatsapp-dry-run"})

    def do_POST(self):  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path not in {"/pietra/whatsapp/dry-run", "/"}:
            self._json({"ok": False, "error": "not_found"}, status=404)
            return
        length = int(self.headers.get("content-length", "0") or "0")
        raw = self.rfile.read(length).decode("utf-8") if length else "{}"
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            self._json({"ok": False, "error": "invalid_json"}, status=400)
            return
        query = parse_qs(parsed.query)
        tenant = query.get("tenant", ["colegio-pietra"])[0]
        response = run(payload, tenant=tenant)
        self._json(response)

    def log_message(self, fmt, *args):  # noqa: A003
        sys.stderr.write("pietra-dry-run " + fmt % args + "\n")

    def _json(self, payload: dict, status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("content-type", "application/json; charset=utf-8")
        self.send_header("content-length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def load_payload(path: str | None) -> dict:
    if path:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    raw = sys.stdin.read()
    return json.loads(raw or "{}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Bridge dry-run WhatsApp/Evolution -> PietraOS")
    parser.add_argument("--input", help="JSON payload file. If omitted, reads stdin.")
    parser.add_argument("--tenant", default="colegio-pietra")
    parser.add_argument("--fora-horario", action="store_true")
    parser.add_argument("--serve", action="store_true", help="Run HTTP server.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8791)
    args = parser.parse_args()

    if args.serve:
        server = ThreadingHTTPServer((args.host, args.port), Handler)
        print(f"pietra-whatsapp-dry-run listening on http://{args.host}:{args.port}")
        server.serve_forever()
        return 0

    payload = load_payload(args.input)
    output = run(payload, tenant=args.tenant, dentro_horario=not args.fora_horario)
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if output.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
