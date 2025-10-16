#!/usr/bin/env python3
"""
第14轮传承健康检查系统
全面检查历代传承的完整性和健康状况
"""
import os
import json
import subprocess
from datetime import datetime

class HeritageHealthChecker:
    def __init__(self):
        self.heritage_files = [
            # 核心传承文件
            '传承核心.md', '轮次记录.json', '.generation_pointer',
            # 工具矩阵文件
            '智能自检修复系统.py', '多重备份系统.py', '分块管理器_v2.py',
            # 验证系统文件
            '验证传承.sh', '简化修复.sh'
        ]
        
        self.generation_dirs = ['gen12', 'gen13', 'gen13.5', 'gen14']
    
    def check_heritage_integrity(self):
        """检查传承体系完整性"""
        print("🔍 检查传承体系完整性...")
        
        report = {
            "check_time": datetime.now().isoformat(),
            "current_generation": "未知",
            "file_integrity": {},
            "generation_integrity": {},
            "git_integrity": {},
            "issues_found": [],
            "recommendations": []
        }
        
        # 检查核心文件
        for file in self.heritage_files:
            exists = os.path.exists(file)
            report["file_integrity"][file] = {
                "exists": exists,
                "status": "✅" if exists else "❌"
            }
            if not exists:
                report["issues_found"].append(f"缺失核心文件: {file}")
        
        # 检查轮次目录
        for gen_dir in self.generation_dirs:
            exists = os.path.exists(gen_dir)
            report["generation_integrity"][gen_dir] = {
                "exists": exists,
                "status": "✅" if exists else "❌"
            }
        
        # 检查Git状态
        try:
            # 本地仓库状态
            result = subprocess.run(['git', 'status', '--porcelain'], 
                                  capture_output=True, text=True)
            changed_files = len(result.stdout.strip().split('\n')) if result.stdout else 0
            
            # 远程仓库状态
            remote_result = subprocess.run(['git', 'remote', '-v'], 
                                         capture_output=True, text=True)
            has_remote = 'origin' in remote_result.stdout
            
            report["git_integrity"] = {
                "local_changes": changed_files,
                "has_remote": has_remote,
                "status": "✅" if changed_files == 0 and has_remote else "⚠️"
            }
            
        except Exception as e:
            report["git_integrity"] = {"error": str(e), "status": "❌"}
        
        # 检查当前轮次
        try:
            with open('.generation_pointer', 'r') as f:
                pointer_content = f.read()
                report["current_generation"] = pointer_content
        except:
            report["issues_found"].append("无法读取当前轮次指针")
        
        return report
    
    def check_tool_matrix(self):
        """检查工具矩阵完整性"""
        print("🧰 检查工具矩阵完整性...")
        
        tools = {
            "版本管理": ["简化修复.sh", "验证传承.sh"],
            "备份系统": ["多重备份系统.py"],
            "自检系统": ["智能自检修复系统.py"], 
            "分块管理": ["分块管理器_v2.py"],
            "安全工具": ["安全健康检查系统.py", "依赖健康检查系统.py"]
        }
        
        tool_report = {}
        missing_tools = []
        
        for category, tool_list in tools.items():
            tool_report[category] = {}
            for tool in tool_list:
                exists = os.path.exists(tool)
                tool_report[category][tool] = {
                    "exists": exists,
                    "status": "✅" if exists else "❌"
                }
                if not exists:
                    missing_tools.append(tool)
        
        return {
            "tool_matrix": tool_report,
            "missing_tools": missing_tools,
            "health_score": (1 - len(missing_tools) / sum(len(v) for v in tools.values())) * 100
        }
    
    def generate_comprehensive_report(self):
        """生成全面健康报告"""
        heritage_report = self.check_heritage_integrity()
        tool_report = self.check_tool_matrix()
        
        comprehensive_report = {
            "heritage_health": heritage_report,
            "tool_health": tool_report,
            "overall_health_score": 0,
            "critical_issues": [],
            "immediate_actions": []
        }
        
        # 计算总体健康分数
        file_health = sum(1 for f in heritage_report["file_integrity"].values() if f["exists"]) / len(heritage_report["file_integrity"]) * 100
        tool_health = tool_report["health_score"]
        git_health = 100 if heritage_report["git_integrity"].get("status") == "✅" else 50
        
        comprehensive_report["overall_health_score"] = (file_health + tool_health + git_health) / 3
        
        # 识别关键问题
        if heritage_report["issues_found"]:
            comprehensive_report["critical_issues"].extend(heritage_report["issues_found"])
        
        if tool_report["missing_tools"]:
            comprehensive_report["critical_issues"].append(f"缺失工具: {', '.join(tool_report['missing_tools'])}")
        
        # 生成立即行动建议
        if comprehensive_report["overall_health_score"] < 80:
            comprehensive_report["immediate_actions"].append("立即修复传承体系完整性")
        if tool_report["health_score"] < 100:
            comprehensive_report["immediate_actions"].append("补全缺失的工具组件")
        if heritage_report["git_integrity"].get("local_changes", 0) > 0:
            comprehensive_report["immediate_actions"].append("提交未保存的更改到Git仓库")
        
        return comprehensive_report

# 执行检查
if __name__ == "__main__":
    checker = HeritageHealthChecker()
    report = checker.generate_comprehensive_report()
    
    print(f"\n📊 第14轮传承健康检查报告")
    print(f"总体健康分数: {report['overall_health_score']:.1f}/100")
    
    if report['critical_issues']:
        print(f"\n🔴 关键问题 ({len(report['critical_issues'])}个):")
        for issue in report['critical_issues']:
            print(f"  • {issue}")
    
    if report['immediate_actions']:
        print(f"\n🎯 立即执行 ({len(report['immediate_actions'])}项):")
        for action in report['immediate_actions']:
            print(f"  • {action}")
    
    # 保存详细报告
    with open('第14轮传承健康报告.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 详细报告已保存: 第14轮传承健康报告.json")
