#!/usr/bin/env python3
"""
PietraOS — Motor de CONVERSAÇÃO (padrão enterprise). Vertical Escola, multi-tenant.

Diferente de um classificador de mensagem única, este é um chatbot de verdade:
  • Sessão por (tenant, remetente) — conversa multi-turno com estado.
  • Persona + saudação na primeira mensagem.
  • Slot-filling — coleta os dados que faltam (ex.: "para qual aluno?").
  • Confiança + fallback — se não entende, oferece menu; após 2 falhas, chama atendente.
  • Risco: sensível/crítico NUNCA responde sozinho — handoff humano com contexto.
  • Encerramento cordial + registro (cartão de atendimento).
Sem LLM — custo zero, determinístico, auditável. (A qualidade da classificação sobe
com LLM local quando houver GPU — ver MEGATRON --llm.)

Uso:
    python pietra_conversa.py "Preciso do historico" --tenant colegio-pietra --de 5511999
    (chame de novo com o mesmo --de para continuar a conversa)
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
sys.path.insert(0, str(BASE))
from pietra_inbox import carregar_config, config_para_tenant, _norm, _assunto  # noqa: E402

MAX_FALLBACK = 2


def _display_escola(tenant: str) -> str:
    return tenant.replace("-", " ").title()


def _classificar_score(texto: str, cfg: dict):
    base = _norm(texto)
    placar = {c: sum(base.count(_norm(k)) for k in d["keywords"])
              for c, d in cfg["categorias"].items()}
    for grave in ("sensivel", "saude"):          # prioridade de segurança
        if placar.get(grave, 0) > 0:
            return grave, placar[grave]
    melhor = max(placar, key=placar.get)
    return melhor, placar[melhor]


def _sess_path(tenant: str, remetente: str) -> Path:
    safe = re.sub(r"[^0-9a-zA-Z]+", "_", remetente)
    return BASE / "tenants" / tenant / "sessions" / f"{safe}.json"


def _load(tenant: str, remetente: str):
    p = _sess_path(tenant, remetente)
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8")), False
    return {"tenant": tenant, "remetente": remetente, "categoria": None,
            "slots": {}, "aguardando_slot": None, "fallback": 0, "estado": "novo",
            "primeiro_texto": None, "historico": [],
            "criado": datetime.now().isoformat(timespec="seconds")}, True


def _save(sess: dict):
    sess["atualizado"] = datetime.now().isoformat(timespec="seconds")
    p = _sess_path(sess["tenant"], sess["remetente"])
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(sess, ensure_ascii=False, indent=2), encoding="utf-8")


def _preencher(template: str, sess: dict, texto: str) -> str:
    out = template.replace("{assunto}", _assunto(sess.get("primeiro_texto") or texto))
    for k, v in sess["slots"].items():
        out = out.replace("{" + k + "}", v)
    return re.sub(r"\{[^}]+\}", "", out).strip()          # limpa slots não usados


def _cartao(sess: dict, cfg: dict, texto: str, bloqueado: bool) -> dict:
    cat = sess["categoria"]
    d = cfg["categorias"][cat]
    risco = d["risco"]
    resposta = None if (bloqueado or not d.get("template")) else _preencher(d["template"], sess, texto)
    return {
        "id": f"atd-{datetime.now().strftime('%Y%m%dT%H%M%S')}-{sess['tenant']}",
        "tenant": sess["tenant"], "remetente": sess["remetente"], "vertical": "escola",
        "ts": datetime.now().isoformat(timespec="seconds"),
        "categoria": cat, "setor": d["setor"], "risco": risco,
        "prioridade": {"baixo": "baixa", "medio": "media", "alto": "alta", "critico": "critica"}[risco],
        "bloqueado": bloqueado,
        "acao": "bloquear_escalar" if cfg["risco_regras"][risco]["escala"]
                else ("bloquear_humano" if bloqueado
                      else ("responder_auto" if cfg["risco_regras"][risco]["responde_auto"]
                            else "sugerir_aprovar")),
        "resposta_sugerida": resposta, "slots": dict(sess["slots"]),
        "texto": (sess.get("primeiro_texto") or texto)[:500],
    }


def _registrar_cartao(cartao: dict):
    d = BASE / "tenants" / cartao["tenant"]
    d.mkdir(parents=True, exist_ok=True)
    with (d / "atendimentos.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(cartao, ensure_ascii=False) + "\n")


def conversar(tenant: str, remetente: str, texto: str, dentro_horario: bool = True) -> dict:
    cfg, escola = config_para_tenant(tenant)      # config da vertical + overrides do tenant
    persona = cfg["persona"]
    sess, nova = _load(tenant, remetente)
    sess["historico"].append({"de": "user", "txt": texto})
    if sess["primeiro_texto"] is None:
        sess["primeiro_texto"] = texto
    respostas = []

    if nova:
        respostas.append(persona["saudacao"].replace("{escola}", escola))
        if not dentro_horario:
            respostas.append(persona["fora_horario"].replace(
                "{horario}", persona["horario_atendimento"]))

    # 1) preenchendo um slot pedido
    if sess["aguardando_slot"]:
        sess["slots"][sess["aguardando_slot"]] = texto.strip()
        sess["aguardando_slot"] = None
    # 2) ainda sem categoria -> classifica
    elif not sess["categoria"]:
        cat, score = _classificar_score(texto, cfg)
        if score == 0:
            sess["fallback"] += 1
            if sess["fallback"] >= MAX_FALLBACK:
                sess["categoria"] = "reuniao"      # cai p/ atendente humano
                respostas.append("Vou te conectar com um atendente. 🙂")
            else:
                respostas.append(persona["fallback"])
                sess["estado"] = "clarificar"
                _save(sess)
                return {"respostas": respostas, "estado": sess["estado"], "cartao": None}
        else:
            sess["categoria"] = cat

    cat = sess["categoria"]
    d = cfg["categorias"][cat]
    risco = d["risco"]
    bloqueado = cfg["risco_regras"][risco]["bloqueia"]

    # 3) risco sensível -> handoff imediato, sem coletar slots
    if bloqueado:
        cartao = _cartao(sess, cfg, texto, bloqueado=True)
        respostas.append(persona["handoff"].replace("{setor}", d["setor"]))
        sess["estado"] = "escalado"
        _registrar_cartao(cartao)
        _save(sess)
        return {"respostas": respostas, "estado": sess["estado"], "cartao": cartao}

    # 4) slot-filling
    faltam = [s for s in d.get("slots", []) if s["nome"] not in sess["slots"]]
    if faltam:
        prox = faltam[0]
        sess["aguardando_slot"] = prox["nome"]
        sess["estado"] = "coletando"
        respostas.append(prox["pergunta"])
        _save(sess)
        return {"respostas": respostas, "estado": sess["estado"], "cartao": None}

    # 5) resolvido
    cartao = _cartao(sess, cfg, texto, bloqueado=False)
    if cartao["resposta_sugerida"]:
        respostas.append(cartao["resposta_sugerida"])
    respostas.append(persona["encerramento"].replace("{setor}", d["setor"]))
    sess["estado"] = "resolvido"
    _registrar_cartao(cartao)
    _save(sess)
    return {"respostas": respostas, "estado": sess["estado"], "cartao": cartao}


def main() -> int:
    ap = argparse.ArgumentParser(description="PietraOS — motor de conversação (escola)")
    ap.add_argument("texto")
    ap.add_argument("--tenant", default="colegio-pietra")
    ap.add_argument("--de", default="5511900000000", help="número/ID do remetente (sessão)")
    ap.add_argument("--fora-horario", action="store_true")
    args = ap.parse_args()
    r = conversar(args.tenant, args.de, args.texto, dentro_horario=not args.fora_horario)
    for msg in r["respostas"]:
        print(f"🤖 {msg}")
    print(f"   [estado: {r['estado']}"
          + (f" · cartão: {r['cartao']['categoria']}/{r['cartao']['risco']}/{r['cartao']['acao']}"
             if r["cartao"] else "") + "]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
