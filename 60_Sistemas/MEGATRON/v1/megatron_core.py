#!/usr/bin/env python3
"""
MEGATRON Core — o CÉREBRO do Intake Universal.

Implementa o MEGATRON Core Spec v0.1: recebe uma entrada normalizada (de qualquer
canal) e devolve a enriquece com domínio, sensibilidade, urgência, agente sugerido,
ação sugerida, requires_human_approval e status. Cognitivo, determinístico, SEM LLM
(custo-zero). Codex encaixa isto no universal_intake_schema; Cursor exibe na fila.

Regra máxima (Core Spec §3): nada externo/sensível age sozinho; padrão = propor.

Uso:
    python megatron_core.py "Fabio, precisamos da prova do 8o ano sobre Africa ate amanha"
    python megatron_core.py "segue o token sk-ABC123..." --source gmail
"""
import argparse
import hashlib
import json
import re
import sys
import unicodedata
from datetime import datetime

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass


def _n(s: str) -> str:
    return unicodedata.normalize("NFKD", (s or "")).encode("ascii", "ignore").decode().lower()


# --- Taxonomia (Core Spec §2) : domínio -> (keywords, agente) --------------
DOMINIOS = {
    "spam":       (["promocao", "oferta", "ganhe", "clique aqui", "desconto", "imperdivel", "spam"], "descarte"),
    "seguranca":  (["token", "senha", "password", "api key", "apikey", "bearer", "credencial", "secret"], "bloqueio"),
    "saude":      (["atestado", "medico", "saude", "doente", "febre", "remedio", "laudo", "alergia"], "humano_restrito"),
    "juridico":   (["processo", "intimacao", "advogado", "juridico", "contrato", "notificacao extrajudicial", "acao judicial"], "humano_restrito"),
    "financeiro": (["boleto", "fatura", "cobranca", "pagamento", "banco", "mensalidade", "nota fiscal", "pix", "inadimpl"], "financeiro"),
    "primus":     (["rpg", "primus", "missao", "cantina", "worldstate", "catalog", "mestre", "personagem"], "codex_primus"),
    "escolaos":   (["prova", "revisao", "avaliacao", "gabarito", "cronograma", "coordenacao", "aula", "conteudo", "comunicado", "material didatico", "simulado"], "agente_escolar"),
    "pietraos":   (["pai", "responsavel", "aluno", "matricula", "meu filho", "minha filha", "reuniao"], "atendente_pietra"),
    "tecnico":    (["erro", "bug", "falha", "exception", "servidor", "deploy", "nao funciona", "travou"], "agente_tecnico"),
    "fabios":     (["megatron", "fabioos", "agente", "rag", "pipeline", "codigo", "sistema"], "megatron"),
}
ORDEM = ["seguranca", "spam", "saude", "juridico", "financeiro", "primus",
         "escolaos", "pietraos", "tecnico", "fabios"]  # prioridade (segurança 1º)

URG_CRITICA = ["ameaca", "violencia", "emergencia", "socorro", "urgentissimo", "agora mesmo"]
URG_ALTA = ["urgente", "hoje", "amanha", "prazo", "imediato", "o quanto antes"]
TAREFA_KW = ["prova", "produzir", "criar", "revisao", "gabarito", "comunicado", "elaborar", "preparar", "gerar"]
PERGUNTA_KW = ["?", "pode", "poderia", "como", "quando", "qual", "duvida"]


def classificar_intake(texto: str, source: str = "manual", sender: str = "",
                       subject: str = "") -> dict:
    base = _n(f"{subject} {texto} {sender}")

    # domínio (segurança e spam têm prioridade)
    dominio = "pessoal"
    agente = "megatron"
    for d in ORDEM:
        kws, ag = DOMINIOS[d]
        if any(k in base for k in kws):
            dominio, agente = d, ag
            break

    # sensibilidade (Core Spec §3)
    if dominio == "seguranca":
        sensibilidade = "forbidden_external"
    elif dominio in ("saude", "juridico"):
        sensibilidade = "restricted"
    elif dominio == "financeiro" or "inadimpl" in base:
        sensibilidade = "restricted" if "inadimpl" in base else "private"
    elif dominio in ("pietraos",):
        sensibilidade = "private"
    elif dominio == "spam":
        sensibilidade = "public"
    else:
        sensibilidade = "internal"

    # urgência
    if any(k in base for k in URG_CRITICA):
        urgencia = "critical"
    elif any(k in base for k in URG_ALTA):
        urgencia = "high"
    else:
        urgencia = "medium" if dominio not in ("spam",) else "none"

    # decisão: o que a entrada vira (Core Spec §5)
    if dominio == "spam":
        acao, requer = "descartar", False
    elif sensibilidade in ("restricted", "forbidden_external") or urgencia == "critical":
        acao, requer = "bloquear_e_escalar", True          # nunca age sozinho
    elif any(k in base for k in TAREFA_KW):
        acao, requer = "criar_tarefa", True
    elif any(k in base for k in PERGUNTA_KW):
        acao, requer = "preparar_resposta_sugerida", True
    else:
        acao, requer = "criar_nota", True

    alerta = urgencia in ("high", "critical") or sensibilidade in ("restricted", "forbidden_external")

    now = datetime.now()
    # id único (Core Spec §1: intake_<ts>_<hash>) — hash evita colisão no mesmo segundo
    _h = hashlib.sha1(f"{subject}{texto}{sender}{now.timestamp()}".encode()).hexdigest()[:6]

    return {
        "id": f"intake_{now.strftime('%Y%m%dT%H%M%S')}_{_h}",
        "source": source, "received_at": datetime.now().isoformat(timespec="seconds"),
        "sender": sender, "subject": subject,
        "summary": (texto or "")[:180],
        "domain": dominio, "sensitivity": sensibilidade, "urgency": urgencia,
        "suggested_agent": agente, "suggested_action": acao,
        "alerta": alerta, "requires_human_approval": requer,
        "rag_permitido": sensibilidade in ("public", "internal") and dominio != "spam",
        "status": "classified",
    }


def _render(c: dict) -> str:
    flags = []
    if c["alerta"]:
        flags.append("🔔 ALERTA")
    if not c["rag_permitido"]:
        flags.append("⛔ sem RAG")
    if c["requires_human_approval"]:
        flags.append("✋ aprovação humana")
    return ("┌── INTAKE (MEGATRON Core) ──\n"
            f"│ domínio: {c['domain']} · sensibilidade: {c['sensitivity']} · urgência: {c['urgency']}\n"
            f"│ agente: {c['suggested_agent']} · ação: {c['suggested_action']}\n"
            f"│ {' · '.join(flags) if flags else 'rotina'}\n"
            f"└── {c['id']} [status: {c['status']}]")


def main() -> int:
    ap = argparse.ArgumentParser(description="MEGATRON Core — classificador do Intake Universal")
    ap.add_argument("texto")
    ap.add_argument("--source", default="manual")
    ap.add_argument("--sender", default="")
    ap.add_argument("--subject", default="")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    c = classificar_intake(args.texto, args.source, args.sender, args.subject)
    print(json.dumps(c, ensure_ascii=False, indent=2) if args.json else _render(c))
    return 0


if __name__ == "__main__":
    sys.exit(main())
