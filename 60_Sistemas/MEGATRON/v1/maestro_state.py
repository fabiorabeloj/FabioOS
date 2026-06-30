#!/usr/bin/env python3
"""
Maestro state export — fonte ÚNICA de verdade do roster de agentes do FabioOS.

Exporta o estado canônico do MEGATRON Maestro (registry de capacidades +
barramento) como JSON para a Interface (Agentarium/Cursor) consumir, em vez de
manter um roster paralelo no backend visual. Read-only; não toca runtime.

Costura anti-divergência: Claude (Maestro) é dono do roster + status; Cursor
renderiza este JSON. Mapeia os campos do registry para o vocabulário do
Agentarium (layer/status), preservando o status real (ativo/planejado/gated).

Uso:
    python maestro_state.py            # grava em state/maestro_state.json
    python maestro_state.py --out X    # caminho custom
"""
import json
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).resolve().parent))
from registry import capacidades          # noqa: E402
from barramento import ler as ler_barramento  # noqa: E402

# registry agente -> AgentLayer do Agentarium (apps/agentarium/.../types.ts)
LAYER = {
    "arquivista": "knowledge", "rag": "knowledge", "grafo": "knowledge",
    "reasoningbank": "knowledge", "barramento": "command", "pesquisador": "knowledge",
    "documentalista": "school", "interface": "interface", "programador": "technical",
    "banco": "technical", "laboratorio": "technical", "coletor_visual": "knowledge",
    "navegador": "technical", "atendente": "personal", "infra": "technical",
    "automacao": "technical",
}
# status real do FabioOS -> AgentStatus do Agentarium
STATUS_MAP = {"ativo": "active", "planejado": "planned", "gated": "planned"}


def build() -> dict:
    cat = capacidades()
    agents = []
    for aid, d in cat.items():
        agents.append({
            "id": aid,
            "name": aid,
            "layer": LAYER.get(aid, "technical"),
            "status": STATUS_MAP.get(d["status"], "planned"),
            "rawStatus": d["status"],          # ativo | planejado | gated (verdade FabioOS)
            "role": d["ferramenta"],
            "capabilities": d["capacidades"],
        })
    msgs = ler_barramento(status="aberto")     # todas as mensagens abertas
    return {
        "generatedAt": datetime.now().isoformat(timespec="seconds"),
        "source": "megatron-maestro",
        "agents": agents,
        "counts": {
            "active": sum(1 for a in agents if a["status"] == "active"),
            "planned": sum(1 for a in agents if a["status"] == "planned"),
            "total": len(agents),
        },
        "barramento": msgs[-25:],              # eventos recentes p/ o EventLog
    }


def main() -> int:
    out = Path(__file__).resolve().parent / "state" / "maestro_state.json"
    if "--out" in sys.argv:
        out = Path(sys.argv[sys.argv.index("--out") + 1])
    out.parent.mkdir(parents=True, exist_ok=True)
    data = build()
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Maestro state -> {out.as_posix()} "
          f"({data['counts']['active']} ativos / {data['counts']['total']} total, "
          f"{len(data['barramento'])} msgs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
