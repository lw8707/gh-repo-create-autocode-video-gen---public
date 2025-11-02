#!/usr/bin/env python3
import os
print("🔍 传承防混乱检查")
print("当前轮次:", open('.current_generation').read().strip() if os.path.exists('.current_generation') else "未设置")
print("轮次目录:", [d for d in os.listdir('.') if d.startswith('gen') and os.path.isdir(d)])
print("✅ 检查完成")
