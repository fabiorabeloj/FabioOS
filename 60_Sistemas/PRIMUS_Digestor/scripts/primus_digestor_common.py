from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from pathlib import Path
from typing import Any, Iterable


REQUIRED_FIELDS = [
    "EntryID",
    "Type",
    "Name",
    "Box",
    "Subbox",
    "Source",
    "Page",
    "Snippet",
    "Affects",
    "NeverAffects",
    "InstancingHints",
    "Confidence",
    "LicenseStatus",
]

ALLOWED_TYPES = {
    "race",
    "subrace",
    "class",
    "subclass",
    "background",
    "feat",
    "spell",
    "item",
    "magic_item",
    "creature",
    "npc",
    "deity",
    "plane",
    "region",
    "settlement",
    "site",
    "dungeon",
    "faction",
    "organization",
    "rule",
    "procedure",
    "generator",
    "mission",
    "encounter",
    "hazard",
    "trap",
    "puzzle",
    "reward",
    "consequence",
}


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def slugify(value: str, fallback: str = "entry") -> str:
    normalized = unicodedata.normalize("NFKD", value or "")
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text).strip("-").lower()
    return slug or fallback


def stable_id(*parts: Any, prefix: str = "ce") -> str:
    raw = "|".join(str(part) for part in parts)
    digest = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:12]
    return f"{prefix}-{digest}"


def clean_space(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").replace("\uf0b7", "-")).strip()


def short_snippet(text: str, limit: int = 220) -> str:
    compact = clean_space(text)
    if len(compact) <= limit:
        return compact
    return compact[: limit - 3].rstrip() + "..."


def parse_args(description: str) -> argparse.ArgumentParser:
    return argparse.ArgumentParser(description=description)


def validate_entry(entry: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field in REQUIRED_FIELDS:
        value = entry.get(field)
        if value in (None, "", []):
            errors.append(f"missing:{field}")
    if entry.get("Type") and entry["Type"] not in ALLOWED_TYPES:
        errors.append(f"invalid_type:{entry['Type']}")
    for field in ("Affects", "NeverAffects", "InstancingHints"):
        if field in entry and not isinstance(entry[field], list):
            errors.append(f"not_list:{field}")
    if entry.get("Confidence") not in (None, "High", "Medium", "Low"):
        errors.append(f"invalid_confidence:{entry.get('Confidence')}")
    if entry.get("LicenseStatus") not in (None, "Open", "Private", "Restricted", "Unknown"):
        errors.append(f"invalid_license:{entry.get('LicenseStatus')}")
    return errors
