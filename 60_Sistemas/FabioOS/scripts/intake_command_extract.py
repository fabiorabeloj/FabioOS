#!/usr/bin/env python3
"""
Extrator determinístico de comando natural — Intake Universal (FabioOS).

Extrai série, tema, prazo e produto de texto livre (comando ou e-mail)
sem LLM. Usado pelo Agentarium na mesa de despacho antes de gravar na fila.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from typing import Any


def _norm(text: str) -> str:
    t = unicodedata.normalize("NFKD", text or "")
    t = t.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"\s+", " ", t).strip()


PRODUTO_RX = [
    (re.compile(r"\b(prova|avaliacao|teste)\b", re.I), "prova"),
    (re.compile(r"\b(revisao|revisar|retomada)\b", re.I), "revisao"),
    (re.compile(r"\b(atividade|exercicio|lista)\b", re.I), "atividade"),
    (re.compile(r"\b(planejamento|plano de aula|aula)\b", re.I), "planejamento"),
    (re.compile(r"\b(gabarito|correcao)\b", re.I), "gabarito"),
    (re.compile(r"\b(redacao|dissertacao|texto dissertativo)\b", re.I), "redacao"),
    (re.compile(r"\b(slide|apresentacao|ppt)\b", re.I), "apresentacao"),
]

SERIE_RX = [
    re.compile(r"\b(\d{1,2})\s*[oº°]?\s*ano\b", re.I),
    re.compile(r"\b(\d{1,2})\s*[aª]?\s*serie\b", re.I),
    re.compile(r"\b(oitavo|nono|setimo|sexto|quinto|quarto|terceiro|segundo|primeiro)\s+ano\b", re.I),
    re.compile(r"\b(ensino\s+medio|em\b|fundamental\s+[12])\b", re.I),
]

TEMA_RX = [
    re.compile(r"\bsobre\s+([A-Za-zÀ-ÿ0-9][A-Za-zÀ-ÿ0-9\s\-]{1,60}?)(?:\s+(?:para|ate|até|amanha|hoje|urgente|ate\b)|[,.]|$)", re.I),
    re.compile(r"\btema\s+([A-Za-zÀ-ÿ0-9][A-Za-zÀ-ÿ0-9\s\-]{1,60}?)(?:\s+(?:para|ate|até|amanha|hoje)|[,.]|$)", re.I),
    re.compile(r"\bde\s+([A-Za-zÀ-ÿ]{3,40}?)\s+(?:para|ate|até|amanha|hoje)\b", re.I),
]

PRAZO_RX = [
    (re.compile(r"\b(amanha|hoje|depois de amanha)\b", re.I), lambda m: m.group(1).lower()),
    (re.compile(r"\bate\s+(segunda|terca|quarta|quinta|sexta|sabado|domingo)\b", re.I), lambda m: f"ate {m.group(1).lower()}"),
    (re.compile(r"\bprazo\s+(\d{1,2}/\d{1,2}(?:/\d{2,4})?)\b", re.I), lambda m: f"prazo {m.group(1)}"),
    (re.compile(r"\b(\d{1,2}/\d{1,2}(?:/\d{2,4})?)\b"), lambda m: m.group(1)),
    (re.compile(r"\b(urgente|imediato)\b", re.I), lambda m: m.group(1).lower()),
]


def _pick_produto(text: str) -> str | None:
    for rx, label in PRODUTO_RX:
        if rx.search(text):
            return label
    return None


def _pick_serie(text: str) -> str | None:
    for rx in SERIE_RX:
        m = rx.search(text)
        if not m:
            continue
        g = m.group(0).strip()
        if re.match(r"^\d", g):
            num = re.search(r"\d+", g)
            if num:
                return f"{num.group()}o ano"
        return g.lower()
    return None


def _pick_tema(text: str) -> str | None:
    for rx in TEMA_RX:
        m = rx.search(text)
        if m:
            tema = m.group(1).strip(" .,-")
            if len(tema) >= 3:
                return tema[:80]
    return None


def _pick_prazo(text: str) -> str | None:
    for rx, fmt in PRAZO_RX:
        m = rx.search(text)
        if m:
            return fmt(m)
    return None


def extrair(texto: str) -> dict[str, Any]:
    raw = (texto or "").strip()
    if not raw:
        return {"serie": None, "tema": None, "prazo": None, "produto": None, "confianca": 0.0}

    produto = _pick_produto(raw)
    serie = _pick_serie(raw)
    tema = _pick_tema(raw)
    prazo = _pick_prazo(raw)

    hits = sum(1 for v in (produto, serie, tema, prazo) if v)
    confianca = round(min(1.0, hits * 0.25 + (0.1 if len(_norm(raw)) > 20 else 0)), 2)

    return {
        "serie": serie,
        "tema": tema,
        "prazo": prazo,
        "produto": produto,
        "confianca": confianca,
    }


def enriquecer_summary(summary: str, ext: dict[str, Any]) -> str:
    parts: list[str] = []
    if ext.get("produto"):
        parts.append(str(ext["produto"]).capitalize())
    if ext.get("serie"):
        parts.append(str(ext["serie"]))
    if ext.get("tema"):
        parts.append(f"sobre {ext['tema']}")
    if ext.get("prazo"):
        parts.append(f"({ext['prazo']})")

    if not parts:
        return summary

    structured = " ".join(parts)
    base = (summary or "").strip()
    if structured.lower() in base.lower():
        return base
    if base:
        return f"{structured} - {base}"
    return structured


def montar_subject(ext: dict[str, Any], fallback: str = "") -> str:
    if ext.get("produto") and ext.get("serie"):
        subj = f"{ext['produto'].capitalize()} {ext['serie']}"
        if ext.get("tema"):
            subj += f" - {ext['tema']}"
        return subj
    return fallback


def texto_de_payload(raw: str) -> str:
    raw = (raw or "").strip()
    if not raw:
        return ""
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return raw

    if isinstance(data, dict):
        for key in ("text", "texto", "command", "comando", "content", "snippet", "body"):
            if data.get(key):
                return str(data[key])
        if isinstance(data.get("items"), list) and data["items"]:
            return texto_de_payload(json.dumps(data["items"][0], ensure_ascii=False))
    return raw


def main() -> int:
    parser = argparse.ArgumentParser(description="Extrai serie/tema/prazo/produto de comando natural.")
    parser.add_argument("--text", help="Texto do comando ou e-mail.")
    parser.add_argument("--self-test", action="store_true", help="Roda casos de teste internos.")
    args = parser.parse_args()

    if args.self_test:
        casos = [
            ("prova do 8o ano sobre Africa para amanha", "prova", "8o ano", "Africa", "amanha"),
            ("revisao 9 ano tema Revolucao Francesa ate sexta", "revisao", "9o ano", "Revolucao Francesa", "ate sexta"),
            ("lista de exercicios fundamental 2", "atividade", None, None, None),
        ]
        ok = True
        for texto, prod, serie, tema, prazo in casos:
            ext = extrair(texto)
            if ext["produto"] != prod:
                print(f"FAIL produto: {texto!r} -> {ext['produto']}", file=sys.stderr)
                ok = False
            if serie and ext.get("serie") != serie:
                # serie matching is flexible
                if not (ext.get("serie") and serie.replace(" ", "") in ext["serie"].replace(" ", "")):
                    print(f"FAIL serie: {texto!r} -> {ext.get('serie')}", file=sys.stderr)
                    ok = False
            if tema and ext.get("tema") and _norm(tema) not in _norm(str(ext.get("tema"))):
                print(f"FAIL tema: {texto!r} -> {ext.get('tema')}", file=sys.stderr)
                ok = False
            if prazo and ext.get("prazo") and prazo not in str(ext.get("prazo")):
                print(f"FAIL prazo: {texto!r} -> {ext.get('prazo')}", file=sys.stderr)
                ok = False
        payload_text = texto_de_payload('{"text":"prova do 8o ano sobre Africa para amanha"}')
        if "Africa" not in payload_text:
            print("FAIL json payload parsing", file=sys.stderr)
            ok = False
        print(json.dumps({"ok": ok}, ensure_ascii=False))
        return 0 if ok else 1

    text = args.text
    if not text:
        text = texto_de_payload(sys.stdin.read())

    if not text:
        print(json.dumps({"error": "text required"}, ensure_ascii=False), file=sys.stderr)
        return 1

    result = extrair(text)
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
