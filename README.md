# PT9L DocReview Project

This project is an exploratory intelligent document review workflow for PT9L medical device project files.

The goal is to build a pipeline that can parse DHF/DMR documents, structure their contents, and later detect consistency or traceability problems across documents.

---

## What This Project Is About

This is not just a document summarization project.

The target is cross-document review:

```text
DHF upstream requirements
  -> design inputs
  -> risk controls
  -> verification / validation
  -> design outputs
  -> DMR production and inspection files
```

Example target question:

```text
If a DHF requirement says thermometer accuracy must be +/-0.2 C,
do downstream design verification and DMR inspection files preserve and verify that same requirement?
```

---

## Main Directories

```text
data_Initial/
  Original DHF and DMR files.

data_Processed/
  Preprocessed files and MinerU/skill parsed outputs.

docs/
  Project notes and reports.

outputs/
  Generated inventory files.

MinerU/
  Local MinerU source repository.

hermes-agent/
  Local Hermes Agent source repository.
```

---

## Existing Processed Data

Important processed folders:

```text
data_Processed/DHF -梳理版_预处理
data_Processed/DMR-全-20260421_预处理
data_Processed/DHF -梳理版_预处理_mineru处理
data_Processed/DMR-全-20260421_预处理_mineru处理
data_Processed/DHF -梳理版_预处理_mineru处理&部分pdf用skill处理
```

The preprocessed folders appear to have:

- removed or excluded unsuitable attachments such as `.ai`, `.dwg`, `.zip`, `.rar`, `.tmp`, `.scc`
- converted old Office formats like `.doc` and `.xls` into `.docx` and `.xlsx`
- preserved parseable files for Markdown conversion

The MinerU folders contain Markdown outputs.

The DHF enhanced folder:

```text
DHF -梳理版_预处理_mineru处理&部分pdf用skill处理
```

contains all Markdown from the normal MinerU version and adds page-level `page-xxx-vlm.md` files for selected PDFs.

---

## Current Status

```text
T00 Project goal confirmation: completed
T01 Document asset inventory: completed
T02 Parsing baseline confirmation: completed
T03 Unified structured JSON: next
```

Completed inventory result:

```text
Original files: 256
DHF: 239
DMR: 17
Duplicate groups: 7
Duplicate files involved: 14
```

Current decision:

```text
Do not rerun full raw document parsing now.
Use existing Markdown outputs as the T03 input baseline.
```

---

## Recommended Workflow

Current recommended path:

```text
Existing Markdown outputs
  -> normalized JSON
  -> knowledge schema
  -> search/query layer
  -> single-file checks
  -> cross-document checks
  -> findings with evidence
  -> Agent-assisted review
```

Next immediate work:

```text
T03: define normalized JSON format and test it on a few sample Markdown files.
```

Recommended first T03 samples:

```text
1. One DMR Markdown file from DMR-全-20260421_预处理_mineru处理
2. One DHF office Markdown file from DHF -梳理版_预处理_mineru处理&部分pdf用skill处理
3. One DHF page-vlm Markdown file from the enhanced DHF folder
```

---

## MinerU Notes

MinerU can output Markdown and JSON-like intermediate files, but the current team baseline mostly uses Markdown.

Safe local command pattern:

```bash
mineru -p "input_path" -o "output_dir" -b pipeline -m auto -l ch
```

Important:

```text
Always pass -b pipeline for lightweight local tests.
Avoid hybrid-auto-engine unless there is enough disk/GPU capacity.
```

The local hybrid path was considered too large and risky for the current environment because dependencies and model caches may consume C drive space.

---

## Hermes / Kimi Notes

Hermes Agent was tested with a Kimi-compatible custom endpoint.

It works, but it is token-heavy and should not be used for broad scanning.

Use Hermes/Kimi later for focused tasks such as:

```text
Given two evidence snippets from DHF and DMR, determine whether they conflict and explain severity.
```

Do not use it to read the full repository or all documents blindly.

---

## Files To Read First

If continuing this project in a new conversation, read:

```text
TASK_STATE.md
AGENTS.md
docs/T00_project_scope.md
docs/T01_inventory_report.md
DocReview_任务状态卡.md
```

