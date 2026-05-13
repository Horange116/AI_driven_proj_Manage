# TASK_STATE

Purpose: current progress snapshot and execution guidance for the PT9L DocReview project. This file is the first file that Codex or a new assistant should read before continuing real project development.

Last updated: 2026-05-08

---

## 0. Current Position

```text
T00 Project goal confirmation: completed
T01 Document asset inventory: completed
T02 Parsing baseline confirmation: completed
T03 Unified structured JSON: completed and validated
T04-0 Semantic schema design: completed
T04-1 Rule-based semantic extraction prototype: next active stage
```

Current immediate task:

```text
Start T04-1 carefully.
Implement a minimal rule-based semantic extraction loop for document_role, version, and a small subset of parameter/table_field extraction.
Also create the first semantic_harness cases.
Do not build full knowledge index, anomaly detection, Agent routing, or Web UI yet.
```

Current core facts:

```text
T03 is complete.
T04-0 is complete.
semantic_unit / knowledge_entity / knowledge_relation schemas have been designed.
The active next task is T04-1: rule-based semantic extraction prototype.
Do not call LLMs to scan the whole corpus.
Do not start complete knowledge graph construction yet.
Do not start anomaly detection, Agent routing, or Web UI yet.
```

---

## 1. File Role Rules: TASK_STATE.md vs Agent开发工程师.md

`TASK_STATE.md` is the real project execution state file.

`Agent开发工程师.md` is the career planning and project packaging file.

Reading order:

```text
1. TASK_STATE.md
2. Agent开发工程师.md
3. Stage-specific project files named by TASK_STATE.md
```

Conflict rule:

```text
Real development progress follows TASK_STATE.md.
Career packaging and long-term job-search goals follow Agent开发工程师.md.
If Agent开发工程师.md mentions Agent Workflow / FastAPI / Docker / LLMOps, it still must not override the current TASK_STATE.md stage.
```

---

## 2. Task Classification Rules

### A. Real project development task

Examples:

```text
T04-1 rule-based semantic extraction prototype
T05 knowledge index
T06 intra-document consistency
T07 inter-document consistency
T08 finding schema
T09/T10 pipeline, tier routing, cost report
harness / evaluation
evidence anchor design
```

Rule:

```text
After completing an A-type task, update TASK_STATE.md.
```

### B. Career packaging / resume planning task

Examples:

```text
resume project wording
AI Agent engineer task list
README presentation angle
interview preparation
```

Rule:

```text
Usually update Agent开发工程师.md, not TASK_STATE.md.
```

### C. Stage completion synchronization task

When a real stage completes:

```text
1. First update TASK_STATE.md with real completion, validation, next task, and limits.
2. Then update Agent开发工程师.md only for packaging impact.
```

---

## 3. Required Completion Response Format

After every completed task, reply briefly:

```text
## 本次完成
- 任务：...
- 文件：...
- TASK_STATE.md：已更新 / 未更新
- Agent开发工程师.md：已更新 / 未更新

## 当前状态
- 阶段：...
- 验证：...
- 下一步：...

## 求职包装
- 已可包装：...
- 待补齐：...

## 风险
- 不能做：...
- 待确认：...
```

Rules:

```text
Keep the completion reply short.
Do not imply a stage is completed unless validation or concrete deliverables prove it.
If a file was not updated, say so directly.
```

---

## 4. Source Documents for Planning

```text
DocReview_任务状态卡.md
docs/Codex_执行总控_2026-05-08.md
tasks/T03_hybrid_auto_json_normalization.md
Agent开发工程师.md
```

Authoritative status:

```text
TASK_STATE.md is authoritative for real project status.
DocReview_任务状态卡.md may be partly outdated.
Agent开发工程师.md is not the source of truth for current implementation stage.
```

---

## 5. Updated Project Mainline

```text
T00/T01/T02: project scope, asset inventory, parsing baseline
  |
  v
T03 / S1: normalized structured JSON from hybrid-auto parser outputs  ✅ completed
  |
  v
T04-0 / S2: semantic schema design                         ✅ completed
  |
  v
T04-1 / S2: rule-based semantic extraction prototype        ← current
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

---

## 6. T03 Completion Record

Task:

```text
Normalize MinerU hybrid-auto parser JSON into DocReview normalized JSON.
```

Validation:

```text
validation_sample.md: PASS, 20 files, 0 failures, 0 duplicates
validation_full.md: PASS, 219 files, 0 failures, 0 duplicates
structure_stability_full.md: PASS, 219 files, 0 invalid, 0 inconsistent fields
```

Output summary:

```text
219/219 document groups converted successfully
DHF: 202 normalized JSON files
DMR: 17 normalized JSON files
6,296 blocks all have source_anchor
```

State classification:

```text
G — full conversion done and validation passed.
```

---

## 7. T04-0 Completion Record

Task:

```text
Design semantic_unit, knowledge_entity, and knowledge_relation schemas from 10 representative normalized JSON samples.
```

Samples:

```text
7 DHF samples + 3 DMR samples.
Covered customer requirements, risk management, design input, project schedule, structural design, FMEA, inspection standard, software validation report, master record, and process FMEA.
```

Files added/updated:

```text
schemas/semantic_unit.schema.json
schemas/knowledge_entity.schema.json
schemas/knowledge_relation.schema.json
docs/T04_semantic_schema_design.md
outputs/t04_semantics/sample_selection.json
outputs/t04_semantics/sample_observation.md
DocReview_任务状态卡.md
```

Schema summary:

```text
semantic_unit: unit_id, doc_id, unit_type, value, normalized_value, confidence, extraction_method, evidence[]
knowledge_entity: entity_id, entity_type, label, canonical_value, aliases[], attributes, source_units[], confidence
knowledge_relation: relation_id, relation_type, from_entity_id, to_entity_id, from_doc_id, to_doc_id, confidence, evidence[], extraction_method, attributes
```

Design decisions:

```text
Keep current hash-based doc_id as the programmatic primary key.
Use source_path + text_snippet in evidence anchors for human traceability.
Rule-first extraction for document_role, version, selected parameter, component, and table_field.
LLM deferred to later L2 routing for complex requirement, verification criteria, risk_control, and cross-doc normalization.
```

Validation:

```text
T04-0 is design validation only.
Validation artifacts: schema files + sample_selection.json + sample_observation.md + design doc.
No full semantic extraction was run in T04-0.
```

State classification:

```text
G — design stage completed; implementation not yet started.
```

Next task:

```text
T04-1 rule-based semantic extraction prototype.
```

---

## 8. Current Active Stage: T04-1 / Rule-Based Semantic Extraction Prototype

Goal:

```text
Implement the first minimal semantic extraction loop using rules only.
Extract semantic_units from a small subset of normalized_full and create initial semantic_harness cases.
```

T04-1 scope:

```text
1. document_role extractor: classify by document_name + stage keywords.
2. version extractor: regex scan title/front blocks.
3. parameter extractor P1 subset: table row keyword matching for temperature, accuracy, voltage, tolerance, error, etc.
4. table_field extractor P1 subset: column/value pair extraction for selected tables.
5. semantic_harness initial cases.
```

Expected outputs:

```text
src/docreview/semantics/extractor.py
src/docreview/semantics/rules.py
outputs/t04_semantics/semantic_units_sample.jsonl
harness/cases/semantic_public.jsonl
harness/reports/semantic_sample_report.json
```

T04-1 should not yet:

```text
- run full extraction over all 219 documents unless the sample succeeds and user approves
- build a full knowledge graph
- build T05 index
- do anomaly detection
- generate findings
- call LLM
- create Agent workflows
- create Web UI
```

---

## 9. Agent and Harness Relationship

Current work is related to Agent and Harness, but it is not yet the Agent layer.

```text
T03/T04 provide the data and semantic substrate that future Agent tools will use.
T04-1 starts the extraction tool logic that may later become extract_claims_tool.
T05 will create query interfaces that may later become search_doc_tool / knowledge_query_tool.
T06/T07 will create comparison logic that may later become compare_sections_tool.
T08 will create report/finding schema that may later become generate_report_tool.
T09/T10 will compose these tools into routing/pipeline/Agent-like workflows.
```

Harness relationship:

```text
T03 validation checked structure and anchors.
T04-1 semantic_harness will check semantic extraction quality.
T06/T07 finding harness will later check precision/recall of consistency findings.
T09/T10 e2e harness will check pipeline, cost, routing, and final output validity.
```

---

## 10. What Not To Do Next

Do not do these next:

```text
- Do not start Web UI.
- Do not start multi-agent routing.
- Do not use Hermes/Kimi to scan the entire project.
- Do not start finding detection before semantic extraction has a tested minimal loop.
- Do not build a full knowledge graph before T04-1 output is reviewed.
- Do not let Agent开发工程师.md override TASK_STATE.md.
```

The next correct move is:

```text
Start T04-1 rule-based semantic extraction prototype and initial semantic_harness.
```
