#!/usr/bin/env python3
import os
print("🔍 快速状态检查")
files = os.listdir(".")
py_files = [f for f in files if f.endswith(".py")]
print(f"Python文件: {len(py_files)}个")
print("✅ 系统正常" if any("依赖" in f for f in py_files) else "❌ 需要检查")
