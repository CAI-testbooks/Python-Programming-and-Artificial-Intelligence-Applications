# -*- coding: utf-8 -*-
# 来源：第9章，书内p188；PDF第200页。
# 整理说明：合并跨页代码；去除教材行号和排版换行。
import tkinter as tk
root = tk.Tk()
LabelA = tk.Label(root, text="LabelA", bg="red")
LabelA.grid(row=0,column=0,columnspan=2,sticky=tk.W+tk.E) # 标签A在0行0列，同时跨越两列且向左右方向拉伸
LabelB = tk.Label(root, text="LabelB", bg="green")
LabelB.grid(row=1,column=1)    # 标签B在1行1列
LabelC = tk.Label(root, text="LabelC", bg="blue")
LabelC.grid(row=1,column=0)    # 标签C在1行0列
LabelD = tk.Label(root, text="LabelD", bg="yellow")
LabelD.grid(row=2,column=3)    # 标签D在2行3列
root.mainloop()
