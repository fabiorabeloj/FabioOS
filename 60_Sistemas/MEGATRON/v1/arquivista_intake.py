#!/usr/bin/env python3
"""
Arquivista do Intake — o ELO FINAL do Intake Universal (Core Spec §6/§9).

Fecha o critério de sucesso do Fabio:
    ... → fila → APROVAÇÃO HUMANA → log → SAÍDA PARA OBSIDIAN → continuidade

É o único ponto que grava no vault, e só sob aprovação humana EXPLÍCITA (`--aprovar`).
Respeita a trava (Core Spec §3): sensibilidade `restricted`/`forbidden_external`
NUNCA vira nota automática — é apenas escalada ao humano (nada sensível toca o Obsidian).
`private` vai para pasta restrita (gitignored). `internal`/`public` viram nota versionada.

Uso:
    python arquivista_intake.py                       # lista a fila "Aguardando Fabio"
    python arquivista_intake.py --aprovar <id|dominio># aprova 1 item → grava nota + log
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
VAULT = BASE.parents[2]                       # .../FabioOs (raiz do vault)
QUEUE = BASE / "state" / "intake_queue.json"
LOG = BASE / "state" / "intake_log.jsonl"
TRIAGEM = VAULT / "00_Inbox" / "Triagem"
RESTRITO = TRIAGEM / "_restrito"              # gitignored

# sensibilidade que NUNCA vira nota automática (só escala ao humano)
NAO_GRAVA = {"restricted", "forbidden_external", "no_rag"}


def _slug(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "_", s).strip("_").lower()
    return (s or "intake")[:48]


def _carregar() -> dict:
    if not QUEUE.exists():
        print(f"⛔ Fila não existe: {QUEUE}\n   Rode antes: python intake_flow.py", file=sys.stderr)
        sys.exit(1)
    return json.loads(QUEUE.read_text(encoding="utf-8"))


def _log(item: dict, resultado: str, onde: str) -> None:
    linha = {
        "ts": datetime.now().isoformat(timespec="seconds"),
        "quem": "arquivista_intake (aprovado por Fabio)",
        "o_que": f"{resultado} {item['id']} ({item['domain']}/{item['sensitivity']})",
        "onde": onde,
        "proximo": "item na memória operacional; retomável",
    }
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(linha, ensure_ascii=False) + "\n")


def _escrever_nota(item: dict) -> Path:
    """Grava a nota/tarefa no Obsidian conforme domínio e sensibilidade."""
    is_tarefa = item["suggested_action"] == "criar_tarefa"
    tipo = "tarefa" if is_tarefa else "nota"
    destino = RESTRITO if item["sensitivity"] == "private" else TRIAGEM
    destino.mkdir(parents=True, exist_ok=True)

    titulo = (item.get("subject") or item.get("summary") or item["domain"]).strip()
    nome = f"{datetime.now():%Y-%m-%d}_{item['domain']}_{_slug(titulo)}.md"
    caminho = destino / nome

    linha_acao = (f"- [ ] {item['suggested_action']} — {item['summary']}"
                  if is_tarefa else item["summary"])

    ext = item.get("extracao") or {}
    bloco_extracao = ""
    if any(ext.get(k) for k in ("produto", "serie", "tema", "prazo")):
        linhas = []
        for chave, rotulo in (("produto", "Produto"), ("serie", "Serie"), ("tema", "Tema"), ("prazo", "Prazo")):
            if ext.get(chave):
                linhas.append(f"- {rotulo}: {ext[chave]}")
        bloco_extracao = "\n## Extracao estruturada\n\n" + "\n".join(linhas) + "\n"

    corpo = f"""---
tipo: {tipo}
area: 00_Inbox
projeto: FabioOS
origem_intake: {item['id']}
fonte: {item['source']}
dominio: {item['domain']}
sensibilidade: {item['sensitivity']}
urgencia: {item['urgency']}
agente_sugerido: {item['suggested_agent']}
status: aguardando-execucao
aprovado_em: {datetime.now().isoformat(timespec='seconds')}
tags: [fabios, intake, {item['domain']}]
---

# {titulo}

> Gerado pelo Intake Universal e **aprovado por Fabio**. Origem: `{item['id']}` ({item['source']}).

## Pendência

{linha_acao}
{bloco_extracao}
## Contexto

- Remetente: {item.get('sender') or '—'}
- Domínio: {item['domain']} · sensibilidade: {item['sensitivity']} · urgência: {item['urgency']}
- Agente sugerido: {item['suggested_agent']}

## Continuidade

- Log: `60_Sistemas/MEGATRON/v1/state/{LOG.name}`
- Corpo bruto (se houver): `{item.get('raw_content_ref', '—')}`
"""
    caminho.write_text(corpo, encoding="utf-8")
    return caminho


def listar(saida: dict) -> int:
    pend = [i for i in saida["fila"] if i["status"] == "waiting_approval"]
    print(f"┌── FILA \"Aguardando Fabio\" ── {len(pend)} pendência(s)")
    for i in pend:
        trava = "  ⛔ sensível: só escala, não vira nota" if i["sensitivity"] in NAO_GRAVA else ""
        print(f"│ {i['id']}")
        print(f"│   {i['domain']}/{i['sensitivity']}/{i['urgency']} → {i['suggested_action']}{trava}")
        print(f"│   \"{i['summary'][:70]}\"")
    print("└── aprovar: python arquivista_intake.py --aprovar <id|dominio>")
    return 0


def aprovar(saida: dict, alvo: str) -> int:
    fila = saida["fila"]
    item = next((i for i in fila if i["id"] == alvo and i["status"] == "waiting_approval"), None)
    if item is None and len(alvo) >= 6:  # sufixo do id (como o chat sugere: "aprova fff2a9")
        cand = [i for i in fila if i["id"].endswith(alvo) and i["status"] == "waiting_approval"]
        item = cand[0] if len(cand) == 1 else None
    if item is None:  # tenta por domínio
        item = next((i for i in fila if i["domain"] == alvo and i["status"] == "waiting_approval"), None)
    if item is None:
        print(f"⛔ Nenhum item 'waiting_approval' com id/domínio = {alvo!r}.", file=sys.stderr)
        return 1

    # TRAVA §3: sensível não vira nota — só escala ao humano
    if item["sensitivity"] in NAO_GRAVA:
        item["status"] = "blocked"
        _log(item, "ESCALADO (sensível, não gravado)", "—")
        QUEUE.write_text(json.dumps(saida, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"⛔ {item['id']} é {item['sensitivity']} → NÃO virou nota (trava §3).")
        print("   Escalado ao humano; nada sensível tocou o Obsidian. Status: blocked.")
        return 0

    caminho = _escrever_nota(item)
    item["status"] = "executed"
    item["nota_ref"] = str(caminho.relative_to(VAULT)).replace("\\", "/")
    rel = item["nota_ref"]
    _log(item, "GRAVOU nota no Obsidian", rel)
    QUEUE.write_text(json.dumps(saida, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"✅ Aprovado e gravado no Obsidian: {rel}")
    print(f"   {item['domain']}/{item['sensitivity']} · status → executed · log atualizado.")
    print("   Ciclo FECHADO: entrada → classificação → aprovação → log → Obsidian.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Arquivista do Intake — aprovação humana → Obsidian")
    ap.add_argument("--aprovar", metavar="ID|DOMINIO", help="aprova 1 item e grava a nota")
    ap.add_argument("--fila", type=Path, help="fila alternativa (default: state/intake_queue.json). "
                    "Use p/ provas isoladas, evitando colisão com a fila viva compartilhada.")
    args = ap.parse_args()
    if args.fila:
        global QUEUE
        QUEUE = args.fila.resolve()
    saida = _carregar()
    return aprovar(saida, args.aprovar) if args.aprovar else listar(saida)


if __name__ == "__main__":
    sys.exit(main())
