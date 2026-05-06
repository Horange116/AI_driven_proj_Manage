# AGENTS

This file defines how AI assistants should work on this repository.

---

## Project Summary

This repository is for the PT9L DocReview project.

The objective is to build an intelligent document review workflow for medical device project files. The core task is to review traceability and consistency between DHF and DMR documents.

Do not treat the project as a generic document summarization task.

Main review chain:

```text
DHF requirements / design inputs
  -> design plans / risk controls / verification / validation
  -> design outputs / drawings / BOM / inspection requirements
  -> DMR production process / work instructions / inspection / release requirements
```

Expected findings include:

- duplicate or copied files
- missing downstream requirements
- parameter conflicts
- version inconsistencies
- broken traceability
- design requirements not reflected in production or inspection files

---

## Collaboration Style

The user is learning while building.

Default assistant behavior:

```text
Explain first.
Inspect before acting.
Keep answers concise.
Show current task state in chat.
Do not blindly modify files.
Do not modify any file unless the user has explicitly approved that specific edit.
Do not perform large batch operations unless explicitly requested.
Ask or state the intended operation before writing files.
```

File modification rule:

```text
Before creating, editing, deleting, moving, or overwriting any file, the assistant must first explain:
1. which file(s) will be changed
2. what will be changed
3. why the change is needed

Then wait for explicit user approval.

The only exception is when the user's latest message directly and clearly asks for that specific file change.
Even then, keep the edit narrowly scoped to the requested change.
```

The user prefers:

- concise key information
- step-by-step learning
- visible reasoning about what each step is doing
- minimal token waste
- local code/scripts only when necessary

If the user asks "current task", show a short status summary instead of telling them to open files.

---

## Current State

Read `TASK_STATE.md` first.

Current high-level state:

```text
T00 completed
T01 completed
T02 completed
T03 next
```

Next work:

```text
T03: Convert existing Markdown outputs into normalized JSON.
```

---

## Data Rules

Important directories:

```text
data_Initial/
  Original files.

data_Processed/
  Preprocessed and parsed files.

outputs/
  Generated inventory and reports.

docs/
  Human-readable reports and notes.
```

Preferred T03 inputs:

```text
data_Processed/DHF -梳理版_预处理_mineru处理&部分pdf用skill处理
data_Processed/DMR-全-20260421_预处理_mineru处理
```

Do not restart by parsing all raw files unless explicitly asked.

---

## Known Decisions

1. Markdown is acceptable as an interim format.
2. JSON is the long-term automation format.
3. Existing processed Markdown should be reused.
4. Local `hybrid-auto-engine` is not recommended due to size, model downloads, and C drive pressure.
5. Use MinerU `pipeline` only for small local experiments.
6. Use Hermes/Kimi only for focused reasoning tasks, not full-folder scanning.

---

## MinerU Notes

Useful command pattern:

```bash
mineru -p "input_path" -o "output_dir" -b pipeline -m auto -l ch
```

Always include:

```text
-b pipeline
```

Otherwise MinerU may default to `hybrid-auto-engine`, which is heavy.

Avoid:

```text
mineru[core]
hybrid-auto-engine
full local model downloads
```

unless the user explicitly decides to allocate disk/GPU resources.

---

## Hermes Notes

Hermes was tested with Kimi through a custom endpoint.

Use it sparingly.

Good use:

```text
Given these two extracted evidence snippets, identify conflict and severity.
```

Bad use:

```text
Scan this entire repository and find all problems.
```

---

## Recommended Next Step

For T03, do not immediately convert everything.

First inspect three sample Markdown structures:

```text
1. one DMR Markdown file
2. one DHF office Markdown file
3. one DHF page-vlm Markdown file
```

Then define a small normalized JSON schema and only then run conversion.
