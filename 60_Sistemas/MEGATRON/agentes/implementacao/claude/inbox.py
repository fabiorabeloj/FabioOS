#!/usr/bin/env python3
"""
Agente Inbox (agent.inbox) — implementação mínima (report-only).

Conforme specs/Agente_Inbox.md. Varre 00_Inbox/, identifica o tipo de cada
entrada, sugere o agente responsável e o domínio. NÃO move nem apaga nada na v1
(mover exige autorização humana explícita — fora desta versão).

Uso:
    python inbox.py
"""
import sys
from pathlib import Path

from _common import vault_root, log_event

ROOT = vault_root()
INBOX = ROOT / "00_Inbox"

# extensão -> (tipo, agente sugerido)
TIPO_AGENTE = {
    ".md": ("markdown", "Arquivista"),
    ".txt": ("texto", "Arquivista"),
    ".pdf": ("pdf", "Arquivista (/ingest-pdf)"),
    ".docx": ("documento", "Arquivista (/ingest-doc)"),
    ".png": ("imagem", "Arquivista (OCR futuro)"),
    ".jpg": ("imagem", "Arquivista (OCR futuro)"),
    ".jpeg": ("imagem", "Arquivista (OCR futuro)"),
    ".mp3": ("áudio", "Arquivista (transcrição futura)"),
    ".wav": ("áudio", "Arquivista (transcrição futura)"),
}

DOMINIO_HINT = {
    "pietra": "PietraOS", "aluno": "PietraOS", "matricula": "PietraOS",
    "prova": "Escola", "geografia": "Escola", "filosofia": "Escola",
    "primus": "PrimusOS", "rpg": "PrimusOS",
}


def dominio_por_nome(nome: str) -> str:
    n = nome.lower()
    for k, v in DOMINIO_HINT.items():
        if k in n:
            return v
    return "indefinido"


def main():
    print("=" * 60)
    print("AGENTE Inbox — triagem de 00_Inbox/ (report-only, não move)")
    print("=" * 60)
    if not INBOX.exists():
        print("\n00_Inbox/ não existe.")
        return 0

    itens = [p for p in sorted(INBOX.rglob("*")) if p.is_file()
             and not p.name.startswith(".")]
    if not itens:
        print("\n✅ Inbox vazia. Nada a triar.")
        log_event("Inbox", "triagem", "inbox vazia")
        return 0

    print(f"\n📥 {len(itens)} entrada(s):\n")
    for p in itens:
        ext = p.suffix.lower()
        tipo, agente = TIPO_AGENTE.get(ext, ("desconhecido", "humano"))
        dom = dominio_por_nome(p.name)
        rel = p.relative_to(ROOT).as_posix()
        print(f"   • {rel}")
        print(f"       tipo: {tipo} | domínio: {dom} | agente sugerido: {agente}")

    print("\nℹ️  Mover/transformar exige autorização humana (não feito na v1).")
    log_event("Inbox", "triagem", f"{len(itens)} item(ns) listado(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
