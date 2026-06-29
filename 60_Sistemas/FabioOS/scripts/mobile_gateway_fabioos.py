#!/usr/bin/env python3
"""Gateway mobile local do FabioOS.

Serve uma pagina web simples para capturar texto pelo celular e salvar notas em
00_Inbox/mobile/. Nao chama APIs externas, nao usa modelos e nao toca RAG/Grafo.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import socket
import sys
from datetime import datetime
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse


for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


def vault_root() -> Path:
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / "60_Sistemas/FabioOS/bootstrap/CLAUDE.md").exists():
            return parent
    raise RuntimeError("Nao encontrei 60_Sistemas/FabioOS/bootstrap/CLAUDE.md acima do script.")


ROOT = vault_root()
INBOX_DIR = ROOT / "00_Inbox" / "mobile"
MAX_BYTES = 200_000


def slugify(value: str, fallback: str = "captura-mobile") -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return (value[:70] or fallback).strip("-")


def safe_target(filename: str) -> Path:
    base = INBOX_DIR.resolve()
    target = (base / filename).resolve()
    if target != base and base not in target.parents:
        raise ValueError("Destino fora da Inbox mobile.")
    return target


def note_path(title: str) -> Path:
    now = datetime.now()
    slug = slugify(title)
    filename = f"{now.strftime('%Y-%m-%d_%H%M%S')}_{slug}.md"
    return safe_target(filename)


def frontmatter_value(value: str) -> str:
    return value.replace("\n", " ").replace('"', "'").strip()


def render_note(title: str, text: str, source: str) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    safe_title = frontmatter_value(title)
    safe_source = frontmatter_value(source or "mobile_gateway")
    return f"""---
tipo: inbox-mobile
area: 00_Inbox
projeto: FabioOS
status: inbox
origem: {safe_source}
classe_dado: Privado
capturado_em: {now}
tags: [fabios, mobile, inbox]
---

# {title}

{text.strip()}

## Processamento sugerido

- [ ] Classificar dominio/dados/permissoes.
- [ ] Decidir se vira nota wiki, tarefa, changelog, SPEC ou descarte.
- [ ] Nao enviar a modelo externo sem aprovacao humana.

<!-- titulo_frontmatter: "{safe_title}" -->
"""


def count_notes() -> int:
    if not INBOX_DIR.exists():
        return 0
    return len(list(INBOX_DIR.glob("*.md")))


def latest_notes(limit: int = 5) -> list[str]:
    if not INBOX_DIR.exists():
        return []
    files = sorted(INBOX_DIR.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    return [p.name for p in files[:limit]]


def local_ips() -> list[str]:
    ips: list[str] = []
    try:
        hostname = socket.gethostname()
        for item in socket.getaddrinfo(hostname, None, family=socket.AF_INET):
            ip = item[4][0]
            if ip.startswith("127.") or ip.startswith("169.254."):
                continue
            if ip not in ips:
                ips.append(ip)
    except Exception:
        pass
    return ips


def response_payload(ok: bool, **extra: object) -> bytes:
    payload = {"ok": ok, **extra}
    return json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")


class FabioOSMobileHandler(BaseHTTPRequestHandler):
    server_version = "FabioOSMobileGateway/0.1"

    def log_message(self, fmt: str, *args: object) -> None:
        sys.stderr.write(f"[{datetime.now().isoformat(timespec='seconds')}] {self.address_string()} {fmt % args}\n")

    @property
    def token(self) -> str:
        return getattr(self.server, "fabioos_token", "")

    def authorized(self) -> bool:
        if not self.token:
            return True
        parsed = urlparse(self.path)
        query_token = parse_qs(parsed.query).get("token", [""])[0]
        header_token = self.headers.get("X-FabioOS-Token", "")
        return query_token == self.token or header_token == self.token

    def send_bytes(self, status: int, body: bytes, content_type: str = "application/json; charset=utf-8") -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def send_json(self, status: int, ok: bool, **extra: object) -> None:
        self.send_bytes(status, response_payload(ok, **extra))

    def read_payload(self) -> dict[str, object]:
        length = int(self.headers.get("Content-Length", "0") or "0")
        if length > MAX_BYTES:
            raise ValueError(f"Payload acima do limite de {MAX_BYTES} bytes.")
        raw = self.rfile.read(length)
        content_type = self.headers.get("Content-Type", "")
        if "application/json" in content_type:
            data = json.loads(raw.decode("utf-8") or "{}")
            if not isinstance(data, dict):
                raise ValueError("JSON precisa ser objeto.")
            return data
        form = parse_qs(raw.decode("utf-8"))
        return {key: values[0] if values else "" for key, values in form.items()}

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/":
            self.send_bytes(HTTPStatus.OK, self.render_home().encode("utf-8"), "text/html; charset=utf-8")
            return
        if parsed.path == "/health":
            self.send_json(
                HTTPStatus.OK,
                True,
                service="FabioOS Mobile Gateway",
                inbox_notes=count_notes(),
                auth_required=bool(self.token),
            )
            return
        if parsed.path == "/api/status":
            if not self.authorized():
                self.send_json(HTTPStatus.UNAUTHORIZED, False, error="token invalido")
                return
            self.send_json(
                HTTPStatus.OK,
                True,
                inbox_notes=count_notes(),
                latest_notes=latest_notes(),
                vault=str(ROOT),
                local_ips=local_ips(),
            )
            return
        self.send_json(HTTPStatus.NOT_FOUND, False, error="endpoint nao encontrado")

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path != "/api/capture":
            self.send_json(HTTPStatus.NOT_FOUND, False, error="endpoint nao encontrado")
            return
        if not self.authorized():
            self.send_json(HTTPStatus.UNAUTHORIZED, False, error="token invalido")
            return
        try:
            data = self.read_payload()
            text = str(data.get("text", "")).strip()
            title = str(data.get("title", "")).strip() or text.splitlines()[0][:80] or "Captura mobile"
            source = str(data.get("source", "mobile_gateway")).strip() or "mobile_gateway"
            dry_run = str(data.get("dry_run", "")).lower() in {"1", "true", "sim", "yes"}
            if not text:
                self.send_json(HTTPStatus.BAD_REQUEST, False, error="texto vazio")
                return
            target = note_path(title)
            if dry_run:
                self.send_json(HTTPStatus.OK, True, dry_run=True, would_write=str(target.relative_to(ROOT)))
                return
            INBOX_DIR.mkdir(parents=True, exist_ok=True)
            target.write_text(render_note(title, text, source), encoding="utf-8")
            self.send_json(HTTPStatus.CREATED, True, saved=str(target.relative_to(ROOT)), inbox_notes=count_notes())
        except Exception as exc:
            self.send_json(HTTPStatus.BAD_REQUEST, False, error=str(exc))

    def render_home(self) -> str:
        auth_note = "Token ativo nesta sessao." if self.token else "Sem token: use apenas em rede local confiavel."
        return f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>FabioOS Mobile Gateway</title>
  <style>
    :root {{ color-scheme: light dark; font-family: system-ui, -apple-system, Segoe UI, sans-serif; }}
    body {{ margin: 0; padding: 18px; background: #111; color: #f4f4f4; }}
    main {{ max-width: 760px; margin: 0 auto; }}
    h1 {{ font-size: 1.35rem; margin: 0 0 6px; }}
    p {{ color: #bdbdbd; line-height: 1.4; }}
    label {{ display: block; margin: 14px 0 6px; font-weight: 700; }}
    input, textarea, button {{ width: 100%; box-sizing: border-box; font: inherit; border-radius: 8px; }}
    input, textarea {{ border: 1px solid #444; background: #1f1f1f; color: #fff; padding: 12px; }}
    textarea {{ min-height: 220px; resize: vertical; }}
    button {{ margin-top: 14px; padding: 13px 16px; border: 0; background: #2e7dff; color: white; font-weight: 800; }}
    .status {{ margin-top: 14px; padding: 12px; border-radius: 8px; background: #1b1b1b; white-space: pre-wrap; }}
    .muted {{ font-size: .92rem; color: #aaa; }}
  </style>
</head>
<body>
<main>
  <h1>FabioOS Mobile Gateway</h1>
  <p class="muted">{html.escape(auth_note)} Capturas vao para <code>00_Inbox/mobile/</code>.</p>
  <label for="title">Titulo opcional</label>
  <input id="title" autocomplete="off" placeholder="Ex.: Ideia para MEGATRON">
  <label for="text">Mensagem</label>
  <textarea id="text" autofocus placeholder="Digite ou cole aqui o que voce quer mandar para o FabioOS"></textarea>
  <button id="send">Salvar no FabioOS</button>
  <div id="status" class="status">Pronto.</div>
</main>
<script>
const params = new URLSearchParams(location.search);
const token = params.get("token") || "";
const statusBox = document.getElementById("status");
document.getElementById("send").addEventListener("click", async () => {{
  const title = document.getElementById("title").value;
  const text = document.getElementById("text").value;
  statusBox.textContent = "Salvando...";
  try {{
    const response = await fetch("/api/capture", {{
      method: "POST",
      headers: {{
        "Content-Type": "application/json",
        "X-FabioOS-Token": token
      }},
      body: JSON.stringify({{ title, text, source: "mobile_browser" }})
    }});
    const data = await response.json();
    if (!response.ok || !data.ok) throw new Error(data.error || "falha ao salvar");
    statusBox.textContent = "Salvo: " + data.saved;
    document.getElementById("text").value = "";
  }} catch (err) {{
    statusBox.textContent = "Erro: " + err.message;
  }}
}});
</script>
</body>
</html>"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Gateway mobile local do FabioOS.")
    parser.add_argument("--bind", default="127.0.0.1", help="endereco de bind; use 0.0.0.0 para celular na LAN")
    parser.add_argument("--port", type=int, default=8787, help="porta HTTP")
    parser.add_argument("--token", default="", help="token local opcional para proteger endpoints")
    args = parser.parse_args()

    server = ThreadingHTTPServer((args.bind, args.port), FabioOSMobileHandler)
    setattr(server, "fabioos_token", args.token)

    print("FabioOS Mobile Gateway iniciado")
    print(f"Local: http://127.0.0.1:{args.port}")
    if args.bind in {"0.0.0.0", "::"}:
        for ip in local_ips():
            print(f"Celular/LAN: http://{ip}:{args.port}")
    if args.token:
        print("Token local habilitado; abra a URL com ?token=<token-local>.")
    else:
        print("Sem token; use apenas em rede local confiavel.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nEncerrando gateway.")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
