#!/usr/bin/env python3
"""
传承健康度检查 - 确保传承连续性
"""
import os
import json
from datetime import datetime

def check_critical_files():
    """检查核心文件完整性"""
    critical_files = [
        "enhanced_security_demo.py",
        "compatible_crypto.py", 
        "knowledge_base.md",
        ".generation_pointer"
    ]
    
    report = {"时间": datetime.now().isoformat(), "文件检查": {}}
    
    for file in critical_files:
        if os.path.exists(file):
            report["文件检查"][file] = {"状态": "✅ 存在", "大小": os.path.getsize(file)}
        else:
            report["文件检查"][file] = {"状态": "❌ 缺失", "大小": 0}
    
    return report

def check_generation_structure():
    """检查轮次目录结构"""
    report = {"轮次结构": {}}
    
    for gen in range(12, 17):
        gen_dir = f"gen{gen}"
        if os.path.exists(gen_dir):
            report["轮次结构"][gen_dir] = "✅ 存在"
            # 检查README
            readme = os.path.join(gen_dir, "README.md")
            if os.path.exists(readme):
                report["轮次结构"][f"{gen_dir}/README.md"] = "✅ 存在"
            else:
                report["轮次结构"][f"{gen_dir}/README.md"] = "❌ 缺失"
        else:
            report["轮次结构"][gen_dir] = "❌ 缺失"
    
    return report

if __name__ == "__main__":
    print("🔍 传承健康度检查报告")
    print("=" * 40)
    
    file_report = check_critical_files()
    structure_report = check_generation_structure()
    
    # 合并报告
    full_report = {**file_report, **structure_report}
    
    # 计算健康度
    total_checks = len(full_report["文件检查"]) + len(full_report["轮次结构"])
    passed_checks = sum(1 for check in full_report["文件检查"].values() if "✅" in check["状态"])
    passed_checks += sum(1 for check in full_report["轮次结构"].values() if "✅" in check)
    
    health_score = (passed_checks / total_checks) * 100 if total_checks > 0 else 0
    
    print(f"📊 传承健康度: {health_score:.1f}%")
    
    if health_score >= 80:
        print("🎉 传承状态: 健康")
    elif health_score >= 60:
        print("👍 传承状态: 一般") 
    else:
        print("🚨 传承状态: 需要紧急修复")
    
    # 保存详细报告
    with open("legacy_health_report.json", "w", encoding="utf-8") as f:
        json.dump(full_report, f, ensure_ascii=False, indent=2)
    
    print(f"📁 详细报告: legacy_health_report.json")
