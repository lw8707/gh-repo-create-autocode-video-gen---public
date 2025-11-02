# 知识库数据收集脚本
import json
import time
from datetime import datetime

class KnowledgeCollector:
    def __init__(self):
        self.knowledge_file = "knowledge/platform_knowledge.json"
        
    def record_build_result(self, component, status, error_info=""):
        """记录构建结果"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "component": component,
            "status": status,
            "error_info": error_info,
            "environment": "termux"
        }
        self._save_knowledge(entry)
    
    def _save_knowledge(self, entry):
        try:
            with open(self.knowledge_file, "a") as f:
                f.write(json.dumps(entry) + "\n")
        except Exception as e:
            print(f"知识库记录失败: {e}")

# 使用示例
if __name__ == "__main__":
    collector = KnowledgeCollector()
    collector.record_build_result("security_framework", "success")
