"""
智能工具矩阵路由系统
基于任务特性自动选择最优工具组合
"""

class ToolMatrixRouter:
    def __init__(self):
        self.tool_matrix = {
            "代码开发": {
                "简单补全": "Cursor Tab",
                "功能块生成": "Claude Code", 
                "复杂问题": "GPT5 Pro",
                "架构设计": "AutoGen多智能体"
            },
            "工作流自动化": {
                "可视化编排": "n8n",
                "浏览器自动化": "Playwright MCP", 
                "多工具协调": "MCP服务器矩阵",
                "监控预警": "自定义Agent"
            },
            "知识管理": {
                "文档处理": "RAG系统",
                "实时学习": "增强增量学习",
                "知识蒸馏": "模型压缩",
                "传承保护": "零删除版本管理"
            }
        }
    
    def route_task(self, task_description):
        """基于任务描述选择最优工具链"""
        if "代码" in task_description or "编程" in task_description:
            return self.tool_matrix["代码开发"]
        elif "自动化" in task_description or "工作流" in task_description:
            return self.tool_matrix["工作流自动化"] 
        elif "学习" in task_description or "知识" in task_description:
            return self.tool_matrix["知识管理"]
        else:
            return "使用默认工具矩阵"

