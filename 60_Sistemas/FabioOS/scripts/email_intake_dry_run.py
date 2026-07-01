#!/usr/bin/env python3
"""
Email Intake Dry-Run - FabioOS.

Recebe mensagens em JSON/JSONL exportadas por um conector autorizado (Codex Gmail,
n8n Gmail, IMAP futuro etc.), classifica e gera uma triagem local restrita.

Regra: este script nunca envia, arquiva, deleta, marca como lido, cria rascunho
no Gmail, chama API externa ou indexa RAG. Ele so escreve um relatorio Markdown
local em pasta gitignored.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
SCRIPTS_DIR = ROOT / "60_Sistemas" / "FabioOS" / "scripts"
MEGATRON_V1 = ROOT / "60_Sistemas" / "MEGATRON" / "v1"
DEFAULT_OUTPUT_DIR = ROOT / "05_Raw_Sources" / "_compat_sources" / "email" / "_restrito" / "triagens"
DEFAULT_QUEUE = ROOT / "60_Sistemas" / "MEGATRON" / "v1" / "state" / "intake_queue.json"

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
if str(MEGATRON_V1) not in sys.path:
    sys.path.insert(0, str(MEGATRON_V1))

from megatron_core import classificar_intake  # noqa: E402
from universal_intake_adapter import build_queue, email_to_item, write_json  # noqa: E402


@dataclass
class EmailItem:
    message_id: str
    thread_id: str
    sender: str
    subject: str
    snippet: str
    labels: list[str]
    timestamp: str
    has_attachment: bool
    attachment_names: list[str] = field(default_factory=list)


@dataclass
class TriageResult:
    fingerprint: str
    domain: str
    urgency: str
    sensitivity: str
    bucket: str
    suggested_action: str
    requires_human: bool
    flags: list[str]
    item: EmailItem


def load_payload(path: Path | None) -> list[dict[str, Any]]:
    raw = sys.stdin.read() if path is None else path.read_text(encoding="utf-8")
    raw = raw.strip()
    if not raw:
        return []
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        data = [json.loads(line) for line in raw.splitlines() if line.strip()]

    if isinstance(data, dict) and isinstance(data.get("emails"), list):
        return data["emails"]
    if isinstance(data, dict):
        return [data]
    if isinstance(data, list):
        return data
    raise ValueError("Payload deve ser JSON object, lista JSON ou JSONL.")


def normalize_email(raw: dict[str, Any]) -> EmailItem:
    attachments = raw.get("attachments") or []
    inline_images = raw.get("inline_images") or []
    attachment_names: list[str] = []
    for entry in [*attachments, *inline_images]:
        if isinstance(entry, dict) and entry.get("filename"):
            attachment_names.append(str(entry["filename"]))

    return EmailItem(
        message_id=str(raw.get("id") or raw.get("message_id") or raw.get("gmail_id") or ""),
        thread_id=str(raw.get("thread_id") or raw.get("threadId") or ""),
        sender=str(raw.get("from_") or raw.get("from") or raw.get("sender") or ""),
        subject=str(raw.get("subject") or "(sem assunto)"),
        snippet=str(raw.get("snippet") or raw.get("body_preview") or raw.get("text") or ""),
        labels=[str(x) for x in (raw.get("labels") or raw.get("label_ids") or [])],
        timestamp=str(raw.get("email_ts") or raw.get("timestamp") or raw.get("date") or ""),
        has_attachment=bool(raw.get("has_attachment") or attachments or inline_images),
        attachment_names=attachment_names,
    )


def text_for_core(item: EmailItem) -> str:
    parts = [item.snippet]
    if item.labels:
        parts.append("labels: " + " ".join(item.labels))
    if item.attachment_names:
        parts.append("attachments: " + " ".join(item.attachment_names[:5]))
    return "\n".join(part for part in parts if part)


def bucket_from_core(classification: dict[str, Any], item: EmailItem) -> tuple[str, str]:
    domain = classification["domain"]
    action = classification["suggested_action"]
    sensitivity = classification["sensitivity"]

    if sensitivity in {"restricted", "forbidden_external", "no_rag"}:
        return "Revisao humana", action
    if domain == "spam" or action == "descartar":
        return "FYI / ruido", action
    if item.has_attachment:
        return "Documento/anexo", action
    if domain in {"pietraos", "escolaos"}:
        return "Escola / Pietra", action
    if domain == "financeiro":
        return "Financeiro", action
    if domain in {"fabios", "primus", "tecnico"}:
        return "Projeto", action
    return "Triagem", action


def classify(item: EmailItem) -> TriageResult:
    core = classificar_intake(
        text_for_core(item),
        source="gmail",
        sender=item.sender,
        subject=item.subject,
    )
    flags: list[str] = []

    if item.has_attachment:
        flags.append("tem_anexo")
    if core["domain"] == "spam":
        flags.append("possivel_ruido")
    if core["sensitivity"] in {"private", "restricted", "no_rag", "forbidden_external"}:
        flags.append("possivel_dado_sensivel")
    if core["urgency"] in {"high", "critical"}:
        flags.append("possivel_urgencia")

    bucket, action = bucket_from_core(core, item)

    digest_source = "|".join([item.message_id, item.thread_id, item.sender, item.subject, item.timestamp])
    fingerprint = hashlib.sha256(digest_source.encode("utf-8")).hexdigest()[:16]

    return TriageResult(
        fingerprint=fingerprint,
        domain=core["domain"],
        urgency=core["urgency"],
        sensitivity=core["sensitivity"],
        bucket=bucket,
        suggested_action=action,
        requires_human=bool(core["requires_human_approval"]),
        flags=flags,
        item=item,
    )


def mask_sender(sender: str) -> str:
    if "<" in sender and ">" in sender:
        name = sender.split("<", 1)[0].strip()
        email = sender.split("<", 1)[1].split(">", 1)[0]
        return f"{name} <{mask_email(email)}>"
    if "@" in sender:
        return mask_email(sender)
    return sender[:80]


def mask_email(email: str) -> str:
    local, _, domain = email.partition("@")
    if not domain:
        return email[:3] + "***"
    return f"{local[:2]}***@{domain}"


def safe_slug(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return value[:60] or "email-triagem"


def render_markdown(results: list[TriageResult], source_name: str) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = [
        "---",
        "tipo: triagem-email",
        "area: 05_Raw_Sources",
        "projeto: FabioOS",
        "classe_dado: Restrito",
        "status: dry-run",
        f"gerado_em: {now}",
        "tags: [fabios, email, gmail, inbox, dry-run]",
        "---",
        "",
        f"# Triagem de Email - Dry Run ({now})",
        "",
        "## Escopo",
        "",
        f"- Fonte do payload: `{source_name}`",
        f"- Mensagens analisadas: {len(results)}",
        "- Efeitos externos: nenhum",
        "- Envio/arquivo/delete/marcar como lido: nao executado",
        "- RAG/Grafo: nao indexado",
        "",
        "## Resultado por mensagem",
        "",
    ]

    for result in results:
        item = result.item
        lines.extend(
            [
                f"### {result.fingerprint} - {item.subject[:120]}",
                "",
                f"- Remetente: {mask_sender(item.sender)}",
                f"- Data: {item.timestamp or 'nao informada'}",
                f"- Dominio: {result.domain}",
                f"- Urgencia: {result.urgency}",
                f"- Sensibilidade: {result.sensitivity}",
                f"- Bucket: {result.bucket}",
                f"- Acao sugerida: {result.suggested_action}",
                f"- Requer humano: {'sim' if result.requires_human else 'nao'}",
                f"- Flags: {', '.join(result.flags) if result.flags else 'nenhuma'}",
                f"- Anexos: {', '.join(item.attachment_names[:5]) if item.attachment_names else 'nao'}",
                "",
                "> Snippet omitido por padrao. Use o conector autorizado para reler a mensagem se Fabio aprovar.",
                "",
            ]
        )

    lines.extend(
        [
            "## Proximos passos",
            "",
            "- Fabio escolhe quais itens podem virar tarefa, resposta sugerida ou nota.",
            "- Itens sensiveis permanecem em pasta restrita e fora do Git.",
            "- Envio externo exige aprovacao explicita.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_report(markdown: str, output_dir: Path, source_name: str) -> Path:
    resolved_root = ROOT.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    resolved_output = output_dir.resolve()
    if resolved_root not in [resolved_output, *resolved_output.parents]:
        raise ValueError("Destino de saida deve permanecer dentro do vault FabioOS.")
    name = f"{datetime.now().strftime('%Y-%m-%d_%H%M%S')}_{safe_slug(source_name)}.md"
    target = output_dir / name
    target.write_text(markdown, encoding="utf-8")
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description="Classifica emails em dry-run sem efeitos externos.")
    parser.add_argument("--input", type=Path, help="JSON, JSONL ou objeto {emails:[...]} exportado por conector autorizado.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--queue-output", type=Path, default=DEFAULT_QUEUE, help="Destino da fila universal JSON.")
    parser.add_argument("--stdout", action="store_true", help="Imprime Markdown em vez de gravar arquivo.")
    parser.add_argument("--queue-json", action="store_true", help="Emite fila universal JSON em vez do Markdown legado.")
    parser.add_argument("--write-queue", action="store_true", help="Grava tambem a fila universal consumivel pelo Cursor.")
    args = parser.parse_args()

    payload = load_payload(args.input)
    if not payload:
        print(
            json.dumps(
                {"ok": False, "error": "Payload vazio ou sem mensagens."},
                ensure_ascii=False,
            ),
            file=sys.stderr,
        )
        return 1

    emails = [normalize_email(raw) for raw in payload]
    results = [classify(item) for item in emails]
    source_name = args.input.name if args.input else "stdin"
    queue = build_queue(
        [email_to_item(raw) for raw in payload],
        gerado_por="email_intake_dry_run.py -> universal_intake_adapter",
    )

    if args.queue_json:
        print(json.dumps(queue, ensure_ascii=False, indent=2))
        return 0

    markdown = render_markdown(results, source_name)

    if args.stdout:
        print(markdown)
        return 0

    target = write_report(markdown, args.output_dir, source_name)
    queue_rel = None
    if args.write_queue:
        queue_target = write_json(args.queue_output, queue)
        queue_rel = queue_target.relative_to(ROOT).as_posix()
    rel = target.relative_to(ROOT).as_posix()
    print(json.dumps({"ok": True, "messages": len(results), "report": rel, "queue": queue_rel}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
