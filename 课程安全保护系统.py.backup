#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【课程安全保护系统】
确保所有课程内容和知识产权得到妥善保护
"""

import os
import json
import hashlib
from datetime import datetime

class 课程保护系统:
    def __init__(self):
        self.课程目录 = "课程体系"
        self.知识产权文件 = "知识产权声明.md"
        self.备份目录 = "课程备份"
        
    def 创建课程结构(self):
        """创建完整的课程目录结构"""
        课程结构 = {
            "基础课程": [
                "01-Termux环境搭建",
                "02-GitHub认证突破", 
                "03-Python基础入门",
                "04-自动化脚本开发"
            ],
            "进阶课程": [
                "05-智能体开发基础",
                "06-问题解决方法论",
                "07-项目管理实践",
                "08-产品思维培养"
            ],
            "高级课程": [
                "09-教育科技产品设计",
                "10-商业模式构建",
                "11-全球化部署策略",
                "12-社区运营管理"
            ]
        }
        
        # 创建目录结构
        if not os.path.exists(self.课程目录):
            os.makedirs(self.课程目录)
            
        for 分类, 课程列表 in 课程结构.items():
            分类路径 = os.path.join(self.课程目录, 分类)
            if not os.path.exists(分类路径):
                os.makedirs(分类路径)
                
            for 课程 in 课程列表:
                课程路径 = os.path.join(分类路径, 课程)
                if not os.path.exists(课程路径):
                    os.makedirs(课程路径)
                    
                # 创建课程说明文件
                说明文件 = os.path.join(课程路径, "课程说明.md")
                if not os.path.exists(说明文件):
                    with open(说明文件, 'w', encoding='utf-8') as f:
                        f.write(f"# {课程}\n\n")
                        f.write("## 课程概述\n\n")
                        f.write("## 学习目标\n\n")
                        f.write("## 课程内容\n\n")
                        f.write("## 实践项目\n\n")
                        f.write(f"创建时间: {datetime.now()}\n")
        
        print("✅ 课程目录结构创建完成")
        return 课程结构
    
    def 生成知识产权声明(self):
        """生成完整的知识产权保护声明"""
        声明内容 = f"""
# 📜 知识产权保护声明

## 项目信息
- **项目名称**: 手机零基础编程革命课程体系
- **创建者**: lw8707
- **创建时间**: {datetime.now()}
- **项目仓库**: https://github.com/lw8707/gh-repo-create-autocode-video-gen---public

## 版权声明
本课程体系包含以下受保护内容：

### 1. 核心教学方法
- 零基础手机端编程学习路径
- 问题驱动的渐进式学习法  
- 从小白到开发者的完整成长记录

### 2. 技术解决方案
- Termux环境配置方案
- GitHub认证突破方法
- 自动化脚本开发流程

### 3. 课程内容体系
- 模块化课程结构
- 实践项目设计
- 学习评估体系

## 使用授权
### 允许使用
- 个人学习使用
- 教育机构内部培训
- 非商业性分享

### 禁止行为  
- 商业性复制和销售
- 未经授权的二次分发
- 去除版权信息的传播

## 联系方式
如有合作意向，请通过GitHub Issues联系。

---
*本声明自动生成，具有法律效力*
"""
        
        with open(self.知识产权文件, 'w', encoding='utf-8') as f:
            f.write(声明内容)
            
        print("✅ 知识产权声明已生成")
    
    def 创建自动备份系统(self):
        """创建课程自动备份系统"""
        if not os.path.exists(self.备份目录):
            os.makedirs(self.备份目录)
            
        备份脚本 = f"""#!/bin/bash
# 课程自动备份脚本
echo "📦 开始课程备份..."
备份时间=$(date +%Y%m%d_%H%M%S)
备份文件="课程备份_$备份时间.tar.gz"

# 备份所有课程文件
tar -czf "{self.备份目录}/$备份文件" {self.课程目录} {self.知识产权文件}

# 计算文件哈希值
md5sum "{self.备份目录}/$备份文件" > "{self.备份目录}/$备份文件.md5"

echo "✅ 备份完成: $备份文件"
echo "🔐 备份位置: {self.备份目录}/"
echo "📊 备份大小: $(du -h "{self.备份目录}/$备份文件" | cut -f1)"
"""

        with open("自动备份.sh", 'w', encoding='utf-8') as f:
            f.write(备份脚本)
            
        os.chmod("自动备份.sh", 0o755)
        print("✅ 自动备份系统已创建")
    
    def 运行完整保护流程(self):
        """运行完整的课程保护流程"""
        print("🛡️ 启动课程安全保护系统...")
        self.创建课程结构()
        self.生成知识产权声明() 
        self.创建自动备份系统()
        
        # 立即执行一次备份
        os.system("./自动备份.sh")
        
        print("🎉 课程安全保护系统部署完成!")

# 运行保护系统
保护系统 = 课程保护系统()
保护系统.运行完整保护流程()
