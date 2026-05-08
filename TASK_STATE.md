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
T04-0 Semantic schema design: next active stage
```

Current immediate task:

```text
Enter T04-0 carefully.
Do not jump directly to full knowledge graph, anomaly detection, Agent routing, or Web UI.
First design semantic_unit / knowledge_entity / knowledge_relation schema from the T03 normalized JSON outputs, and resolve the doc_id, source path, and evidence anchor strategy.
```

Current core facts:

```text
T03 is complete.
normalized JSON has been generated and validated.
The active next task is T04-0: semantic extraction schema design.
Do not call LLMs to scan the whole corpus.
Do not start complete knowledge graph construction yet.
Do not start anomaly detection, Agent routing, or Web UI yet.
```

---

## 1. File Role Rules: TASK_STATE.md vs Agent开发工程师.md

The project now has two different planning files with different purposes.

### 1.1 TASK_STATE.md

`TASK_STATE.md` is the real project execution state file.

It records:

```text
- actual current progress
- active stage
- next executable task
- completed and validated artifacts
- blocked items
- forbidden jumps
- execution boundaries for Codex or a new assistant
```

It answers:

```text
Where is the project now?
What is the active stage?
What should be done next?
Which files have actually been generated?
Which tasks have actually been completed and validated?
What should not be done now?
What should Codex or a new assistant read first?
```

Rules for this file:

```text
Keep it factual, restrained, and executable.
Do not write job-search packaging language here.
Do not exaggerate project progress.
Do not mark future Agent features as completed.
Only record completed work when there is concrete output and validation.
```

### 1.2 Agent开发工程师.md

`Agent开发工程师.md` is a career planning and project packaging file.

It records:

```text
- how this project can later be packaged for AI Agent engineer / LLM application / RAG / LLMOps internship roles
- future capability gaps to fill
- Agent, RAG, Tool Calling, LLMOps, FastAPI, Docker, README, resume and interview preparation tasks
- which future features can become resume highlights
- which tasks belong to presentation and job-search packaging rather than current real project state
```

Rules for this file:

```text
It may contain future plans, resume wording, interview preparation, and packaging strategy.
It must not force TASK_STATE.md to jump stages.
It must not override the current active project stage.
```

### 1.3 Reading Order

Every time work resumes, read files in this order:

```text
1. TASK_STATE.md
2. Agent开发工程师.md
3. Stage-specific project files named by TASK_STATE.md
```

For the current T04-0 stage, also read:

```text
DocReview_任务状态卡.md
docs/Codex_执行总控_2026-05-08.md
outputs/t03_hybrid_auto/validation_full.md
outputs/t03_hybrid_auto/structure_stability_full.md
Representative samples from outputs/t03_hybrid_auto/normalized_full/ if needed
```

### 1.4 Conflict Priority

If `TASK_STATE.md` and `Agent开发工程师.md` appear to conflict:

```text
Real development progress follows TASK_STATE.md.
Career packaging and long-term job-search goals follow Agent开发工程师.md.
```

Example:

```text
If Agent开发工程师.md mentions Agent Workflow, FastAPI, Docker, LLMOps, or README packaging,
but TASK_STATE.md says the current stage is T04-0 and forbids Agent workflows,
then do not implement Agent Workflow now.
```

---

## 2. Task Classification Rules

Before executing any task, classify it as A, B, or C.

### A. Real project development task

Examples:

```text
T04-0 semantic schema design
T04-1 rule-based semantic extraction prototype
T05 knowledge index
T06 intra-document consistency
T07 inter-document consistency
T08 finding schema
T09/T10 pipeline, tier routing, cost report
harness / evaluation
normalized JSON schema validation
evidence anchor design
```

Main files/directories modified:

```text
TASK_STATE.md
docs/
schemas/
scripts/
outputs/
tests/
eval/
project code
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
interview preparation
README presentation angle
project highlight extraction
job description matching
GitHub packaging strategy
resume project description versions
```

Main files modified:

```text
Agent开发工程师.md
README.md presentation sections
interview materials
resume materials
```

Rule:

```text
Usually do not update TASK_STATE.md unless the task also reflects a real project stage change.
```

### C. Stage completion synchronization task

When a real project stage completes, update both files in order.

First update `TASK_STATE.md` with:

```text
- which stage completed
- files added or modified
- validation result
- current state
- next active task
- what still must not be done
- whether the project is allowed to enter the next stage
```

Then update `Agent开发工程师.md` only for career packaging impact:

```text
- how this stage can be described as an ability point
- which resume highlights became available
- how the project capability map changed
- what still needs to be added for job applications
- whether README, architecture diagram, or interview wording should be updated
```

---

## 3. Rules for Modifying TASK_STATE.md

When editing `TASK_STATE.md`:

```text
1. Only write what is actually completed.
2. Do not write planned work as completed work.
3. Every stage must say whether it has a harness or validation method.
4. Every finding or semantic object must remain traceable to an evidence anchor.
5. If LLMs are called, record cost or at least call count.
6. If a stage is not complete, do not mark it completed.
7. If an older document is outdated, explicitly say which document is outdated and which file is authoritative.
```

Recommended stage completion record format:

```text
## X. T04-0 Completion Record

Task:
...

Files added/updated:
...

Validation:
...

State classification:
G / Y / R

Next task:
...
```

---

## 4. Required Completion Response Format

After every completed task, the assistant should reply in this structure:

```text
## 本次完成

- 完成了什么任务
- 新增/修改了哪些文件
- 是否更新 TASK_STATE.md
- 是否更新 Agent开发工程师.md

## 当前项目真实状态

- 当前阶段：
- 是否完成：
- 验证方式：
- 下一步：

## 求职包装状态

- 当前可写进简历的能力：
- 尚未完成但未来可包装的能力：
- 下一步为了投递应补齐：

## 风险与限制

- 当前不能做什么
- 哪些地方需要人工确认
```

Rules:

```text
For real development tasks, report TASK_STATE.md status explicitly.
For career packaging tasks, report Agent开发工程师.md status explicitly.
If a file was not updated, say so directly.
Do not imply a stage is completed unless validation or concrete deliverables prove it.
```

---

## 5. Source Documents for Planning

The current real project plan is the merged result of these files:

```text
DocReview_任务状态卡.md
  Original T00-T12 project task card and current status record.

docs/Codex_执行总控_2026-05-08.md
  New staged plan from the teacher's updated thinking:
  S1 parse standardization, S2 semantic extraction, S3 intra-document consistency,
  S4 inter-document consistency, S5 cross-document/class-level patterns,
  S6 end-to-end pipeline and tiered routing.

tasks/T03_hybrid_auto_json_normalization.md
  Concrete T03 task spec for converting MinerU hybrid-auto JSON into DocReview normalized JSON.

Agent开发工程师.md
  Career packaging and long-term AI Agent engineer preparation plan.
  It is not the source of truth for current implementation stage.
```

Important interpretation:

```text
DocReview_任务状态卡.md may still describe T03 as the next task.
That is outdated for current execution.
TASK_STATE.md is authoritative for real project status.
T03 is completed and validated.
The next stage is T04-0 semantic schema design based on outputs/t03_hybrid_auto/normalized_full/.
```

---

## 6. Updated Project Mainline

```text
T00/T01/T02: project scope, asset inventory, parsing baseline
  |
  v
T03 / S1: normalized structured JSON from hybrid-auto parser outputs  ✅ completed
  |
  v
T04 / S2: semantic extraction schema and knowledge-layer design       ← current
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

## 7. T03 Completion Record

T03 task:

```text
Normalize MinerU hybrid-auto parser JSON into DocReview normalized JSON.
```

Input directories checked:

```text
data_Processed/DHF -梳理版_预处理_hybrid-auto处理
data_Processed/DMR-全-20260421_预处理_hybrid-auto处理
```

Both directories exist.

Raw JSON statistics:

| Type | DHF | DMR | Total |
|---|---:|---:|---:|
| *_content_list.json | 219 | 17 | 236 |
| *_content_list_v2.json | 219 | 17 | 236 |
| *_middle.json | 219 | 17 | 236 |
| *_model.json | 219 | 17 | 236 |
| other_json | 0 | 0 | 0 |
| total JSON | 876 | 68 | 944 |

Document groups:

```text
219 total groups
DHF: 202 groups
DMR: 17 groups
```

T03 scripts present:

```text
scripts/t03_build_hybrid_inventory.py
scripts/t03_analyze_hybrid_samples.py
scripts/normalize_hybrid_auto_json.py
scripts/t03_validate_normalized_sample.py
scripts/t03_check_normalized_structure_stability.py
```

T03 outputs present:

```text
outputs/t03_hybrid_auto/inventory.json
outputs/t03_hybrid_auto/inventory.md
outputs/t03_hybrid_auto/sample_analysis.json
outputs/t03_hybrid_auto/sample_analysis.md
outputs/t03_hybrid_auto/normalized_sample/
outputs/t03_hybrid_auto/manifest_sample.json
outputs/t03_hybrid_auto/validation_sample.md
outputs/t03_hybrid_auto/normalized_full/
outputs/t03_hybrid_auto/manifest_full.json
outputs/t03_hybrid_auto/validation_full.md
outputs/t03_hybrid_auto/structure_stability_sample.md
outputs/t03_hybrid_auto/structure_stability_full.md
```

Validation result:

```text
validation_sample.md: PASS, 20 files, 0 failures, 0 duplicates
validation_full.md: PASS, 219 files, 0 failures, 0 duplicates
structure_stability_full.md: PASS, 219 files, 0 invalid, 0 inconsistent fields
```

Full conversion result:

```text
219/219 document groups converted successfully
DHF: 202 normalized JSON files
DMR: 17 normalized JSON files
All 219 used content_list_v2 as main input
No fallback source was needed
6,296 blocks all have source_anchor
```

T03 state classification:

```text
G — full conversion done and validation passed.
```

T03 is complete.

---

## 8. T03 Known Design Note Before T04

Important issue:

```text
Current normalized JSON doc_id format appears to be hash-based, e.g. DHF_753b59aabd93.
The earlier planning documents considered path-based doc_id schemes.
```

Before building the knowledge layer, Codex must decide how to handle doc_id.

Recommended decision:

```text
Keep current hash-based doc_id as the stable primary key if it is already used throughout normalized_full.
Add path-derived metadata fields for human traceability instead of renaming doc_id.
Do not rewrite all T03 outputs just to change doc_id unless a concrete downstream breakage is proven.
```

T04 should explicitly document:

```text
doc_id policy
source path policy
evidence anchor policy
whether semantic units reference doc_id + block_id + source_anchor
```

---

## 9. Current Active Stage: T04-0 / Semantic Schema Design

T04 belongs to teacher stage S2:

```text
Extract semantic information from file contents.
```

Goal:

```text
Design the schema for semantic units, knowledge entities, and knowledge relations using real normalized JSON samples.
Do not build full extraction yet.
```

T04-0 should answer:

```text
1. What semantic objects do we need for later consistency review?
2. How do those objects point back to T03 evidence anchors?
3. Which objects can be extracted by rules now?
4. Which objects may later require LLM assistance?
5. What small labeled set should become semantic_harness cases?
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
```

Expected T04-0 outputs:

```text
docs/T04_semantic_schema_design.md
schemas/semantic_unit.schema.json
schemas/knowledge_entity.schema.json
schemas/knowledge_relation.schema.json
outputs/t04_semantics/sample_selection.json
outputs/t04_semantics/sample_observation.md
```

T04-0 should not yet:

```text
- build the full knowledge index
- extract all entities from all 219 documents
- run anomaly detection
- create findings
- call LLM over the whole corpus
- build Agent workflows
- create Web UI
```

---

## 10. Recommended T04-0 Codex Prompt

Use this prompt next:

```text
请在本地仓库中开始 T04-0：语义抽取 schema 设计。

仓库路径：

/home/s2025244189/s2025244265/Projects/AI_driven_proj_Manage

请先阅读：

TASK_STATE.md
Agent开发工程师.md
DocReview_任务状态卡.md
docs/Codex_执行总控_2026-05-08.md
outputs/t03_hybrid_auto/validation_full.md
outputs/t03_hybrid_auto/structure_stability_full.md

注意：

TASK_STATE.md 是真实项目状态文件，以它为当前开发进度准绳。
Agent开发工程师.md 是求职包装与长期能力规划文件，不能用它来推动当前项目跳阶段。
如果两者冲突，以 TASK_STATE.md 为准。

当前状态：

T03 已完成。outputs/t03_hybrid_auto/normalized_full/ 中已有 219 个 normalized JSON，validation_full 和 structure_stability_full 均 PASS。

本轮任务只做 T04-0，不做完整 T04/T05。

目标：

基于 normalized_full 中的真实 JSON 样本，设计 semantic_unit、knowledge_entity、knowledge_relation 三类 schema，并形成后续语义抽取和 harness 的设计依据。

请完成：

1. 从 outputs/t03_hybrid_auto/normalized_full/ 中选择 10 个代表性 normalized JSON：
   - 至少 7 个 DHF
   - 至少 3 个 DMR，如 DMR 不足则全部选取
   - 尽量覆盖不同目录阶段/文档类型

2. 读取这 10 个样本文档的结构和文本片段，观察能稳定抽取哪些语义对象。

3. 重点观察这些对象：
   - document_role
   - version
   - parameter
   - requirement
   - verification
   - risk_control
   - component
   - table_field

4. 设计并写入以下 schema：

   schemas/semantic_unit.schema.json
   schemas/knowledge_entity.schema.json
   schemas/knowledge_relation.schema.json

5. 写设计说明文档：

   docs/T04_semantic_schema_design.md

   内容包括：
   - T04 的目标和边界
   - T03 normalized JSON 如何进入 T04
   - doc_id 策略：当前 hash-based doc_id 是否保留，如何用 source path 做人工追溯
   - semantic_unit / entity / relation 的字段解释
   - 每个语义对象如何引用 evidence anchor
   - 哪些字段先用规则抽取
   - 哪些字段后续可能需要 LLM
   - T04 后续如何建立 semantic_harness

6. 生成样本观察输出：

   outputs/t04_semantics/sample_selection.json
   outputs/t04_semantics/sample_observation.md

7. 如果仓库已有 schemas/knowledge.schema.json 或 docs/W2_design.md，请不要直接覆盖；先读取并吸收有用内容，再决定是否补充或新建 T04 文件。

限制：

- 不要修改 data_Processed/
- 不要重跑 MinerU
- 不要调用 LLM
- 不要做全量实体抽取
- 不要建立完整知识索引
- 不要做异常检测
- 不要生成 findings
- 不要创建 Web
- 不要因为 Agent开发工程师.md 中有 Agent / FastAPI / Docker / LLMOps 规划，就提前做这些内容

最终回复必须使用 TASK_STATE.md 规定的完成任务回复格式，并包含：

1. 选择了哪 10 个样本文档
2. 新增或更新了哪些文件
3. semantic_unit schema 的核心字段
4. knowledge_entity schema 的核心字段
5. knowledge_relation schema 的核心字段
6. doc_id 策略建议
7. 哪些语义对象可以先用规则抽取
8. 哪些语义对象后续可能需要 LLM
9. 是否更新了 TASK_STATE.md；如果没有完成 T04-0，不要把它标记为 completed
10. 下一步建议：T04-1 应该做什么
```

---

## 11. Harness / Evaluation Strategy

Teacher's updated requirement:

```text
Every stage needs a harness to evaluate accuracy and support optimization.
```

Practical sequencing:

```text
T03: structure validation and source_anchor validation completed.
T04: next build semantic extraction harness on a small labeled set.
T06/T07: later build finding-level precision/recall harness.
T09/T10: later build pipeline and cost harness.
```

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

Do not build a huge generic harness before T04 schema is stable.

---

## 12. What Not To Do Next

Do not do these next:

```text
- Do not start Web UI.
- Do not start multi-agent routing.
- Do not design all S1-S6 modules at once.
- Do not use Hermes/Kimi to scan the entire project.
- Do not start finding detection before semantic schema exists.
- Do not build a full knowledge graph before T04 schema is reviewed.
- Do not let Agent开发工程师.md override TASK_STATE.md.
```

The next correct move is:

```text
Start T04-0 semantic schema design using 10 representative normalized JSON samples.
```
