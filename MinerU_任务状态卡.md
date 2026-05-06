# MinerU 任务状态卡

用途：把 MinerU 的关键任务和关键函数拆成可逐个理解的卡片。建议按 `T00 -> T12` 顺序阅读。

状态说明：

- `待了解`：还没有开始看
- `了解中`：正在看源码或流程
- `已了解`：已经能说明它的输入、职责和输出

---

## 学习对话约定

后续讲解按“AI Agent / AI 工程岗位面试视角”推进，不只解释代码做了什么，也补充为什么这样设计、这种设计在工程上解决了什么问题。

每张任务卡建议按下面结构学习：

```text
1. 这一步在整体流程里的位置
2. 它接收什么输入
3. 它做了什么关键决策
4. 它把什么交给下一步
5. 面试中可能被问到的技术点
6. 如果你要复述，应该怎么讲
```

对话要求：

- 一次只讲一个任务卡，不跳太快。
- 每一步都尽量用“输入 -> 处理 -> 输出”的形式解释。
- 你可以随时打断提问，我会停在当前任务卡继续解释。
- 对关键函数，我会说明它的职责边界，而不是逐行念代码。
- 对 AI Agent 相关岗位，我会额外强调：任务编排、接口抽象、异步任务、工具调用、后端路由、状态管理、可观测性、容错和扩展性。
- 每张卡理解后，可以把状态从 `待了解` 改成 `了解中` 或 `已了解`。

---

## 学习深度待办

这些内容后续再细看。当前先按主流程推进，不在入口层停太久。

| 优先级 | 主题 | 状态 | 为什么要学 |
|---|---|---|---|
| 高 | FastAPI / HTTP API | 待办 | AI Agent 最常通过 HTTP API 调用外部工具 |
| 高 | 同步接口 `/file_parse` 与异步接口 `/tasks` 的区别 | 待办 | 长任务、任务状态、轮询结果是 Agent 工程常见面试点 |
| 高 | `task_id`、任务队列、状态管理 | 待办 | 理解工具调用从提交到完成的完整生命周期 |
| 中 | CLI 如何作为 API 客户端 / 编排器 | 待办 | 理解本地批处理和服务化能力如何复用同一套流程 |
| 低 | Gradio WebUI | 待办 | 主要服务人工交互和 Demo，Agent 场景不是重点 |
| 低 | Router 多服务调度 | 待办 | 生产部署、负载分发、多 GPU 场景需要了解概念 |

当前学习策略：

```text
当前已调整为“核心解析链路优先”。

先不逐卡学习入口和任务系统，优先理解 MinerU 最关键的问题：
它是如何把 PDF / 图片 / DOCX / PPTX / XLSX 里的内容解析出来的。

重点学习链路：
T02 读取输入文件
  -> T04 do_parse() 核心分流
  -> T05 Office 原生解析
  -> T07 pipeline 后端
  -> T08 VLM 后端
  -> T09 hybrid 后端
  -> T10 middle_json 统一结构
  -> T11 输出 Markdown / JSON / 图片

之后再回头深入：
FastAPI 异步任务、Agent 工具封装、Router 生产部署、CLI 任务规划
```

---

## 总览流程

```text
T00 用户入口
  |
  v
T01 CLI / API / WebUI 接收文件和参数
  |
  v
T02 读取输入文件
  |
  v
T03 创建解析任务
  |
  v
T04 do_parse() 核心调度
  |
  +--> T05 Office 文件解析
  |
  +--> T06 PDF / 图片预处理
  |
  +--> T07 pipeline 后端
  |
  +--> T08 VLM 后端
  |
  +--> T09 hybrid 后端
  |
  v
T10 生成 middle_json
  |
  v
T11 输出 Markdown / JSON / 图片 / 可视化文件
  |
  v
T12 API / CLI / WebUI 返回结果
```

---

## T00 - 用户入口选择

```text
状态：已了解
阶段：入口层
核心问题：用户通过什么方式把文档交给 MinerU？
```

关键入口：

- CLI：`mineru -p <input_path> -o <output_path>`
- API：`mineru-api`
- WebUI：`mineru-gradio`
- Router：`mineru-router`

相关文件：

- `pyproject.toml`
- `mineru/cli/client.py`
- `mineru/cli/fast_api.py`
- `mineru/cli/gradio_app.py`
- `mineru/cli/router.py`

作用：

```text
用户不直接调用底层模型。
用户先进入 CLI / API / WebUI / Router 这些外层入口。
这些入口负责收集文件、参数、后端选择和输出目录。
```

输入：

- 本地文件路径
- 上传文件
- 输出目录
- backend 参数
- OCR / 表格 / 公式等解析参数

输出：

- 一个待执行的解析请求

下游：

- T01

面试视角：

```text
T00 看起来只是“入口选择”，但它体现的是系统边界设计。
一个 AI 工程系统通常不会只暴露一种入口，而是把同一套能力封装成 CLI、HTTP API、WebUI、Router 等不同产品形态。
```

你需要知道的技术细节：

- `pyproject.toml` 的 `[project.scripts]` 把命令名映射到 Python 函数，例如 `mineru = "mineru.cli.client:main"`。
- CLI 适合本地批处理和自动化脚本。
- FastAPI 适合被其他系统、平台、Agent 框架调用。
- WebUI 适合人工上传和交互式验证。
- Router 适合多服务、多 GPU、多 worker 的统一入口和负载分发。
- 入口层不应该直接耦合模型推理细节，否则后续很难扩展新入口或新后端。

AI Agent 类岗位常见追问：

```text
为什么要同时提供 CLI、API 和 WebUI？
```

可以这样答：

```text
这是同一套核心能力的多入口封装。
CLI 服务工程师和批处理任务，API 服务系统集成和 Agent 工具调用，WebUI 服务人工验证和低代码使用。
它们共享后面的任务编排和解析链路，避免重复实现。
```

```text
如果要把 MinerU 接入一个 AI Agent，你更可能用哪个入口？
```

可以这样答：

```text
通常优先用 FastAPI，因为 Agent 可以把文档解析封装成 tool，通过 HTTP 上传文件、提交任务、轮询状态、获取 Markdown/JSON 结果。
如果是在本机自动化脚本里，也可以直接调用 CLI。
生产环境大批量任务则可能通过 Router 接到多个 mineru-api worker。
```

---

## T01 - CLI / API / WebUI 编排层

```text
状态：了解中
阶段：任务编排层
核心问题：不同入口如何统一进入同一套解析流程？
```

关键函数：

- `mineru.cli.client.main()`
- `mineru.cli.client.run_orchestrated_cli()`
- `mineru.cli.fast_api.create_app()`
- `mineru.cli.fast_api.parse_pdf()`
- `mineru.cli.fast_api.submit_parse_task()`
- `mineru.cli.gradio_app.main()`

相关文件：

- `mineru/cli/client.py`
- `mineru/cli/fast_api.py`
- `mineru/cli/gradio_app.py`

作用：

```text
把不同入口统一成解析任务。

CLI 入口：
如果用户没有传 --api-url，CLI 会自动启动一个临时 mineru-api。
如果用户传了 --api-url，CLI 会调用已有的本地或远程 API。

API 入口：
接收 HTTP 上传文件，创建同步或异步任务。

WebUI 入口：
提供可视化上传界面，背后仍然调用 mineru-api。
```

输入：

- 用户文件
- 用户参数

输出：

- 标准化后的任务参数

下游：

- T02
- T03

---

## T02 - 读取输入文件

```text
状态：待了解
阶段：输入处理
核心问题：MinerU 如何把不同格式文件转成可处理的数据？
```

关键函数：

- `mineru.cli.common.read_fn()`
- `mineru.utils.guess_suffix_or_lang.guess_suffix_by_bytes()`
- `mineru.utils.pdf_image_tools.images_bytes_to_pdf_bytes()`

相关文件：

- `mineru/cli/common.py`
- `mineru/utils/guess_suffix_or_lang.py`
- `mineru/utils/pdf_image_tools.py`

作用：

```text
读取文件字节，并判断文件类型。

PDF：
直接读取为 PDF bytes。

图片：
先转换成 PDF bytes，再走 PDF 解析逻辑。

DOCX / PPTX / XLSX：
保留原始 bytes，后续进入 Office 原生解析逻辑。
```

输入：

- 文件路径或上传文件

输出：

- `pdf_bytes_list`
- `pdf_file_names`
- `file_suffix`

下游：

- T03
- T04

---

## T03 - 创建 API 异步任务

```text
状态：待了解
阶段：API 任务管理
核心问题：API 模式下，MinerU 如何管理任务状态？
```

关键函数 / 类：

- `mineru.cli.fast_api.create_async_parse_task()`
- `mineru.cli.fast_api.AsyncParseTask`
- `mineru.cli.fast_api.AsyncTaskManager`
- `AsyncTaskManager.submit()`
- `AsyncTaskManager._process_task()`
- `AsyncTaskManager._run_task()`

相关文件：

- `mineru/cli/fast_api.py`

作用：

```text
API 不直接在请求函数里解析文件。
它会先创建一个任务对象 AsyncParseTask。
任务进入 AsyncTaskManager 队列。
后台 worker 再执行真正的解析。
```

任务状态：

- `pending`
- `processing`
- `completed`
- `failed`

输入：

- 上传文件
- 解析参数

输出：

- `task_id`
- 任务状态
- 结果查询地址

下游：

- T04
- T12

---

## T04 - 核心调度 do_parse()

```text
状态：待了解
阶段：核心调度
核心问题：MinerU 的主流程在哪里分流？
```

关键函数：

- `mineru.cli.common.do_parse()`
- `mineru.cli.common.aio_do_parse()`

相关文件：

- `mineru/cli/common.py`

作用：

```text
这是 MinerU 解析链路的核心调度函数。

它负责：
1. 先处理 Office 文件
2. 删除已经由 Office 分支处理过的文件
3. 对 PDF / 图片转来的 PDF bytes 做预处理
4. 根据 backend 参数选择 pipeline / vlm / hybrid
5. 调用对应后端
6. 触发统一输出
```

分流逻辑：

```text
do_parse()
  |
  +-- _process_office_doc()
  |
  +-- backend == "pipeline"
  |      |
  |      v
  |   _process_pipeline()
  |
  +-- backend.startswith("vlm-")
  |      |
  |      v
  |   _process_vlm()
  |
  +-- backend.startswith("hybrid-")
         |
         v
      _process_hybrid()
```

输入：

- 输出目录
- 文件名列表
- 文件 bytes 列表
- 语言列表
- backend
- parse_method
- formula/table 参数

输出：

- 不直接返回结构化内容
- 主要通过写文件产生结果

下游：

- T05
- T06
- T07
- T08
- T09
- T11

---

## T05 - Office 文件解析

```text
状态：待了解
阶段：Office 原生解析
核心问题：DOCX / PPTX / XLSX 为什么不走 PDF pipeline？
```

关键函数：

- `mineru.cli.common._process_office_doc()`
- `mineru.backend.office.docx_analyze.office_docx_analyze()`
- `mineru.backend.office.pptx_analyze.office_pptx_analyze()`
- `mineru.backend.office.xlsx_analyze.office_xlsx_analyze()`
- `mineru.backend.office.model_output_to_middle_json.result_to_middle_json()`

相关文件：

- `mineru/cli/common.py`
- `mineru/backend/office/docx_analyze.py`
- `mineru/backend/office/pptx_analyze.py`
- `mineru/backend/office/xlsx_analyze.py`
- `mineru/backend/office/model_output_to_middle_json.py`

作用：

```text
Office 文件可以从原始结构中提取段落、表格、样式、图片等信息。
因此它们不需要先转成 PDF 再 OCR。
这样速度更快，也更能保留 Office 文档原有结构。
```

输入：

- DOCX / PPTX / XLSX bytes

输出：

- `middle_json`
- `model_output`

下游：

- T10
- T11

---

## T06 - PDF / 图片预处理

```text
状态：待了解
阶段：PDF 预处理
核心问题：PDF 在进模型前做了什么准备？
```

关键函数：

- `mineru.cli.common._prepare_pdf_bytes()`
- `mineru.cli.common.convert_pdf_bytes_to_bytes()`
- `mineru.utils.pdfium_guard.rewrite_pdf_bytes_with_pdfium()`

相关文件：

- `mineru/cli/common.py`
- `mineru/utils/pdfium_guard.py`

作用：

```text
对 PDF bytes 做标准化处理。
如果用户指定 start_page_id / end_page_id，也会在这里截取页码范围。
图片输入在 T02 已经被转成 PDF，所以这里也会统一按 PDF 处理。
```

输入：

- PDF bytes
- 起始页
- 结束页

输出：

- 处理后的 PDF bytes

下游：

- T07
- T08
- T09

---

## T07 - pipeline 后端

```text
状态：待了解
阶段：传统多模型解析
核心问题：pipeline 后端具体做什么？
```

关键函数 / 类：

- `mineru.cli.common._process_pipeline()`
- `mineru.backend.pipeline.pipeline_analyze.doc_analyze_streaming()`
- `mineru.backend.pipeline.pipeline_analyze.ModelSingleton`
- `mineru.backend.pipeline.pipeline_analyze.custom_model_init()`
- `mineru.backend.pipeline.model_init.MineruPipelineModel`

相关文件：

- `mineru/cli/common.py`
- `mineru/backend/pipeline/pipeline_analyze.py`
- `mineru/backend/pipeline/model_init.py`
- `mineru/backend/pipeline/model_json_to_middle_json.py`

作用：

```text
pipeline 是传统文档解析流水线。
它通常包含：
1. PDF 页面渲染成图片
2. 版面检测
3. OCR
4. 表格识别
5. 公式识别
6. 段落和阅读顺序整理
7. 转成 middle_json
```

特点：

- 稳定
- 多语言支持较好
- 可 CPU / GPU
- 低幻觉

输入：

- PDF bytes
- lang
- parse_method
- formula/table 参数

输出：

- `middle_json`
- `model_list`

下游：

- T10
- T11

---

## T08 - VLM 后端

```text
状态：待了解
阶段：视觉语言模型解析
核心问题：VLM 后端和 pipeline 有什么区别？
```

关键函数 / 类：

- `mineru.cli.common._process_vlm()`
- `mineru.cli.common._async_process_vlm()`
- `mineru.backend.vlm.vlm_analyze.doc_analyze()`
- `mineru.backend.vlm.vlm_analyze.aio_doc_analyze()`
- `mineru.backend.vlm.vlm_analyze.ModelSingleton`
- `mineru_vl_utils.MinerUClient`

相关文件：

- `mineru/cli/common.py`
- `mineru/backend/vlm/vlm_analyze.py`
- `mineru/backend/vlm/model_output_to_middle_json.py`
- `mineru/backend/vlm/vlm_middle_json_mkcontent.py`

作用：

```text
VLM 后端使用视觉语言模型直接理解页面图像。
它更擅长复杂版面、图文混排、表格和语义结构。
```

可用形态：

- `vlm-auto-engine`
- `vlm-http-client`
- `vlm-vllm-engine`
- `vlm-lmdeploy-engine`
- `vlm-mlx-engine`

输入：

- PDF bytes
- VLM backend
- server_url，可选
- formula/table 参数

输出：

- `middle_json`
- `infer_result`

下游：

- T10
- T11

---

## T09 - hybrid 后端

```text
状态：待了解
阶段：混合解析
核心问题：hybrid 为什么同时需要 pipeline 和 VLM？
```

关键函数 / 类：

- `mineru.cli.common._process_hybrid()`
- `mineru.cli.common._async_process_hybrid()`
- `mineru.backend.hybrid.hybrid_analyze.doc_analyze()`
- `mineru.backend.hybrid.hybrid_analyze.aio_doc_analyze()`
- `mineru.backend.hybrid.hybrid_model_output_to_middle_json.result_to_middle_json()`

相关文件：

- `mineru/cli/common.py`
- `mineru/backend/hybrid/hybrid_analyze.py`
- `mineru/backend/hybrid/hybrid_model_output_to_middle_json.py`
- `mineru/backend/hybrid/hybrid_magic_model.py`

作用：

```text
hybrid 后端把 pipeline 和 VLM 组合起来。

pipeline 负责稳定的检测、OCR、基础结构。
VLM 负责更高精度的页面理解、复杂区域识别和语义补强。
```

特点：

- 精度高
- 依赖更多
- 本地 hybrid 需要 pipeline 依赖，如 torch
- `hybrid-http-client` 仍需要部分本地 pipeline 能力

输入：

- PDF bytes
- lang
- parse_method
- VLM backend
- server_url，可选

输出：

- `middle_json`
- `infer_result`
- `_vlm_ocr_enable`

下游：

- T10
- T11

---

## T10 - middle_json 中间结构

```text
状态：待了解
阶段：统一结构层
核心问题：为什么所有后端都要变成 middle_json？
```

关键函数：

- `pipeline.model_json_to_middle_json.*`
- `vlm.model_output_to_middle_json.*`
- `hybrid.hybrid_model_output_to_middle_json.*`
- `office.model_output_to_middle_json.result_to_middle_json()`

相关文件：

- `mineru/backend/pipeline/model_json_to_middle_json.py`
- `mineru/backend/vlm/model_output_to_middle_json.py`
- `mineru/backend/hybrid/hybrid_model_output_to_middle_json.py`
- `mineru/backend/office/model_output_to_middle_json.py`

作用：

```text
不同后端的模型输出格式不一样。
MinerU 会把它们统一转换成 middle_json。

之后的 Markdown、content_list、图片引用、可视化输出，
都基于这个统一结构生成。
```

典型内容：

- 页面信息
- 文本块
- 标题块
- 表格块
- 图片块
- 公式块
- bbox 坐标
- 阅读顺序
- 后端标记
- 版本信息

输入：

- pipeline / VLM / hybrid / Office 的原始模型输出

输出：

- `middle_json`

下游：

- T11

---

## T11 - 输出文件生成

```text
状态：待了解
阶段：结果导出
核心问题：Markdown 和 JSON 是在哪里生成的？
```

关键函数：

- `mineru.cli.common._process_output()`
- `mineru.backend.pipeline.pipeline_middle_json_mkcontent.union_make()`
- `mineru.backend.vlm.vlm_middle_json_mkcontent.union_make()`
- `mineru.backend.office.office_middle_json_mkcontent.union_make()`
- `mineru.utils.draw_bbox.draw_layout_bbox()`
- `mineru.utils.draw_bbox.draw_span_bbox()`

相关文件：

- `mineru/cli/common.py`
- `mineru/backend/pipeline/pipeline_middle_json_mkcontent.py`
- `mineru/backend/vlm/vlm_middle_json_mkcontent.py`
- `mineru/backend/office/office_middle_json_mkcontent.py`
- `mineru/utils/draw_bbox.py`

作用：

```text
把 middle_json 转成最终文件。
这是用户真正能看到和使用的结果。
```

输出文件：

- `<name>.md`
- `<name>_middle.json`
- `<name>_content_list.json`
- `<name>_content_list_v2.json`
- `<name>_model.json`
- `<name>_origin.pdf`
- `images/`
- `<name>_layout.pdf`
- `<name>_span.pdf`

输入：

- `middle_json`
- `model_output`
- 原始 PDF / Office bytes
- 输出目录

输出：

- 本地解析结果文件

下游：

- T12

---

## T12 - 返回结果

```text
状态：待了解
阶段：结果交付
核心问题：不同入口如何把结果交给用户？
```

关键函数：

- `mineru.cli.fast_api.build_result_dict()`
- `mineru.cli.fast_api.create_result_zip()`
- `mineru.cli.fast_api.build_result_response()`
- `mineru.cli.client.run_orchestrated_cli()`
- `mineru.cli.gradio_app.stream_to_markdown()`

相关文件：

- `mineru/cli/fast_api.py`
- `mineru/cli/client.py`
- `mineru/cli/gradio_app.py`

作用：

```text
CLI：
结果保存在用户指定的输出目录。

API：
可以返回 JSON，也可以打包成 ZIP 返回。

WebUI：
把 Markdown 和预览内容展示在页面上。
```

输入：

- T11 写出的结果文件

输出：

- 本地目录
- HTTP JSON
- HTTP ZIP
- WebUI 展示内容

---

## 学习顺序建议

```text
当前推荐：核心解析链路优先
T02 -> T04 -> T05 -> T07 -> T08 -> T09 -> T10 -> T11

第一轮：理解不同文件如何进入不同解析路径
T02 -> T04 -> T05

第二轮：理解三种 PDF / 图片解析后端
T07 -> T08 -> T09

第三轮：理解为什么要统一成 middle_json，以及如何导出结果
T10 -> T11

暂缓：
T03 API 异步任务管理、T12 返回结果、Router 生产调度
```

---

## 当前学习看板

| ID | 任务 | 状态 | 关键文件 |
|---|---|---|---|
| T00 | 用户入口选择 | 已了解 | `pyproject.toml` |
| T01 | CLI / API / WebUI 编排层 | 暂缓 | `mineru/cli/*` |
| T02 | 读取输入文件 | 重点待了解 | `mineru/cli/common.py` |
| T03 | 创建 API 异步任务 | 暂缓 | `mineru/cli/fast_api.py` |
| T04 | 核心调度 do_parse() | 重点待了解 | `mineru/cli/common.py` |
| T05 | Office 文件解析 | 重点待了解 | `mineru/backend/office/*` |
| T06 | PDF / 图片预处理 | 重点待了解 | `mineru/cli/common.py` |
| T07 | pipeline 后端 | 重点待了解 | `mineru/backend/pipeline/*` |
| T08 | VLM 后端 | 重点待了解 | `mineru/backend/vlm/*` |
| T09 | hybrid 后端 | 重点待了解 | `mineru/backend/hybrid/*` |
| T10 | middle_json 中间结构 | 重点待了解 | `mineru/backend/*/*middle_json*` |
| T11 | 输出文件生成 | 重点待了解 | `mineru/cli/common.py` |
| T12 | 返回结果 | 暂缓 | `mineru/cli/fast_api.py` |
