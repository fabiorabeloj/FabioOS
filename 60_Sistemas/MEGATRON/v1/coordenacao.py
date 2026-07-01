#!/usr/bin/env python3
"""
Coordenação FabioOS — o readout único de "quem está em quê, e em que velocidade".

Ponte imediata para a dor real: os agentes (Claude/Codex/Cursor) avançam em
velocidades diferentes e sem se ver. Este script junta, num só painel, as três
fontes de estado que JÁ existem — sem depender do Cursor/Agentarium:

  1. Barramento  (50_Registros/Barramento_Multiagente.md)   → quem mandou o quê
  2. Fila Intake (state/intake_queue.json)                  → o que aguarda o Fabio
  3. Frentes     (60_Sistemas/FabioOS/Registro_Frentes_Ativas.md) → locks de arquivo

Read-only. Não escreve nada. Não age. Só mostra.

Uso:
    python coordenacao.py            # painel de texto
    python coordenacao.py --json     # mesmo estado em JSON (p/ Cursor/Agentarium)
"""
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE = Path(__file__).resolve().parent
VAULT = BASE.parents[2]
BARRAMENTO = VAULT / "50_Registros" / "Barramento_Multiagente.md"
FRENTES = VAULT / "60_Sistemas" / "FabioOS" / "Registro_Frentes_Ativas.md"
QUEUE = BASE / "state" / "intake_queue.json"

_DATA = re.compile(r"^\d{4}-\d{2}-\d{2}")


def _linhas_tabela(path: Path):
    """Gera as linhas de dados (list de células) de tabelas markdown do arquivo."""
    if not path.exists():
        return
    for ln in path.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if not ln.startswith("|"):
            continue
        cels = [c.strip() for c in ln.strip("|").split("|")]
        if len(cels) >= 2 and "---" not in cels[0]:
            yield cels


def ler_barramento():
    msgs = []
    for c in _linhas_tabela(BARRAMENTO):
        if len(c) >= 6 and _DATA.match(c[0]):
            msgs.append({"ts": c[0], "de": c[1], "para": c[2],
                         "tipo": c[3], "status": c[4], "mensagem": c[5]})
    return msgs


def ler_frentes():
    frentes = []
    for c in _linhas_tabela(FRENTES):
        # cabeçalho da tabela de frentes começa com "Frente"
        if len(c) >= 4 and c[0].lower() != "frente" and not _DATA.match(c[0]):
            frentes.append({"frente": c[0], "dono": c[1], "estado": c[3] if len(c) > 3 else "?"})
    return frentes


def ler_fila():
    if not QUEUE.exists():
        return []
    return json.loads(QUEUE.read_text(encoding="utf-8")).get("fila", [])


def montar():
    msgs = ler_barramento()
    # última atividade por agente (velocidade)
    velocidade = {}
    for m in msgs:
        velocidade[m["de"]] = max(velocidade.get(m["de"], ""), m["ts"])
    # atividade recente REAL (cronológica). Nota: o status "aberto" do barramento
    # não é confiável (ninguém marca "resolvido"), então mostramos o que de fato
    # aconteceu por último, não o que está "aberto".
    recentes = sorted(msgs, key=lambda m: m["ts"])[-8:]

    fila = ler_fila()
    aguardando = [i for i in fila if i["status"] == "waiting_approval"]
    frentes = [f for f in ler_frentes() if f["estado"].lower() not in ("concluida", "concluída", "concluido", "concluído")]

    return {
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
        "barramento": {"total": len(msgs)},
        "velocidade": velocidade,
        "atividade_recente": recentes,
        "fila_aguardando_fabio": [
            {"id": i["id"], "domain": i["domain"], "sensitivity": i["sensitivity"],
             "urgency": i["urgency"], "action": i["suggested_action"]} for i in aguardando],
        "frentes_ativas": frentes,
    }


def render(e: dict) -> str:
    L = []
    L.append(f"╔══ COORDENAÇÃO FabioOS · {e['gerado_em']} ══╗")
    L.append(f"║ barramento: {e['barramento']['total']} msgs")

    L.append("╟── velocidade (última atividade por agente) ──")
    if e["velocidade"]:
        for ag, ts in sorted(e["velocidade"].items(), key=lambda kv: kv[1], reverse=True):
            L.append(f"║   {ag:<8} {ts}")
    else:
        L.append("║   (sem registro)")

    L.append(f"╟── atividade recente (últimas {len(e['atividade_recente'])}, cronológica) ──")
    for m in e["atividade_recente"]:
        hora = m["ts"][11:16] if len(m["ts"]) >= 16 else m["ts"]
        L.append(f"║   {hora} [{m['tipo']}] {m['de']}→{m['para']}: {m['mensagem'][:56]}")
    if not e["atividade_recente"]:
        L.append("║   (sem atividade)")

    L.append(f"╟── fila AGUARDANDO FABIO ({len(e['fila_aguardando_fabio'])}) ──")
    for i in e["fila_aguardando_fabio"]:
        L.append(f"║   {i['domain']}/{i['sensitivity']}/{i['urgency']} → {i['action']}")
    if not e["fila_aguardando_fabio"]:
        L.append("║   (fila vazia)")

    L.append(f"╟── frentes ativas / locks ({len(e['frentes_ativas'])}) ──")
    for f in e["frentes_ativas"]:
        L.append(f"║   {f['frente']} ({f['dono']}, {f['estado']})")
    if not e["frentes_ativas"]:
        L.append("║   (nenhum lock ativo)")

    L.append("╚" + "═" * 48 + "╝")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description="Readout de coordenação multiagente (read-only)")
    ap.add_argument("--json", action="store_true", help="emite estado em JSON")
    args = ap.parse_args()
    e = montar()
    print(json.dumps(e, ensure_ascii=False, indent=2) if args.json else render(e))
    return 0


if __name__ == "__main__":
    sys.exit(main())
