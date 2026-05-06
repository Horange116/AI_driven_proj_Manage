# T03 Pipeline Spec: Normalize hybrid-auto JSON

## Goal

Build a reproducible local pipeline that converts MinerU hybrid-auto parser JSON into DocReview normalized JSON.

This task is for Codex running inside the repository. Codex should solve it by writing and running local Python scripts and shell commands. Do not solve it by manually reading JSON files one by one in chat, and do not rely on external assistant tools to inspect every JSON file.

T03 only builds the structured data layer. Do not perform DHF/DMR consistency review findings in this task.

## Scope

Only process these two folders:

```text
data_Processed/DHF -梳理版_预处理_hybrid-auto处理
data_Processed/DMR-全-20260421_预处理_hybrid-auto处理
```

Use this path inventory if helpful:

```text
tasks/hybrid_auto_json_paths.md
```

If the path inventory contains paths beginning with `Projects/AI_driven_proj_Manage/`, convert them to repository-relative paths before reading files.

## Do not modify

Do not modify, delete, move, or overwrite anything under:

```text
data_Processed/
```

Do not rerun MinerU.

Do not call LLMs or external APIs.

Do not run full-batch normalized JSON conversion until the sample pipeline passes and the user approves full conversion.

## Raw JSON grouping rule

A typical processed document directory contains up to four JSON files:

```text
*_content_list.json
*_content_list_v2.json
*_middle.json
*_model.json
```

For each document group:

```text
main source:      *_content_list_v2.json
fallback source:  *_content_list.json
auxiliary refs:   *_middle.json, *_model.json
```

If both v1 and v2 exist, do not create duplicate normalized documents. Use v2 as the main source and record v1 as fallback metadata.

## Output locations

Create scripts under:

```text
scripts/
```

Create generated outputs under:

```text
outputs/t03_hybrid_auto/
```

Expected generated files:

```text
outputs/t03_hybrid_auto/inventory.json
outputs/t03_hybrid_auto/inventory.md
outputs/t03_hybrid_auto/sample_analysis.json
outputs/t03_hybrid_auto/sample_analysis.md
outputs/t03_hybrid_auto/normalized_sample/
outputs/t03_hybrid_auto/manifest_sample.json
outputs/t03_hybrid_auto/validation_sample.md
```

---

# Pipeline

## P00. Prepare output directory

Run:

```bash
mkdir -p outputs/t03_hybrid_auto/normalized_sample
```

Expected result:

```text
outputs/t03_hybrid_auto/normalized_sample/ exists
```

## P01. Build hybrid-auto inventory

Create:

```text
scripts/t03_build_hybrid_inventory.py
```

Purpose:

Discover JSON files, normalize paths, classify file roles, and group files by processed document directory.

Run:

```bash
python scripts/t03_build_hybrid_inventory.py \
  --dhf-root "data_Processed/DHF -梳理版_预处理_hybrid-auto处理" \
  --dmr-root "data_Processed/DMR-全-20260421_预处理_hybrid-auto处理" \
  --path-list tasks/hybrid_auto_json_paths.md \
  --out-json outputs/t03_hybrid_auto/inventory.json \
  --out-md outputs/t03_hybrid_auto/inventory.md
```

Required behavior:

- Accept a missing DMR folder gracefully, but report it clearly.
- Normalize path-list entries into repository-relative paths.
- Only keep paths under the two allowed hybrid-auto folders.
- Classify JSON role by suffix: `content_list`, `content_list_v2`, `middle`, `model`, `other_json`.
- Group files by source document directory.
- Record parser subfolder as `office`, `hybrid_auto`, or `unknown`.
- Select `main_source` using v2 first, then v1 fallback.

Required inventory fields:

```text
summary.json_files
summary.document_groups
summary.dhf_groups
summary.dmr_groups
summary.content_list
summary.content_list_v2
summary.middle
summary.model
summary.other_json
groups[].group_id
groups[].dataset
groups[].document_dir
groups[].parser_subdir
groups[].main_source
groups[].fallback_source
groups[].auxiliary.middle
groups[].auxiliary.model
groups[].all_json
warnings[]
```

P01 acceptance criteria:

- `inventory.json` is valid JSON.
- `inventory.md` gives a concise human-readable summary.
- Every group has at most one selected `main_source`.
- If both v1 and v2 exist, `main_source` is v2.
- No output is written under `data_Processed/`.

## P02. Analyze representative samples

Create:

```text
scripts/t03_analyze_hybrid_samples.py
```

Purpose:

Read a small representative subset from `inventory.json` and summarize raw JSON structure. This stage confirms the converter assumptions.

Run:

```bash
python scripts/t03_analyze_hybrid_samples.py \
  --inventory outputs/t03_hybrid_auto/inventory.json \
  --out-json outputs/t03_hybrid_auto/sample_analysis.json \
  --out-md outputs/t03_hybrid_auto/sample_analysis.md \
  --max-samples 12
```

Sampling targets:

- at least 2 DHF `content_list_v2` samples
- at least 1 DMR `content_list_v2` sample, if DMR exists
- at least 1 fallback `content_list` sample
- at least 1 `office` sample
- at least 1 `hybrid_auto` sample
- at least 1 `_middle.json` sample
- at least 1 `_model.json` sample

Required analysis fields per sample:

```text
path
json_role
top_level_type
top_level_length
block_type_counts
common_fields
has_text
has_table_body
has_content_html
has_page_idx
notes
```

Do not copy large JSON content into the report. Keep snippets short if absolutely needed.

P02 acceptance criteria:

- `sample_analysis.json` is valid JSON.
- `sample_analysis.md` explains whether v2 is suitable as the main input.
- Parse failures are listed with path and error.

## P03. Implement normalizer

Create:

```text
scripts/normalize_hybrid_auto_json.py
```

Purpose:

Convert selected document groups into DocReview normalized JSON.

Run sample mode only:

```bash
python scripts/normalize_hybrid_auto_json.py \
  --inventory outputs/t03_hybrid_auto/inventory.json \
  --out-dir outputs/t03_hybrid_auto/normalized_sample \
  --manifest outputs/t03_hybrid_auto/manifest_sample.json \
  --limit 20
```

Do not run without `--limit` in this task unless explicitly approved later.

Main input selection:

```text
if content_list_v2 exists: use content_list_v2
else if content_list exists: use content_list
else: skip group and record failure
```

Minimum normalized document fields:

```text
doc_id
dataset
stage
document_name
parse_backend
parser_subdir
source_json_path
fallback_source_json_path
auxiliary_json_paths
blocks
```

Minimum normalized block fields:

```text
block_id
block_order
type
raw_type
page_idx
text
raw_html
source_anchor.json_path
source_anchor.page_idx
source_anchor.block_order
```

Normalization rules for `*_content_list.json`:

- `text` -> block text
- `table_body` -> `raw_html` and plain text
- `header` -> normalized type `header`
- `footer` -> normalized type `footer`
- `page_idx` -> page index

Normalization rules for `*_content_list_v2.json`:

- flatten nested page/block lists into one ordered `blocks` list
- outer list index is page index when block has no explicit `page_idx`
- `content.html` -> `raw_html` and plain text
- `content.page_header_content` -> normalized type `header`
- `content.page_footer_content` -> normalized type `footer`
- nested text fragments under `content` -> joined plain text

Text extraction rules:

- Use Python standard library where possible.
- A simple HTML stripper based on `html.parser` is acceptable.
- Preserve readable table cell order.
- Do not use OCR.
- Do not call an LLM.

P03 acceptance criteria:

- Script records per-file failures in the manifest instead of silently skipping.
- Sample outputs are valid JSON.
- The same source document is not duplicated because both v1 and v2 exist.
- No output is written under `data_Processed/`.

## P04. Validate normalized sample

Create:

```text
scripts/t03_validate_normalized_sample.py
```

Run:

```bash
python scripts/t03_validate_normalized_sample.py \
  --input-dir outputs/t03_hybrid_auto/normalized_sample \
  --manifest outputs/t03_hybrid_auto/manifest_sample.json \
  --out-md outputs/t03_hybrid_auto/validation_sample.md
```

Validation checks:

- every normalized file is valid JSON
- required document fields exist
- `blocks` is a list
- every block has required block fields
- table blocks keep `raw_html` when source has HTML
- no duplicate `doc_id`

P04 acceptance criteria:

- `validation_sample.md` exists.
- Validation result is clearly PASS or FAIL.
- Failures include file path and reason.

## P05. Stop point

Stop after sample validation.

Do not run full conversion in this task unless the user explicitly approves it after reviewing:

```text
outputs/t03_hybrid_auto/inventory.md
outputs/t03_hybrid_auto/sample_analysis.md
outputs/t03_hybrid_auto/validation_sample.md
```

---

# Final deliverables

Codex should produce or update:

```text
scripts/t03_build_hybrid_inventory.py
scripts/t03_analyze_hybrid_samples.py
scripts/normalize_hybrid_auto_json.py
scripts/t03_validate_normalized_sample.py
outputs/t03_hybrid_auto/inventory.json
outputs/t03_hybrid_auto/inventory.md
outputs/t03_hybrid_auto/sample_analysis.json
outputs/t03_hybrid_auto/sample_analysis.md
outputs/t03_hybrid_auto/normalized_sample/
outputs/t03_hybrid_auto/manifest_sample.json
outputs/t03_hybrid_auto/validation_sample.md
```

# Final response expected from Codex

After running the pipeline, report only:

```text
1. Commands executed
2. Files created
3. Summary counts from inventory
4. Sample conversion result
5. Validation PASS/FAIL
6. Whether full conversion is ready to run
```

Do not include large JSON dumps in the final response.
