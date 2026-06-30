from __future__ import annotations

import sys
from pathlib import Path

from primus_digestor_common import parse_args, write_jsonl


def iter_files(paths: list[str]) -> list[Path]:
    found: list[Path] = []
    for raw in paths:
        p = Path(raw)
        if p.is_dir():
            found.extend(x for x in p.rglob("*") if x.is_file())
        elif p.is_file():
            found.append(p)
    return found


def extract_txt(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8", errors="replace")
    return [{"source_path": str(path), "source_name": path.name, "page": 1, "text": text, "extractor": "text"}]


def extract_pdf(path: Path) -> list[dict]:
    try:
        import fitz  # type: ignore
    except Exception:
        try:
            from pypdf import PdfReader  # type: ignore
        except Exception as exc:
            raise RuntimeError("PDF extraction requires PyMuPDF or pypdf") from exc
        reader = PdfReader(str(path))
        rows = []
        for i, page in enumerate(reader.pages, start=1):
            rows.append({"source_path": str(path), "source_name": path.name, "page": i, "text": page.extract_text() or "", "extractor": "pypdf"})
        return rows

    doc = fitz.open(str(path))
    rows = []
    for i, page in enumerate(doc, start=1):
        rows.append({"source_path": str(path), "source_name": path.name, "page": i, "text": page.get_text("text"), "extractor": "pymupdf"})
    return rows


def extract_docx(path: Path) -> list[dict]:
    try:
        import docx  # type: ignore
    except Exception as exc:
        raise RuntimeError("DOCX extraction requires python-docx") from exc
    document = docx.Document(str(path))
    text = "\n".join(p.text for p in document.paragraphs if p.text.strip())
    return [{"source_path": str(path), "source_name": path.name, "page": 1, "text": text, "extractor": "python-docx"}]


def main() -> int:
    parser = parse_args("Extract text from PRIMUS source files into JSONL pages.")
    parser.add_argument("paths", nargs="+")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    rows: list[dict] = []
    for path in iter_files(args.paths):
        suffix = path.suffix.lower()
        try:
            if suffix in {".txt", ".md"}:
                rows.extend(extract_txt(path))
            elif suffix == ".pdf":
                rows.extend(extract_pdf(path))
            elif suffix == ".docx":
                rows.extend(extract_docx(path))
        except Exception as exc:
            rows.append({"source_path": str(path), "source_name": path.name, "page": None, "text": "", "extractor": "error", "error": str(exc)})

    write_jsonl(Path(args.out), rows)
    print(f"wrote {len(rows)} pages -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
