import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY", ""),
    base_url="https://api.deepseek.com"
)

# 报告模板的 prompt 定义
TEMPLATES = {
    "tech_weekly": {
        "name": "技术周报",
        "icon": "💻",
        "description": "适合技术人员提交的工作周报",
        "sections": ["本周完成", "进行中", "问题与风险", "下周计划"],
        "prompt": """你是专业的技术周报撰写助手。请根据用户提供的零散工作记录，生成一份结构清晰的技术周报。

要求：
1. 将内容整理为以下结构：
   - **本周完成**：列出已完成的工作项（归类、排序）
   - **进行中**：列出正在推进的工作
   - **问题与风险**：遇到的问题和风险点
   - **下周计划**：建议的下一步工作安排
2. 语言简洁专业，使用技术术语
3. 每项用 1-2 句话描述
4. 如果用户内容不够详细，合理推断和补充
5. 保持客观，不要过度吹嘘

请严格以 JSON 格式输出，结构如下：
{{
  "title": "周报标题",
  "completed": ["完成项1", "完成项2"],
  "in_progress": ["进行中1", "进行中2"],
  "issues": ["问题1", "问题2"],
  "next_week": ["计划1", "计划2"],
  "summary": "一句话本周总结"
}}"""
    },
    "project_weekly": {
        "name": "项目周报",
        "icon": "📊",
        "description": "适合项目经理汇报项目进展",
        "sections": ["项目进展", "里程碑", "风险预警", "资源需求"],
        "prompt": """你是专业的项目周报撰写助手。请根据用户提供的项目信息，生成一份项目进展周报。

要求：
1. 将内容整理为以下结构：
   - **项目进展**：各模块/任务的推进情况
   - **里程碑**：已达成和即将达成的关键节点
   - **风险预警**：潜在风险和应对措施
   - **资源需求**：需要协调的资源和支持
2. 体现项目管理视角，关注进度、质量、成本
3. 用数据说话（如果有量化信息）
4. 标注优先级（紧急/重要/一般）

请严格以 JSON 格式输出：
{{
  "title": "项目周报标题",
  "progress": ["进展1", "进展2"],
  "milestones": ["里程碑1", "里程碑2"],
  "risks": ["风险1", "风险2"],
  "resource_needs": ["资源需求1", "资源需求2"],
  "summary": "一句话项目整体评价"
}}"""
    },
    "work_summary": {
        "name": "工作总结",
        "icon": "📋",
        "description": "适合月度/季度/年度工作总结",
        "sections": ["工作成果", "能力成长", "不足与改进", "未来规划"],
        "prompt": """你是专业的工作总结撰写助手。请根据用户提供的零散工作记录，生成一份高质量的工作总结。

要求：
1. 将内容整理为以下结构：
   - **工作成果**：主要完成的工作和取得的成绩（用数据量化）
   - **能力成长**：技能提升、经验积累
   - **不足与改进**：有待改进的地方和改进方案
   - **未来规划**：下一阶段的计划和目标
2. 语言正式、有逻辑
3. 突出亮点和价值贡献
4. 成果部分尽量量化（完成了X个、提升了Y%等）

请严格以 JSON 格式输出：
{{
  "title": "工作总结标题",
  "achievements": ["成果1", "成果2"],
  "growth": ["成长1", "成长2"],
  "improvements": ["改进1", "改进2"],
  "future_plans": ["规划1", "规划2"],
  "summary": "一句话整体评价"
}}"""
    },
    "meeting_notes": {
        "name": "会议纪要",
        "icon": "🎯",
        "description": "适合整理会议内容和决议",
        "sections": ["议题讨论", "决议事项", "行动项", "下次会议"],
        "prompt": """你是专业的会议纪要整理助手。请根据用户提供的会议记录，生成一份清晰的会议纪要。

要求：
1. 将内容整理为以下结构：
   - **议题讨论**：每个议题的讨论要点和结论
   - **决议事项**：会议上达成的决定和共识
   - **行动项**：具体待办事项，标注责任人和截止时间
   - **下次会议**：下次会议的时间和议题
2. 语言精炼，突出重点
3. 行动项必须包含"做什么、谁负责、何时完成"
4. 决议要明确，不能模糊

请严格以 JSON 格式输出：
{{
  "title": "会议纪要标题",
  "discussions": ["讨论要点1", "讨论要点2"],
  "decisions": ["决议1", "决议2"],
  "action_items": ["行动项1（责任人-截止时间）", "行动项2（责任人-截止时间）"],
  "next_meeting": "下次会议信息",
  "summary": "一句话会议总结"
}}"""
    }
}


def generate_report(content: str, template_key: str, extra_info: str = "") -> dict:
    """
    调用 DeepSeek API 生成结构化报告
    
    Args:
        content: 用户输入的零散工作内容
        template_key: 模板类型（tech_weekly / project_weekly / work_summary / meeting_notes）
        extra_info: 补充信息（如日期范围、部门、项目名等）
    
    Returns:
        dict: 结构化的报告数据
    """
    template = TEMPLATES.get(template_key, TEMPLATES["tech_weekly"])
    
    user_message = f"请根据以下工作记录，生成一份【{template['name']}】：\n\n"
    
    if extra_info:
        user_message += f"补充信息：{extra_info}\n\n"
    
    user_message += f"工作记录：\n{content}"
    
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": template["prompt"]},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            response_format={"type": "json_object"}
        )
        
        result_text = response.choices[0].message.content
        report_data = json.loads(result_text)
        
        # 添加模板元信息
        report_data["_template_key"] = template_key
        report_data["_template_name"] = template["name"]
        report_data["_template_icon"] = template["icon"]
        report_data["_sections"] = template["sections"]
        
        return report_data
        
    except json.JSONDecodeError:
        # AI 返回的不是合法 JSON，尝试提取
        return {
            "title": f"{template['name']}",
            "error": "AI 返回格式异常，请重试",
            "_template_key": template_key,
            "_template_name": template["name"],
            "_template_icon": template["icon"],
            "_sections": template["sections"],
            "summary": "生成失败"
        }
    except Exception as e:
        return {
            "title": f"{template['name']}",
            "error": str(e),
            "_template_key": template_key,
            "_template_name": template["name"],
            "_template_icon": template["icon"],
            "_sections": template["sections"],
            "summary": f"生成失败：{str(e)}"
        }


def regenerate_section(content: str, template_key: str, section: str, current_text: str) -> str:
    """
    重新生成报告中的某一个段落（用户不满意某个部分时）
    
    Args:
        content: 原始工作内容
        template_key: 模板类型
        section: 要重新生成的段落名
        current_text: 当前段落的内容
    
    Returns:
        str: 重新生成后的段落内容
    """
    template = TEMPLATES.get(template_key, TEMPLATES["tech_weekly"])
    
    prompt = f"""{template['prompt']}

现在请只重新生成报告中的"{section}"部分。
用户对当前的"{section}"内容不满意，当前内容为：
{current_text}

请给出改进后的版本。只输出该部分的内容，以 JSON 数组格式返回，例如：
["改进后的条目1", "改进后的条目2"]"""

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "user", "content": f"原始工作记录：\n{content}\n\n{prompt}"}
            ],
            temperature=0.8,
            response_format={"type": "json_object"}
        )
        result = json.loads(response.choices[0].message.content)
        # 返回第一个数组字段
        for key, value in result.items():
            if isinstance(value, list):
                return value
        return current_text
    except:
        return current_text
