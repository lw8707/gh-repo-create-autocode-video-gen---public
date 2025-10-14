#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【记忆保障系统】
确保跨对话记忆的可靠性和可恢复性
功能：自动备份、冲突解决、灾难恢复
"""

import os
import json
from datetime import datetime

class 记忆保障系统:
    def __init__(self):
        self.记忆目录 = "记忆库"
        self.备份目录 = f"{self.记忆目录}/自动备份"
        os.makedirs(self.备份目录, exist_ok=True)
    
    def 创建记忆备份(self):
        """创建记忆备份"""
        print("💾 【创建记忆备份】")
        
        备份文件 = []
        
        # 备份所有记忆文件
        for 文件 in os.listdir(self.记忆目录):
            if 文件.endswith('.json'):
                源文件路径 = os.path.join(self.记忆目录, 文件)
                备份文件路径 = f"{self.备份目录}/{文件}.{datetime.now().strftime('%Y%m%d_%H%M%S')}.backup"
                
                try:
                    with open(源文件路径, 'r', encoding='utf-8') as 源文件:
                        数据 = json.load(源文件)
                    
                    with open(备份文件路径, 'w', encoding='utf-8') as 备份文件:
                        json.dump(数据, 备份文件, ensure_ascii=False, indent=2)
                    
                    备份文件.append(备份文件路径)
                    print(f"   ✅ 备份: {文件} -> {os.path.basename(备份文件路径)}")
                    
                except Exception as e:
                    print(f"   ❌ 备份失败 {文件}: {e}")
        
        print(f"📊 总计备份: {len(备份文件)} 个文件")
        return 备份文件
    
    def 检查记忆健康度(self):
        """检查记忆系统健康度"""
        print("❤️ 【记忆系统健康检查】")
        
        检查结果 = {
            "记忆文件": 0,
            "备份文件": 0,
            "最近更新": None,
            "问题": []
        }
        
        # 检查记忆文件
        for 文件 in os.listdir(self.记忆目录):
            if 文件.endswith('.json') and 文件 != "验证测试记录.json":
                检查结果["记忆文件"] += 1
                
                # 检查文件可读性
                文件路径 = os.path.join(self.记忆目录, 文件)
                try:
                    with open(文件路径, 'r', encoding='utf-8') as f:
                        数据 = json.load(f)
                    
                    最后时间 = 数据.get("最后更新时间", 数据.get("创建时间"))
                    if 最后时间:
                        if not 检查结果["最近更新"] or 最后时间 > 检查结果["最近更新"]:
                            检查结果["最近更新"] = 最后时间
                            
                except Exception as e:
                    检查结果["问题"].append(f"文件 {文件} 损坏: {e}")
        
        # 检查备份文件
        if os.path.exists(self.备份目录):
            检查结果["备份文件"] = len([f for f in os.listdir(self.备份目录) if f.endswith('.backup')])
        
        # 输出检查结果
        print(f"   📄 记忆文件: {检查结果['记忆文件']} 个")
        print(f"   💾 备份文件: {检查结果['备份文件']} 个")
        print(f"   🕒 最近更新: {检查结果['最近更新']}")
        
        if 检查结果["问题"]:
            print("   ❌ 发现问题:")
            for 问题 in 检查结果["问题"]:
                print(f"      - {问题}")
        else:
            print("   ✅ 记忆系统健康")
        
        return len(检查结果["问题"]) == 0
    
    def 灾难恢复(self):
        """记忆系统灾难恢复"""
        print("🚑 【记忆系统灾难恢复】")
        
        if not os.path.exists(self.备份目录):
            print("   ❌ 没有备份文件可用于恢复")
            return False
        
        # 查找最新的备份文件
        备份文件 = [f for f in os.listdir(self.备份目录) if f.endswith('.backup')]
        if not 备份文件:
            print("   ❌ 没有找到备份文件")
            return False
        
        备份文件.sort(reverse=True)
        最新备份 = 备份文件[0]
        
        print(f"   🔄 从备份恢复: {最新备份}")
        
        # 提取原始文件名（去掉时间戳和.backup）
        原始文件名 = ".".join(最新备份.split(".")[:-2]) + ".json"
        目标路径 = os.path.join(self.记忆目录, 原始文件名)
        备份路径 = os.path.join(self.备份目录, 最新备份)
        
        try:
            with open(备份路径, 'r', encoding='utf-8') as 备份文件:
                备份数据 = json.load(备份文件)
            
            with open(目标路径, 'w', encoding='utf-8') as 目标文件:
                json.dump(备份数据, 目标文件, ensure_ascii=False, indent=2)
            
            print(f"   ✅ 恢复成功: {原始文件名}")
            return True
            
        except Exception as e:
            print(f"   ❌ 恢复失败: {e}")
            return False

# 运行记忆保障系统
保障系统 = 记忆保障系统()

print("🛡️ 【启动记忆保障系统】")
健康 = 保障系统.检查记忆健康度()

if 健康:
    print("✅ 记忆系统健康，创建备份...")
    保障系统.创建记忆备份()
else:
    print("🔧 记忆系统有问题，尝试恢复...")
    保障系统.灾难恢复()

print("\n🎯 【记忆保障完成】")
print("💪 现在我们的对话记忆有了多重保障！")
