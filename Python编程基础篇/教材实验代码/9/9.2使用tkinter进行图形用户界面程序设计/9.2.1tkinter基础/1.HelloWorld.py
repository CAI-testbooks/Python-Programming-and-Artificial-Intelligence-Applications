# -*- coding: utf-8 -*-
# 来源：第9章，书内p175；PDF第187页。
# 整理说明：将未定义的app改为root。
import tkinter as tk                       # 导入tkinter模块
root = tk.Tk()                              # 创建主窗口
L = tk.Label(root, text = "Hello World!")   # 创建标签类实例对象
L.pack()                                   # 指定Pack布局

def change_button_text():
    btn.configure(text="已点击")            # 定义按钮点击事件处理函数

btn = tk.Button(root, text="点击我", command=change_button_text) #创建按钮类实例对象
btn.pack()                                 # 指定Pack布局
root.mainloop()                             # 开始事件循环
