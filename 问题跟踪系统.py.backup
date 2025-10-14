#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【问题跟踪系统】
确保每个问题都按优先级解决
避免跳跃式开发，保证系统稳定性
"""

import json
import os
from datetime import datetime

class 问题跟踪系统:
    def __init__(self):
        self.问题文件 = "记忆库/问题跟踪.json"
        os.makedirs("记忆库", exist_ok=True)
    
    def 登记问题(self, 问题描述, 优先级, 当前状态, 相关文件=None):
        """登记新问题"""
        问题列表 = self.读取问题列表()
        
        新问题 = {
            "id": len(问题列表) + 1,
            "描述": 问题描述,
            "优先级": 优先级,
            "状态": 当前状态,
            "创建时间": datetime.now().isoformat(),
            "更新时间": datetime.now().isoformat(),
            "相关文件": 相关文件 or []
        }
        
        问题列表.append(新问题)
        self.保存问题列表(问题列表)
        
        print(f"📝 问题已登记: #{新问题['id']} {问题描述}")
        return 新问题['id']
    
    def 更新问题状态(self, 问题id, 新状态, 进展说明=""):
        """更新问题状态"""
        问题列表 = self.读取问题列表()
        
        for 问题 in 问题列表:
            if 问题['id'] == 问题id:
                问题['状态'] = 新状态
                问题['更新时间'] = datetime.now().isoformat()
                if 进展说明:
                    问题['进展说明'] = 进展说明
                break
        
        self.保存问题列表(问题列表)
        print(f"🔄 问题 #{问题id} 状态更新为: {新状态}")
    
    def 读取问题列表(self):
        """读取问题列表"""
        try:
            if os.path.exists(self.问题文件):
                with open(self.问题文件, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except:
            pass
        
        return []
    
    def 保存问题列表(self, 问题列表):
        """保存问题列表"""
        with open(self.问题文件, 'w', encoding='utf-8') as f:
            json.dump(问题列表, f, ensure_ascii=False, indent=2)
    
    def 显示问题看板(self):
        """显示问题看板"""
        问题列表 = self.读取问题列表()
        
        print("\n" + "📋" * 20)
        print("📋 【问题跟踪看板】")
        print("📋" * 20)
        
        # 按优先级分组
        优先级分组 = {
            "🚨 紧急": [],
            "🔧 高": [], 
            "📚 中": [],
            "💰 低": []
        }
        
        for 问题 in 问题列表:
            优先级分组[问题['优先级']].append(问题)
        
        for 优先级, 问题组 in 优先级分组.items():
            if 问题组:
                print(f"\n{优先级}优先级:")
                for 问题 in 问题组:
                    print(f"   #{问题['id']} {问题['描述']} - {问题['状态']}")
    
    def 获取下一个待解决问题(self):
        """获取下一个需要解决的问题"""
        问题列表 = self.读取问题列表()
        
        优先级顺序 = ["🚨 紧急", "🔧 高", "📚 中", "💰 低"]
        
        for 优先级 in 优先级顺序:
            for 问题 in 问题列表:
                if 问题['优先级'] == 优先级 and 问题['状态'] == "待解决":
                    return 问题
        
        return None

# 初始化问题跟踪系统
跟踪系统 = 问题跟踪系统()

# 登记当前的核心问题
print("📝 【登记核心问题】")

跨对话问题id = 跟踪系统.登记问题(
    "跨对话记忆系统不稳定，新对话无法读取历史记忆",
    "🚨 紧急",
    "待解决",
    ["跨对话记忆系统.py", "极简跨对话记忆.py"]
)

GitHub问题id = 跟踪系统.登记问题(
    "GitHub认证失败，无法同步代码到云端", 
    "🔧 高",
    "待解决",
    ["GitHub认证自动化.py", "GitHub_Token问题解决.py"]
)

课程问题id = 跟踪系统.登记问题(
    "课程内容制作和商业化实施",
    "📚 中", 
    "待处理",
    ["教育产业化规划.py", "课程内容生成器.py"]
)

# 显示问题看板
跟踪系统.显示问题看板()

# 获取下一个要解决的问题
下一个问题 = 跟踪系统.获取下一个待解决问题()
if 下一个问题:
    print(f"\n🎯 【下一步行动】")
    print(f"   立即解决: #{下一个问题['id']} {下一个问题['描述']}")
    print(f"   优先级: {下一个问题['优先级']}")
else:
    print("\n✅ 所有问题都已解决！")

print("\n📋 问题跟踪系统已就绪")
print("💪 现在我们可以有条不紊地解决问题了！")
