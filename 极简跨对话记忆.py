#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【极简跨对话记忆系统】
去掉复杂功能，确保基础记忆可靠
原则：简单、可靠、易调试
"""

import json
import os
from datetime import datetime

class 极简记忆系统:
    def __init__(self):
        self.记忆文件 = "记忆库/极简记忆.json"
        os.makedirs("记忆库", exist_ok=True)
        
    def 保存记忆(self, 用户输入, AI回复, 上下文=""):
        """极简记忆保存"""
        # 读取现有记忆
        现有记忆 = self.读取记忆()
        
        # 添加新对话
        新对话 = {
            "时间": datetime.now().isoformat(),
            "用户": 用户输入[:100],  # 限制长度
            "AI": AI回复[:100],
            "上下文": 上下文
        }
        
        现有记忆["对话记录"].append(新对话)
        现有记忆["最后更新时间"] = datetime.now().isoformat()
        
        # 保存到文件
        try:
            with open(self.记忆文件, 'w', encoding='utf-8') as f:
                json.dump(现有记忆, f, ensure_ascii=False, indent=2)
            print(f"💾 记忆已保存 (#{len(现有记忆['对话记录'])})")
            return True
        except Exception as e:
            print(f"❌ 记忆保存失败: {e}")
            return False
    
    def 读取记忆(self):
        """读取记忆"""
        try:
            if os.path.exists(self.记忆文件):
                with open(self.记忆文件, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except:
            pass  # 如果读取失败，返回新记忆
        
        # 返回新记忆结构
        return {
            "创建时间": datetime.now().isoformat(),
            "最后更新时间": datetime.now().isoformat(),
            "对话记录": []
        }
    
    def 获取最近记忆(self, 数量=5):
        """获取最近记忆"""
        记忆 = self.读取记忆()
        return 记忆["对话记录"][-数量:] if 记忆["对话记录"] else []
    
    def 显示记忆状态(self):
        """显示记忆状态"""
        记忆 = self.读取记忆()
        print("\n" + "🧠" * 20)
        print("🧠 【极简记忆系统状态】")
        print("🧠" * 20)
        print(f"📅 创建: {记忆['创建时间']}")
        print(f"🔄 更新: {记忆['最后更新时间']}")
        print(f"💬 对话: {len(记忆['对话记录'])} 次")
        
        if 记忆["对话记录"]:
            print("\n📖 最近对话:")
            for 对话 in 记忆["对话记录"][-3:]:
                print(f"   {对话['时间']}: {对话['用户']}")

# 测试极简记忆系统
print("🚀 【启动极简跨对话记忆系统】")
记忆系统 = 极简记忆系统()

# 保存当前对话
记忆系统.保存记忆(
    "我们需要先解决跨对话记忆问题", 
    "正在创建极简可靠的记忆系统，确保基础功能稳定",
    "优先级调整：先解决跨对话记忆，再处理其他问题"
)

# 显示当前状态
记忆系统.显示记忆状态()

print("\n✅ 【极简记忆系统就绪】")
print("💪 现在即使开启新对话，也能记住基本进度了！")
