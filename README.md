# 📝 AI 报告自动生成器 | AI Report Generator

> [中文](#中文) | [English](#english)

---

<a id="中文"></a>
## 🇨🇳 中文

> 把零散、无结构的工作笔记转化为格式专业的 Word 文档。支持多种报告模板：周报、项目进展、工作总结、会议纪要。

![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red?logo=streamlit)
![DeepSeek](https://img.shields.io/badge/DeepSeek-API-blue)
![python-docx](https://img.shields.io/badge/python--docx-1.1+-green)

![System Screenshot](screenshots/main.png)

### 🎯 应用场景

**工作场景：**
- **周报** — 随手记下本周做了什么，AI 自动组织成结构化周报（已完成/进行中/问题/下周计划）
- **项目进展报告** — 贴入零散的项目笔记，输出含里程碑、风险、下一步的正式报告
- **会议纪要** — 丢入粗糙的会议记录（或转录文本），生成含参会人、讨论要点、决策、待办的正式纪要
- **工作总结** — 月末/季末？把所有成就倒出来，AI 生成专业总结文档
- **绩效自评** — 整理全年成果，生成自评文档

**个人场景：**
- **学习笔记整理** — 把凌乱笔记整理成有结构的总结
- **活动报告** — 参加会议/培训后，把笔记转成正式报告分享给团队
- **博客草稿** — 粗糙想法 → 结构化草稿（引言、主体、结论）

### 核心差异化

大多数 AI 写作工具只生成纯文本。本工具更进一步——生成**格式完整的 Word 文档（.docx）**，含标题层级、加粗、项目符号、表格，专业排版，可以直接提交给领导或团队。

### ✨ 功能特性

- 📝 **智能内容组织** — AI 自动将零散笔记分类到对应板块
- 📋 **4 种报告模板** — 技术周报、项目周报、工作总结、会议纪要
- 📥 **一键导出 Word** — 生成 `.docx` 文件，含专业排版（标题、加粗、列表、表格）
- 👁️ **实时预览** — 导出前在浏览器中预览报告
- ✏️ **灵活输入** — 支持结构化表单输入和自由文本输入
- 🎨 **专业样式** — Word 导出含统一字体、间距、配色

### 📋 模板说明

| 模板 | 适用场景 | 板块 |
|------|----------|------|
| **技术周报** | 工程师、开发者 | 已完成任务、进行中工作、问题与方案、下周计划 |
| **项目周报** | 项目经理 | 项目概述、里程碑进度、风险评估、资源状况 |
| **工作总结** | 月度/季度回顾 | 关键成果、挑战、成长方向、未来目标 |
| **会议纪要** | 会议后记录 | 会议信息、参会人、讨论主题、决策、待办事项 |

### 🏗️ 系统架构

```
┌─────────────────────────────────────────────────┐
│              Streamlit Web UI                    │
│  ┌──────────┐  ┌───────────┐  ┌─────────────┐  │
│  │ 选择模板  │  │   输入    │  │  预览 & 导出 │  │
│  └────┬─────┘  └─────┬─────┘  └──────┬──────┘  │
└───────┼──────────────┼────────────────┼─────────┘
        │              │                │
┌───────▼──────────────▼────────────────▼─────────┐
│              后端模块                             │
│  ┌───────────────────┐  ┌───────────────────┐  │
│  │ report_generator  │  │  doc_exporter     │  │
│  │ .py               │  │  .py              │  │
│  │ (AI → 结构化      │  │  (Markdown →      │  │
│  │  报告内容)         │  │   .docx 格式化)   │  │
│  └───────────────────┘  └───────────────────┘  │
└─────────────────────────────────────────────────┘
                                 │
                                 ▼
                       ┌──────────────────┐
                       │  DeepSeek API    │
                       │  (内容生成)       │
                       └──────────────────┘
```

### 📁 项目结构

```
ai-report-generator/
├── app.py                  # Streamlit Web 界面
├── report_generator.py     # AI 报告生成引擎（模板 + DeepSeek）
├── doc_exporter.py         # Word 文档导出（python-docx 格式化）
├── requirements.txt        # Python 依赖
├── .env.example            # 环境变量模板
├── screenshots/            # UI 截图
│   └── main.png
└── 启动应用.bat             # Windows 快速启动
```

### 🚀 快速开始

```bash
git clone https://github.com/SsllF8/ai-report-generator.git
cd ai-report-generator
python -m venv .venv && .venv\Scripts\activate   # Windows
pip install -r requirements.txt
cp .env.example .env  # 填入 DEEPSEEK_API_KEY
streamlit run app.py
```

### ⚙️ 环境变量配置

| 变量名 | 必填 | 说明 |
|--------|------|------|
| `DEEPSEEK_API_KEY` | ✅ | DeepSeek API 密钥 |

### 🛠️ 技术栈

| 组件 | 技术 | 用途 |
|------|------|------|
| Web 框架 | Streamlit | 报告编辑与预览 UI |
| 大模型 | DeepSeek | 内容生成与组织 |
| 文档生成 | python-docx | Word 文档创建与格式化 |
| 模板系统 | 自研（Python） | 每种报告类型的结构化 prompt 模板 |

### 📖 工作原理

1. **模板选择** — 用户选择报告模板，模板定义输出结构（板块、标题、语气）
2. **笔记输入** — 用户输入零散的工作笔记
3. **AI 生成** — 笔记发给 DeepSeek，附带模板特定的 prompt：
   - 将每条笔记分类到合适的板块
   - 扩展和润色语言
   - 保持专业语气
   - 严格遵循模板结构
4. **预览** — 生成的报告在浏览器中展示为格式化 Markdown
5. **导出** — Markdown 报告转换为 `.docx`：
   - 标题层级（H1, H2, H3）
   - 加粗强调
   - 项目符号和编号列表
   - 表格
   - 统一字体和间距

### 💡 面试要点 / Interview Talking Points

**1. 为什么不直接让 AI 在网页上输出，还要导出 Word？**
- 企业环境中，正式文档必须是 Word 格式（审批、归档、打印）
- 纯文本没有排版，不能直接提交给领导
- python-docx 可以生成**接近人工排版**的文档，这才是"工具"而不是"玩具"

**2. 模板系统的设计思路？**
- 每种模板对应一个独立的 system prompt，定义输出结构
- 用 prompt 约束 AI 输出格式，比后处理正则更可靠
- 可扩展：加新模板只需要加一个新的 prompt 模板

**3. Markdown → Word 转换怎么做的？**
- python-docx 直接操作 Word 的 XML 结构
- 解析 Markdown 中的标题（#）、加粗（**）、列表（-）、表格
- 通过 Document.styles 设置全局字体和间距

**4. 这个项目体现了什么能力？**
- **NLP 应用能力**：用 LLM 做文本分类和生成
- **文档工程能力**：python-docx 操作，Markdown 解析
- **产品思维**：解决了"写周报"这个真实痛点

### ⚠️ 搭建中可能遇到的问题 / Troubleshooting

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| AI 生成的报告格式不统一 | 不同模板的 prompt 约束力不够 | 在 prompt 中加入更多 few-shot 示例 |
| Word 导出中文乱码 | python-docx 默认字体不支持中文 | 设置字体为"微软雅黑"或"宋体" |
| 导出的 Word 排版错乱 | Markdown 解析不完整 | 增强解析逻辑，处理嵌套列表和表格 |
| Streamlit 预览和 Word 不一致 | 两者渲染引擎不同 | 在 doc_exporter 中手动处理样式映射 |
| 报告内容过于模板化 | prompt 指令过于机械 | 在 prompt 中允许 AI 适当扩展和润色 |

### 🚀 扩展方向 / Future Enhancements

- **更多模板** — 年终总结、产品 PRD、技术方案、OKR 复盘
- **自定义模板编辑器** — 用户自己定义报告结构和 prompt
- **历史报告管理** — 保存、搜索、对比历史报告
- **多人协作** — 团队成员可以贡献各自的笔记，合并生成一份报告
- **邮件发送** — 一键通过 SMTP 发送报告到指定邮箱
- **数据驱动报告** — 从数据库/API 拉取数据（KPI、指标）自动填充
- **语音输入** — 支持语音录入笔记（Whisper ASR），解放双手

---

<a id="english"></a>
## 🇬🇧 English

> Transform scattered, unstructured work notes into polished, professionally formatted Word documents. Supports multiple report templates including weekly reports, project updates, work summaries, and meeting minutes.

![System Screenshot](screenshots/main.png)

### Use Cases

**Workplace:**
- **Weekly Reports** — Bullet points → structured weekly report with completed/in-progress/blockers/next week
- **Project Status Updates** — Unstructured notes → formatted progress report with milestones and risks
- **Meeting Minutes** — Rough notes → properly formatted minutes with attendees, decisions, and action items
- **Work Summaries** — Monthly/quarterly accomplishments → professional summary document
- **Performance Reviews** — Year-end achievements → self-evaluation document

### Key Differentiator

Most AI writing tools generate plain text. This tool produces **properly formatted Word documents (.docx)** with headings, tables, bullet lists, and professional styling — ready to submit to your manager.

### Features

- 📝 **Smart Content Organization** — AI categorizes notes into structured sections
- 📋 **4 Report Templates** — Technical Weekly, Project Weekly, Work Summary, Meeting Minutes
- 📥 **One-Click Word Export** — `.docx` with professional formatting
- 👁️ **Live Preview** — Preview in browser before export
- ✏️ **Flexible Input** — Structured form or free-form text

### Architecture

```
┌─────────────────────────────────────────────────┐
│              Streamlit Web UI                    │
│  ┌──────────┐  ┌───────────┐  ┌─────────────┐  │
│  │ Template │  │   Input   │  │  Preview &  │  │
│  │ Selection│  │   Notes   │  │  Export     │  │
│  └────┬─────┘  └─────┬─────┘  └──────┬──────┘  │
└───────┼──────────────┼────────────────┼─────────┘
        │              │                │
┌───────▼──────────────▼────────────────▼─────────┐
│              Backend Modules                     │
│  ┌───────────────────┐  ┌───────────────────┐  │
│  │ report_generator  │  │  doc_exporter     │  │
│  │ (AI → Structured  │  │  (Markdown →      │  │
│  │  Report Content)  │  │   .docx)          │  │
│  └───────────────────┘  └───────────────────┘  │
└─────────────────────────────────────────────────┘
                                 │
                                 ▼
                       ┌──────────────────┐
                       │  DeepSeek API    │
                       └──────────────────┘
```

### Quick Start

```bash
git clone https://github.com/SsllF8/ai-report-generator.git
cd ai-report-generator
python -m venv .venv && .venv\Scripts\activate   # Windows
pip install -r requirements.txt
cp .env.example .env  # Fill in your DEEPSEEK_API_KEY
streamlit run app.py
```

### Interview Talking Points

**1. Why export to Word instead of just displaying text?**
- Enterprise requires Word format for approval, archiving, and printing
- Plain text can't be submitted directly to management
- python-docx generates near-manual-quality formatting — this is a real tool, not a toy

**2. Template system design?**
- Each template = an independent system prompt defining output structure
- Prompt constraints more reliable than post-processing regex
- Extensible: adding a new template = adding a new prompt

**3. How does Markdown → Word conversion work?**
- python-docx operates on Word's XML structure directly
- Parse Markdown headings (#), bold (**), lists (-), tables
- Set global fonts and spacing via Document.styles

### Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Inconsistent AI output format | Prompt constraints not strong enough | Add more few-shot examples in prompt |
| Chinese garbled in Word export | Default font doesn't support Chinese | Set font to "微软雅黑" or "宋体" |
| Layout issues in export | Incomplete Markdown parsing | Enhance parser for nested lists and tables |
| Preview vs Word mismatch | Different rendering engines | Manually handle style mapping in doc_exporter |
| Reports feel templated | Prompts too mechanical | Allow AI to expand and polish content |

### Future Enhancements

- **More Templates** — Annual summary, PRD, technical specs, OKR review
- **Custom Template Editor** — Users define their own report structures
- **Report History** — Save, search, and compare past reports
- **Team Collaboration** — Merge notes from multiple team members
- **Email Delivery** — One-click SMTP report sending
- **Data-Driven Reports** — Auto-fill from database/API (KPIs, metrics)
- **Voice Input** — Whisper ASR for hands-free note taking

## 📄 License

This project is licensed under the MIT License.
