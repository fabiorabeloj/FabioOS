from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SAMPLE = ROOT / "tests" / "sample_blocks.jsonl"


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, cwd=ROOT)


def main() -> int:
    tmp = Path(tempfile.mkdtemp(prefix="primus_digestor_"))
    try:
        catalog = tmp / "catalog_entries.jsonl"
        report = tmp / "validation.json"
        out_dir = tmp / "markdown"
        run([sys.executable, str(SCRIPTS / "03_classify_entries.py"), "--input", str(SAMPLE), "--out", str(catalog), "--license", "Private"])
        run([sys.executable, str(SCRIPTS / "04_validate_entries.py"), "--input", str(catalog), "--report", str(report), "--strict"])
        run([sys.executable, str(SCRIPTS / "05_export_markdown.py"), "--input", str(catalog), "--out", str(out_dir)])
        generated = list(out_dir.glob("*.md"))
        if len(generated) != 3:
            raise SystemExit(f"expected 3 markdown files, got {len(generated)}")
        print("PRIMUS Digestor smoke test OK")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
