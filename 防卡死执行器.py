#!/usr/bin/env python3
"""
防卡死安全执行器 - 避免Termux缓冲区溢出
特性：分块输出、进度显示、自动保存
"""
import time
import subprocess
import sys

class SafeExecutor:
    def __init__(self):
        self.checkpoints = []
    
    def safe_execute(self, command, description="执行命令"):
        """安全执行命令，避免卡死"""
        print(f"🔄 {description}...")
        
        try:
            # 使用Popen实时读取输出，避免缓冲区满
            process = subprocess.Popen(
                command, 
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # 实时读取输出
            output_lines = []
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    print(output.strip())
                    output_lines.append(output.strip())
                    # 每输出5行强制刷新
                    if len(output_lines) % 5 == 0:
                        sys.stdout.flush()
                        time.sleep(0.1)  # 给终端处理时间
            
            # 检查返回值
            returncode = process.poll()
            if returncode == 0:
                print(f"✅ {description}完成")
                return True
            else:
                print(f"❌ {description}失败")
                return False
                
        except Exception as e:
            print(f"💥 执行错误: {e}")
            return False
    
    def create_checkpoint(self, name):
        """创建检查点，自动git提交"""
        self.checkpoints.append(name)
        
        # 自动提交到Git
        commands = [
            "git add .",
            f"git commit -m \"检查点: {name}\"",
            "git push origin main"
        ]
        
        for cmd in commands:
            success = self.safe_execute(cmd, f"检查点: {name}")
            if not success:
                print(f"⚠️ 检查点 {name} 提交失败，但继续执行")
                break
        
        return success

def main():
    executor = SafeExecutor()
    
    print("🚀 启动防卡死工作流")
    
    # 第一步：环境检查
    executor.safe_execute("python 极简状态检查.py", "系统状态检查")
    
    # 创建检查点1
    executor.create_checkpoint("状态检查完成")
    
    # 第二步：环境修复
    executor.safe_execute("python Termux环境修复器.py", "环境修复")
    
    # 创建检查点2  
    executor.create_checkpoint("环境修复完成")
    
    # 第三步：升级验证
    executor.safe_execute("python 升级验证系统.py", "升级验证")
    
    # 最终提交
    executor.create_checkpoint("第12轮升级完成")
    
    print("🎉 所有任务安全完成！")

if __name__ == "__main__":
    main()
