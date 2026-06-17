#!/usr/bin/env python3
"""Inspect available resume PDFs and report category/resume mapping state."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def infer_label(name: str) -> str:
    lower = name.lower()
    if any(k in name for k in ["Agent", "RAG", "应用", "工具"]):
        return "agent_or_applied_ai"
    if any(k in name for k in ["视觉", "影像", "CV", "cv"]):
        return "cv_or_imaging"
    if any(k in name for k in ["大模型", "多模态", "LLM", "VLM"]):
        return "llm_or_multimodal"
    if any(k in name for k in ["后训练", "RL", "评测", "Infra", "infra"]):
        return "post_training_or_infra"
    if "resume" in lower:
        return "general_resume"
    return "unknown"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", nargs="?", default=".")
    parser.add_argument("--max-depth", type=int, default=1)
    parser.add_argument("--expected-categories", type=int)
    args = parser.parse_args()

    root = Path(args.directory)
    pdfs = []
    for path in root.rglob("*.pdf"):
        depth = len(path.relative_to(root).parts)
        if depth <= args.max_depth:
            pdfs.append(path)
    pdfs = sorted(pdfs)
    variants = [{"path": str(p), "name": p.name, "label": infer_label(p.name)} for p in pdfs]
    count = len(variants)
    state = "unknown"
    if args.expected_categories is not None:
        if count == 0:
            state = "initialization"
        elif count < args.expected_categories:
            state = "transitional"
        elif count == args.expected_categories:
            state = "complete"
        else:
            state = "more_resumes_than_categories"
    result = {
        "directory": str(root),
        "resume_pdf_count": count,
        "expected_categories": args.expected_categories,
        "mapping_state": state,
        "variants": variants,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
