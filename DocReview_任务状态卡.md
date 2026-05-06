# DocReview 任务状态卡

用途：把 PT9L 智能文档复核系统拆成可逐步推进、可验收、可复盘的任务卡。建议按 `T00 -> T12` 顺序推进。

当前目标：基于 PT9L 真实历史文档，做出一套从文件解析、知识层、异常检测、分级路由到 Web 复核界面的端到端智能复核系统。

---

## 当前进展摘要

```text
T00 项目目标确认：已完成
T01 文档资产盘点：已完成
T02 文件解析基线：已完成
T03 统一结构化 JSON：下一步
```

已完成的关键工作：

- 明确项目目标：不是单纯文档总结，而是基于 DHF / DMR 上下游关系做一致性和追溯审核。
- 完成原始资料资产盘点：当前项目资料已形成文件清单、格式分布和重复文件报告。
- 确认已有预处理结果：`data_Processed` 中已经存在去重、格式转换后的预处理目录。
- 确认已有 Markdown 解析基线：DHF / DMR 均已有 MinerU 处理结果。
- 确认 DHF 有增强解析版本：`DHF -梳理版_预处理_mineru处理&部分pdf用skill处理` 包含普通 MinerU 版全部 Markdown，并额外增加 page 级 VLM/skill Markdown。
- 确认后续优先输入：T03 优先基于已处理的 Markdown 结果做统一结构化 JSON，而不是重新从原始 Word/PDF 全量解析。

当前建议：

```text
下一阶段进入 T03：把已有 Markdown / page-vlm Markdown 统一整理成可被程序处理的 normalized JSON。
```

---

## 状态说明

- `待办`：尚未开始
- `进行中`：正在分析、实现或验证
- `已完成`：已有可检查产物，并通过本卡验收
- `阻塞`：缺少关键输入、环境或决策，无法继续推进

---

## 项目背景和要求

以下要求来自任务说明和前期群聊补充，用于约束后续设计和实现。

核心目标：

```text
不是单纯做文件总结，而是按文件之间的上下游关系做审核。
重点是从研发需求一路追溯到设计、验证、生产和检验文件，发现断链、冲突、遗漏或降级。
```

典型审核关系：

```text
DHF 前序需求 / 设计输入
  -> 设计方案 / 风险控制 / 验证确认
  -> 设计输出 / 图纸 / BOM / 检验要求
  -> DMR 作业指导 / 生产工艺 / 检验规范 / 出货要求
```

示例：

```text
如果前面需求规定美国体温计精度为 ±0.2°C，
后续设计验证和生产检验文件也应体现并保证 ±0.2°C。
如果生产端写成其他精度、缺少检验要求，或只抽检不全检，就应进入冲突/断链复核。
```

Agent 要求：

- 不要求本地模型，不依赖本机显卡。
- LLM / Agent 能力优先通过 API 使用，例如 Kimi / OpenAI / OpenClaw 等。
- 最终效果应能输出类似“研发要求 vs 生产现状”的冲突分析表，包含对比项、双方证据、严重程度和说明。
- Agent 的重点不是聊天，而是调取解析结果、知识层和证据链，完成跨文件关系审核。

文件处理要求：

- 可以先用 Markdown 跑通流程，便于人和 LLM 阅读。
- JSON 是后续自动化流水线的目标格式，便于程序处理、索引、查询和规则检测。
- 长期目标是新项目文件夹放入后，系统能自动解析、建索引、检测并输出 findings。

推进方式：

- 本项目采用“以教代学”方式推进，不是 AI 直接代做完整项目。
- 默认由用户理解、判断和执行关键步骤；AI 主要负责检查、讲解、方案建议和必要时代执行。
- 涉及写入、批量处理或状态更新时，需先说明目的和影响。

---

## 工作约定

每张任务卡按下面结构推进：

```text
1. 这一步在整体流程里的位置
2. 它接收什么输入
3. 它做什么处理
4. 它输出什么
5. 怎么验收
6. 后续依赖它做什么
```

关键原则：

- 先做文件解析和结构化数据，再做多智能体。
- 先用规则抓确定性问题，再用 LLM / Agent 处理高成本推理问题。
- 每条 finding 必须可追溯到原始文件和证据片段。
- 每周都保留 `design.md`、`method.md`、bad case 复盘和 AI 使用记录。
- 交付目标不是方案，而是能跑起来的 pipeline 和复核界面。

---

## 总览流程

```text
T00 项目目标确认
  |
  v
T01 文档资产盘点
  |
  v
T02 文件解析基线
  |
  v
T03 统一结构化 JSON
  |
  v
T04 知识层 Schema
  |
  v
T05 知识索引与查询接口
  |
  v
T06 单文件异常检测
  |
  v
T07 跨文档关联检测
  |
  v
T08 Finding 证据链格式
  |
  v
T09 分级路由 / 多智能体架构
  |
  v
T10 端到端 Pipeline
  |
  v
T11 Web 复核界面
  |
  v
T12 导出 / Dashboard / 复盘材料
```

---

## 里程碑映射

| 周期 | 对应任务 | 核心产物 |
|---|---|---|
| W1 | T01 - T03 | 文件清单、解析结果、统一 JSON |
| W2 | T04 - T05 | 知识层 schema、索引、查询接口 |
| W3 | T06、T08 | 单文件异常检测、finding 标准格式 |
| W4 | T07、T08 | 跨文档异常检测、证据链增强 |
| W5 | T09 - T10 | 分级路由、多智能体编排、端到端命令 |
| W6 | T11 - T12 | Web 界面、导出、dashboard、答辩材料 |

---

## T00 - 项目目标确认

```text
状态：已完成
阶段：启动
核心问题：我们到底要复核哪些文档、发现哪些问题、交付给谁使用？
```

目标：

明确 DocReview 项目的业务边界和工程交付边界。

输入：

- `index_v2(2).html` 任务说明
- `DHF -梳理版`
- `DMR-全-20260421`
- `MinerU_任务状态卡.md`

处理：

- 确认 PT9L 文档范围。
- 确认主要异常类型：复制改名、参数漂移、多版本并存、追溯断链、模板污染、空白/占位符等。
- 确认最终用户：QA / 复核员 / 外审支持人员。
- 确认交付形态：命令行 pipeline + Web 复核界面 + findings 导出。

输出：

- 项目范围说明：`docs/T00_project_scope.md`
- 异常类型清单：`docs/T00_project_scope.md`
- 初版验收指标：`docs/T00_project_scope.md`

验收：

- 能用一段话说明系统要解决的问题。
- 能列出第一批要检测的 finding 类型。
- 能说明哪些属于 W1/W2 基础工程，哪些属于后续智能体工作。

下游：

- T01 文档资产盘点

---

## T01 - 文档资产盘点

```text
状态：已完成
阶段：W1
核心问题：项目里到底有哪些文件？格式、路径、大小、重复情况如何？
```

目标：

建立 PT9L 文档资产台账，为解析、去重、分组和后续复核提供基础数据。

输入：

- `DHF -梳理版`
- `DMR-全-20260421`

处理：

- 扫描所有文件路径。
- 统计扩展名、文件大小、修改时间。
- 计算 hash / MD5，用于识别完全重复文件。
- 按 DHF / DMR / 阶段 / 文档类型初步分类。

输出：

- `outputs/inventory/files_manifest.json`
- `outputs/inventory/files_manifest.csv`
- `outputs/inventory/duplicates_report.json`
- `docs/T01_inventory_report.md`

验收：

- 能回答总文件数、各格式数量、重复文件组数量。
- 每个文件都有唯一 `doc_id`。
- 每个文件记录原始路径、文件名、扩展名、大小、hash、所属资料集。

下游：

- T02 文件解析基线
- T07 跨文档关联检测

---

## T02 - 文件解析基线

```text
状态：已完成
阶段：W1
核心问题：如何把 .doc / .docx / .xlsx / .pdf 等文件稳定转成机器可处理内容？
```

目标：

建立文档解析基线，让下游至少能拿到文本、表格、页面/段落定位和基础元数据。

输入：

- T01 文件资产台账
- MinerU 解析能力
- 必要的 Office / PDF 解析工具
- `data_Processed/DHF -梳理版_预处理`
- `data_Processed/DMR-全-20260421_预处理`
- `data_Processed/DHF -梳理版_预处理_mineru处理`
- `data_Processed/DHF -梳理版_预处理_mineru处理&部分pdf用skill处理`
- `data_Processed/DMR-全-20260421_预处理_mineru处理`

处理：

- 对支持格式调用 MinerU 或本地解析器。
- 对解析失败文件记录失败原因。
- 对扫描 PDF 或图片型 PDF 使用 OCR fallback。
- 保留解析产物与原文件之间的映射关系。

输出：

- `outputs/parsed/{doc_id}/raw_parse.json`
- `outputs/parsed/{doc_id}/content.md`
- `outputs/parsed/{doc_id}/parse_meta.json`
- `outputs/parsed/parse_failures.json`
- 当前采用已有基线输出：`data_Processed/*_mineru处理*`

当前结论：

- 预处理目录已将老 Office 文件转为 `docx/xlsx`，并排除了 `ai/dwg/zip/rar/tmp/scc` 等不适合直接解析的附件。
- DMR 已有 MinerU Markdown 输出。
- DHF 普通 MinerU 版已有 Markdown 输出。
- DHF skill 增强版包含普通版全部 Markdown，并额外增加 158 个 page 级 Markdown，适合作为后续优先解析基线。
- T02 不再重跑全量解析，后续进入 T03 时优先消费已有 Markdown 结果。

验收：

- 公开挑战文件可成功解析。
- 每个成功解析文件至少有文本或表格内容。
- 解析失败文件有明确错误分类，而不是静默跳过。

下游：

- T03 统一结构化 JSON

---

## T03 - 统一结构化 JSON

```text
状态：待办
阶段：W1
核心问题：不同格式解析结果如何变成统一、稳定、可测试的数据结构？
```

目标：

把不同来源的解析结果规范化成统一 JSON，作为知识层和检测规则的唯一输入。

输入：

- T02 原始解析结果

处理：

- 定义统一文档结构：document、sections、blocks、tables、spans、evidence anchors。
- 标准化页码、段落号、表格坐标、文本片段。
- 对文件级元数据、解析质量、语言、格式进行统一记录。

输出：

- `outputs/normalized/{doc_id}.json`
- `schemas/normalized_document.schema.json`
- `outputs/normalized/quality_report.json`

验收：

- 所有成功解析文件都能生成统一 JSON。
- JSON 可通过 schema 校验。
- 任意文本块都能追溯到原始文件和位置。

下游：

- T04 知识层 Schema
- T06 单文件异常检测

---

## T04 - 知识层 Schema

```text
状态：待办
阶段：W2
核心问题：复核系统需要沉淀哪些实体、关系和可查询字段？
```

目标：

设计面向 PT9L 文档复核的知识层模型。

输入：

- T03 统一 JSON
- PT9L 文档目录结构
- 目标 finding 类型

处理：

- 设计实体：文档、版本、部件、参数、测试项、风险、需求、验证项、变更记录等。
- 设计关系：引用、验证、派生、冲突、同名、同版本、同 hash 等。
- 定义字段级证据引用格式。

输出：

- `schemas/knowledge.schema.json`
- `docs/W2_design.md`
- 初版实体关系说明

验收：

- 能支持 W2 的查询题。
- 能支持 W3/W4 所需的异常检测。
- 每个实体和关系都能回溯到原文证据。

下游：

- T05 知识索引与查询接口

---

## T05 - 知识索引与查询接口

```text
状态：待办
阶段：W2
核心问题：后续规则、Agent 和 Web 如何查询知识层？
```

目标：

建立可查询的知识索引，提供稳定接口给检测模块和 Agent 使用。

输入：

- T03 统一 JSON
- T04 知识层 schema

处理：

- 抽取实体和关系。
- 建立全文索引、字段索引、hash 索引、参数索引。
- 提供按 doc_id、实体、参数、版本、证据片段查询的接口。

输出：

- `outputs/knowledge/entities.jsonl`
- `outputs/knowledge/relations.jsonl`
- `outputs/knowledge/index.duckdb` 或同等索引文件
- `src/knowledge/query.py`

验收：

- 能回答公开查询题。
- 查询结果包含证据定位。
- 后续检测模块不直接读原始解析文件，而是优先读知识层。

下游：

- T06 单文件异常检测
- T07 跨文档关联检测
- T09 分级路由 / 多智能体架构

---

## T06 - 单文件异常检测

```text
状态：待办
阶段：W3
核心问题：只看一份文件时，能发现哪些明显异常？
```

目标：

实现单文件级 finding 检测。

输入：

- T03 统一 JSON
- T05 知识查询接口

处理：

- 检测空白、占位符、模板残留、乱码、异常日期、明显数量级冲突。
- 检测标题和内容不匹配。
- 对规则无法判断的问题交给 LLM 或人工复核候选队列。

输出：

- `outputs/findings/single_file_findings.jsonl`
- `docs/W3_method.md`

验收：

- 每条 finding 有 severity、confidence、evidence、rule_id。
- 能跑公开 finding 集。
- 有 precision / recall 统计。

下游：

- T08 Finding 证据链格式
- T10 端到端 Pipeline

---

## T07 - 跨文档关联检测

```text
状态：待办
阶段：W4
核心问题：只有全量扫描才能发现哪些问题？
```

目标：

实现跨文件、跨阶段、跨版本的关联异常检测。

输入：

- T01 文件资产台账
- T05 知识层索引
- T06 单文件 findings

处理：

- 检测 hash 完全相同但文件名/用途不同。
- 检测同一参数在不同文档中的冲突。
- 检测同一文档多版本并存但缺少变更记录。
- 检测需求、风险、验证、设计输出之间的追溯断链。
- 检测类级模板污染和异常统计模式。

输出：

- `outputs/findings/cross_doc_findings.jsonl`
- `docs/W4_method.md`

验收：

- 能复现公开跨文档 finding。
- 参数冲突类 finding 必须给出双方或多方证据。
- 追溯断链类 finding 必须说明缺失的链路节点。

下游：

- T08 Finding 证据链格式
- T09 分级路由 / 多智能体架构

---

## T08 - Finding 证据链格式

```text
状态：待办
阶段：W3/W4
核心问题：如何让 QA 5 秒判断 finding 是否可信？
```

目标：

定义并实现统一 finding 输出格式。

输入：

- T06 单文件 findings
- T07 跨文档 findings

处理：

- 统一 finding 字段。
- 统一 evidence anchor。
- 定义 severity、confidence、source、tier、review_status。
- 支持多个证据片段和冲突证据对。

输出：

- `schemas/finding.schema.json`
- `outputs/findings/findings.jsonl`

建议字段：

```json
{
  "finding_id": "F-000001",
  "type": "parameter_conflict",
  "severity": "high",
  "confidence": 0.92,
  "tier": "L1",
  "source": "rule.parameter_conflict",
  "summary": "...",
  "evidence": [],
  "recommendation": "...",
  "review_status": "pending"
}
```

验收：

- findings 能通过 schema 校验。
- 每条 finding 至少有一个可追溯 evidence。
- Web 和导出功能只依赖这个统一格式。

下游：

- T10 端到端 Pipeline
- T11 Web 复核界面

---

## T09 - 分级路由 / 多智能体架构

```text
状态：待办
阶段：W5
核心问题：哪些问题走规则，哪些问题升级给 LLM 或专家 Agent？
```

目标：

设计并实现成本可控、可追踪的分级处理架构。

输入：

- T05 知识查询接口
- T06 单文件检测
- T07 跨文档检测
- T08 finding 格式

处理：

- 定义 L0/L1/L2/L3 分层：
  - L0：纯规则，无 LLM 成本
  - L1：结构化规则 + 知识层查询
  - L2：LLM 判断单点复杂问题
  - L3：多 Agent 协作处理跨文档复杂问题
- 定义 Agent 职责：
  - Coordinator Agent：任务拆解、状态管理、路由
  - Ingest Agent：解析和质量检查
  - Knowledge Agent：知识层查询和证据召回
  - Single Review Agent：单文件复核
  - Cross Review Agent：跨文档复核
  - QA Agent：低置信度复核和结论校验
  - Cost Agent：记录 token、耗时、命中率和升级原因
- 设计低置信度升级机制。

输出：

- `docs/W5_design.md`
- `src/routing/tiered_router.py`
- `outputs/reports/cost.json`
- `outputs/reports/ai_usage_log.jsonl`

验收：

- 每条 finding 记录来自哪个层级。
- 低置信度任务能自动升级。
- 能输出成本和命中率统计。

下游：

- T10 端到端 Pipeline

---

## T10 - 端到端 Pipeline

```text
状态：待办
阶段：W5
核心问题：能否一条命令从原始文档跑到最终 findings？
```

目标：

把 T01-T09 串成可重复运行的 pipeline。

输入：

- 原始 PT9L 文档目录
- 配置文件
- 各阶段模块

处理：

- 实现一键运行命令。
- 支持断点续跑。
- 支持只跑某个阶段。
- 记录每阶段耗时、输入、输出、错误。

输出：

- `src/pipeline/run_review.py`
- `configs/default.yaml`
- `outputs/findings/findings.jsonl`
- `outputs/reports/run_report.json`

验收：

- 从空输出目录开始能完整跑通。
- 任一阶段失败时有明确错误报告。
- 重复运行不会破坏已有中间产物，或有明确覆盖策略。

下游：

- T11 Web 复核界面
- T12 导出 / Dashboard / 复盘材料

---

## T11 - Web 复核界面

```text
状态：待办
阶段：W6
核心问题：复核员能否在浏览器里高效查看、筛选、标记 finding？
```

目标：

建立可用的人工复核界面。

输入：

- T08/T10 findings
- 原文证据定位
- 运行报告

处理：

- 实现 finding 列表。
- 支持按 severity、type、confidence、status、source 筛选。
- 支持 finding 详情和证据展示。
- 支持人工标记：确认、误报、待讨论。
- 支持持久化复核状态。

输出：

- FastAPI 后端
- React 或等价前端
- `outputs/review/review_state.json`

验收：

- 复核员打开浏览器即可使用。
- 能查看 finding 详情和证据。
- 标记状态刷新后不丢失。

下游：

- T12 导出 / Dashboard / 复盘材料

---

## T12 - 导出 / Dashboard / 复盘材料

```text
状态：待办
阶段：W6
核心问题：如何把系统结果交付给 QA、外审和答辩？
```

目标：

完成最终交付材料和复盘材料。

输入：

- T10 运行结果
- T11 人工复核状态
- 每周 design / method / bad case
- AI 使用日志

处理：

- 导出 Excel / JSON findings。
- 生成 dashboard：finding 数量、类型分布、severity 分布、复核状态、成本曲线。
- 整理 6 周方法论档案。
- 整理 bad case 和改进记录。
- 准备 20 min 演示和 10 min 答辩材料。

输出：

- `outputs/exports/findings.xlsx`
- `outputs/exports/findings.json`
- `outputs/reports/dashboard.json`
- `docs/final_method_archive.md`
- `docs/final_presentation_outline.md`

验收：

- QA 能拿导出文件复核。
- 能说明成本和精度权衡。
- 能说明哪些模块可迁移到别的项目，哪些需要重写。

下游：

- 项目结项 / 答辩

---

## 当前建议推进顺序

```text
当前优先级：

1. T03 统一结构化 JSON
2. T04 知识层 Schema
3. T05 知识索引与查询接口
4. T06 单文件异常检测

暂缓：

- T09 多智能体架构
- T11 Web 复核界面

原因：

多智能体和 Web 都依赖稳定的数据结构、知识层和 finding 格式。先把 W1/W2 的底座做好，后面 Agent 才有可靠上下文可用。
```
