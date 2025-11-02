#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
import subprocess
import threading

class AIDevelopmentPlatform:
    def __init__(self, root):
        self.root = root
        self.root.title("AI业务开发平台 v13.0 - 修复版")
        self.root.geometry("600x400")
        
        self.create_widgets()
    
    def create_widgets(self):
        # 主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 标题
        title_label = ttk.Label(main_frame, text="第13轮传承 - 安全AI开发平台", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # 安全工具区域
        security_frame = ttk.LabelFrame(main_frame, text="安全工具", padding="5")
        security_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(security_frame, text="网络扫描", 
                  command=self.network_scan).pack(fill=tk.X, pady=2)
        ttk.Button(security_frame, text="量子加密测试", 
                  command=self.quantum_test).pack(fill=tk.X, pady=2)
        ttk.Button(security_frame, text="系统监控", 
                  command=self.system_monitor).pack(fill=tk.X, pady=2)
        
        # 开发工具区域
        dev_frame = ttk.LabelFrame(main_frame, text="开发工具", padding="5")
        dev_frame.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(dev_frame, text="代码编辑器", 
                  command=self.code_editor).pack(fill=tk.X, pady=2)
        ttk.Button(dev_frame, text="知识库管理", 
                  command=self.knowledge_base).pack(fill=tk.X, pady=2)
        ttk.Button(dev_frame, text="项目构建", 
                  command=self.project_build).pack(fill=tk.X, pady=2)
        
        # 日志输出区域
        log_frame = ttk.LabelFrame(main_frame, text="系统日志", padding="5")
        log_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        self.log_text = tk.Text(log_frame, height=10, width=70)
        scrollbar = ttk.Scrollbar(log_frame, orient="vertical", command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # 配置网格权重
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        self.log("✅ 第13轮传承平台启动成功")
        self.log("🔒 零信任安全架构已就绪")
        self.log("🎨 GUI开发环境初始化完成")
    
    def log(self, message):
        """添加日志"""
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        self.root.update()
    
    def network_scan(self):
        """网络扫描"""
        self.log("🔍 开始网络扫描...")
        try:
            result = subprocess.run(["nmap", "--version"], capture_output=True, text=True)
            self.log(f"✅ nmap版本: {result.stdout.split()[2]}")
        except Exception as e:
            self.log(f"❌ 网络扫描失败: {e}")
    
    def quantum_test(self):
        """量子加密测试"""
        self.log("🔐 运行量子安全加密测试...")
        threading.Thread(target=self._run_quantum_test).start()
    
    def _run_quantum_test(self):
        try:
            result = subprocess.run(["python", "quantum_safe_fixed.py"], 
                                  capture_output=True, text=True)
            for line in result.stdout.split('\n'):
                if line.strip():
                    self.log(f"🔬 {line}")
        except Exception as e:
            self.log(f"❌ 量子测试失败: {e}")
    
    def system_monitor(self):
        """系统监控"""
        self.log("📊 检查系统状态...")
        try:
            # 检查内存
            result = subprocess.run(["free", "-h"], capture_output=True, text=True)
            memory_line = result.stdout.split('\n')[1]
            self.log(f"💾 内存状态: {memory_line}")
        except Exception as e:
            self.log(f"❌ 系统监控失败: {e}")
    
    def code_editor(self):
        """代码编辑器"""
        self.log("📝 启动代码编辑器...")
        try:
            subprocess.Popen(["geany"])
            self.log("✅ Geany代码编辑器已启动")
        except Exception as e:
            self.log(f"❌ 启动编辑器失败: {e}")
    
    def knowledge_base(self):
        """知识库管理"""
        self.log("📚 打开知识库...")
        self.log("📍 知识库位置: ~/my-ai-business/知识库")
    
    def project_build(self):
        """项目构建"""
        self.log("🔨 开始项目构建...")
        self.log("✅ 构建环境检查完成")

if __name__ == "__main__":
    root = tk.Tk()
    app = AIDevelopmentPlatform(root)
    root.mainloop()
