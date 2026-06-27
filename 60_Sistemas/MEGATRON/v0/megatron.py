#!/usr/bin/env python3
"""
MEGATRON v0 — interface cognitiva mínima do FabioOS (capstone / bloco B5).

Princípios (read-only, propose-only):
  - roteia a mensagem do usuário pelas ferramentas do MCP FabioOS (consultar_rag,
    consultar_grafo, buscar_nota) — reaproveita, não duplica;
  - responde por RECUPERAÇÃO, sempre com FONTES; não chama LLM/API (custo zero);
  - aplica a Regra da Ignorância Explícita quando falta evidência;
  - AÇÕES (commit/criar/enviar/apagar) NÃO são executadas: devolve proposta +
    "requer aprovação humana" e indica o agente responsável.

Uso:
    python megatron.py "Qual é a fase atual do FabioOS?"
    python megatron.py "O que se relaciona com PietraOS?"
"""
from pathlib import Path
from datetime import datetime
import asyncio
import re
import sys

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass


def _vault_root() -> Path:
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / "CLAUDE.md").exists():
            return parent
    return p.parents[3]


VAULT = _vault_root()
sys.path.insert(0, str(VAULT / "60_Sistemas" / "MCP_FabioOS"))
LOG = VAULT / "60_Sistemas" / "MEGATRON" / "v0" / "logs" / "megatron_log.md"

from server import mcp           # reaproveita o MCP FabioOS (in-memory)  # noqa: E402
from fastmcp import Client       # noqa: E402

ACAO = ("commit", "push", "criar", "apagar", "delet", "mover", "enviar",
        "executar", "instalar", "remover", "gerar changelog")
STATUS = ("fase atual", "status", "pendencia", "pendência", "proximo passo",
          "próximo passo", "o que falta", "roadmap", "onde estamos")
RELACAO = ("relaciona", "relacionado", "conectado", "relação", "relacao",
           "depende", "vizinho", "ligado a")
# Distância cosseno (bge-m3): relevantes ~0.28-0.35; sem sentido ~0.60-0.64.
# Acima do limiar → Ignorância Explícita (calibrado em 2026-06-27).
LIMIAR_IGNORANCIA = 0.5


def classificar(msg: str) -> str:
    m = msg.lower()
    if any(k in m for k in ACAO):
        return "acao"
    if any(k in m for k in STATUS):
        return "status"
    if any(k in m for k in RELACAO):
        return "relacao"
    return "consulta"


def registrar(intent: str, msg: str) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    if not LOG.exists():
        LOG.write_text("# Log MEGATRON v0\n\n| timestamp | intent | mensagem |\n"
                       "|---|---|---|\n", encoding="utf-8")
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"| {ts} | {intent} | {msg[:80].replace('|', '/')} |\n")


def _txt(r) -> str:
    v = getattr(r, "data", None)
    if v is None:
        v = getattr(r, "content", None)
    if isinstance(v, list):
        return "".join(getattr(b, "text", str(b)) for b in v)
    return str(v if v is not None else r)


async def responder(msg: str) -> str:
    intent = classificar(msg)
    registrar(intent, msg)

    if intent == "acao":
        return ("🛑 AÇÃO detectada — MEGATRON v0 é propose-only.\n"
                f"  • Pedido: {msg}\n"
                "  • NÃO executo commit/criação/envio/exclusão. Requer APROVAÇÃO "
                "HUMANA e roteamento ao agente certo (SafeCommit, Arquivista, etc.).")

    async with Client(mcp) as c:
        rag = _txt(await c.call_tool("consultar_rag", {"pergunta": msg, "k": 5}))
        partes = [f"🔎 {msg}\n"]
        m = re.search(r"dist=([0-9.]+)", rag or "")
        melhor = float(m.group(1)) if m else None
        sem_evidencia = (
            (not rag) or ("Nenhum trecho" in rag) or len(rag.strip()) < 40
            or (melhor is not None and melhor > LIMIAR_IGNORANCIA)
        )
        if sem_evidencia:
            extra = (f" (melhor relevância dist={melhor:.2f} acima do limiar "
                     f"{LIMIAR_IGNORANCIA})" if melhor is not None else "")
            partes.append("⚠️ Ignorância explícita: não há evidência suficiente no "
                          f"vault para responder com confiança{extra}. Refine a "
                          "pergunta ou registre a lacuna.")
        else:
            partes.append("📚 Recuperado do vault (com fontes):\n" + rag)
            if intent == "relacao":
                termo = msg.rstrip("?.! ").split()[-1]
                grafo = _txt(await c.call_tool("consultar_grafo",
                                               {"termo": termo, "top": 6}))
                partes.append("\n🕸️ Relações (grafo):\n" + grafo)
            partes.append("\nℹ️ Resposta por recuperação (sem geração/LLM). "
                          "Confira as fontes citadas.")
        return "\n".join(partes)


def main() -> int:
    if len(sys.argv) < 2:
        print('Uso: python megatron.py "sua pergunta ou pedido"')
        return 1
    print(asyncio.run(responder(" ".join(sys.argv[1:]))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
