"""
真实状态监控 - 防止认知偏差
只报告真实状态，不虚假承诺
"""

class TruthMonitor:
    def __init__(self):
        self.truth_records = []
    
    def record_truth(self, category, expected, actual):
        """记录真实状态"""
        status = "✅" if expected == actual else "❌"
        record = {
            "category": category,
            "expected": expected,
            "actual": actual, 
            "truth": status,
            "timestamp": "2025-10-17 02:00:00"
        }
        self.truth_records.append(record)
        return record
    
    def generate_truth_report(self):
        """生成真实报告"""
        report = "# 真实状态报告 - 无认知偏差\n\n"
        report += "## 问题诊断\n"
        
        for record in self.truth_records:
            report += f"- {record['category']}: {record['actual']} {record['truth']}\n"
        
        # 计算真实度
        total = len(self.truth_records)
        truthful = len([r for r in self.truth_records if r['truth'] == "✅"])
        truth_percentage = (truthful / total) * 100 if total > 0 else 0
        
        report += f"\n## 真实度评估\n"
        report += f"- 总检查项: {total}\n"
        report += f"- 真实项: {truthful}\n" 
        report += f"- 真实度: {truth_percentage:.1f}%\n"
        
        return report

# 使用示例
monitor = TruthMonitor()
monitor.record_truth("Git状态", "干净", "有未提交更改")
monitor.record_truth("代码语法", "无错误", "有红色代码") 
monitor.record_truth("上传机制", "正常", "正常")

print(monitor.generate_truth_report())
