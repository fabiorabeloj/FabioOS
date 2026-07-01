#!/usr/bin/env python3
"""
PietraOS — export do estado da fila para a Interface (Cursor/Agentarium).

Lê os atendimentos + sessões de um tenant e gera um JSON que a aba "PietraOS Inbox"
consome (fila de cartões + resumo + persona). Contém texto de mensagens (sensível)
→ fica na pasta gitignored do tenant. Read-only.

Uso:
    python pietra_state.py --tenant colegio-pietra
"""
import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))
from pietra_inbox import carregar_config  # noqa: E402


def build(tenant: str, limite: int = 50) -> dict:
    tdir = BASE / "tenants" / tenant
    f = tdir / "atendimentos.jsonl"
    itens = []
    if f.exists():
        itens = [json.loads(l) for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]
    fila = itens[-limite:][::-1]                 # mais recentes primeiro
    por_risco = {}
    for it in itens:
        por_risco[it["risco"]] = por_risco.get(it["risco"], 0) + 1
    cfg = carregar_config()
    return {
        "generatedAt": datetime.now().isoformat(timespec="seconds"),
        "source": "pietraos-inbox", "tenant": tenant, "vertical": "escola",
        "cores_risco": {"baixo": "#22c55e", "medio": "#eab308",
                        "alto": "#f97316", "critico": "#dc2626"},
        "acoes": ["Responder", "Encaminhar", "Pedir dados", "Arquivar"],
        "resumo": {
            "total": len(itens), "por_risco": por_risco,
            "sensiveis": por_risco.get("alto", 0) + por_risco.get("critico", 0),
            "pendentes": sum(1 for it in itens if it["acao"] != "responder_auto"),
        },
        "fila": fila,
        "persona": cfg.get("persona", {}),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tenant", default="colegio-pietra")
    args = ap.parse_args()
    out = BASE / "tenants" / args.tenant / "pietra_state.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    data = build(args.tenant)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"PietraOS state -> {out.as_posix()} "
          f"({data['resumo']['total']} atendimentos, {data['resumo']['sensiveis']} sensíveis)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
