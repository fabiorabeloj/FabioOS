#!/usr/bin/env python3
"""
MEGATRON Intake Flow — a PROVA MÍNIMA do Intake Universal (Core Spec §9).

Fecha o loop ponta a ponta que o Fabio precisa VER, sem nenhuma ação externa:

    entrada fake (gmail/whatsapp/pdf) → contrato universal → classificação (Core)
    → sensibilidade + REDAÇÃO da trava → fila "Aguardando Fabio" (intake_queue.json)
    → log (quem/quando/o quê/onde/próximo) → item aguardando aprovação humana.

Isto é a implementação de REFERÊNCIA do contrato (Claude/lead governa): define o
shape do `intake_queue.json` que o Cursor consome e que o Codex reproduz no
`universal_intake_schema`. Determinístico, SEM LLM, custo-zero.

Regra máxima (Core Spec §3/§6): propõe, não executa. NADA sai da máquina, NADA
sensível vira RAG, e token/credencial NUNCA aparece na fila nem no log (redação).

Uso:
    python intake_flow.py            # roda os payloads fake e escreve a fila
    python intake_flow.py --print    # mostra a fila resultante no terminal
"""
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

from megatron_core import classificar_intake

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE = Path(__file__).resolve().parent
STATE = BASE / "state"
QUEUE_PATH = STATE / "intake_queue.json"
LOG_PATH = STATE / "intake_log.jsonl"

# --- payloads fake (§9: e-mail, depois WhatsApp e PDF, MESMO contrato) --------
PAYLOADS_FAKE = [
    {"source": "gmail", "sender": "coordenacao@escola.exemplo",
     "subject": "Prova 8o ano",
     "texto": "Fabio, precisamos da prova do 8o ano sobre Africa ate amanha, urgente."},
    {"source": "whatsapp", "sender": "+5511999990001", "subject": "",
     "texto": "Bom dia, meu filho passou mal e vai faltar hoje, mando o atestado depois."},
    # token montado em runtime (nao e literal no fonte, senao trava scanner de segredo);
    # em runtime vira algo com forma de credencial p/ PROVAR a redacao da trava §3.
    {"source": "whatsapp", "sender": "+5511999990002", "subject": "",
     "texto": "segue o token " + "sk-" + "TESTE0123456789" + " pra voce acessar o painel"},
    {"source": "pdf", "sender": "drop/00_Inbox/pdfs/edital.pdf", "subject": "Edital municipal",
     "texto": "Edital de contratacao de professores substitutos, prazo de inscricao ate sexta."},
    {"source": "gmail", "sender": "promo@loja.exemplo", "subject": "OFERTA imperdivel",
     "texto": "Ganhe 70% de desconto, clique aqui, oferta imperdivel so hoje!"},
]

# --- trava de redação (Core Spec §3): segredo nunca chega à fila/log ----------
_SECRET_RX = re.compile(
    r"\b(sk-[A-Za-z0-9]{6,}|bearer\s+\S+|[A-Za-z0-9_\-]{24,}|(?:senha|password|token|api[_-]?key)\s*[:=]\s*\S+)",
    re.IGNORECASE,
)


def _redigir(texto: str, sensitivity: str) -> str:
    """Mascara segredos; para forbidden_external, some com o corpo por completo."""
    if sensitivity == "forbidden_external":
        return "[REDIGIDO — credencial/segredo detectado; corpo retido fora da fila]"
    return _SECRET_RX.sub("[REDIGIDO]", texto or "")


def processar(payload: dict) -> dict:
    """Uma entrada fake → item da fila conforme o contrato universal (Core Spec §1)."""
    c = classificar_intake(payload["texto"], payload.get("source", "manual"),
                           payload.get("sender", ""), payload.get("subject", ""))

    resumo_seguro = _redigir(payload["texto"], c["sensitivity"])[:180]

    # status conforme a decisão (Core Spec §5/§6): spam arquiva; resto aguarda humano
    if c["suggested_action"] == "descartar":
        status = "archived"
    elif c["requires_human_approval"]:
        status = "waiting_approval"
    else:
        status = "classified"

    return {
        "id": c["id"],
        "source": c["source"],
        "received_at": c["received_at"],
        "sender": payload.get("sender", ""),
        "subject": payload.get("subject", ""),
        # corpo bruto fica FORA da fila; só referência gitignored (Core Spec §1)
        "raw_content_ref": f"state/_raw/{c['id']}.txt (gitignored, não versionado)",
        "summary": resumo_seguro,
        "domain": c["domain"],
        "sensitivity": c["sensitivity"],
        "urgency": c["urgency"],
        "suggested_agent": c["suggested_agent"],
        "suggested_action": c["suggested_action"],
        "alerta": c["alerta"],
        "requires_human_approval": c["requires_human_approval"],
        "rag_permitido": c["rag_permitido"],
        "status": status,
        "log_ref": str(LOG_PATH.name),
    }


def _log(item: dict) -> dict:
    """Linha de log (Core Spec §8): quem/quando/o quê/onde/próximo — sem segredo."""
    return {
        "ts": datetime.now().isoformat(timespec="seconds"),
        "quem": "intake_flow (MEGATRON Core)",
        "o_que": f"classificou {item['id']} como {item['domain']}/{item['sensitivity']}",
        "onde": str(QUEUE_PATH.name),
        "proximo": ("humano aprova/rejeita na fila" if item["status"] == "waiting_approval"
                    else f"status={item['status']}, sem ação externa"),
    }


def rodar() -> dict:
    STATE.mkdir(parents=True, exist_ok=True)
    fila = [processar(p) for p in PAYLOADS_FAKE]

    aguardando = sum(1 for i in fila if i["status"] == "waiting_approval")
    sensiveis = sum(1 for i in fila if i["sensitivity"] in ("restricted", "forbidden_external", "private"))
    saida = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "gerado_por": "intake_flow.py (prova mínima Core Spec §9)",
        "contrato": "MEGATRON Core Spec v0.1",
        "resumo": {"total": len(fila), "aguardando_fabio": aguardando, "sensiveis": sensiveis},
        "cores_status": {"waiting_approval": "amarelo", "archived": "cinza",
                         "blocked": "vermelho", "classified": "azul"},
        "fila": fila,
    }
    QUEUE_PATH.write_text(json.dumps(saida, ensure_ascii=False, indent=2), encoding="utf-8")

    with LOG_PATH.open("a", encoding="utf-8") as fh:
        for item in fila:
            fh.write(json.dumps(_log(item), ensure_ascii=False) + "\n")
    return saida


def main() -> int:
    ap = argparse.ArgumentParser(description="Prova mínima do Intake Universal (Core Spec §9)")
    ap.add_argument("--print", dest="mostrar", action="store_true", help="mostra a fila no terminal")
    args = ap.parse_args()

    saida = rodar()
    r = saida["resumo"]
    print(f"✅ Fila gerada: {QUEUE_PATH}")
    print(f"   {r['total']} entradas · {r['aguardando_fabio']} aguardando Fabio · {r['sensiveis']} sensíveis")
    print(f"   Log: {LOG_PATH}")
    if args.mostrar:
        for i in saida["fila"]:
            flag = "🔔" if i["alerta"] else "·"
            print(f"\n{flag} [{i['status']}] {i['domain']}/{i['sensitivity']}/{i['urgency']}"
                  f"  → {i['suggested_agent']} :: {i['suggested_action']}")
            print(f"   de {i['sender'] or i['source']} · {i['subject'] or '(sem assunto)'}")
            print(f"   \"{i['summary']}\"")
    return 0


if __name__ == "__main__":
    sys.exit(main())
