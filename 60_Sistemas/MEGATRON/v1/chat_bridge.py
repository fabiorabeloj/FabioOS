#!/usr/bin/env python3
"""
Chat Bridge — dá OLHOS e MÃOS reais ao chat MEGATRON do Agentarium.

O chat do Agentarium (Cursor) responde via OpenRouter (LLM genérico) — conversa,
mas não enxerga o sistema. Esta ponte roteia PRIMEIRO as mensagens do Fabio para
o cérebro real (determinístico, custo-zero); só o que não for operacional cai no
LLM. É o nó que UNE os fios: chat ↔ coordenação ↔ fila ↔ barramento ↔ arquivista.

O backend chama:  python chat_bridge.py "<texto>"   → JSON {handled, reply, tipo}
  handled=true  → o chat responde com dado REAL do sistema
  handled=false → backend segue para o OpenRouter (conversa)

Comandos entendidos (determinísticos):
  "status" / "coordenacao" / "briefing"     → readout real (coordenacao.py)
  "fila" / "pendencias"                     → fila "Aguardando Fabio" com ids
  "aprova <id|dominio>"                     → arquivista grava nota (aprovação humana)
  "manda pro codex: <msg>" (cursor/todos)   → posta no barramento como de=fabio
  texto com cara de tarefa (prova/criar...) → vira pendência estruturada na fila

Segurança: mesmas travas de sempre — sensível não vira nota; segredo é redigido
pelo intake_flow; nada externo acontece por aqui.
"""
import argparse
import contextlib
import io
import json
import re
import sys
import unicodedata
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))
sys.path.insert(0, str(BASE.parents[1] / "FabioOS" / "scripts"))

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

from barramento import postar                      # noqa: E402
from coordenacao import montar                     # noqa: E402
from intake_flow import QUEUE_PATH, _log, processar  # noqa: E402
from megatron_core import classificar_intake       # noqa: E402

try:
    from intake_command_extract import extrair     # noqa: E402
except Exception:  # extractor é opcional
    extrair = None


def _n(s: str) -> str:
    return unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower().strip()


# --- rotas -------------------------------------------------------------------
RX_APROVA = re.compile(r"^aprovar?\s+(\S+)\s*$", re.IGNORECASE)
RX_RELAY = re.compile(
    r"^(?:manda|avisa|fala|diz|ordena|ordem)\s+(?:pr[oa]|para)\s*o?\s*"
    r"(codex|cursor|megatron|todos)\s*[:,;\-]?\s*(.+)$", re.IGNORECASE)
STATUS_KW = ("status", "coordenacao", "briefing", "quem esta", "quem ta", "velocidade",
             "andamento", "frentes", "resumo do sistema", "o que esta rolando", "o que ta rolando")
FILA_KW = ("fila", "pendencia", "pendencias", "aguardando")


def rota_status() -> str:
    e = montar()
    L = [f"📡 Coordenação · {e['gerado_em'][11:16]}"]
    if e["velocidade"]:
        vel = " · ".join(f"{ag} {ts[5:16]}" for ag, ts in
                         sorted(e["velocidade"].items(), key=lambda kv: kv[1], reverse=True))
        L.append(f"Última atividade: {vel}")
    ag = e["fila_aguardando_fabio"]
    L.append(f"Fila aguardando você: {len(ag)}" + (
        " — " + "; ".join(f"{i['domain']}/{i['urgency']}→{i['action']}" for i in ag[:4]) if ag else ""))
    if e["atividade_recente"]:
        m = e["atividade_recente"][-1]
        L.append(f"Último evento: {m['ts'][11:16]} [{m['tipo']}] {m['de']}→{m['para']}: {m['mensagem'][:70]}")
    L.append(f"Frentes ativas: {len(e['frentes_ativas'])}")
    return "\n".join(L)


def rota_fila() -> str:
    if not QUEUE_PATH.exists():
        return "Fila vazia (nenhum intake ainda)."
    fila = json.loads(QUEUE_PATH.read_text(encoding="utf-8")).get("fila", [])
    pend = [i for i in fila if i["status"] == "waiting_approval"]
    if not pend:
        return "✅ Fila limpa — nada aguardando aprovação."
    L = [f"📥 Aguardando você: {len(pend)}"]
    for i in pend:
        trava = " ⛔sensível" if i["sensitivity"] in ("restricted", "forbidden_external", "no_rag") else ""
        L.append(f"• {i['domain']}/{i['urgency']} → {i['suggested_action']}{trava}\n"
                 f"  \"{i['summary'][:60]}\" · aprova {i['id']}")
    return "\n".join(L)


def rota_aprovar(alvo: str) -> str:
    from arquivista_intake import _carregar, aprovar
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
        try:
            aprovar(_carregar(), alvo)
        except SystemExit:
            pass
    return buf.getvalue().strip() or f"Nada a aprovar com '{alvo}'."


def rota_relay(destino: str, msg: str) -> str:
    postar(de="fabio", para=destino.lower(), tipo="ordem", mensagem=msg)
    return (f"📨 Enviado ao barramento → {destino.lower()}: \"{msg[:80]}\"\n"
            f"(agentes leem na retomada; Cursor vê pela UI)")


def rota_tarefa(texto: str) -> str | None:
    """Texto com cara de tarefa vira pendência estruturada na fila (aguarda aprovação)."""
    c = classificar_intake(texto, source="chat", sender="fabio")
    if c["suggested_action"] not in ("criar_tarefa",):
        return None  # não é tarefa → deixa o LLM conversar
    item = processar({"source": "chat", "sender": "fabio", "subject": "", "texto": texto})
    if extrair:
        ext = {k: v for k, v in (extrair(texto) or {}).items() if v}
        if ext.get("confianca", 0) and len(ext) > 1:
            item["extracao"] = ext
    # anexa na fila viva (não regenera; preserva o que já existe)
    if QUEUE_PATH.exists():
        saida = json.loads(QUEUE_PATH.read_text(encoding="utf-8"))
    else:
        saida = {"contrato": "MEGATRON Core Spec v0.1", "cores_status": {}, "resumo": {}, "fila": []}
    saida["fila"].append(item)
    pend = [i for i in saida["fila"] if i["status"] == "waiting_approval"]
    saida["resumo"] = {"total": len(saida["fila"]), "aguardando_fabio": len(pend),
                       "sensiveis": sum(1 for i in saida["fila"] if i["sensitivity"] in
                                        ("private", "restricted", "forbidden_external"))}
    QUEUE_PATH.write_text(json.dumps(saida, ensure_ascii=False, indent=2), encoding="utf-8")
    _log(item)
    ext = item.get("extracao") or {}
    chips = " · ".join(f"{k}={v}" for k, v in ext.items() if k != "confianca") or "—"
    return (f"📥 Virou pendência ({item['domain']}/{item['urgency']}): {item['summary'][:70]}\n"
            f"Extração: {chips}\n"
            f"Aguardando sua aprovação → responda: aprova {item['id']}")


def rotear(texto: str) -> dict:
    t = _n(texto)

    m = RX_APROVA.match(texto.strip())
    if m:
        return {"handled": True, "tipo": "aprovacao", "reply": rota_aprovar(m.group(1))}

    m = RX_RELAY.match(texto.strip())
    if m:
        return {"handled": True, "tipo": "barramento", "reply": rota_relay(m.group(1), m.group(2))}

    if any(k in t for k in STATUS_KW):
        return {"handled": True, "tipo": "status", "reply": rota_status()}

    if any(t.startswith(k) or t == k for k in FILA_KW):
        return {"handled": True, "tipo": "fila", "reply": rota_fila()}

    r = rota_tarefa(texto)
    if r:
        return {"handled": True, "tipo": "tarefa", "reply": r}

    return {"handled": False, "tipo": "conversa", "reply": ""}


def main() -> int:
    ap = argparse.ArgumentParser(description="Ponte chat Agentarium → cérebro MEGATRON")
    ap.add_argument("texto")
    args = ap.parse_args()
    print(json.dumps(rotear(args.texto), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
