#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【跨对话记忆测试】
验证：当前对话的记忆能否被新对话读取
这是整个系统的基础
"""

import json
import os

def 测试跨对话记忆():
    print("🧪 【跨对话记忆测试】")
    print("=" * 50)
    
    # 检查记忆文件是否存在
    记忆目录 = "记忆库/跨对话记忆"
    if not os.path.exists(记忆目录):
        print("❌ 记忆目录不存在")
        return False
    
    记忆文件列表 = [f for f in os.listdir(记忆目录) if f.endswith('.json')]
    if not 记忆文件列表:
        print("❌ 没有找到记忆文件")
        return False
    
    print(f"✅ 找到记忆文件: {len(记忆文件列表)} 个")
    
    # 读取第一个记忆文件
    记忆文件路径 = os.path.join(记忆目录, 记忆文件列表[0])
    try:
        with open(记忆文件路径, 'r', encoding='utf-8') as f:
            记忆数据 = json.load(f)
        
        print("📊 记忆内容摘要:")
        print(f"   用户标识: {记忆数据.get('用户标识', '未知')}")
        print(f"   对话历史: {len(记忆数据.get('对话历史', []))} 条")
        print(f"   项目进度: {记忆数据.get('项目进度', {}).get('当前阶段', '未知')}")
        print(f"   最后更新: {记忆数据.get('最后更新时间', '未知')}")
        
        # 显示最近对话
        最近对话 = 记忆数据.get('对话历史', [])[-3:] if 记忆数据.get('对话历史') else []
        if 最近对话:
            print("\n💬 最近对话:")
            for 对话 in 最近对话:
                print(f"   - {对话.get('用户输入', '')[:50]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ 读取记忆文件失败: {e}")
        return False

def 模拟新对话():
    """模拟开启新对话时的记忆恢复"""
    print("\n🔄 【模拟新对话记忆恢复】")
    print("=" * 50)
    
    # 这模拟的是用户开启新的聊天界面
    # 系统应该能自动加载之前的记忆
    
    记忆目录 = "记忆库/跨对话记忆"
    记忆文件列表 = [f for f in os.listdir(记忆目录) if f.endswith('.json')] if os.path.exists(记忆目录) else []
    
    if 记忆文件列表:
        print("✅ 新对话: 检测到历史记忆")
        记忆文件路径 = os.path.join(记忆目录, 记忆文件列表[0])
        
        try:
            with open(记忆文件路径, 'r', encoding='utf-8') as f:
                记忆数据 = json.load(f)
            
            最近进度 = 记忆数据.get('项目进度', {})
            print(f"🎯 恢复项目进度: {最近进度.get('当前阶段', '未知')}")
            print(f"✅ 已完成步骤: {len(最近进度.get('完成步骤', []))} 个")
            print(f"🚀 下一步计划: {最近进度.get('下一步', '未知')}")
            
            # 显示记忆连续性
            对话总数 = len(记忆数据.get('对话历史', []))
            print(f"💬 历史对话总数: {对话总数}")
            
            if 对话总数 > 0:
                print("📖 记忆连续性: ✅ 正常")
                return True
            else:
                print("📖 记忆连续性: ❌ 异常")
                return False
                
        except Exception as e:
            print(f"❌ 新对话记忆恢复失败: {e}")
            return False
    else:
        print("❌ 新对话: 未找到历史记忆")
        return False

# 运行测试
print("开始跨对话记忆系统验证...")
当前对话状态 = 测试跨对话记忆()
新对话状态 = 模拟新对话()

print("\n" + "📋" * 20)
print("📋 【跨对话记忆测试结果】")
print("📋" * 20)

if 当前对话状态 and 新对话状态:
    print("🎉 测试结果: ✅ 完全通过")
    print("💪 跨对话记忆系统工作正常！")
    print("🚀 可以继续解决GitHub同步问题")
else:
    print("⚠️ 测试结果: ❌ 需要修复")
    if not 当前对话状态:
        print("   问题: 当前对话记忆保存异常")
    if not 新对话状态:
        print("   问题: 新对话记忆恢复异常")
    print("🔧 需要先修复跨对话记忆问题")

print("📋" * 20)
