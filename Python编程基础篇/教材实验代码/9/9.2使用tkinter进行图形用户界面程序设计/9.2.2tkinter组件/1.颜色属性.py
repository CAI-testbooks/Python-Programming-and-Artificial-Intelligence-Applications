# -*- coding: utf-8 -*-
# 来源：第9章，书内p176；PDF第188页。
# 整理说明：补齐窗口及标签对象。
import tkinter as tk
root=tk.Tk()
label1=tk.Label(root,text='背景颜色');label1.pack()
label2=tk.Label(root,text='前景颜色');label2.pack()
label1.config(bg='#000ffffff')
label2.config(fg='red')
root.mainloop()
