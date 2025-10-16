"""
认知偏差检测系统
检测和防止虚假报告
"""

class CognitiveBiasDetector:
    def __init__(self):
        self.biases_detected = []
    
    def detect_biases(self, reported_state, actual_state):
        """检测认知偏差"""
        biases = []
        
        # 过度乐观偏差
        if reported_state == "已修复" and actual_state == "未修复":
            biases.append("过度乐观偏差 - 报告修复但实际未修复")
        
        # 确认偏差  
        if "✅" in reported_state and "❌" in actual_state:
            biases.append("确认偏差 - 只看到支持预期的证据")
        
        # 后见之明偏差
        if "本来就应该" in reported_state and "实际上不是" in actual_state:
            biases.append("后见之明偏差 - 事后认为理所当然")
        
        self.biases_detected.extend(biases)
        return biases
    
    def apply_antidotes(self):
        """应用偏差解药"""
        antidotes = []
        
        if any("过度乐观" in bias for bias in self.biases_detected):
            antidotes.append("🔍 实施真实诊断 - 不假设修复")
        
        if any("确认偏差" in bias for bias in self.biases_detected):
            antidotes.append("📊 建立真实监控 - 客观测量")
            
        if any("后见之明" in bias for bias in self.biases_detected):
            antidotes.append("⏱️ 记录时间线 - 避免事后合理化")
        
        return antidotes

# 检测当前情况的偏差
detector = CognitiveBiasDetector()
biases = detector.detect_biases(
    "红色代码已修复", 
    "红色代码仍然存在"
)
print("🤔 检测到的认知偏差:", biases)
print("💊 偏差解药:", detector.apply_antidotes())
