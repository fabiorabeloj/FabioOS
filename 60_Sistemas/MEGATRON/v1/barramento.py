#!/usr/bin/env python3
"""
Barramento Multiagente do FabioOS — mailbox append-only entre agentes.

Padrão absorvido do agent-teams do ruflo (mailbox + estado compartilhado +
notify-lead), reimplementado governado e local: um arquivo markdown append-only
no vault (`50_Registros/Barramento_Multiagente.md`), legível no Obsidian e
parseável pelo MEGATRON.

Append-only = à prova de colisão: cada agente só ADICIONA uma linha ao fim;
nunca reescreve linhas existentes.

Uso:
    python barramento.py postar --de claude --para cursor --tipo ordem --msg "..."
    python barramento.py ler --para claude
    python barramento.py ler                 # tudo em aberto
"""
from pathlib import Path
from datetime import datetime
import argparse
import sys

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass


def _vault_root() -> Path:
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / "60_Sistemas/FabioOS/bootstrap/CLAUDE.md").exists():
            return parent
    return p.parents[3]


VAULT = _vault_root()
BUS = VAULT / "50_Registros" / "Barramento_Multiagente.md"
AGENTES_VALIDOS = ("claude", "codex", "cursor", "megatron", "lead", "todos")


def _esc(s: str) -> str:
    return s.replace("|", "/").replace("\n", " ").strip()


def _match(pa: str, para: str) -> bool:
    """Destinatário pa casa com a caixa 'para'? (todos -> todos; lead -> claude)."""
    if para is None:
        return True
    para = para.lower()
    if pa == para or pa == "todos":
        return True
    if para == "claude" and pa == "lead":
        return True
    return False


def postar(de: str, para: str, tipo: str, mensagem: str, status: str = "aberto") -> dict:
    """Adiciona uma mensagem ao fim do barramento. Devolve um Resultado."""
    de, para = de.lower().strip(), para.lower().strip()
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"| {ts} | {de} | {para} | {_esc(tipo)} | {status} | {_esc(mensagem)} |\n"
    BUS.parent.mkdir(parents=True, exist_ok=True)
    if not BUS.exists():
        BUS.write_text(
            "# Barramento Multiagente — FabioOS\n\n## Mensagens\n\n"
            "| ts | de | para | tipo | status | mensagem |\n|---|---|---|---|---|---|\n",
            encoding="utf-8")
    with BUS.open("a", encoding="utf-8") as f:
        f.write(linha)
    aviso = "" if para in AGENTES_VALIDOS else f" (⚠️ destinatário '{para}' fora da lista)"
    return {"tipo": "barramento", "ok": True, "titulo": f"Mensagem postada → {para}",
            "corpo": f"[{ts}] {de}→{para} ({tipo}): {mensagem}{aviso}",
            "fontes": [{"source_path": BUS.relative_to(VAULT).as_posix(),
                        "header_path": "Mensagens"}],
            "sugestao": "", "artefato": None}


def ler(para: str = None, status: str = "aberto") -> list:
    """Lê mensagens do barramento (não destrutivo). Filtra por destinatário e status."""
    if not BUS.exists():
        return []
    msgs = []
    for line in BUS.read_text(encoding="utf-8", errors="ignore").splitlines():
        if not line.startswith("| ") or "---" in line:
            continue
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cols) != 6:
            continue
        ts, de, pa, tp, st, msg = cols
        if ts == "ts" or de == "de":        # cabeçalho da tabela
            continue
        if status and st != status:
            continue
        if not _match(pa, para):
            continue
        msgs.append({"ts": ts, "de": de, "para": pa, "tipo": tp,
                     "status": st, "mensagem": msg})
    return msgs


def main() -> int:
    ap = argparse.ArgumentParser(description="Barramento Multiagente FabioOS")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("postar")
    p.add_argument("--de", required=True)
    p.add_argument("--para", required=True)
    p.add_argument("--tipo", default="aviso")
    p.add_argument("--msg", required=True)
    p.add_argument("--status", default="aberto")

    l = sub.add_parser("ler")
    l.add_argument("--para", default=None)
    l.add_argument("--status", default="aberto")

    args = ap.parse_args()
    if args.cmd == "postar":
        r = postar(args.de, args.para, args.tipo, args.msg, args.status)
        print(f"✅ {r['titulo']}\n{r['corpo']}")
        return 0
    msgs = ler(args.para, args.status)
    cx = f"para '{args.para}'" if args.para else "(todas)"
    print(f"📬 Barramento {cx} — {len(msgs)} mensagem(ns) em '{args.status}':")
    for m in msgs:
        print(f"  • [{m['ts']}] {m['de']}→{m['para']} ({m['tipo']}): {m['mensagem']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
