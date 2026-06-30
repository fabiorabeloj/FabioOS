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
import os
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
LOG = VAULT / "60_Sistemas" / "MEGATRON" / "v1" / "logs" / "megatron_v1_log.md"
STATUS_FILE = VAULT / "60_Sistemas" / "FabioOS" / "STATUS.md"
NEXT_FILE = VAULT / "60_Sistemas" / "FabioOS" / "NEXT_ACTIONS.md"

from server import mcp           # reaproveita o MCP FabioOS (in-memory)  # noqa: E402
from fastmcp import Client       # noqa: E402
from registry import (resolver, resolver_capacidade,  # noqa: E402
                      capacidades as cap_catalogo, rotear)  # despacho + Maestro
from barramento import ler as ler_barramento  # caixa multiagente  # noqa: E402
from reasoningbank import (recomendar as rb_recomendar,  # noqa: E402
                           registrar as rb_registrar)  # memória de experiências

LIMIAR_IGNORANCIA = 0.5  # dist cosseno bge-m3: <0.5 relevante; >0.5 → ignorância

# Cérebro local (opt-in via --llm). Padrão: OFF (recuperação custo-zero, sem LLM).
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2:3b")


def _llm_ollama(prompt: str, model: str = None) -> str:
    """Gera texto com o LLM LOCAL (Ollama). Só é chamado em modo --llm.
    Sem rede externa, sem custo de API — roda na máquina (GPU se disponível)."""
    import json as _json
    import urllib.request as _u
    data = _json.dumps({"model": model or OLLAMA_MODEL, "prompt": prompt,
                        "stream": False}).encode("utf-8")
    req = _u.Request(OLLAMA_HOST + "/api/generate", data=data,
                     headers={"Content-Type": "application/json"})
    with _u.urlopen(req, timeout=180) as r:
        return _json.loads(r.read().decode("utf-8")).get("response", "").strip()

STATUS_KW = ("fase atual", "status", "pendencia", "pendência", "proximo passo",
             "próximo passo", "o que falta", "roadmap", "onde estamos", "estado")
RELACAO_KW = ("relaciona", "relacionado", "conectado", "relação", "relacao",
              "depende", "vizinho", "ligado a")
CAPACIDADE_KW = ("o que voce pode", "o que você pode", "quais capacidades",
                 "suas capacidades", "capacidade", "quem faz", "quem pode",
                 "o que sabe fazer", "o que consegue fazer", "quem consegue",
                 "time de agentes", "equipe de agentes", "o que voce faz",
                 "o que você faz")
ESTRATEGIA_KW = ("melhor forma", "melhor abordagem", "melhor jeito", "como devo",
                 "como faco", "como faço", "qual estrategia", "qual a estrategia",
                 "qual estratégia", "ja deu certo", "já deu certo", "o que funciona",
                 "recomenda", "recomendacao", "recomendação")
PESQUISA_KW = ("pesquis", "colet", "crawl", "raspar", "rastrear", "scrape",
               "baixar a pagina", "ler o site", "ler a pagina")
DOCUMENTO_KW = ("pdf", "ocr", "juntar documento", "merge pdf", "dividir pdf",
                "comprimir pdf", "assinar pdf", "processar documento", "stirling")
URL_RE = re.compile(r"https?://\S+")
# Ação → classe de permissão (matriz simplificada da Fase 17).
# Usar RADICAIS para pegar conjugações (apagar/apague/apaga; enviar/envie/envia).
ACAO_EXTERNA = ("push", "envi", "whatsapp", "email", "e-mail", "publica", "deploy")
ACAO_SENSIVEL = ("apag", "delet", "remov", "exclu", "reindex", "mover", "mova",
                 "token", "credencial", "instal")
ACAO_ESCRITA = ("commit", "criar", "crie", "escrev", "salva", "gerar", "registr")


def classificar(msg: str):
    m = msg.lower()
    if any(k in m for k in ESTRATEGIA_KW):
        return "estrategia", None
    if any(k in m for k in ACAO_EXTERNA):
        return "acao", "externa"
    if any(k in m for k in ACAO_SENSIVEL):
        return "acao", "sensivel"
    if any(k in m for k in ACAO_ESCRITA):
        return "acao", "escrita_segura"
    if any(k in m for k in CAPACIDADE_KW):
        return "capacidade", None
    if any(k in m for k in DOCUMENTO_KW):
        return "documento", None
    if URL_RE.search(msg) or any(k in m for k in PESQUISA_KW):
        return "pesquisa", None
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


def _capacidades_resultado() -> dict:
    """O Maestro anuncia o time: capacidades por status (ativo/planejado/gated)."""
    cat = cap_catalogo()
    grupos = {"ativo": [], "planejado": [], "gated": []}
    for agente, d in cat.items():
        grupos.get(d["status"], []).append(
            f"- **{agente}** ({d['ferramenta']}): {', '.join(d['capacidades'])}")
    rotulo = {"ativo": "✅ Ativos (executam hoje)",
              "planejado": "🛠️ Planejados (candidatos da stack, não instalados)",
              "gated": "🔒 Gated (requer aprovação humana/runtime)"}
    corpo = []
    for st in ("ativo", "planejado", "gated"):
        corpo.append(f"### {rotulo[st]}")
        corpo += (grupos[st] or ["- (nenhum)"])
        corpo.append("")
    n_ativo = len(grupos["ativo"])
    return {
        "tipo": "capacidades", "ok": True,
        "titulo": f"Capacidades do FabioOS — {n_ativo} agente(s) ativo(s)",
        "corpo": "\n".join(corpo).strip(),
        "fontes": [{"source_path": "60_Sistemas/MEGATRON/v1/registry.py",
                    "header_path": "AGENTES"}],
        "sugestao": "Capacidades planejadas/gated entram via Matriz de Aptidão + SPEC + aprovação.",
        "artefato": None,
    }


def _titulo_do_pedido(msg: str) -> str:
    """Extrai um título do pedido de escrita, removendo o verbo inicial."""
    t = msg.strip().rstrip("?.! ")
    for v in ("criar uma nota sobre", "criar nota sobre", "registrar pendencia",
              "registrar pendência", "registrar", "registre", "criar", "crie",
              "gerar", "salvar", "escrever", "anotar", "anote"):
        if t.lower().startswith(v):
            return (t[len(v):].strip() or msg.strip())
    return t or msg.strip()


def _pendencias_abertas(n: int = 5) -> list:
    """Extrai as primeiras pendências abertas (- [ ]) do NEXT_ACTIONS."""
    if not NEXT_FILE.exists():
        return []
    out = []
    for line in NEXT_FILE.read_text(encoding="utf-8", errors="ignore").splitlines():
        s = line.strip()
        if s.startswith("- [ ]"):
            out.append(s[5:].strip())
            if len(out) >= n:
                break
    return out


def briefing() -> dict:
    """Fatia 1 — briefing proativo. Resultado estruturado a partir das FONTES
    canônicas (STATUS/NEXT_ACTIONS). Rápido: sem RAG/modelo. Contrato congelado
    em Ordens_Coordenacao_Paralela_MEGATRON_2026-06-29.md."""
    registrar("briefing", "(sem args)")
    pend = _pendencias_abertas(5)
    inbox = ler_barramento(para="claude", status="aberto")
    hoje = datetime.now().strftime("%Y-%m-%d")
    corpo = ["## Estado operacional (fontes canônicas)\n", _ler_estado(),
             "\n## Pendências abertas (topo)"]
    corpo += ([f"- {p}" for p in pend] if pend
              else ["- (nenhuma pendência aberta em NEXT_ACTIONS)"])
    corpo.append("\n## Caixa de entrada (barramento multiagente)")
    corpo += ([f"- [{m['de']}→{m['para']}] {m['tipo']}: {m['mensagem']}" for m in inbox]
              if inbox else ["- (nenhuma mensagem aberta para o lead)"])
    fontes = [{"source_path": f.relative_to(VAULT).as_posix(), "header_path": ""}
              for f in (STATUS_FILE, NEXT_FILE) if f.exists()]
    sugestao = (f"Responder no barramento: {inbox[0]['de']} pediu '{inbox[0]['mensagem'][:60]}'"
                if inbox else (pend[0] if pend else "Revisar STATUS/NEXT_ACTIONS."))
    return {
        "tipo": "briefing",
        "ok": True,
        "titulo": f"Briefing FabioOS — {hoje}",
        "corpo": "\n".join(corpo),
        "fontes": fontes,
        "sugestao": sugestao,
        "artefato": None,
    }


def _render(resultado: dict) -> str:
    """Render mínimo p/ terminal. TEMPORÁRIO — Cursor substitui por
    apresentacao.render() (ver Ordens de Coordenação). Não embeleza: só monta."""
    linhas = [f"🧠 {resultado['titulo']}", "", resultado["corpo"]]
    if resultado.get("sugestao"):
        linhas += ["", f"💡 Próxima ação sugerida: {resultado['sugestao']}"]
    if resultado.get("fontes"):
        linhas += ["", "Fontes: "
                   + ", ".join(f["source_path"] for f in resultado["fontes"])]
    linhas += ["", f"[{resultado['tipo'].upper()}] · recuperação sem LLM (custo zero)"]
    return "\n".join(linhas)


def _fontes_do_rag(rag: str) -> list:
    """Extrai caminhos de fontes (.md) do texto recuperado, p/ o contrato Resultado."""
    seen, out = set(), []
    for p in re.findall(r"[\w/_\-]+\.md", rag or ""):
        if p not in seen:
            seen.add(p)
            out.append({"source_path": p, "header_path": ""})
        if len(out) >= 5:
            break
    return out


def _termo_chave(msg: str) -> str:
    palavras = [w for w in re.findall(r"\w+", msg) if len(w) > 3]
    return palavras[-1] if palavras else msg.strip()


def _sintese(fontes: list, termo: str) -> str:
    onde = ", ".join(f["source_path"] for f in fontes[:3]) or "(sem fontes diretas)"
    return (f"- **Onde ler:** {onde}\n"
            f"- **Termo central:** {termo}\n"
            f"- **Honestidade:** recuperação + relação estruturada (sem LLM, custo zero); "
            f"não é texto gerado. Para síntese redigida, é preciso aprovar uso de modelo.")


async def responder(msg: str, confirmar: bool = False, usar_llm: bool = False) -> str:
    intent, classe = classificar(msg)
    registrar(f"{intent}:{classe}" if classe else intent, msg)

    # ESTRATÉGIA — o Maestro consulta a própria memória de experiências
    if intent == "estrategia":
        termo = _termo_chave(msg)
        return _render(rb_recomendar(termo))

    # DOCUMENTO — roteia por capacidade (processar_pdf -> documentalista/Stirling)
    if intent == "documento":
        run_doc = resolver_capacidade("processar_pdf")
        if run_doc is None:
            return ("🛑 Capacidade 'processar_pdf' não está ativa (documentalista/Stirling "
                    "indisponível). Posso propor, não executar.")
        return _render(await asyncio.to_thread(run_doc))

    # CAPACIDADE — o Maestro anuncia o time (read-only, sem RAG)
    if intent == "capacidade":
        return _render(_capacidades_resultado())

    # PESQUISA — roteia por capacidade (coletar_web -> pesquisador/Crawl4AI)
    if intent == "pesquisa":
        url_m = URL_RE.search(msg)
        rota = rotear("coletar_web")
        if not url_m:
            return _render({"tipo": "abstencao", "ok": False,
                            "titulo": "🔎 Pesquisa web",
                            "corpo": "Preciso de uma URL para coletar. Ex.: "
                                     "`megatron \"pesquise https://exemplo.com/doc\"`.",
                            "fontes": [], "sugestao": "Informe a URL.", "artefato": None})
        run_pesq = resolver_capacidade("coletar_web")
        if run_pesq is None:     # capacidade existe mas agente não está ativo
            alvo = f"{rota['agente']} ({rota['ferramenta']}, {rota['status']})" if rota else "nenhum agente"
            return (f"🛑 Capacidade 'coletar_web' não está ativa — rotearia para {alvo}; "
                    f"requer instalação/aprovação. Posso propor, não executar.")
        url = url_m.group(0)
        # pesquisador.run faz asyncio.run interno -> roda em thread p/ evitar loop aninhado
        r = await asyncio.to_thread(lambda: run_pesq(url, dry_run=not confirmar))
        if confirmar and r.get("ok"):   # auto-learning: só em coleta real
            rb_registrar("coletar_web", "pesquisador/crawl4ai",
                         sucesso=True, confianca=0.7, nota="via Maestro")
        return _render(r)

    # AÇÃO — diferencia permissão; nunca executa sem aprovação
    if intent == "acao":
        # escrita segura: DESPACHA ao Arquivista. Sem --confirmar = dry-run (propõe);
        # com --confirmar (aprovação humana) = cria o rascunho de fato (Fatia 3).
        if classe == "escrita_segura":
            run_agente = resolver(classe)
            if run_agente is not None:
                titulo = _titulo_do_pedido(msg)
                r = run_agente(titulo,
                               f"(rascunho proposto a partir do pedido: {msg})",
                               dry_run=not confirmar)
                if confirmar and r.get("ok"):   # auto-learning: só em execução real
                    rb_registrar("escrever_nota", "arquivista (dry-run->confirmar)",
                                 sucesso=True, confianca=0.7, nota="via Maestro")
                return _render(r)
        # sensível / externa permanecem BLOQUEADAS (sem agente automático)
        rotulo = {"externa": "AÇÃO EXTERNA", "sensivel": "AÇÃO SENSÍVEL"}[classe]
        agente = {"externa": "aprovação humana + n8n/OpenClaw",
                  "sensivel": "aprovação humana (SafeCommit/segurança)"}[classe]
        return (f"🛑 {rotulo} detectada — MEGATRON v1 é read-only/propose-only.\n"
                f"  • Pedido: {msg}\n"
                f"  • NÃO executo. Classe de permissão: {classe} → requer **aprovação humana** "
                f"e roteamento para: {agente}.\n"
                f"  • Posso **preparar/propor** o passo, não realizá-lo.")

    # CONSULTA / RELAÇÃO / STATUS — cadeia RAG -> grafo -> síntese (Fatia 4),
    # unificada no contrato Resultado.
    async with Client(mcp) as c:
        rag = _txt(await c.call_tool("consultar_rag", {"pergunta": msg, "k": 5}))
        m = re.search(r"dist=([0-9.]+)", rag or "")
        melhor = float(m.group(1)) if m else None
        sem_evidencia = ((not rag) or ("Nenhum trecho" in rag) or len(rag.strip()) < 40
                         or (melhor is not None and melhor > LIMIAR_IGNORANCIA))

        # Abstenção (Ignorância Explícita) — exceto status, que vem de fonte canônica
        if sem_evidencia and intent != "status":
            extra = (f" (melhor dist={melhor:.2f} > limiar {LIMIAR_IGNORANCIA})"
                     if melhor is not None else "")
            corpo = ("⚠️ Ignorância explícita: não há evidência suficiente no vault "
                     f"para responder com confiança{extra}.")
            return _render({"tipo": "abstencao", "ok": False, "titulo": f"🔎 {msg}",
                            "corpo": corpo, "fontes": [],
                            "sugestao": "Refine a pergunta ou registre a lacuna no vault.",
                            "artefato": None})

        fontes = _fontes_do_rag(rag)
        corpo = []
        if intent == "status":
            corpo.append("## Estado operacional (fontes canônicas)\n" + _ler_estado())
        corpo.append("## Recuperado do vault\n" + rag)

        # elo da cadeia: grafo sobre o termo-chave (sempre, não só em 'relacao')
        termo = _termo_chave(msg)
        grafo = _txt(await c.call_tool("consultar_grafo", {"termo": termo, "top": 6}))
        if grafo and "Nenhum" not in grafo and len(grafo.strip()) > 10:
            corpo.append(f"\n## Relações no grafo (termo: {termo})\n" + grafo)

        corpo.append("\n## Síntese\n" + _sintese(fontes, termo))

        # Cérebro local (opt-in): gera resposta redigida SOBRE a recuperação
        if usar_llm:
            prompt = (f"Responda em PT-BR, conciso, usando APENAS os trechos do vault "
                      f"FabioOS abaixo. Se não houver base, diga que não sabe.\n\n"
                      f"Pergunta: {msg}\n\nTrechos:\n{rag}\n\nResposta:")
            try:
                corpo.append("\n## Resposta redigida (cérebro local · Ollama)\n"
                             + _llm_ollama(prompt))
            except Exception as e:
                corpo.append(f"\n## Cérebro local indisponível\n(Ollama não respondeu: {e})")

        return _render({"tipo": "resposta", "ok": True, "titulo": f"🔎 {msg}",
                        "corpo": "\n".join(corpo), "fontes": fontes,
                        "sugestao": "Confira as fontes; para agir, peça e eu preparo o "
                                    "passo (aprovação humana antes de executar).",
                        "artefato": None})


def main() -> int:
    args = sys.argv[1:]
    confirmar = "--confirmar" in args
    usar_llm = "--llm" in args
    args = [a for a in args if a not in ("--confirmar", "--llm")]
    if not args:
        # sem argumento -> briefing proativo (Fatia 1): "Bom dia, FabioOS"
        print(_render(briefing()))
        return 0
    print(asyncio.run(responder(" ".join(args), confirmar=confirmar, usar_llm=usar_llm)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
