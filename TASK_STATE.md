# TASK_STATE

Purpose: current progress snapshot and execution guidance for the PT9L DocReview project. This file is the first file that Codex or a new assistant should read before continuing work.

Last updated: 2026-05-08

---

## 0. Current Position

```text
T00 Project goal confirmation: completed
T01 Document asset inventory: completed
T02 Parsing baseline confirmation: completed
T03 Unified structured JSON: likely completed or near completion, but must be verified
T04 Semantic extraction / knowledge-layer schema: next major stage after T03 validation passes
```

Current immediate task:

```text
Do not start new feature development yet.
First inspect the T03 hybrid-auto JSON normalization outputs and decide whether T03 is truly complete.
```

Reason:

```text
The older project state said T03 was the next task.
The newer work has introduced a T03 hybrid-auto JSON normalization task and may already have produced normalized JSON outputs.
Before moving to semantic extraction, Codex must verify what exists, whether the output quality is acceptable, and whether full conversion has been completed.
```

---

## 1. Source Documents for Planning

The current plan is the merged result of these files:

```text
DocReview_任务状态卡.md
  Original T00-T12 project task card and current status record.

/docs/Codex_执行总控_2026-05-08.md
  New staged plan from the teacher's updated thinking:
  S1 parse standardization, S2 semantic extraction, S3 intra-document consistency,
  S4 inter-document consistency, S5 cross-document/class-level patterns,
  S6 end-to-end pipeline and tiered routing.

tasks/T03_hybrid_auto_json_normalization.md
  Concrete T03 task spec for converting MinerU hybrid-auto JSON into DocReview normalized JSON.
```

Important interpretation:

```text
DocReview_任务状态卡.md still says T03 is the next task.
That is now partly outdated.
T03 should be treated as the active/completion-verification stage, not as a fresh design task.
```

---

## 2. Updated Project Mainline

The mainline is now:

```text
T00/T01/T02: project scope, asset inventory, parsing baseline
  |
  v
T03 / S1: normalized structured JSON from hybrid-auto parser outputs
  |
  v
T04 / S2: semantic extraction schema and knowledge-layer design
  |
  v
T05: knowledge index and query interface
  |
  v
T06 / S3: intra-document semantic consistency checks
  |
  v
T07 / S4/S5: inter-document consistency, traceability, class-level patterns
  |
  v
T08: unified finding evidence-chain schema
  |
  v
T09/T10 / S6: tiered routing, cost tracking, end-to-end pipeline
  |
  v
T11/T12: Web review UI, export, dashboard, final archive
```

Teacher's updated stage model:

| Stage | Meaning | Relationship to original T tasks |
|---|---|---|
| S1 | File parsing / structured normalization | T03 |
| S2 | Extract semantic information from file contents | T04/T05 |
| S3 | Internal semantic consistency within each file | T06/T08 |
| S4 | Semantic consistency across files | T07/T08 |
| S5 | Cross-document association + class-level patterns: MD5 fraud, parameter drift, multi-version coexistence, traceability breaks, template pollution, class-level statistics | T07/T08 |
| S6 | End-to-end pipeline + L0/L1/L2/L3 tiered routing, upgrade mechanism, cost report | T09/T10 |

Every stage must eventually have a harness/evaluation process.

Core principles:

```text
No harness, no completion.
No evidence anchor, no trustworthy finding.
No schema validation, no knowledge-layer input.
No cost log, no LLM call in the main pipeline.
```

---

## 3. Current Data Baseline

Original data directories:

```text
data_Initial/
  Original project files.

data_Processed/
  Processed files from teammate and prior experiments.
```

Previously confirmed parse baselines:

```text
data_Processed/DHF -梳理版_预处理
data_Processed/DMR-全-20260421_预处理
data_Processed/DHF -梳理版_预处理_mineru处理
data_Processed/DMR-全-20260421_预处理_mineru处理
data_Processed/DHF -梳理版_预处理_mineru处理&部分pdf用skill处理
```

New T03 hybrid-auto focus directories:

```text
data_Processed/DHF -梳理版_预处理_hybrid-auto处理
data_Processed/DMR-全-20260421_预处理_hybrid-auto处理
```

Absolute local paths mentioned by the user:

```text
/home/s2025244189/s2025244265/Projects/AI_driven_proj_Manage/data_Processed/DHF -梳理版_预处理_hybrid-auto处理
/home/s2025244189/s2025244265/Projects/AI_driven_proj_Manage/data_Processed/DMR-全-20260421_预处理_hybrid-auto处理
```

Rules:

```text
Do not modify, delete, move, or overwrite anything under data_Processed/.
Do not rerun MinerU unless the user explicitly asks.
Do not call LLMs or external APIs during T03 validation.
```

---

## 4. Completed Work Summary

### T00 - Project Goal Confirmation

Status: completed.

Key conclusions:

- The project is not simple document summarization.
- The goal is DHF/DMR consistency and traceability review.
- The final system should output findings with evidence.
- LLM/Agent work is allowed later, but only after structured data and evidence anchors exist.

Relevant file:

```text
docs/T00_project_scope.md
```

### T01 - Document Asset Inventory

Status: completed.

Known result:

```text
Total original files: 256
DHF: 239
DMR: 17
Duplicate groups found: 7
Duplicate files involved: 14
```

Generated files:

```text
outputs/inventory/files_manifest.json
outputs/inventory/files_manifest.csv
outputs/inventory/duplicates_report.json
docs/T01_inventory_report.md
```

### T02 - Parsing Baseline Confirmation

Status: completed.

Known result:

```text
DHF original: 239 files
DHF preprocessed: 203 files
DMR original: 17 files
DMR preprocessed: 18 files
```

Older Markdown baseline:

```text
DHF normal MinerU version: 225 md files
DHF enhanced skill version: 383 md files
DMR MinerU version: 17 md files
```

Important update:

```text
The current T03 work appears to have shifted from Markdown normalization to hybrid-auto JSON normalization.
This is acceptable if the hybrid-auto outputs are richer and can be normalized reliably.
```

### T03 - Unified Structured JSON

Status: active / needs verification.

Relevant task spec:

```text
tasks/T03_hybrid_auto_json_normalization.md
```

T03 scope:

```text
Normalize MinerU hybrid-auto parser JSON into DocReview normalized JSON.
Do not do semantic extraction, findings, consistency review, or LLM reasoning in T03.
```

Expected T03 output area:

```text
outputs/t03_hybrid_auto/
```

Expected scripts:

```text
scripts/t03_build_hybrid_inventory.py
scripts/t03_analyze_hybrid_samples.py
scripts/normalize_hybrid_auto_json.py
scripts/t03_validate_normalized_sample.py
```

Expected sample outputs:

```text
outputs/t03_hybrid_auto/inventory.json
outputs/t03_hybrid_auto/inventory.md
outputs/t03_hybrid_auto/sample_analysis.json
outputs/t03_hybrid_auto/sample_analysis.md
outputs/t03_hybrid_auto/normalized_sample/
outputs/t03_hybrid_auto/manifest_sample.json
outputs/t03_hybrid_auto/validation_sample.md
```

Possible later full-conversion outputs should remain under:

```text
outputs/t03_hybrid_auto/
```

T03 should be considered complete only if:

```text
1. The two hybrid-auto input directories exist.
2. Inventory has been generated and looks complete.
3. Sample analysis has confirmed usable JSON structure.
4. Normalized samples exist.
5. Validation passes.
6. Full conversion has either been completed and validated, or the user explicitly accepts sample-only completion.
7. Every normalized block has source anchors back to source JSON path, page index, and block order.
8. No duplicate document is created just because both content_list and content_list_v2 exist.
```

---

## 5. Immediate Next Action for Codex

The next Codex task should be inspection only.

Task name:

```text
T03-check: inspect hybrid-auto normalized JSON status and recommend next step
```

Codex should check:

```text
1. Whether both hybrid-auto input directories exist.
2. How many JSON files they contain.
3. Counts by role:
   - *_content_list.json
   - *_content_list_v2.json
   - *_middle.json
   - *_model.json
   - other json
4. Whether outputs/t03_hybrid_auto/ exists.
5. Whether expected T03 output files exist.
6. Whether expected scripts exist.
7. Whether normalized_sample exists and how many files it contains.
8. Whether validation_sample.md reports PASS or FAIL.
9. Whether full normalized conversion has already been produced.
10. Whether T03 is ready to hand off to T04.
```

Codex must not:

```text
- modify data_Processed/
- rerun MinerU
- call LLMs
- implement T04
- implement anomaly detection
- create Web UI
- run full conversion unless the user explicitly asks
```

Expected final answer from Codex:

```text
1. hybrid-auto input directories: exist / missing
2. JSON count and role statistics
3. T03 scripts: present / missing
4. T03 output files: present / missing
5. normalized_sample count
6. validation_sample PASS / FAIL / missing
7. current T03 state classification:
   A. not started
   B. inventory only
   C. sample analysis done
   D. normalized sample done
   E. sample validation done
   F. ready for full conversion
   G. full conversion done
8. minimum next task
9. whether to enter T04 now
```

---

## 6. Decision Rules After T03-check

### Case A/B/C/D: T03 not yet validated

Next step:

```text
Continue T03 only.
Do not enter T04.
Finish sample validation first according to tasks/T03_hybrid_auto_json_normalization.md.
```

### Case E: sample validation passed, full conversion not run

Next step:

```text
Ask the user whether to approve full conversion.
If approved, run full T03 conversion and validation under outputs/t03_hybrid_auto/.
Do not enter T04 until full output shape is known.
```

### Case F: ready for full conversion

Next step:

```text
Run full conversion only after user approval.
Then validate all normalized JSON.
```

### Case G: full conversion done and validation passed

Next step:

```text
Enter T04-0: semantic extraction schema design from normalized JSON samples.
Do not jump directly to knowledge graph, Agent, or finding detection.
```

### If validation fails

Next step:

```text
Fix T03 normalized JSON converter or schema assumptions.
Do not enter T04.
```

---

## 7. Next Major Stage: T04 / S2 Semantic Extraction

Only start this after T03 validation passes.

Goal:

```text
Extract semantic information from normalized JSON so later modules can check consistency and traceability.
```

T04-0 should be a design/sample task, not a full extraction task.

Recommended T04-0 task:

```text
Pick 10 representative normalized JSON documents.
Design semantic_unit schema and knowledge entity schema.
Manually/locally inspect what fields can be extracted reliably.
Do not build full knowledge index yet.
```

Priority semantic objects:

| Semantic object | Examples | Why needed |
|---|---|---|
| document_role | design input, risk analysis, verification report, inspection spec | upstream/downstream relation |
| version | V1.0, Rev.A, effective date | multi-version detection |
| parameter | voltage, accuracy, temperature range, tolerance | parameter drift/conflict |
| requirement | shall, must, should, acceptance criteria | traceability source |
| verification | test item, method, result, acceptance standard | requirement validation |
| risk_control | hazard, mitigation, residual risk | risk closure |
| component | PCB, probe, housing, label, package | cross-document alignment |
| table_field | field name/value pairs from tables | structured comparison |

T04 expected design outputs:

```text
docs/T04_semantic_schema_design.md
schemas/semantic_unit.schema.json
schemas/knowledge_entity.schema.json
schemas/knowledge_relation.schema.json
```

T04 should not yet:

```text
- do full anomaly detection
- call LLM across the whole corpus
- create Agent workflows
- create Web UI
```

---

## 8. Harness / Evaluation Strategy

Teacher's updated requirement:

```text
Every stage needs a harness to evaluate accuracy and support optimization.
```

Practical sequencing:

```text
T03: first validate schema, anchors, parse completeness.
T04: then build semantic extraction harness on a small labeled set.
T06/T07: build finding-level precision/recall harness.
T09/T10: build pipeline and cost harness.
```

Do not build a huge generic harness before T03 output is stable.

Minimum harness progression:

```text
parse_harness:
  validates normalized JSON structure, block anchors, duplicate handling, failure records.

semantic_harness:
  validates extracted parameters, versions, document role, evidence anchors.

intra_doc_harness:
  validates single-file consistency findings.

inter_doc_harness:
  validates conflict pairs and traceability findings.

pattern_harness:
  validates MD5 fraud, parameter drift, multi-version coexistence, traceability break, template pollution, class-level statistics.

e2e_harness:
  validates one-command pipeline, cost report, tier routing, final findings schema.
```

---

## 9. Collaboration and Execution Rules

Default behavior for assistants/Codex:

```text
Inspect before acting.
Explain purpose and impact before modifying files.
Do not blindly modify files.
Prefer small tasks with clear stop points.
Do not use LLM/Agent for full-folder blind scanning.
Do not place generated outputs under data_Processed/.
Show status in chat; do not force the user to open files to understand the state.
```

For coding tasks:

```text
Write scripts under scripts/ or src/ as specified.
Write generated outputs under outputs/.
Write planning documents under docs/ or tasks/.
Keep each Codex prompt scoped to one small stage.
```

For LLM/Agent use:

```text
No LLM in T03.
In T04, LLM may be considered only for small, high-value semantic normalization after rule-based extraction is tested.
All later LLM calls must eventually be logged with prompt/model/tokens/cost/confidence.
```

---

## 10. Recommended Next Codex Prompt

Use this prompt next:

```text
请在本地仓库中检查当前 T03 进展，并判断下一步是否可以进入 T04。

仓库路径：

/home/s2025244189/s2025244265/Projects/AI_driven_proj_Manage

请先阅读：

TASK_STATE.md
tasks/T03_hybrid_auto_json_normalization.md
DocReview_任务状态卡.md

重点检查这两个目录：

/home/s2025244189/s2025244265/Projects/AI_driven_proj_Manage/data_Processed/DHF -梳理版_预处理_hybrid-auto处理
/home/s2025244189/s2025244265/Projects/AI_driven_proj_Manage/data_Processed/DMR-全-20260421_预处理_hybrid-auto处理

本轮不要写新功能，先做“产物体检 + 下一步建议”。

请完成：

1. 检查两个 hybrid-auto 目录是否存在。
2. 统计两个目录下的 JSON 文件数量。
3. 按文件类型分类统计：
   - *_content_list.json
   - *_content_list_v2.json
   - *_middle.json
   - *_model.json
   - other json
4. 检查 outputs/t03_hybrid_auto/ 是否存在。
5. 检查 T03 预期脚本和输出文件是否齐全。
6. 如果存在 inventory.md、sample_analysis.md、validation_sample.md，请读取并总结。
7. 判断 T03 当前处于 A-G 哪个状态。
8. 给出最小下一步建议。
9. 判断是否可以进入 T04。

限制：

- 不要修改 data_Processed/
- 不要重跑 MinerU
- 不要调用 LLM
- 不要做 T04 代码实现
- 不要做异常检测
- 不要创建 Web
- 本轮只输出检查报告和下一步建议

最终回复：

1. 两个 hybrid-auto 目录是否存在
2. JSON 文件总数和分类统计
3. T03 输出文件是否齐全
4. 已有脚本是否齐全
5. normalized_sample 是否存在，数量是多少
6. validation_sample.md 的 PASS / FAIL 状态
7. 当前 T03 阶段判断：A/B/C/D/E/F/G
8. 如果 T03 未完成，下一步最小任务是什么
9. 如果 T03 已完成，下一步是否进入 T04
10. 建议下一条 Codex prompt 应该是什么
```

---

## 11. What Not To Do Next

Do not do these next:

```text
- Do not start Web UI.
- Do not start multi-agent routing.
- Do not design all S1-S6 modules at once.
- Do not build a large generic harness before T03 output is stable.
- Do not use Hermes/Kimi to scan the entire project.
- Do not start finding detection before semantic schema exists.
```

The next correct move is:

```text
Verify T03 hybrid-auto normalization status.
Then decide between:
1. finish T03 full conversion/validation, or
2. enter T04 semantic schema design.
```
