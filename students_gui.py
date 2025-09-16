import tkinter as tk
from students import students  # 假设 students.py 里有 students 列表

# 查询函数，根据输入框内容查找学生信息
def search():
    query = entry.get()  # 获取输入框内容
    result = ""
    # 遍历学生列表，查找姓名或学号匹配的学生
    for s in students:
        if s["name"] == query or s["student_id"] == query:
            result = f"姓名: {s['name']}, 学号: {s['student_id']}"
            break
    else:
        # 如果没有找到，显示未找到信息
        result = "未找到该学生"
    result_label.config(text=result)  # 更新结果标签内容

root = tk.Tk()  # 创建主窗口
root.title("学生信息查询")  # 设置窗口标题

# 使窗口无边框，便于自定义拖动
root.overrideredirect(True)

# 拖动窗口时记录鼠标按下时的位置
def start_move(event):
    root.x = event.x  # 记录鼠标相对窗口左上角的x坐标
    root.y = event.y  # 记录鼠标相对窗口左上角的y坐标

# 拖动窗口时根据鼠标移动调整窗口位置
def do_move(event):
    x = event.x_root - root.x  # 计算窗口新的x坐标
    y = event.y_root - root.y  # 计算窗口新的y坐标
    root.geometry(f"+{x}+{y}")  # 移动窗口到新位置

# 绑定鼠标事件，实现窗口拖动
root.bind("<ButtonPress-1>", start_move)  # 鼠标左键按下时记录位置
root.bind("<B1-Motion>", do_move)         # 鼠标左键拖动时移动窗口

# 创建标签，提示用户输入
tk.Label(root, text="输入姓名或学号:").pack(pady=(20, 5))
# 创建输入框
entry = tk.Entry(root)
entry.pack()

# 创建查询按钮，点击后执行search函数
tk.Button(root, text="查询", command=search).pack(pady=5)
# 创建用于显示查询结果的标签
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# 创建关闭按钮，放在窗口底部，点击后关闭窗口
close_btn = tk.Button(root, text="关闭", command=root.destroy)
close_btn.pack(side="bottom", pady=10)

# 进入主事件循环，显示窗口
root.mainloop()