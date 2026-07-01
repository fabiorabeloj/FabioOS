#!/usr/bin/env python3
"""
PietraOS — Inbox Operacional (vertical Escola). MOTOR multi-tenant.

Processa uma mensagem (texto/foto/PDF/áudio) e devolve um CARTÃO DE ATENDIMENTO:
classifica a demanda, define o risco, roteia ao setor, sugere resposta (quando o
risco permite) e registra. **Risco alto/crítico NUNCA responde sozinho** — bloqueia
e escala. Config-driven (a vertical é dados, não código) e multi-tenant (cada escola
é um tenant com dados isolados). Sem LLM — custo zero.

Uso:
    python pietra_inbox.py "Segue o atestado do meu filho" --tenant colegio-pietra
    python pietra_inbox.py "Quero matricular meu filho" --tenant colegio-pietra --confirmar
    python pietra_inbox.py relatorio --tenant colegio-pietra
"""
import argparse
import json
import re
import sys
import unicodedata
from datetime import datetime
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE = Path(__file__).resolve().parent
VERTICAL = "escola"
CONFIG_PATH = BASE / "verticais" / VERTICAL / "config.json"


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return s.lower()


def carregar_config() -> dict:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def config_para_tenant(tenant: str):
    """Config da vertical + overrides do tenant (tenants/<tenant>/tenant.json,
    gitignored). É AQUI que as respostas do formulário da coordenação viram sistema:
    escola_nome, setores (roteamento), tom e assinatura. Devolve (cfg, escola_nome)."""
    cfg = carregar_config()
    ov = {}
    p = BASE / "tenants" / tenant / "tenant.json"
    if p.exists():
        try:
            ov = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            ov = {}
    escola = ov.get("escola_nome") or tenant.replace("-", " ").title()
    for cat, setor in (ov.get("setores") or {}).items():
        if cat in cfg["categorias"] and setor:
            cfg["categorias"][cat]["setor"] = setor
    if ov.get("tom"):
        cfg["persona"]["tom"] = ov["tom"]
    if ov.get("assinatura"):
        cfg["persona"]["assinatura"] = ov["assinatura"]
    if ov.get("prioridade_sensivel"):
        for cat in ("sensivel", "saude", "reclamacao"):
            if cat in cfg["categorias"]:
                cfg["categorias"][cat]["setor"] = ov["prioridade_sensivel"]
    return cfg, escola


def classificar(texto: str, cfg: dict) -> str:
    """Pontua a mensagem contra as keywords de cada categoria. Sensível/crítico
    tem prioridade (ganha empate) para nunca vazar um caso grave como FAQ."""
    base = _norm(texto)
    placar = {}
    for cat, d in cfg["categorias"].items():
        placar[cat] = sum(base.count(_norm(k)) for k in d["keywords"])
    # prioridade de segurança: se houver qualquer sinal sensível/saúde, sobe
    for grave in ("sensivel", "saude"):
        if placar.get(grave, 0) > 0:
            return grave
    melhor = max(placar, key=placar.get)
    return melhor if placar[melhor] > 0 else cfg.get("categoria_padrao", "faq")


def _assunto(texto: str) -> str:
    t = re.sub(r"\s+", " ", texto).strip()
    return (t[:50] + "…") if len(t) > 50 else t


def processar(texto: str, tenant: str = "demo", remetente: str = "desconhecido",
              midia: str = "texto", confirmar: bool = False) -> dict:
    cfg = carregar_config()
    cat = classificar(texto, cfg)
    d = cfg["categorias"][cat]
    risco = d["risco"]
    regra = cfg["risco_regras"][risco]

    bloqueado = regra["bloqueia"]
    if d.get("template") and not bloqueado:
        resposta = d["template"].replace("{assunto}", _assunto(texto))
    else:
        resposta = None
    if regra["responde_auto"]:
        acao = "responder_auto"
    elif regra["escala"]:
        acao = "bloquear_escalar"
    elif bloqueado:
        acao = "bloquear_humano"
    else:
        acao = "sugerir_aprovar"

    prioridade = {"baixo": "baixa", "medio": "media", "alto": "alta", "critico": "critica"}[risco]
    cartao = {
        "id": f"atd-{datetime.now().strftime('%Y%m%dT%H%M%S')}-{tenant}",
        "tenant": tenant, "vertical": VERTICAL,
        "ts": datetime.now().isoformat(timespec="seconds"),
        "remetente": remetente, "midia": midia,
        "categoria": cat, "setor": d["setor"], "risco": risco,
        "prioridade": prioridade, "acao": acao, "bloqueado": bloqueado,
        "resposta_sugerida": resposta,
        "texto": texto[:500],
    }
    if confirmar:
        _registrar(cartao)
    return cartao


def _tenant_dir(tenant: str) -> Path:
    return BASE / "tenants" / tenant


def _registrar(cartao: dict) -> None:
    d = _tenant_dir(cartao["tenant"])
    d.mkdir(parents=True, exist_ok=True)
    with (d / "atendimentos.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(cartao, ensure_ascii=False) + "\n")


def relatorio(tenant: str, dias: int = 7) -> dict:
    f = _tenant_dir(tenant) / "atendimentos.jsonl"
    if not f.exists():
        return {"tenant": tenant, "total": 0, "msg": "Sem atendimentos registrados."}
    itens = [json.loads(l) for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]
    por_cat, por_setor, sensiveis, pendentes = {}, {}, 0, 0
    for it in itens:
        por_cat[it["categoria"]] = por_cat.get(it["categoria"], 0) + 1
        por_setor[it["setor"]] = por_setor.get(it["setor"], 0) + 1
        if it["risco"] in ("alto", "critico"):
            sensiveis += 1
        if it["acao"] != "responder_auto":
            pendentes += 1
    top = lambda d: sorted(d.items(), key=lambda kv: kv[1], reverse=True)
    return {
        "tenant": tenant, "total": len(itens),
        "por_categoria": top(por_cat), "setor_mais_acionado": top(por_setor)[0] if por_setor else None,
        "casos_sensiveis": sensiveis, "pendentes_aprovacao": pendentes,
    }


def _render_cartao(c: dict) -> str:
    L = ["┌── CARTÃO DE ATENDIMENTO ──",
         f"│ Categoria: {c['categoria']}   Setor: {c['setor']}",
         f"│ Risco: {c['risco'].upper()}   Prioridade: {c['prioridade']}   Ação: {c['acao']}"]
    if c["bloqueado"]:
        L.append("│ 🛑 SENSÍVEL — não responder automaticamente; escalar humano.")
    if c["resposta_sugerida"]:
        L.append(f"│ Sugestão: \"{c['resposta_sugerida']}\"")
    else:
        L.append("│ Sugestão: (nenhuma — requer humano)")
    L.append(f"└── {c['id']}")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description="PietraOS Inbox Operacional (escola)")
    ap.add_argument("texto", help="mensagem OU 'relatorio'")
    ap.add_argument("--tenant", default="colegio-pietra")
    ap.add_argument("--remetente", default="desconhecido")
    ap.add_argument("--midia", default="texto")
    ap.add_argument("--confirmar", action="store_true", help="registra o atendimento")
    args = ap.parse_args()
    if args.texto == "relatorio":
        r = relatorio(args.tenant)
        print(f"📊 Relatório — {args.tenant}: {r['total']} atendimentos")
        if r["total"]:
            print("  Por categoria:", r["por_categoria"])
            print("  Setor mais acionado:", r["setor_mais_acionado"])
            print(f"  Casos sensíveis: {r['casos_sensiveis']} | Pendentes de aprovação: {r['pendentes_aprovacao']}")
        return 0
    print(_render_cartao(processar(args.texto, args.tenant, args.remetente,
                                   args.midia, args.confirmar)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
