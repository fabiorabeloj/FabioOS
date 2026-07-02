#!/usr/bin/env python3
"""
Digest da Manhã — o ritual de 10 minutos do Fabio (plano 7 pontos, ponto 2).

O contrato: às 6h30 este digest está pronto. Ele traz NO MÁXIMO:
  · 5 linhas do que os agentes fizeram (barramento + git desde ontem)
  · decisões pendentes em LOTE com código curto (a, b, c...) e recomendação
  · fila "Aguardando Fabio" agrupada
  · 1 ação do dia
O Fabio responde tudo de uma vez no chat: `aprova a, c` · `nega b` · pronto.
Regra de ouro: se exigir mais de 10 min/dia dele, é bug do sistema.

Uso:
    python digest.py            # imprime o digest (e grava Digest_Hoje.md + mapa)
    python digest.py --quiet    # só grava (modo tarefa agendada 6h30)

Códigos: cada decisão ganha uma letra. O mapa letra→alvo fica em
state/digest_map.json e é consumido pela rota `aprova <letras>` do chat_bridge.
Sensível (restricted/forbidden) NUNCA entra em lote — aparece marcado, decisão individual.
"""
import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

BASE = Path(__file__).resolve().parent
VAULT = BASE.parents[2]
sys.path.insert(0, str(BASE))

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

from coordenacao import montar  # noqa: E402

QUEUE = BASE / "state" / "intake_queue.json"
MAPA = BASE / "state" / "digest_map.json"
SAIDA = VAULT / "10_Dashboard" / "Digest_Hoje.md"
DECISOES = VAULT / "50_Registros" / "Decisoes"
SENSIVEL = {"restricted", "forbidden_external", "no_rag"}


def _fila():
    if not QUEUE.exists():
        return []
    return [i for i in json.loads(QUEUE.read_text(encoding="utf-8")).get("fila", [])
            if i.get("status") == "waiting_approval"]


def _adrs_pendentes():
    out = []
    for f in sorted(DECISOES.glob("ADR_*.md")):
        try:
            head = f.read_text(encoding="utf-8")[:400]
        except Exception:
            continue
        if re.search(r"^status:\s*proposto-aguardando-ratificacao", head, re.M):
            titulo = f.stem.replace("ADR_", "").replace("_", " ")
            out.append({"path": str(f.relative_to(VAULT)).replace("\\", "/"), "titulo": titulo})
    return out


def _git_ontem():
    try:
        r = subprocess.run(
            ["git", "log", "--since=yesterday 06:00", "--format=%h %s"],
            cwd=VAULT, capture_output=True, text=True, encoding="utf-8", timeout=10)
        return [l for l in r.stdout.strip().splitlines() if l][:6]
    except Exception:
        return []


def montar_digest() -> tuple[str, dict]:
    e = montar()
    hoje = datetime.now()
    fila = _fila()
    adrs = _adrs_pendentes()
    commits = _git_ontem()

    # --- códigos curtos p/ decisão em lote ---
    mapa, letras = {}, "abcdefghijklmnopqrstuvwxyz"
    li = 0
    decisoes = []
    for i in fila:
        cod = letras[li]; li += 1
        sens = i["sensitivity"] in SENSIVEL
        mapa[cod] = {"tipo": "fila", "id": i["id"], "sensivel": sens}
        rec = "⛔ individual (sensível — não entra em lote)" if sens else (
            "recomendo APROVAR" if i["suggested_action"] in ("criar_tarefa", "criar_nota") else "avaliar")
        decisoes.append(f"**({cod})** [{i['domain']}/{i['urgency']}] {i['suggested_action']} — "
                        f"\"{(i.get('summary') or '')[:60]}\" · {rec}")
    for a in adrs:
        cod = letras[li]; li += 1
        mapa[cod] = {"tipo": "adr", "path": a["path"], "sensivel": False}
        decisoes.append(f"**({cod})** RATIFICAR ADR: {a['titulo'][:70]} · recomendo APROVAR (conteúdo bom; regra é sobre autoridade)")

    # --- 5 linhas do que rolou ---
    linhas_feito = []
    for m in e["atividade_recente"][-5:]:
        linhas_feito.append(f"- {m['ts'][5:16]} **{m['de']}→{m['para']}** [{m['tipo']}]: {m['mensagem'][:90]}")
    if commits:
        linhas_feito.append(f"- git: {len(commits)} commit(s) desde ontem — último: `{commits[0][:70]}`")

    # ação do dia: primeira prova real de Filosofia é o marco da semana (plano 7 pontos, dia 3)
    tem_prova_fil = any((VAULT / "60_Sistemas" / "Escola").rglob("*[Ff]ilosofia*prova*")) or \
                    any((VAULT / "60_Sistemas" / "Escola").rglob("*prova*[Ff]ilosofia*"))
    acao_do_dia = ("Ver Plano Mestre §5 — ordem da semana." if tem_prova_fil else
                   "Criar a PROVA REAL de Filosofia — peça na sessão do Claude: 'cria a prova de "
                   "Filosofia' (série+tema). Meta: <15 min do pedido ao DOCX. É o dia em que o "
                   "FabioOS te devolve tempo de verdade.")

    corpo = f"""---
tipo: digest
area: 10_Dashboard
projeto: FabioOS
gerado_em: {hoje.isoformat(timespec='seconds')}
tags: [fabios, digest, ritual-da-manha]
---

# ☀️ Digest — {hoje.strftime('%d/%m %H:%M')}

## O que os agentes fizeram (últimas 24h)
{chr(10).join(linhas_feito) or '- (silêncio no barramento)'}

## Decisões em lote — responda no chat: `aprova a, c` · `nega b`
{chr(10).join(decisoes) or '✅ Nada aguardando decisão. Dia limpo.'}

## Ação do dia
🎯 {acao_do_dia}

---
*Ritual: ≤10 min. Se passar disso, é bug do sistema — reporte.*
*Fila completa: `fila` no chat · Estado: `status` · [[60_Sistemas/FabioOS/Plano_Mestre_FabioOS_2026-07-01|Plano Mestre]]*
"""
    return corpo, mapa


def gerar(quiet: bool = False) -> str:
    corpo, mapa = montar_digest()
    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    SAIDA.write_text(corpo, encoding="utf-8")
    MAPA.write_text(json.dumps(mapa, ensure_ascii=False, indent=1), encoding="utf-8")
    if not quiet:
        print(corpo)
        print(f"[gravado: {SAIDA.relative_to(VAULT)} · mapa: {len(mapa)} código(s)]")
    return corpo


def main() -> int:
    ap = argparse.ArgumentParser(description="Digest da manhã — ritual de 10 min do Fabio")
    ap.add_argument("--quiet", action="store_true", help="só grava (tarefa agendada)")
    args = ap.parse_args()
    gerar(quiet=args.quiet)
    return 0


if __name__ == "__main__":
    sys.exit(main())
