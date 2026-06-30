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

import shutil  # noqa: E402
from megatron import responder, classificar, briefing, VAULT  # noqa: E402
from registry import resolver  # noqa: E402
from barramento import ler as ler_barramento, _match  # noqa: E402
import arquivista  # noqa: E402  (path injetado pelo registry)
from reasoningbank import recomendar  # noqa: E402
from registry import rotear, capacidades as cap_catalogo  # noqa: E402

# (pergunta, intent_esperado, classe_esperada, marcador esperado na resposta)
CASOS = [
    ("O que e o FabioOS?",                              "consulta", None, "RESPOSTA"),
    ("Como o MEGATRON declara ignorancia explicita?",   "consulta", None, "RESPOSTA"),
    ("O que se relaciona com PietraOS?",                "relacao",  None, "RESPOSTA"),
    ("Qual e a fase atual do FabioOS?",                 "status",   None, "Estado operacional"),
    ("Qual a cor favorita do dragao de Marte em 1850?", "consulta", None, "Ignorância"),
    ("envie um WhatsApp para o pai do aluno",           "acao", "externa", "AÇÃO EXTERNA"),
    ("apague o fabioos_db agora",                       "acao", "sensivel", "AÇÃO SENSÍVEL"),
    ("criar uma nota sobre energia solar",              "acao", "escrita_segura", "Proposta de nota"),
    ("o que voce pode fazer?",                          "capacidade", None, "Capacidades do FabioOS"),
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
    # Fatia 1 — briefing proativo (sem args) devolve Resultado estruturado.
    b = briefing()
    ok_brief = (b.get("tipo") == "briefing" and b.get("ok") is True
                and "Estado operacional" in b.get("corpo", ""))
    passes += ok_brief
    total = len(CASOS) + 1
    print(f"[{'PASS' if ok_brief else 'FALHA'}] briefing -> tipo={b.get('tipo')} | "
          f"corpo com estado: {'sim' if 'Estado operacional' in b.get('corpo','') else 'NAO'} "
          f"| sugestao: {'sim' if b.get('sugestao') else 'NAO'}")

    # Fatia 2 — registro de agentes: escrita_segura despachável; sensivel/externa não.
    ok_reg = (callable(resolver("escrita_segura"))
              and resolver("sensivel") is None
              and resolver("externa") is None)
    passes += ok_reg
    total += 1
    print(f"[{'PASS' if ok_reg else 'FALHA'}] registry -> escrita_segura despachável; "
          f"sensivel/externa bloqueadas")

    # Barramento — ler() não destrutivo + matching de destinatário (lead->claude).
    inbox = ler_barramento(para="claude", status="aberto")
    ok_bus = (isinstance(inbox, list)
              and _match("todos", "claude") and _match("lead", "claude")
              and not _match("cursor", "claude"))
    passes += ok_bus
    total += 1
    print(f"[{'PASS' if ok_bus else 'FALHA'}] barramento -> ler() ok ({len(inbox)} p/ claude); "
          f"matching todos/lead->claude correto")

    # Fatia 3 — write path (dry_run=False) cria rascunho real; self-cleaning.
    testdir = "00_Inbox/_golden_tmp"
    r3 = arquivista.run("Golden Confirm Test", "conteudo de teste",
                        dest=testdir, dry_run=False)
    criado = (VAULT / r3["artefato"]) if r3.get("artefato") else None
    ok_confirm = bool(r3["ok"] and criado and criado.exists())
    if criado and criado.exists():
        criado.unlink()
    tmproot = VAULT / testdir
    if tmproot.exists():
        shutil.rmtree(tmproot, ignore_errors=True)
    passes += ok_confirm
    total += 1
    print(f"[{'PASS' if ok_confirm else 'FALHA'}] fatia3 confirmar -> rascunho criado "
          f"({r3.get('artefato')}) e removido")

    # ReasoningBank-lite — recomenda 'scan' p/ commit; abstém p/ tarefa desconhecida.
    rec = recomendar("commit")
    abst = recomendar("tarefa_que_nunca_existiu_123")
    ok_rb = (rec["tipo"] == "sugestao" and "scan" in rec["sugestao"].lower()
             and abst["tipo"] == "abstencao")
    passes += ok_rb
    total += 1
    print(f"[{'PASS' if ok_rb else 'FALHA'}] reasoningbank -> commit recomenda "
          f"'{rec.get('sugestao','')[:30]}'; desconhecida -> {abst['tipo']}")

    # Maestro — roteamento por capacidade (ativo despachável; externo honesto).
    r_escrever = rotear("escrever_nota")
    r_codigo = rotear("escrever_codigo")
    r_nada = rotear("capacidade_inexistente_xyz")
    ok_rota = (r_escrever and r_escrever["status"] == "ativo"
               and r_codigo and r_codigo["status"] == "planejado"
               and r_codigo["ferramenta"] == "OpenHands"
               and r_nada is None
               and len(cap_catalogo("ativo")) >= 4)
    passes += ok_rota
    total += 1
    print(f"[{'PASS' if ok_rota else 'FALHA'}] maestro -> escrever_nota=ativo, "
          f"escrever_codigo=planejado(OpenHands), inexistente=None")

    print(f"\nResultado golden: {passes}/{total}")
    return 0 if passes == total else 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
