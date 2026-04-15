import streamlit as st
import os
from datetime import datetime
from report_generator import generate_report, TEMPLATES
from doc_exporter import export_to_word

# ============ 页面配置 ============
st.set_page_config(
    page_title="AI 报告生成器",
    page_icon="📝",
    layout="wide"
)

# 自定义样式
st.markdown("""
<style>
    .main-header {
        font-size: 2rem;
        font-weight: 700;
        color: #2C3E50;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1rem;
        color: #95A5A6;
        text-align: center;
        margin-bottom: 2rem;
    }
    .template-card {
        padding: 1.2rem;
        border-radius: 10px;
        border: 2px solid #ECF0F1;
        background: #FAFAFA;
        cursor: pointer;
        transition: all 0.2s;
    }
    .template-card:hover {
        border-color: #3498DB;
        background: #EBF5FB;
    }
    .template-card.selected {
        border-color: #3498DB;
        background: #D6EAF8;
    }
    .section-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #2C3E50;
        padding: 0.8rem 0 0.5rem 0;
        border-bottom: 2px solid #3498DB;
        margin-bottom: 0.5rem;
    }
    .report-item {
        padding: 0.4rem 0 0.4rem 1rem;
        color: #333;
        border-left: 3px solid #3498DB;
        margin-bottom: 0.3rem;
    }
    .summary-box {
        padding: 1rem;
        background: #FEF9E7;
        border-left: 4px solid #F1C40F;
        border-radius: 4px;
        margin-bottom: 1.5rem;
    }
    div[data-testid="stTextInput"] > div > div > input {
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

# ============ 会话状态 ============
if "report_data" not in st.session_state:
    st.session_state.report_data = None
if "raw_content" not in st.session_state:
    st.session_state.raw_content = ""
if "template_key" not in st.session_state:
    st.session_state.template_key = "tech_weekly"
if "export_path" not in st.session_state:
    st.session_state.export_path = None

# ============ 主界面 ============
st.markdown('<div class="main-header">📝 AI 报告生成器</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">输入零散工作记录，AI 自动生成结构化报告并导出 Word</div>', unsafe_allow_html=True)

# ============ 模板选择 ============
st.subheader("📄 选择报告模板")
cols = st.columns(4)
template_keys = list(TEMPLATES.keys())

for i, key in enumerate(template_keys):
    t = TEMPLATES[key]
    selected = st.session_state.template_key == key
    
    with cols[i]:
        card_html = f"""
        <div class="template-card {'selected' if selected else ''}">
            <div style="font-size: 1.8rem; text-align: center;">{t['icon']}</div>
            <div style="font-size: 1rem; font-weight: 600; text-align: center; color: #2C3E50;">{t['name']}</div>
            <div style="font-size: 0.8rem; text-align: center; color: #7F8C8D; margin-top: 0.3rem;">{t['description']}</div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
        if st.button(f"选择", key=f"btn_{key}", use_container_width=True,
                     type="primary" if selected else "secondary"):
            st.session_state.template_key = key
            st.rerun()

st.markdown("---")

# ============ 内容输入 ============
col_input, col_extra = st.columns([3, 1])

with col_input:
    st.subheader("✏️ 输入工作内容")
    content = st.text_area(
        "在这里输入你的零散工作记录（每行一条，随便写就行）",
        value=st.session_state.raw_content,
        height=200,
        placeholder="示例：\n- 修复了登录页面的 bug\n- 开发了用户管理模块\n- 开会讨论了下周的排期\n- 学习了 Docker 部署\n- 数据库查询有点慢，需要优化\n- 客户反馈了两个新需求"
    )
    st.session_state.raw_content = content

with col_extra:
    st.subheader("📝 补充信息")
    extra_info = st.text_area(
        "可选：补充一些背景信息",
        height=100,
        placeholder="示例：\n部门：技术部\n周期：4月第3周\n项目：企业知识库系统"
    )

# ============ 生成按钮 ============
st.markdown("---")
if st.button("🚀 生成报告", type="primary", use_container_width=True, disabled=not content.strip()):
    with st.spinner("AI 正在生成报告，请稍候..."):
        st.session_state.report_data = generate_report(
            content=content,
            template_key=st.session_state.template_key,
            extra_info=extra_info
        )
        st.session_state.export_path = None
    st.rerun()

# ============ 报告预览 ============
if st.session_state.report_data:
    report = st.session_state.report_data
    
    if report.get("error"):
        st.error(f"❌ 报告生成失败：{report['error']}")
    else:
        st.markdown("---")
        st.subheader(f"📖 报告预览")
        
        # 摘要
        if report.get("summary"):
            st.markdown(f"""
            <div class="summary-box">
                <strong>摘要：</strong>{report['summary']}
            </div>
            """, unsafe_allow_html=True)
        
        # 各段落
        section_display = {
            "tech_weekly": [
                ("completed", "✅ 本周完成"),
                ("in_progress", "🔄 进行中"),
                ("issues", "⚠️ 问题与风险"),
                ("next_week", "📋 下周计划"),
            ],
            "project_weekly": [
                ("progress", "📈 项目进展"),
                ("milestones", "🏁 里程碑"),
                ("risks", "🔴 风险预警"),
                ("resource_needs", "💡 资源需求"),
            ],
            "work_summary": [
                ("achievements", "🏆 工作成果"),
                ("growth", "📈 能力成长"),
                ("improvements", "🔧 不足与改进"),
                ("future_plans", "🎯 未来规划"),
            ],
            "meeting_notes": [
                ("discussions", "💬 议题讨论"),
                ("decisions", "✅ 决议事项"),
                ("action_items", "🎯 行动项"),
            ],
        }
        
        template_key = report.get("_template_key", "tech_weekly")
        sections = section_display.get(template_key, section_display["tech_weekly"])
        
        for field_name, section_title in sections:
            items = report.get(field_name, [])
            if not items:
                continue
            
            st.markdown(f'<div class="section-title">{section_title}</div>', unsafe_allow_html=True)
            
            for item in items:
                st.markdown(f'<div class="report-item">{item}</div>', unsafe_allow_html=True)
        
        # 按钮区域
        st.markdown("---")
        btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])
        
        with btn_col1:
            if st.button("📥 导出 Word 文档", type="primary", use_container_width=True):
                with st.spinner("正在生成 Word 文档..."):
                    filepath = export_to_word(report)
                    st.session_state.export_path = filepath
                st.rerun()
        
        with btn_col2:
            if st.button("🔄 重新生成", use_container_width=True):
                st.session_state.report_data = None
                st.session_state.export_path = None
                st.rerun()
        
        with btn_col3:
            if st.button("🗑️ 清空内容", use_container_width=True):
                st.session_state.raw_content = ""
                st.session_state.report_data = None
                st.session_state.export_path = None
                st.rerun()
        
        # 下载提示
        if st.session_state.export_path:
            filepath = st.session_state.export_path
            st.success(f"📄 文档已保存：{filepath}")
            with open(filepath, "rb") as f:
                st.download_button(
                    label="⬇️ 下载 Word 文档",
                    data=f.read(),
                    file_name=os.path.basename(filepath),
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    use_container_width=True
                )

# ============ 使用说明 ============
st.markdown("---")
with st.expander("📖 使用说明"):
    st.markdown("""
    **使用步骤：**
    1. **选择模板** — 根据需要选择周报、总结、会议纪要等模板
    2. **输入内容** — 在文本框中输入零散的工作记录，每行一条就行
    3. **补充信息**（可选）— 可以添加部门、周期、项目名等背景信息
    4. **生成报告** — 点击按钮，AI 自动整理成结构化报告
    5. **预览 & 导出** — 在页面预览效果，满意后导出 Word 文档

    **小技巧：**
    - 内容写得越详细，生成的报告越丰富
    - 不用在意格式，AI 会自动整理
    - 可以直接复制粘贴聊天记录、备忘录等
    - 导出的 Word 文档可以直接用 Office/WPS 编辑
    """)
