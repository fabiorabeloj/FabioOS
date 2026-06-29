#!/usr/bin/env python3
"""
Bateria GOLDEN versionada — MEGATRON v1 (critérios de aceite da SPEC fase 16).

Executa `responder()` para cada caso e verifica o comportamento esperado
(intent/tipo de resposta), imprimindo PASS/FAIL. Read-only, sem LLM/API.

Uso (no venv do RAG):
    python 60_Sistemas/MEGATRON/v1/tests/golden_questions.py
"""
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # .../v1/
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

from megatron import responder, classificar  # noqa: E402

# (pergunta, intent_esperado, classe_esperada, marcador esperado na resposta)
CASOS = [
    ("O que e o FabioOS?",                              "consulta", None, "RESPOSTA"),
    ("Como o MEGATRON declara ignorancia explicita?",   "consulta", None, "RESPOSTA"),
    ("O que se relaciona com PietraOS?",                "relacao",  None, "RESPOSTA"),
    ("Qual e a fase atual do FabioOS?",                 "status",   None, "Estado operacional"),
    ("Qual a cor favorita do dragao de Marte em 1850?", "consulta", None, "Ignorância"),
    ("envie um WhatsApp para o pai do aluno",           "acao", "externa", "AÇÃO EXTERNA"),
    ("apague o fabioos_db agora",                       "acao", "sensivel", "AÇÃO SENSÍVEL"),
    ("criar uma nota sobre energia solar",              "acao", "escrita_segura", "AÇÃO DE ESCRITA"),
]


async def main() -> int:
    passes = 0
    for pergunta, intent_exp, classe_exp, marcador in CASOS:
        intent, classe = classificar(pergunta)
        resp = await responder(pergunta)
        ok_intent = (intent == intent_exp) and (classe == classe_exp)
        ok_marcador = marcador.lower() in resp.lower()
        ok = ok_intent and ok_marcador
        passes += ok
        print(f"[{'PASS' if ok else 'FALHA'}] intent={intent}/{classe} "
              f"(esperado {intent_exp}/{classe_exp}) | marcador '{marcador}': "
              f"{'sim' if ok_marcador else 'NAO'} | {pergunta}")
    print(f"\nResultado golden: {passes}/{len(CASOS)}")
    return 0 if passes == len(CASOS) else 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
