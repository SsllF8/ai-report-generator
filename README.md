# 📝 AI Report Generator

> Transform scattered, unstructured work notes into polished, professionally formatted Word documents. Supports multiple report templates including weekly reports, project updates, work summaries, and meeting minutes.

![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red?logo=streamlit)
![DeepSeek](https://img.shields.io/badge/DeepSeek-API-blue)
![python-docx](https://img.shields.io/badge/python--docx-1.1+-green)

![System Screenshot](screenshots/main.png)

## 🎯 Use Cases

### Workplace Scenarios
- **Weekly Reports** — Jot down bullet points of what you did this week, and the AI organizes them into a structured weekly report with sections: completed work, in-progress items, blockers, and next week's plan
- **Project Status Updates** — Paste unstructured project notes and get a formatted project progress report with milestones, risks, and next steps
- **Meeting Minutes** — Throw in rough meeting notes (or a transcript) and get properly formatted minutes with attendees, discussion points, decisions, and action items
- **Work Summaries** — End of month/quarter? Dump all your accomplishments and the AI creates a professional summary document
- **Performance Reviews** — Compile your achievements throughout the year and generate a self-evaluation document

### Personal Scenarios
- **Learning Notes** — Convert messy study notes into organized summaries with key concepts and takeaways
- **Event Reports** — After attending a conference or workshop, turn your notes into a formal event report to share with your team
- **Blog Post Drafts** — Rough ideas → structured draft with introduction, body sections, and conclusion

### Key Differentiator
Most AI writing tools generate plain text. This tool goes further — it produces **properly formatted Word documents (.docx)** with headings, tables, bullet lists, and professional styling that you can directly submit to your manager or team.

## ✨ Features

### Core Capabilities
- 📝 **Smart Content Organization** — AI automatically categorizes scattered notes into structured sections (completed/in-progress/issues/plans)
- 📋 **4 Report Templates** — Technical Weekly Report, Project Weekly Report, Work Summary, Meeting Minutes
- 📥 **One-Click Word Export** — Generate `.docx` files with professional formatting (headings, bold text, bullet lists, tables)
- 👁️ **Live Preview** — Preview the generated report in the browser before exporting
- ✏️ **Custom Input** — Support for both structured form input and free-form text input
- 🎨 **Professional Styling** — Word exports include proper fonts, spacing, colors, and layout

### Templates

| Template | Best For | Sections |
|----------|----------|----------|
| **Technical Weekly Report** | Engineers, developers | Completed tasks, in-progress work, issues & solutions, next week's plan |
| **Project Weekly Report** | Project managers | Project overview, milestone progress, risk assessment, resource status |
| **Work Summary** | Monthly/quarterly reviews | Key achievements, challenges, growth areas, future goals |
| **Meeting Minutes** | Post-meeting documentation | Meeting info, attendees, discussion topics, decisions, action items |

## 🏗️ Architecture

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
│  │ .py               │  │  .py              │  │
│  │ (AI → Structured  │  │  (Markdown →      │  │
│  │  Report Content)  │  │   .docx with      │  │
│  │                   │  │   formatting)      │  │
│  └───────────────────┘  └───────────────────┘  │
└─────────────────────────────────────────────────┘
                                 │
                                 ▼
                       ┌──────────────────┐
                       │  DeepSeek API    │
                       │  (Content Gen)   │
                       └──────────────────┘
```

## 📁 Project Structure

```
ai-report-generator/
├── app.py                  # Streamlit web interface
├── report_generator.py     # AI report generation engine (templates + DeepSeek)
├── doc_exporter.py         # Word document export (python-docx formatting)
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables template
├── screenshots/            # UI screenshots
│   └── main.png
└── 启动应用.bat             # Windows quick start
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- DeepSeek API Key ([Get one here](https://platform.deepseek.com))

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/SsllF8/ai-report-generator.git
cd ai-report-generator

# 2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env and fill in your DEEPSEEK_API_KEY

# 5. Run the application
streamlit run app.py
```

Or simply double-click `启动应用.bat` on Windows.

### How to Use

1. **Choose Template** — Select from Technical Weekly Report, Project Weekly Report, Work Summary, or Meeting Minutes
2. **Input Notes** — Type or paste your scattered work notes in the text area. For example:
   ```
   - 修复了用户登录页面的 bug，原因是 token 过期逻辑没处理好
   - 完成了数据导出功能的开发
   - 数据库查询有点慢，需要优化索引
   - 和产品经理讨论了下个版本的需求排期
   - 帮新同事 review 了代码
   - 下周计划：开始做报表模块
   ```
3. **Generate** — Click "生成报告" and the AI will organize your notes into a structured report
4. **Preview & Export** — Review the preview, then click "导出 Word" to download a formatted `.docx` file

## ⚙️ Configuration

| Variable | Required | Description |
|----------|----------|-------------|
| `DEEPSEEK_API_KEY` | ✅ | Your DeepSeek API key |

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Web Framework | Streamlit | Report editing & preview UI |
| LLM | DeepSeek | Content generation and organization |
| Document Generation | python-docx | Word document creation with formatting |
| Template System | Custom (Python) | Structured prompt templates per report type |

## 🔧 How It Works

1. **Template Selection** — User selects a report template, which defines the output structure (sections, headings, tone)
2. **Note Input** — User enters unstructured notes about their work
3. **AI Generation** — The notes are sent to DeepSeek with a template-specific prompt that instructs the AI to:
   - Classify each note into the appropriate section
   - Expand and polish the language
   - Maintain a professional tone
   - Follow the template's structure exactly
4. **Preview** — Generated report is displayed in the browser as formatted Markdown
5. **Export** — The Markdown report is converted to a `.docx` file with:
   - Proper heading hierarchy (H1, H2, H3)
   - Bold text for emphasis
   - Bullet lists and numbered lists
   - Tables where applicable
   - Consistent fonts and spacing

## 📄 License

This project is licensed under the MIT License.
