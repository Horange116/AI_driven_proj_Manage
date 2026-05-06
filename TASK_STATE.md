# TASK_STATE

Purpose: current progress snapshot for the PT9L DocReview project. This file is meant to let a new conversation or another agent quickly understand what has already happened and what should happen next.

Last updated: 2026-05-06

---

## Current Position

```text
T00 Project goal confirmation: completed
T01 Document asset inventory: completed
T02 Parsing baseline confirmation: completed
T03 Unified structured JSON: next task
```

Current main task:

```text
Enter T03 and design how to convert existing Markdown / page-level Markdown outputs into normalized JSON.
```

Do not restart from raw parsing unless there is a clear reason. The current decision is to consume the existing processed Markdown baseline first.

---

## Project Goal

The project is not simple document summarization.

The goal is to build an intelligent review workflow for PT9L medical device project documents, focused on consistency and traceability across:

```text
DHF upstream requirements / design inputs
  -> design plans / risk controls / verification / validation
  -> design outputs / drawings / BOM / inspection requirements
  -> DMR production instructions / process control / inspection / release documents
```

Expected final behavior:

```text
Given a new project folder,
the system should automatically parse documents,
build structured data,
find conflicts or broken traceability,
and output findings with evidence.
```

Example review pattern:

```text
DHF requirement: thermometer accuracy must be +/-0.2 C
DMR production/inspection file: should preserve and verify +/-0.2 C
If downstream files say +/-0.5 C, omit the check, or downgrade full inspection to sampling, it should become a finding candidate.
```

---

## Collaboration Rule

The user is learning while building. Default behavior should be:

```text
Explain first.
Inspect before acting.
Do not blindly modify files.
Prefer concise explanations.
Only write files or run batch jobs when explicitly asked.
Show task status in chat; do not force the user to open state files.
```

The user wants participation, not a fully delegated black-box build.

---

## Data Directories

```text
data_Initial/
  Original project files.

data_Processed/
  Processed files from teammate and our exploration.

docs/
  Project notes and reports.

outputs/
  Generated inventories and other local outputs.

MinerU/
  Local MinerU source repository.

hermes-agent/
  Local Hermes Agent source repository.
```

Important processed directories:

```text
data_Processed/DHF -梳理版_预处理
data_Processed/DMR-全-20260421_预处理
data_Processed/DHF -梳理版_预处理_mineru处理
data_Processed/DMR-全-20260421_预处理_mineru处理
data_Processed/DHF -梳理版_预处理_mineru处理&部分pdf用skill处理
```

Interpretation:

```text
*_预处理
  Cleaned input folders: duplicates and unsuitable attachments were handled;
  old Office formats were converted to docx/xlsx.

*_mineru处理
  MinerU pipeline Markdown baseline.

*_mineru处理&部分pdf用skill处理
  Enhanced DHF version. It contains all Markdown from the normal MinerU version
  and adds page-level VLM/skill Markdown for selected PDFs.
```

---

## Completed Work

### T00 - Project Goal Confirmation

Status: completed.

Key conclusions:

- The project is about DHF/DMR relationship review, not simple file summarization.
- Markdown is acceptable as an interim format.
- JSON is the long-term target for automation.
- Local large model execution is not required.
- LLM/Agent work can use remote APIs such as Kimi through Hermes, but only after the data is prepared.

Relevant file:

```text
docs/T00_project_scope.md
```

### T01 - Document Asset Inventory

Status: completed.

Original inventory result:

```text
Total original files: 256
DHF: 239
DMR: 17
Duplicate groups found: 7
Duplicate files involved: 14
```

Original format distribution highlights:

```text
pdf: 91
doc: 75
xls: 45
xlsx: 17
docx: 9
ai: 9
dwg: 2
zip/rar/tmp/scc: several
```

Generated files:

```text
outputs/inventory/files_manifest.json
outputs/inventory/files_manifest.csv
outputs/inventory/duplicates_report.json
docs/T01_inventory_report.md
```

Important interpretation:

```text
The task page mentioned about 196 documents, but the workspace has 256 files.
The difference is due to attachments, duplicate nested folders, drawings, archives, temp files, and source design files.
```

### T02 - Parsing Baseline Confirmation

Status: completed.

We did not rerun full parsing. We inspected the already processed data.

Preprocessing appears to have done:

```text
1. Removed/excluded unsuitable attachments:
   .ai, .dwg, .zip, .rar, .tmp, .scc

2. Converted old Office formats:
   .doc -> .docx
   .xls -> .xlsx

3. Kept parseable formats:
   .docx, .xlsx, .pdf, small number of images
```

Original vs preprocessed:

```text
DHF original: 239 files
DHF preprocessed: 203 files

DMR original: 17 files
DMR preprocessed: 18 files
```

Known excluded DHF files by filename comparison:

```text
08 T1样机/12-生物相容性/同PT5生物相容性报告/vssver2.scc
09-设计输出/PT9L-设计输出清单一.rar
09-设计输出/设计输出清单二.zip
09-设计输出/PT9L-设计输出清单一/设计输出清单一/~WRL2792.tmp
09-设计输出/设计输出清单二/早期图纸.zip
09-设计输出/设计输出清单二/设计输出清单二.zip
09-设计输出/设计输出清单二/设计输出清单二/图纸/T-Z1-上盖-v2.0-20241104.pdf
09-设计输出/设计输出清单二/设计输出清单二/图纸/T-Z1-下盖-v1.0-20241104.pdf
09-设计输出/设计输出清单二/设计输出清单二/图纸/T-Z1-探头盖-v1.0-20241104.pdf
```

Markdown baseline comparison:

```text
DHF normal MinerU version:
  total files: 1234
  md files: 225

DHF enhanced skill version:
  total files: 1629
  md files: 383

The enhanced version contains all Markdown files from the normal version and adds 158 extra md files.
The extra files are mostly page-xxx-vlm.md outputs from selected PDFs.

DMR MinerU version:
  md files: 17
```

Important decision:

```text
Use the enhanced DHF version as preferred T03 input.
Use the DMR MinerU Markdown output as DMR input.
Do not rerun full MinerU parsing for now.
```

---

## Hermes / Kimi Experiment

Hermes Agent was installed and tested.

Findings:

- Windows native Hermes was problematic.
- WSL/Ubuntu is preferred for running Hermes.
- Kimi API through a custom endpoint was tested and returned a response.
- Hermes is token-heavy as an agent framework; do not use it for casual chat or full-folder blind scanning.

Practical rule:

```text
Use Hermes/Kimi only for small, high-value reasoning tasks after local preprocessing.
Do not ask Hermes to scan the entire project folder.
```

Good future use:

```text
Feed selected normalized JSON snippets or evidence pairs into Hermes
to generate conflict explanations and severity suggestions.
```

---

## MinerU Experiment

MinerU command became available in the conda base environment.

Important command pattern:

```bash
mineru -p "input_path" -o "output_dir" -b pipeline -m auto -l ch
```

Important issue:

```text
If -b pipeline is omitted, MinerU defaults to hybrid-auto-engine,
which requires heavy dependencies.
```

Do not use local `hybrid-auto-engine` for now:

- It is too large.
- It may download model caches to C drive.
- It is not appropriate for the current machine/storage setup.
- The current project already has a usable Markdown baseline.

Recommended approach:

```text
Only use pipeline for small experiments if needed.
Avoid mineru[core], hybrid-auto-engine, and full local model downloads.
```

---

## Next Task - T03 Unified Structured JSON

Goal:

```text
Convert existing Markdown outputs into normalized JSON that downstream code can process consistently.
```

Why:

```text
Markdown is good for humans and LLMs.
JSON is better for automation, indexing, rule checks, and evidence tracking.
```

Recommended T03 input folders:

```text
data_Processed/DHF -梳理版_预处理_mineru处理&部分pdf用skill处理
data_Processed/DMR-全-20260421_预处理_mineru处理
```

T03 should not start by processing all content semantically.

First design a simple file-level normalized schema:

```json
{
  "doc_id": "...",
  "dataset": "DHF or DMR",
  "stage": "...",
  "document_name": "...",
  "source_md_path": "...",
  "parse_backend": "office | auto | page_vlm",
  "blocks": [
    {
      "block_id": "...",
      "type": "heading | paragraph | table | image | unknown",
      "text": "...",
      "source_anchor": {
        "md_path": "...",
        "line_start": 1,
        "line_end": 10
      }
    }
  ]
}
```

First T03 subtask:

```text
Pick 3 sample Markdown files:
1 DMR office/auto md
1 DHF office md
1 DHF page-vlm md

Inspect structure and define the minimum normalized JSON schema.
```

Do not full-run conversion until sample schema is agreed.

