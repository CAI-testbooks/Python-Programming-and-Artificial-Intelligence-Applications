# -*- coding: utf-8 -*-
# 来源：第9章，书内p189；PDF第201页。
# 整理说明：给Place布局指定可见窗口尺寸，避免默认窗口过小。
import tkinter as tk
root = tk.Tk()
root.geometry('360x240')
A_label = tk.Label(root, text="Label A", bg="red")
B_label = tk.Label(root, text="Label B", bg="green")
A_label.place(x=0, y=100)   # 使用绝对坐标确定标签A的位置
B_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER) # 使用相对坐标让标签B永远 居于窗口正中央
root.mainloop()
