from __future__ import annotations

import json
import sys
from pathlib import Path

from primus_digestor_common import read_jsonl, validate_entry


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Validate PRIMUS CatalogEntries.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--report", default="")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    entries = read_jsonl(Path(args.input))
    problems = []
    for entry in entries:
        errors = validate_entry(entry)
        if errors:
            problems.append({"EntryID": entry.get("EntryID"), "Name": entry.get("Name"), "errors": errors})

    result = {"input": args.input, "entries": len(entries), "valid": len(entries) - len(problems), "invalid": len(problems), "problems": problems}
    print(json.dumps(result, ensure_ascii=False, indent=2))

    if args.report:
        report_path = Path(args.report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    if args.strict and problems:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
