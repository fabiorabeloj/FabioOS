#!/usr/bin/env python3
"""
Registro de Capacidades do MEGATRON (o "Maestro").

Cada agente — interno (já funcional) ou futuro (ferramenta candidata da stack
operacional) — **anuncia suas capacidades**. O orquestrador (`megatron.py`) roteia
uma subtarefa para o agente que a possui, e é **honesto** sobre o que ainda não
existe: `ativo` (funciona agora), `planejado` (ferramenta candidata, não instalada),
`gated` (requer aprovação humana / runtime / serviço externo).

Padrão da "próxima evolução do FabioOS": cada agente declara o que sabe fazer e o
Maestro decide quem executa. Ferramentas externas só entram via Matriz de Aptidão
+ SPEC + aprovação do Fabio (ver Mapa de Arquitetura Operacional).

Apenas capacidades de agentes `ativo` são despacháveis hoje. As demais são
roteáveis em modo "proposta" (o Maestro diz quem faria, mas não executa).
"""
import sys
from pathlib import Path

V1 = Path(__file__).resolve().parent
AGENTES_DIR = V1.parent / "agentes" / "implementacao" / "claude"
if str(AGENTES_DIR) not in sys.path:
    sys.path.insert(0, str(AGENTES_DIR))

# Catálogo de capacidades. status: ativo | planejado | gated
AGENTES = {
    "arquivista": {"status": "ativo", "ferramenta": "interno (arquivista.py)",
                   "capacidades": ["escrever_nota", "classificar_dominio"]},
    "rag": {"status": "ativo", "ferramenta": "interno (RAG Chroma+bge-m3)",
            "capacidades": ["consultar_conhecimento"]},
    "grafo": {"status": "ativo", "ferramenta": "interno (Grafo)",
              "capacidades": ["consultar_relacoes"]},
    "reasoningbank": {"status": "ativo", "ferramenta": "interno (reasoningbank.py)",
                      "capacidades": ["recomendar_estrategia"]},
    "barramento": {"status": "ativo", "ferramenta": "interno (barramento.py)",
                   "capacidades": ["comunicar_agentes"]},
    # Futuros — stack operacional (não instalados; ver Mapa de Arquitetura)
    "programador": {"status": "planejado", "ferramenta": "OpenHands",
                    "capacidades": ["escrever_codigo", "corrigir_bug", "abrir_pr"]},
    "pesquisador": {"status": "planejado", "ferramenta": "Crawl4AI",
                    "capacidades": ["coletar_web", "alimentar_rag"]},
    "documentalista": {"status": "planejado", "ferramenta": "Stirling PDF",
                       "capacidades": ["processar_pdf", "ocr", "merge_split_pdf"]},
    "banco": {"status": "planejado", "ferramenta": "Supabase / Qdrant",
              "capacidades": ["armazenar_memoria", "armazenar_vetores"]},
    "interface": {"status": "planejado", "ferramenta": "Open WebUI",
                  "capacidades": ["chat_multimodelo"]},
    "laboratorio": {"status": "planejado", "ferramenta": "Langflow",
                    "capacidades": ["prototipar_fluxo"]},
    "coletor_visual": {"status": "planejado", "ferramenta": "Maxun",
                       "capacidades": ["scraper_visual"]},
    # Gated — requer aprovação humana / runtime / serviço externo
    "navegador": {"status": "gated", "ferramenta": "Browser Use",
                  "capacidades": ["navegar_web", "baixar_arquivo", "preencher_formulario"]},
    "atendente": {"status": "gated", "ferramenta": "Dify + WhatsApp/Pietra",
                  "capacidades": ["atender_whatsapp"]},
    "infra": {"status": "gated", "ferramenta": "Coolify",
              "capacidades": ["deploy", "hospedar"]},
    "automacao": {"status": "gated", "ferramenta": "n8n / Temporal",
                  "capacidades": ["automacao_recorrente", "orquestrar_tarefa_longa"]},
}

# Classe de permissão (Fase 17) -> agente despachável HOJE (escrita segura).
CLASSE_AGENTE = {"escrita_segura": "arquivista"}


def resolver(classe: str):
    """Retorna a função `run` do agente da classe de permissão, ou None.
    Mantido para o despacho de escrita_segura (Fatia 2/3). Import lazy."""
    if classe == "escrita_segura":
        import arquivista
        return arquivista.run
    return None


def capacidades(status: str = None) -> dict:
    """Catálogo de capacidades (opcionalmente filtrado por status)."""
    if status is None:
        return AGENTES
    return {a: d for a, d in AGENTES.items() if d["status"] == status}


def rotear(capacidade: str) -> dict:
    """Encontra o agente que possui a capacidade. Devolve {agente, status,
    ferramenta} ou None. Match por igualdade ou substring."""
    cap = capacidade.lower().strip()
    for agente, d in AGENTES.items():
        for c in d["capacidades"]:
            if cap == c or cap in c or c in cap:
                return {"agente": agente, "status": d["status"],
                        "ferramenta": d["ferramenta"], "capacidade": c}
    return None
