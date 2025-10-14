#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【小白调试学习系统】
将错误转化为学习机会
功能：错误记录、解决方案、经验积累、课程生成
"""

import json
import os
from datetime import datetime

class 调试学习系统:
    def __init__(self):
        self.错误案例库文件 = "记忆库/错误案例库.json"
        self.学习经验文件 = "记忆库/学习经验.json"
        os.makedirs("记忆库", exist_ok=True)
    
    def 记录错误案例(self, 错误类型, 错误信息, 错误代码, 解决方案, 学习要点):
        """记录错误案例"""
        错误案例 = {
            "时间戳": datetime.now().isoformat(),
            "错误类型": 错误类型,
            "错误信息": 错误信息,
            "错误代码": 错误代码,
            "解决方案": 解决方案,
            "学习要点": 学习要点,
            "经验价值": "免费课程素材",
            "难度等级": "小白入门"
        }
        
        # 加载现有案例库
        案例库 = self.加载案例库()
        案例库["错误案例"].append(错误案例)
        
        # 保存更新后的案例库
        with open(self.错误案例库文件, 'w', encoding='utf-8') as f:
            json.dump(案例库, f, ensure_ascii=False, indent=2)
        
        print(f"📝 错误案例已记录: {错误类型}")
    
    def 加载案例库(self):
        """加载错误案例库"""
        if os.path.exists(self.错误案例库文件):
            with open(self.错误案例库文件, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            return {"错误案例": [], "统计信息": {"总案例数": 0, "最近更新": ""}}
    
    def 记录学习经验(self, 经验主题, 详细内容, 适用场景, 价值评估):
        """记录学习经验"""
        学习经验 = {
            "时间戳": datetime.now().isoformat(),
            "经验主题": 经验主题,
            "详细内容": 详细内容,
            "适用场景": 适用场景,
            "价值评估": value评估,
            "课程潜力": "高"
        }
        
        # 加载现有经验库
        经验库 = self.加载经验库()
        经验库["学习经验"].append(学习经验)
        
        # 保存更新后的经验库
        with open(self.学习经验文件, 'w', encoding='utf-8') as f:
            json.dump(经验库, f, ensure_ascii=False, indent=2)
        
        print(f"🎓 学习经验已记录: {经验主题}")
    
    def 加载经验库(self):
        """加载学习经验库"""
        if os.path.exists(self.学习经验文件):
            with open(self.学习经验文件, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            return {"学习经验": [], "统计信息": {"总经验数": 0, "最近更新": ""}}
    
    def 显示案例库摘要(self):
        """显示错误案例库摘要"""
        案例库 = self.加载案例库()
        经验库 = self.加载经验库()
        
        print("\n" + "📚" * 20)
        print("📚 【小白调试学习系统】")
        print("📚" * 20)
        print(f"❌ 错误案例: {len(案例库['错误案例'])} 个")
        print(f"🎓 学习经验: {len(经验库['学习经验'])} 条")
        print(f"💰 课程价值: ￥{len(案例库['错误案例']) * 89 + len(经验库['学习经验']) * 79}")
        print("📚" * 20)
        
        # 显示最近的错误案例
        if 案例库["错误案例"]:
            print("\n🔍 【最近错误案例】")
            最近案例 = 案例库["错误案例"][-3:]  # 显示最后3个
            for 案例 in 最近案例:
                print(f"   🐛 {案例['错误类型']}: {案例['错误信息'][:30]}...")

# 运行调试学习系统
学习系统 = 调试学习系统()

# 记录我们刚才遇到的错误
学习系统.记录错误案例(
    错误类型="NameError（变量未定义）",
    错误信息="name '设备_info' is not defined",
    错误代码="用户哈希 = hashlib.md5(f\"{设备_info}\".encode()).hexdigest()[:8]",
    解决方案="将'设备_info'改为正确的变量名'设备信息'",
    学习要点=["变量必须先定义后使用", "变量名拼写必须一致", "Python大小写敏感"]
)

# 记录学习经验
学习系统.记录学习经验(
    经验主题="GitHub Token认证失败解决方案",
    详细内容="GitHub不再支持密码认证，必须使用Personal Access Token，需要正确配置repo权限",
    适用场景="所有GitHub命令行操作",
    价值评估="高价值，解决常见痛点"
)

# 记录调试经验
学习系统.记录学习经验(
    经验主题="Python错误调试方法",
    详细内容="阅读错误信息→定位错误行→分析错误原因→实施修复→验证结果",
    适用场景="所有Python编程场景",
    价值评估="核心技能，高频使用"
)

# 显示系统状态
学习系统.显示案例库摘要()

print("\n🎉 【调试学习系统就绪】")
print("💎 每个错误都是我们课程的宝贵财富！")
