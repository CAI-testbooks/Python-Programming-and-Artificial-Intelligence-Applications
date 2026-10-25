# -*- coding: utf-8 -*-
# 来源：第9章，书内p186；PDF第198页。
# 整理说明：合并跨页代码；去除教材行号和排版换行。
import tkinter as tk
root = tk.Tk()
LabelA = tk.Label(root, text="LabelA", bg="red")
LabelA.pack(fill=tk.BOTH, expand=tk.FALSE)
LabelB = tk.Label(root, text="LabelB", bg="green")
LabelB.pack(fill=tk.NONE, expand=tk.TRUE)
LabelC = tk.Label(root, text="LabelC", bg="blue")
LabelC.pack(fill=tk.NONE, expand=tk.TRUE, anchor = tk.NE)
LabelD = tk.Label(root, text="LabelD", bg="yellow")
LabelD.pack(fill=tk.BOTH, side=tk.RIGHT)
root.mainloop()
