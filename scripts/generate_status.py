#!/usr/bin/env python3
"""Round 3 status generator for nepal-market-research (Markdown repo).

Counts real files, never a typed constant:
- case_studies = subdirectories of case-studies/
- datasets = data/*.csv files
This repo has no code test suite; tests fields are null with a note.
Writes status.json.
"""
import argparse
import json
from datetime import date
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    root = Path(ap.parse_args().root)
    cs = root / "case-studies"
    case_studies = len([d for d in cs.iterdir() if d.is_dir()]) if cs.is_dir() else 0
    datasets = len(list((root / "data").glob("*.csv"))) if (root / "data").is_dir() else 0
    status = {
        "repo": "nepal-market-research",
        "case_studies": case_studies,
        "datasets": datasets,
        "tests_passed": None,
        "tests_total": None,
        "tests_note": "No code tests (Markdown/research repo)",
        "generated_by": "scripts/generate_status.py (Round 3: file counts from disk)",
        "generated_at": date.today().isoformat(),
        "method": "case-study subdirectories and data/*.csv counted from disk",
    }
    (root / "status.json").write_text(json.dumps(status, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(status, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
