"""Utilitários comuns dos agentes MEGATRON (implementação mínima, stdlib)."""
import sys
from pathlib import Path
from datetime import datetime

# Console do Windows usa cp1252 por padrão; força UTF-8 para emojis/acentos.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


def vault_root() -> Path:
    """Sobe a árvore procurando o CLAUDE.md (raiz do vault)."""
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / "CLAUDE.md").exists():
            return parent
    return p.parents[5]  # fallback: agentes/implementacao/claude/ -> raiz


def agentes_dir() -> Path:
    return vault_root() / "60_Sistemas" / "MEGATRON" / "agentes"


def log_path() -> Path:
    return agentes_dir() / "logs" / "agentes_log.md"


def log_event(agente: str, acao: str, detalhe: str = "") -> None:
    """Grava uma linha de rastro no log dos agentes (sem segredos)."""
    lp = log_path()
    lp.parent.mkdir(parents=True, exist_ok=True)
    if not lp.exists():
        lp.write_text(
            "# Log de Execução — Agentes MEGATRON\n\n"
            "| timestamp | agente | ação | detalhe |\n|---|---|---|---|\n",
            encoding="utf-8",
        )
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    detalhe = detalhe.replace("|", "/").replace("\n", " ")
    with lp.open("a", encoding="utf-8") as f:
        f.write(f"| {ts} | {agente} | {acao} | {detalhe} |\n")
