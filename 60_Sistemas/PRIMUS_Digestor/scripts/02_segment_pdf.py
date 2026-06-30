from __future__ import annotations

import re
import sys
from pathlib import Path

from primus_digestor_common import clean_space, read_jsonl, stable_id, write_jsonl


HEADING_RE = re.compile(r"^[A-Z0-9][A-Z0-9\s:;,\-()]{3,80}$")


def split_blocks(text: str) -> list[str]:
    chunks = re.split(r"\n\s*\n+", text or "")
    blocks: list[str] = []
    for chunk in chunks:
        compact = clean_space(chunk)
        if len(compact) >= 20:
            blocks.append(compact)
    return blocks


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Segment extracted PRIMUS pages into candidate blocks.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    pages = read_jsonl(Path(args.input))
    blocks: list[dict] = []
    for page in pages:
        for idx, text in enumerate(split_blocks(page.get("text", "")), start=1):
            first = text.split(". ", 1)[0][:80]
            heading = first if HEADING_RE.match(first.upper()) else ""
            blocks.append(
                {
                    "block_id": stable_id(page.get("source_name"), page.get("page"), idx, prefix="blk"),
                    "source_path": page.get("source_path"),
                    "source_name": page.get("source_name"),
                    "page": page.get("page"),
                    "block_index": idx,
                    "heading": heading,
                    "text": text,
                }
            )

    write_jsonl(Path(args.out), blocks)
    print(f"wrote {len(blocks)} blocks -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
