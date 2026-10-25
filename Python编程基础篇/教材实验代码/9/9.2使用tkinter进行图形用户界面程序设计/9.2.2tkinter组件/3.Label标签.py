# -*- coding: utf-8 -*-
# 来源：第9章，书内p178；PDF第190页。
# 整理说明：合并跨页代码；去除教材行号和排版换行。
import tkinter as tk
root = tk.Tk()
Label_str = "Label是用于显示文本或图片的标签组件,主要用于界面上各项功能的提示。"
label = tk.Label(root, bitmap='info',text=Label_str)  # 设置标签显示位图和文本
label.config(width=500, height=100)                   # 设置标签高和宽
label.config(bd=3, relief=tk.SOLID)                   # 设置标签边框宽度和样式
label.config(compound=tk.LEFT)                        # 设置位图在文本左侧显示
label.config(justify=tk.LEFT)                         # 设置文本左对齐
label.config(anchor=tk.E)                             # 设置内容在标签的右侧显示
label.config(font=('黑体',15))                        # 设置字体
label.config(wraplength=400)                          # 设置文本回卷宽度
label.pack()
root.mainloop()
