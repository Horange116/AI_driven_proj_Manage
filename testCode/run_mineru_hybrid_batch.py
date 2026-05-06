#!/usr/bin/env python3
"""Recursively run MinerU hybrid-auto-engine for the PT9L DHF/DMR folders."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path("/home/s2025244189/s2025244265/AI_driven_proj_Manage")
DATA_PROCESSED = PROJECT_ROOT / "data_Processed"

JOBS = {
    "DHF": {
        "input": DATA_PROCESSED / "DHF -梳理版_预处理",
        "output": DATA_PROCESSED / "DHF -梳理版_预处理_hybrid-auto处理",
    },
    "DMR": {
        "input": DATA_PROCESSED / "DMR-全-20260421_预处理",
        "output": DATA_PROCESSED / "DMR-全-20260421_预处理_hybrid-auto处理",
    },
}

SUPPORTED_SUFFIXES = {
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".docx",
    ".xlsx",
    ".pptx",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run MinerU hybrid-auto-engine recursively for DHF and DMR.",
    )
    parser.add_argument(
        "--only",
        choices=["DHF", "DMR", "all"],
        default="all",
        help="Choose which dataset to process. Default: all.",
    )
    parser.add_argument(
        "--conda-env",
        default="mineru",
        help="Conda environment name that contains the mineru command. Default: mineru.",
    )
    parser.add_argument(
        "--model-source",
        default="modelscope",
        help="Set MINERU_MODEL_SOURCE if it is not already set. Default: modelscope.",
    )
    parser.add_argument(
        "--backend",
        default="hybrid-auto-engine",
        help="MinerU backend. Default: hybrid-auto-engine.",
    )
    parser.add_argument(
        "--method",
        default="auto",
        choices=["auto", "txt", "ocr"],
        help="MinerU parse method. Default: auto.",
    )
    parser.add_argument(
        "--lang",
        default="ch",
        help="Document language for OCR. Default: ch.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Process at most N files, useful for a smoke test. Default: 0 means no limit.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-run files even when a previous output folder already contains results.",
    )
    parser.add_argument(
        "--fail-fast",
        action="store_true",
        help="Stop immediately if one file fails. Default: continue and summarize failures.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned files without running MinerU.",
    )
    return parser.parse_args()


def iter_input_files(input_root: Path) -> list[Path]:
    files = [
        path
        for path in input_root.rglob("*")
        if path.is_file() and path.suffix.lower() in SUPPORTED_SUFFIXES
    ]
    return sorted(files, key=lambda p: str(p.relative_to(input_root)).lower())


def expected_doc_dir(input_root: Path, output_root: Path, source_file: Path) -> Path:
    rel_path = source_file.relative_to(input_root)
    return output_root / rel_path.parent / source_file.stem


def has_existing_result(doc_dir: Path) -> bool:
    if not doc_dir.exists():
        return False
    return any(
        path.is_file()
        and (
            path.suffix.lower() == ".md"
            or path.name.endswith("_content_list.json")
            or path.name.endswith("_content_list_v2.json")
            or path.name.endswith("_middle.json")
        )
        for path in doc_dir.rglob("*")
    )


def build_command(args: argparse.Namespace, source_file: Path, output_dir: Path) -> list[str]:
    return [
        "conda",
        "run",
        "-n",
        args.conda_env,
        "mineru",
        "-p",
        str(source_file),
        "-o",
        str(output_dir),
        "-b",
        args.backend,
        "-m",
        args.method,
        "-l",
        args.lang,
    ]


def run_one(
    args: argparse.Namespace,
    dataset: str,
    input_root: Path,
    output_root: Path,
    source_file: Path,
    index: int,
    total: int,
    env: dict[str, str],
) -> int:
    rel_path = source_file.relative_to(input_root)
    file_output_root = output_root / rel_path.parent
    doc_dir = expected_doc_dir(input_root, output_root, source_file)
    file_output_root.mkdir(parents=True, exist_ok=True)

    if not args.force and has_existing_result(doc_dir):
        print(f"[SKIP] {dataset} {index}/{total}: {rel_path}")
        return 0

    cmd = build_command(args, source_file, file_output_root)
    print(f"[RUN ] {dataset} {index}/{total}: {rel_path}")
    print("       " + " ".join(quote_arg(part) for part in cmd))

    if args.dry_run:
        return 0

    completed = subprocess.run(cmd, env=env, text=True)
    if completed.returncode == 0:
        print(f"[DONE] {dataset} {index}/{total}: {rel_path}")
    else:
        print(f"[FAIL] {dataset} {index}/{total}: {rel_path} | code={completed.returncode}")
    return completed.returncode


def quote_arg(value: str) -> str:
    if not value:
        return "''"
    if any(char.isspace() for char in value) or any(char in value for char in "'\"()&;"):
        return "'" + value.replace("'", "'\"'\"'") + "'"
    return value


def main() -> int:
    args = parse_args()

    selected = ["DHF", "DMR"] if args.only == "all" else [args.only]
    env = os.environ.copy()
    env.setdefault("MINERU_MODEL_SOURCE", args.model_source)

    print("MinerU hybrid batch started:", datetime.now().isoformat(timespec="seconds"))
    print("PROJECT_ROOT:", PROJECT_ROOT)
    print("MINERU_MODEL_SOURCE:", env.get("MINERU_MODEL_SOURCE", ""))
    print("Selected datasets:", ", ".join(selected))

    failures: list[tuple[str, Path, int]] = []
    processed_count = 0

    for dataset in selected:
        input_root = JOBS[dataset]["input"]
        output_root = JOBS[dataset]["output"]

        if not input_root.exists():
            print(f"[ERROR] Missing input folder for {dataset}: {input_root}")
            return 2

        files = iter_input_files(input_root)
        if args.limit > 0:
            files = files[: args.limit]

        print(f"\n[{dataset}] input : {input_root}")
        print(f"[{dataset}] output: {output_root}")
        print(f"[{dataset}] files : {len(files)}")

        for index, source_file in enumerate(files, start=1):
            code = run_one(
                args=args,
                dataset=dataset,
                input_root=input_root,
                output_root=output_root,
                source_file=source_file,
                index=index,
                total=len(files),
                env=env,
            )
            if code == 0:
                processed_count += 1
                continue

            failures.append((dataset, source_file, code))
            if args.fail_fast:
                break

        if failures and args.fail_fast:
            break

    print("\nMinerU hybrid batch finished:", datetime.now().isoformat(timespec="seconds"))
    print("Successful or skipped files:", processed_count)
    print("Failed files:", len(failures))

    for dataset, source_file, code in failures:
        print(f"[FAILED] {dataset} code={code}: {source_file}")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
