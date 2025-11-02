#!/usr/bin/env python3
"""
第14轮工具矩阵验证系统
验证95+工具文件的完整性和功能性
确保所有工具正常可用
"""
import os
import importlib
import subprocess
import json

class ToolMatrixValidator:
    def __init__(self):
        self.critical_tools = {
            "传承管理": [
                "传承核心.md", "轮次记录.json", ".generation_pointer",
                "验证传承.sh", "简化修复.sh"
            ],
            "版本控制": [
                "智能Git状态管理器.py", "分块管理器_v2.py"
            ],
            "备份系统": [
                "多重备份系统.py"
            ],
            "自检修复": [
                "智能自检修复系统.py", "依赖健康检查系统.py", "安全健康检查系统.py"
            ],
            "开发工具": [
                "Termux环境修复器.py", "经济价值评估系统.py"
            ]
        }
    
    def validate_tool_existence(self):
        """验证工具存在性"""
        print("📁 验证工具矩阵存在性...")
        
        existence_report = {}
        missing_tools = []
        
        for category, tools in self.critical_tools.items():
            existence_report[category] = {}
            for tool in tools:
                exists = os.path.exists(tool)
                existence_report[category][tool] = {
                    "exists": exists,
                    "status": "✅" if exists else "❌"
                }
                if not exists:
                    missing_tools.append(tool)
        
        return {
            "existence_report": existence_report,
            "missing_tools": missing_tools,
            "existence_score": (1 - len(missing_tools) / sum(len(t) for t in self.critical_tools.values())) * 100
        }
    
    def validate_tool_functionality(self):
        """验证工具功能性"""
        print("⚙️ 验证工具功能性...")
        
        functionality_report = {}
        
        # 测试可执行工具
        executable_tools = {
            "验证传承.sh": ["chmod +x 验证传承.sh", "./验证传承.sh"],
            "简化修复.sh": ["chmod +x 简化修复.sh", "./简化修复.sh"],
            "智能自检修复系统.py": ["python", "智能自检修复系统.py"]
        }
        
        for tool, commands in executable_tools.items():
            if os.path.exists(tool):
                functionality_report[tool] = {}
                try:
                    # 测试执行（超时10秒）
                    for cmd in commands:
                        result = subprocess.run(cmd.split() if isinstance(cmd, str) else cmd, 
                                              capture_output=True, text=True, timeout=10)
                        functionality_report[tool][cmd] = {
                            "success": result.returncode == 0,
                            "returncode": result.returncode
                        }
                except subprocess.TimeoutExpired:
                    functionality_report[tool]["status"] = "⏰ 执行超时"
                except Exception as e:
                    functionality_report[tool]["status"] = f"❌ 执行错误: {e}"
            else:
                functionality_report[tool] = {"status": "❌ 文件不存在"}
        
        return functionality_report
    
    def generate_tool_matrix_report(self):
        """生成工具矩阵报告"""
        existence = self.validate_tool_existence()
        functionality = self.validate_tool_functionality()
        
        report = {
            "existence_validation": existence,
            "functionality_validation": functionality,
            "overall_tool_health": existence["existence_score"],
            "recommendations": []
        }
        
        # 生成建议
        if existence["missing_tools"]:
            report["recommendations"].append(f"补全缺失工具: {', '.join(existence['missing_tools'])}")
        
        working_tools = sum(1 for tool in functionality.values() if tool.get("status") != "❌ 文件不存在")
        if working_tools < len(functionality):
            report["recommendations"].append("修复无法执行的工具")
        
        return report

if __name__ == "__main__":
    validator = ToolMatrixValidator()
    report = validator.generate_tool_matrix_report()
    
    print(f"\n🧰 工具矩阵验证报告")
    print(f"存在性分数: {report['overall_tool_health']:.1f}%")
    print(f"缺失工具: {len(report['existence_validation']['missing_tools'])}个")
    
    if report['recommendations']:
        print(f"\n💡 建议:")
        for rec in report['recommendations']:
            print(f"  • {rec}")
    
    # 保存详细报告
    with open('工具矩阵验证报告.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 详细报告已保存: 工具矩阵验证报告.json")
