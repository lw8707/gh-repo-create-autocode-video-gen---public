#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【跨对话记忆系统 - 修复版】
修复：设备_info变量未定义的错误
记录：小白编程常见错误和调试过程
"""

import os
import json
import requests
from datetime import datetime
import hashlib

class 跨对话记忆系统:
    def __init__(self):
        self.用户标识 = self.获取用户标识()
        self.记忆库目录 = "记忆库/跨对话记忆"
        self.本地记忆文件 = f"{self.记忆库目录}/{self.用户标识}.json"
        self.云端记忆URL = "https://raw.githubusercontent.com/lw8707/gh-repo-create-autocode-video-gen---public/main/记忆库/跨对话记忆/"
        
        # 创建目录
        os.makedirs(self.记忆库目录, exist_ok=True)
        
        # 初始化记忆
        self.记忆数据 = self.加载记忆()
        
    def 获取用户标识(self):
        """生成用户唯一标识 - 修复版"""
        print("🔧 【修复说明】")
        print("   原错误: 使用了未定义的变量 '设备_info'")
        print("   修复: 使用正确的变量名 '设备信息'")
        print("   学习点: Python变量名必须正确定义后才能使用")
        
        # 修复：使用正确的变量名
        设备信息 = os.uname()
        用户哈希 = hashlib.md5(f"{设备信息}".encode()).hexdigest()[:8]
        return f"用户_{用户哈希}"
    
    def 加载记忆(self):
        """加载跨对话记忆"""
        print("🔄 【加载跨对话记忆】")
        
        # 尝试从本地加载
        本地记忆 = self.从本地加载记忆()
        
        # 尝试从GitHub加载（如果本地没有）
        if not 本地记忆 or len(本地记忆.get("对话历史", [])) == 0:
            print("🌐 从GitHub加载记忆...")
            云端记忆 = self.从GitHub加载记忆()
            if 云端记忆:
                本地记忆 = 云端记忆
                self.保存记忆到本地(本地记忆)
        
        # 如果都没有，创建新记忆
        if not 本地记忆:
            本地记忆 = self.创建新记忆()
        
        print(f"💾 加载完成: {len(本地记忆.get('对话历史', []))} 次对话记录")
        return 本地记忆
    
    def 从本地加载记忆(self):
        """从本地文件加载记忆"""
        try:
            if os.path.exists(self.本地记忆文件):
                with open(self.本地记忆文件, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"❌ 本地记忆加载失败: {e}")
        return None
    
    def 从GitHub加载记忆(self):
        """从GitHub仓库加载记忆"""
        try:
            记忆URL = f"{self.云端记忆URL}{self.用户标识}.json"
            response = requests.get(记忆URL, timeout=10)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"❌ GitHub记忆加载失败: {e}")
        return None
    
    def 创建新记忆(self):
        """创建新的记忆结构"""
        return {
            "用户标识": self.用户标识,
            "创建时间": datetime.now().isoformat(),
            "最后更新时间": datetime.now().isoformat(),
            "对话历史": [],
            "项目进度": {},
            "学习内容": [],
            "问题解决方案": []
        }
    
    def 添加对话记录(self, 用户输入, AI回复, 对话上下文=""):
        """添加对话记录到记忆"""
        对话记录 = {
            "时间戳": datetime.now().isoformat(),
            "用户输入": 用户输入,
            "AI回复": AI回复[:500],  # 限制长度
            "上下文": 对话上下文,
            "会话ID": f"会话_{len(self.记忆数据['对话历史']) + 1}"
        }
        
        self.记忆数据["对话历史"].append(对话记录)
        self.记忆数据["最后更新时间"] = datetime.now().isoformat()
        
        # 立即保存到本地
        self.保存记忆到本地(self.记忆数据)
        
        print(f"📝 对话记录已保存 (#{len(self.记忆数据['对话历史'])})")
    
    def 获取最近对话(self, 数量=5):
        """获取最近的对话记录"""
        对话历史 = self.记忆数据.get("对话历史", [])
        return 对话历史[-数量:] if 对话历史 else []
    
    def 获取项目进度(self):
        """获取项目进度"""
        return self.记忆数据.get("项目进度", {})
    
    def 更新项目进度(self, 进度更新):
        """更新项目进度"""
        self.记忆数据["项目进度"].update(进度更新)
        self.记忆数据["最后更新时间"] = datetime.now().isoformat()
        self.保存记忆到本地(self.记忆数据)
        print("📈 项目进度已更新")
    
    def 保存记忆到本地(self, 记忆数据):
        """保存记忆到本地文件"""
        try:
            with open(self.本地记忆文件, 'w', encoding='utf-8') as f:
                json.dump(记忆数据, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"❌ 本地记忆保存失败: {e}")
    
    def 显示记忆摘要(self):
        """显示记忆摘要"""
        记忆 = self.记忆数据
        print("\n" + "🧠" * 20)
        print("🧠 【跨对话记忆系统】")
        print("🧠" * 20)
        print(f"👤 用户: {记忆['用户标识']}")
        print(f"📅 创建: {记忆['创建时间']}")
        print(f"🔄 更新: {记忆['最后更新时间']}")
        print(f"💬 对话: {len(记忆['对话历史'])} 次")
        print(f"🎯 进度: {len(记忆.get('项目进度', {}))} 项")
        print(f"📚 学习: {len(记忆.get('学习内容', []))} 条")
        print("🧠" * 20)
        
        # 显示最近对话
        最近对话 = self.获取最近对话(3)
        if 最近对话:
            print("\n📖 【最近对话】")
            for 对话 in 最近对话:
                print(f"   {对话['时间戳']}: {对话['用户输入'][:50]}...")

# 测试修复后的跨对话记忆系统
print("🚀 【启动修复版跨对话记忆系统】")
print("💡 这次我们修复了 '设备_info' 变量未定义的错误")

记忆系统 = 跨对话记忆系统()

# 记录当前对话
记忆系统.添加对话记录(
    "修复了设备_info变量未定义的错误", 
    "将错误的'设备_info'改为正确的'设备信息'变量，这是Python编程常见错误",
    "用户遇到NameError，变量未定义错误，这是宝贵的学习经验"
)

# 更新项目进度
记忆系统.更新项目进度({
    "当前阶段": "修复跨对话记忆系统错误",
    "完成步骤": ["环境配置", "基础工具安装", "GitHub集成准备", "调试变量错误"],
    "下一步": "完成GitHub认证和记忆同步",
    "宝贵经验": "变量必须先定义后使用，这是编程基础"
})

# 显示记忆状态
记忆系统.显示记忆摘要()

print("\n🎉 【修复成功！跨对话记忆系统现在正常工作了！】")
print("💪 这个错误和修复过程将成为我们课程的宝贵案例")
