# -*- coding: utf-8 -*-
# 来源：第9章，书内p190；PDF第202页。
# 整理说明：补齐组件和callback，保留教材绑定方法。
import tkinter as tk
root=tk.Tk()
label=tk.Label(root,text='等待事件');label.pack()
entryA=tk.Entry(root);entryA.pack()
entryB=tk.Entry(root);entryB.pack()
A=root
def callback(event):
    label.config(text=f'事件：{event.type}；组件：{event.widget.winfo_class()}')
entryA.bind_class("Entry", "<Key>", callback)  # 绑定Entry类的Key事件
root.mainloop()
