from __future__ import annotations

import re
import sys
from pathlib import Path

from primus_digestor_common import read_jsonl, short_snippet, stable_id, write_jsonl


RULES = [
    ("spell", ["magia", "conjur", "espaco de magia", "nivel de magia"]),
    ("class", ["classe", "caracteristicas de classe", "dado de vida"]),
    ("background", ["antecedente", "personalidade"]),
    ("race", ["raca", "racial", "elfo", "anao", "halfling", "draconato"]),
    ("creature", ["criatura", "monstro", "dragao", "goblin", "morto-vivo"]),
    ("item", ["equipamento", "item", "arma", "armadura"]),
    ("plane", ["plano", "cosmologia", "multiverso", "astral", "etereo"]),
    ("faction", ["faccao", "ordem", "culto", "alianca", "sociedade"]),
    ("region", ["regiao", "reino", "cidade", "cordilheira", "floresta"]),
    ("encounter", ["encontro", "teste", "cd ", "combate"]),
    ("mission", ["missao", "aventura", "recompensa", "contrato"]),
]


def classify(text: str) -> str:
    low = text.lower()
    for type_name, keywords in RULES:
        if any(k in low for k in keywords):
            return type_name
    return "rule"


def box_for(type_name: str) -> str:
    if type_name in {"race", "class", "background", "feat", "spell", "item", "magic_item", "rule"}:
        return "Grimorio"
    if type_name in {"creature", "npc", "deity"}:
        return "Bestiario"
    if type_name in {"plane", "region", "settlement", "site", "dungeon"}:
        return "Atlas"
    if type_name in {"mission", "encounter", "hazard", "trap", "puzzle", "reward", "consequence", "procedure", "generator"}:
        return "Motor"
    return "Enciclopedia"


def name_from(block: dict, type_name: str) -> str:
    heading = (block.get("heading") or "").strip()
    if heading:
        return heading.title()[:80]
    text = block.get("text", "")
    first = re.split(r"[.;:\n]", text, 1)[0].strip()
    return (first or type_name).title()[:80]


def default_affects(type_name: str) -> list[str]:
    mapping = {
        "spell": ["encounter", "resource", "magic_effect"],
        "class": ["character_creation", "progression"],
        "background": ["character_creation", "hooks"],
        "race": ["character_creation", "ancestry_hooks"],
        "creature": ["encounter", "threat"],
        "item": ["equipment", "reward"],
        "plane": ["cosmology", "travel"],
        "faction": ["conflict", "reputation"],
        "region": ["worldstate", "travel"],
        "mission": ["instance", "delta_p"],
    }
    return mapping.get(type_name, ["catalog"])


def default_hints(type_name: str) -> list[str]:
    mapping = {
        "spell": ["encounter_effect", "puzzle_solution"],
        "class": ["player_option", "npc_template"],
        "background": ["social_hook", "debt_or_contact"],
        "race": ["ancestry_hook", "settlement_hook"],
        "creature": ["encounter", "threat_vector"],
        "item": ["reward", "access_key"],
        "plane": ["travel_hook", "world_modifier"],
        "faction": ["patron", "rival", "reputation_shift"],
        "region": ["site_seed", "travel_route"],
        "mission": ["mission_contract"],
    }
    return mapping.get(type_name, ["reference"])


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Classify PRIMUS blocks into CatalogEntries.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--license", default="Restricted", choices=["Open", "Private", "Restricted", "Unknown"])
    parser.add_argument("--subbox", default="Canon")
    args = parser.parse_args()

    blocks = read_jsonl(Path(args.input))
    entries = []
    for block in blocks:
        text = block.get("text", "")
        type_name = classify(text)
        entry_id = stable_id(block.get("source_name"), block.get("page"), block.get("block_id"), prefix="ce")
        entries.append(
            {
                "EntryID": entry_id,
                "Type": type_name,
                "Name": name_from(block, type_name),
                "Box": box_for(type_name),
                "Subbox": args.subbox,
                "Source": block.get("source_name") or "unknown",
                "SourcePath": block.get("source_path") or "",
                "Page": block.get("page") or "",
                "Snippet": short_snippet(text),
                "Summary": short_snippet(text, limit=140),
                "Affects": default_affects(type_name),
                "NeverAffects": ["core_rules_without_validation", "worldstate_without_delta_p"],
                "InstancingHints": default_hints(type_name),
                "Confidence": "Medium" if type_name != "rule" else "Low",
                "LicenseStatus": args.license,
                "Notes": "Heuristic classification; review before promotion.",
            }
        )

    write_jsonl(Path(args.out), entries)
    print(f"wrote {len(entries)} entries -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
