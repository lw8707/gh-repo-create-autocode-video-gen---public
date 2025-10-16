#!/usr/bin/env python3
"""
按钮组件 - 零代码GUI开发环境
"""
import tkinter as tk
from tkinter import ttk

class DragDropButton:
    """可拖拽按钮组件"""
    
    def __init__(self, master, text="按钮", command=None):
        self.master = master
        self.text = text
        self.command = command
        
        self.button = ttk.Button(master, text=text, command=self._execute_command)
        self.is_dragging = False
        
        # 绑定拖拽事件
        self.button.bind("<ButtonPress-1>", self.start_drag)
        self.button.bind("<B1-Motion>", self.on_drag)
        self.button.bind("<ButtonRelease-1>", self.stop_drag)
    
    def start_drag(self, event):
        self.is_dragging = True
        self.start_x = event.x
        self.start_y = event.y
    
    def on_drag(self, event):
        if self.is_dragging:
            x = self.button.winfo_x() + (event.x - self.start_x)
            y = self.button.winfo_y() + (event.y - self.start_y)
            self.button.place(x=x, y=y)
    
    def stop_drag(self, event):
        self.is_dragging = False
    
    def _execute_command(self):
        if self.command and not self.is_dragging:
            self.command()
    
    def place(self, x, y):
        self.button.place(x=x, y=y)
    
    def get_properties(self):
        return {
            "type": "button",
            "text": self.text,
            "x": self.button.winfo_x(),
            "y": self.button.winfo_y()
        }

class VisualGUIEditor:
    """可视化GUI编辑器"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("零代码GUI开发环境 - 第14轮")
        self.root.geometry("1000x700")
        
        self.components = []
        self.setup_ui()
    
    def setup_ui(self):
        # 工具栏
        toolbar = ttk.Frame(self.root)
        toolbar.pack(side="top", fill="x")
        
        # 组件面板
        component_panel = ttk.LabelFrame(self.root, text="组件库", width=200)
        component_panel.pack(side="left", fill="y")
        
        # 设计画布
        design_canvas = ttk.LabelFrame(self.root, text="设计区域")
        design_canvas.pack(side="left", fill="both", expand=True)
        
        # 属性面板
        property_panel = ttk.LabelFrame(self.root, text="属性", width=200)
        property_panel.pack(side="right", fill="y")
        
        # 添加组件按钮
        components = ["按钮", "输入框", "标签", "列表", "表格"]
        for comp in components:
            btn = ttk.Button(component_panel, text=comp, 
                           command=lambda c=comp: self.add_component(c))
            btn.pack(fill="x", padx=5, pady=2)
        
        self.design_frame = ttk.Frame(design_canvas)
        self.design_frame.pack(fill="both", expand=True)
        
        # 代码生成按钮
        generate_btn = ttk.Button(toolbar, text="生成代码", command=self.generate_code)
        generate_btn.pack(side="right", padx=5)
    
    def add_component(self, comp_type):
        """添加组件到设计区域"""
        if comp_type == "按钮":
            component = DragDropButton(self.design_frame, text="新按钮")
            component.place(50, 50)
            self.components.append(component)
    
    def generate_code(self):
        """生成可执行代码"""
        code = '''#!/usr/bin/env python3
"""
生成的GUI应用 - 由零代码平台创建
"""
import tkinter as tk
from tkinter import ttk

class GeneratedApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("生成的应用")
        self.root.geometry("600x400")
        self.create_widgets()
    
    def create_widgets(self):
'''
        
        for i, comp in enumerate(self.components):
            props = comp.get_properties()
            code += f'''
        # 组件 {i+1}
        self.button_{i} = ttk.Button(self.root, text="{props['text']}")
        self.button_{i}.place(x={props['x']}, y={props['y']})
'''
        
        code += '''
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = GeneratedApp()
    app.run()
'''
        
        with open("generated_gui_app.py", "w", encoding="utf-8") as f:
            f.write(code)
        
        print("✅ GUI代码已生成: generated_gui_app.py")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    editor = VisualGUIEditor()
    editor.run()
