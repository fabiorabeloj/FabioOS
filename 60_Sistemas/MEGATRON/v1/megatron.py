#!/usr/bin/env python3
"""
MEGATRON v1 — interface cognitiva com Ignorância Explícita e roteamento controlado.

Evolui a v0 (mantida como rollback) conforme a SPEC
`60_Sistemas/FabioOS/specs/2026-06-29_megatron-v1-ignorancia-explicita.md`:
  - consulta memória antes de responder (STATUS/NEXT_ACTIONS + RAG + Grafo via MCP);
  - declara Ignorância Explícita quando a recuperação é fraca (limiar de distância);
  - diferencia RESPOSTA (com fontes) / SUGESTÃO / AÇÃO (requer aprovação humana);
  - classifica a ação por permissão (leitura / escrita segura / sensível / externa);
  - read-only e propose-only: não escreve, não envia, não executa ação externa;
  - sem LLM/API (recuperação, custo zero); registra log.

Uso:
    python megatron.py "Qual é a fase atual do FabioOS?"
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
        if (parent / "60_Sistemas/FabioOS/bootstrap/CLAUDE.md").exists():
            return parent
    return p.parents[3]


VAULT = _vault_root()
sys.path.insert(0, str(VAULT / "60_Sistemas" / "MCP_FabioOS"))
LOG = VAULT / "60_Sistemas" / "MEGATRON" / "v1" / "logs" / "megatron_v1_50_Registros/Logs_Agentes/log.md"
STATUS_FILE = VAULT / "60_Sistemas" / "FabioOS" / "STATUS.md"
NEXT_FILE = VAULT / "60_Sistemas" / "FabioOS" / "NEXT_ACTIONS.md"

from server import mcp           # reaproveita o MCP FabioOS (in-memory)  # noqa: E402
from fastmcp import Client       # noqa: E402

LIMIAR_IGNORANCIA = 0.5  # dist cosseno bge-m3: <0.5 relevante; >0.5 → ignorância

STATUS_KW = ("fase atual", "status", "pendencia", "pendência", "proximo passo",
             "próximo passo", "o que falta", "roadmap", "onde estamos", "estado")
RELACAO_KW = ("relaciona", "relacionado", "conectado", "relação", "relacao",
              "depende", "vizinho", "ligado a")
# Ação → classe de permissão (matriz simplificada da Fase 17).
# Usar RADICAIS para pegar conjugações (apagar/apague/apaga; enviar/envie/envia).
ACAO_EXTERNA = ("push", "envi", "whatsapp", "email", "e-mail", "publica", "deploy")
ACAO_SENSIVEL = ("apag", "delet", "remov", "exclu", "reindex", "mover", "mova",
                 "token", "credencial", "instal")
ACAO_ESCRITA = ("commit", "criar", "crie", "escrev", "salva", "gerar", "registr")


def classificar(msg: str):
    m = msg.lower()
    if any(k in m for k in ACAO_EXTERNA):
        return "acao", "externa"
    if any(k in m for k in ACAO_SENSIVEL):
        return "acao", "sensivel"
    if any(k in m for k in ACAO_ESCRITA):
        return "acao", "escrita_segura"
    if any(k in m for k in STATUS_KW):
        return "status", None
    if any(k in m for k in RELACAO_KW):
        return "relacao", None
    return "consulta", None


def registrar(intent: str, msg: str) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    if not LOG.exists():
        LOG.write_text("# Log MEGATRON v1\n\n| timestamp | intent | mensagem |\n"
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


def _ler_estado() -> str:
    """Lê STATUS/NEXT_ACTIONS (fonte operacional) — não inventa estado."""
    partes = []
    for nome, f in (("STATUS", STATUS_FILE), ("NEXT_ACTIONS", NEXT_FILE)):
        if f.exists():
            txt = f.read_text(encoding="utf-8", errors="ignore")
            # pega o trecho de "Estado canonico" ou as primeiras linhas úteis
            corte = txt[:900].strip()
            partes.append(f"### {nome} ({f.relative_to(VAULT).as_posix()})\n{corte}")
    return "\n\n".join(partes) or "(STATUS/NEXT_ACTIONS não encontrados)"


async def responder(msg: str) -> str:
    intent, classe = classificar(msg)
    registrar(f"{intent}:{classe}" if classe else intent, msg)

    # AÇÃO — diferencia permissão; nunca executa
    if intent == "acao":
        rotulo = {"externa": "AÇÃO EXTERNA", "sensivel": "AÇÃO SENSÍVEL",
                  "escrita_segura": "AÇÃO DE ESCRITA"}[classe]
        agente = {"externa": "aprovação humana + n8n/OpenClaw",
                  "sensivel": "aprovação humana (SafeCommit/segurança)",
                  "escrita_segura": "SafeCommit/Arquivista"}[classe]
        return (f"🛑 {rotulo} detectada — MEGATRON v1 é read-only/propose-only.\n"
                f"  • Pedido: {msg}\n"
                f"  • NÃO executo. Classe de permissão: {classe} → requer **aprovação humana** "
                f"e roteamento para: {agente}.\n"
                f"  • Posso **preparar/propor** o passo, não realizá-lo.")

    async with Client(mcp) as c:
        rag = _txt(await c.call_tool("consultar_rag", {"pergunta": msg, "k": 5}))
        m = re.search(r"dist=([0-9.]+)", rag or "")
        melhor = float(m.group(1)) if m else None
        sem_evidencia = ((not rag) or ("Nenhum trecho" in rag) or len(rag.strip()) < 40
                         or (melhor is not None and melhor > LIMIAR_IGNORANCIA))

        partes = [f"🔎 {msg}\n"]

        if intent == "status":
            # estado operacional vem das FONTES canônicas, não de adivinhação
            partes.append("📊 Estado operacional (fontes canônicas):\n" + _ler_estado())

        if sem_evidencia and intent != "status":
            extra = (f" (melhor dist={melhor:.2f} > limiar {LIMIAR_IGNORANCIA})"
                     if melhor is not None else "")
            partes.append("⚠️ Ignorância explícita: não há evidência suficiente no vault "
                          f"para responder com confiança{extra}. Refine a pergunta ou "
                          "registre a lacuna.")
            tipo = "ABSTENÇÃO"
        else:
            partes.append("📚 Recuperado do vault (com fontes):\n" + rag)
            if intent == "relacao":
                termo = msg.rstrip("?.! ").split()[-1]
                grafo = _txt(await c.call_tool("consultar_grafo",
                                               {"termo": termo, "top": 6}))
                partes.append("\n🕸️ Relações (grafo):\n" + grafo)
            tipo = "RESPOSTA"

        partes.append(f"\n[{tipo}] · recuperação sem LLM (custo zero) · "
                      "💡 próxima ação sugerida: confira as fontes; para agir, peça e eu "
                      "preparo o passo (aprovação humana antes de executar).")
        return "\n".join(partes)


def main() -> int:
    if len(sys.argv) < 2:
        print('Uso: python megatron.py "sua pergunta ou pedido"')
        return 1
    print(asyncio.run(responder(" ".join(sys.argv[1:]))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
