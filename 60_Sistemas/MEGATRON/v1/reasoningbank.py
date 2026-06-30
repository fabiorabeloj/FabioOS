#!/usr/bin/env python3
"""
ReasoningBank-lite — memória de experiências do MEGATRON (FabioOS).

Padrão absorvido do ReasoningBank do ruflo, reimplementado local e governado
(SPEC `60_Sistemas/FabioOS/specs/2026-06-29_reasoningbank-lite-megatron.md`):
registra `experiência = {tarefa, abordagem, resultado, contexto, confianca}` num
JSONL append-only e recomenda a abordagem de maior sucesso, com decaimento
temporal. Sem API, sem banco externo. Sugere — nunca decide.

Append-only = à prova de colisão. Falhas também contam (puxam a abordagem p/ baixo).

Uso:
    python reasoningbank.py recomendar --tarefa commit
    python reasoningbank.py registrar --tarefa commit --abordagem "scan antes" --sucesso 1
"""
from pathlib import Path
from datetime import datetime
import argparse
import json
import math
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
STORE = Path(__file__).resolve().parent / "reasoningbank" / "experiencias.jsonl"
DECAY_POR_DIA = 0.005           # confiança decai ~0.5%/dia (meia-vida ~139 dias)
PENALIDADE_FALHA = -0.6         # falha reduz o placar da abordagem


def _r(tipo, ok, titulo, corpo="", sugestao="", fontes=None):
    """Contrato congelado Resultado (ver Ordens de Coordenação)."""
    return {"tipo": tipo, "ok": ok, "titulo": titulo, "corpo": corpo,
            "fontes": fontes or [{"source_path": STORE.relative_to(VAULT).as_posix(),
                                  "header_path": ""}],
            "sugestao": sugestao, "artefato": None}


def _ler_todas() -> list:
    if not STORE.exists():
        return []
    out = []
    for line in STORE.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return out


def _casa_tarefa(t_exp: str, t_alvo: str) -> bool:
    a, b = (t_exp or "").lower(), (t_alvo or "").lower()
    return a == b or b in a or a in b


def _idade_dias(ts: str) -> float:
    try:
        d = datetime.fromisoformat(ts)
        return max(0.0, (datetime.now() - d).total_seconds() / 86400.0)
    except Exception:
        return 0.0


def _peso(e: dict) -> float:
    conf = float(e.get("confianca", 0.5))
    decay = math.exp(-DECAY_POR_DIA * _idade_dias(e.get("ts", "")))
    sucesso = bool((e.get("resultado") or {}).get("success", False))
    sinal = 1.0 if sucesso else PENALIDADE_FALHA
    return conf * decay * sinal


def registrar(tarefa: str, abordagem: str, sucesso: bool,
              contexto: dict = None, confianca: float = 0.7, nota: str = "") -> dict:
    STORE.parent.mkdir(parents=True, exist_ok=True)
    exp = {"ts": datetime.now().isoformat(timespec="seconds"),
           "tarefa": tarefa, "abordagem": abordagem,
           "resultado": {"success": bool(sucesso), "nota": nota},
           "contexto": contexto or {}, "confianca": float(confianca)}
    with STORE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(exp, ensure_ascii=False) + "\n")
    return _r("sugestao", True, f"Experiência registrada: {tarefa}",
              corpo=f"{abordagem} → {'sucesso' if sucesso else 'falha'}")


def recomendar(tarefa: str, contexto: dict = None, min_evidencia: int = 1) -> dict:
    exps = [e for e in _ler_todas() if _casa_tarefa(e.get("tarefa", ""), tarefa)]
    if len(exps) < min_evidencia:
        return _r("abstencao", False, f"Sem experiência suficiente para '{tarefa}'",
                  corpo="Histórico fraco — alinhado à Ignorância Explícita do MEGATRON.")
    placar = {}
    for e in exps:
        placar[e["abordagem"]] = placar.get(e["abordagem"], 0.0) + _peso(e)
    ordenado = sorted(placar.items(), key=lambda kv: kv[1], reverse=True)
    melhor, score = ordenado[0]
    if score <= 0:
        return _r("abstencao", False, f"Nenhuma abordagem confiável para '{tarefa}'",
                  corpo="As experiências conhecidas falharam — não recomendo nenhuma ainda.")
    linhas = [f"- {ab}: {sc:+.2f}" for ab, sc in ordenado]
    corpo = (f"Recomendo **{melhor}** (placar {score:+.2f}, "
             f"{len(exps)} experiência(s)). Placar:\n" + "\n".join(linhas))
    return _r("sugestao", True, f"Estratégia recomendada para '{tarefa}'",
              corpo=corpo, sugestao=melhor)


def main() -> int:
    ap = argparse.ArgumentParser(description="ReasoningBank-lite MEGATRON")
    sub = ap.add_subparsers(dest="cmd", required=True)
    rc = sub.add_parser("recomendar")
    rc.add_argument("--tarefa", required=True)
    rg = sub.add_parser("registrar")
    rg.add_argument("--tarefa", required=True)
    rg.add_argument("--abordagem", required=True)
    rg.add_argument("--sucesso", type=int, default=1)
    rg.add_argument("--confianca", type=float, default=0.7)
    rg.add_argument("--nota", default="")
    args = ap.parse_args()
    if args.cmd == "registrar":
        r = registrar(args.tarefa, args.abordagem, bool(args.sucesso),
                      confianca=args.confianca, nota=args.nota)
    else:
        r = recomendar(args.tarefa)
    print(f"{'✅' if r['ok'] else '🤔'} {r['titulo']}\n{r['corpo']}")
    if r["sugestao"]:
        print(f"💡 {r['sugestao']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
