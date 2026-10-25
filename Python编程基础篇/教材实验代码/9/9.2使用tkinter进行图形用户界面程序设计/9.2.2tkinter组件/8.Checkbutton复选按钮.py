# -*- coding: utf-8 -*-
# 来源：第9章，书内p183,184；PDF第195,196页。
# 整理说明：合并跨页代码；去除教材行号和排版换行。
import tkinter as tk

def update_checkbutton_text(): # 复选按钮的回调函数，通过检查所有控制变量的值获取选中项
    selected_languages = [languages[i] for i in range(len(languages)) if check_vars[i].get() == 1]
    checkbutton_label.config(text="你喜欢的编程语言: " + ", ".join(selected_languages))

def update_radiobutton_text(): # 单选按钮的回调函数，通过共享控制变量的值获取选中项
    selected_language = radio_var.get()
    radiobutton_label.config(text="你最喜欢的编程语言: " + selected_language)

root = tk.Tk()

languages = ["Python", "Java", "C++", "JavaScript", "Ruby", "Go", "Swift"]
check_vars = [tk.IntVar() for _ in range(len(languages))]

checkbutton_label = tk.Label(root, text="你喜欢的编程语言: ")
checkbutton_label.pack(side=tk.TOP, padx=10, pady=5)

checkbutton_frame = tk.Frame(root)          # 框架组件Frame
checkbutton_frame.pack(side=tk.TOP, padx=10, pady=5)

for i, language in enumerate(languages):    # 每个复选按钮对应不同的控制变量
    tk.Checkbutton(checkbutton_frame, text=language, variable=check_vars[i], command=update_checkbutton_text).pack(side=tk.LEFT, padx=5, pady=5)

# 创建单选按钮的控制变量
radio_var = tk.StringVar()

# 创建单选按钮
radiobutton_label = tk.Label(root, text="你最喜欢的编程语言: ")
radiobutton_label.pack(side=tk.TOP, padx=10, pady=5)

radiobutton_frame = tk.Frame(root)   # 框架组件Frame
radiobutton_frame.pack(side=tk.TOP, padx=10, pady=5)

for language in languages:           # 一组单选按钮共同对应同一个控制变量
    tk.Radiobutton(radiobutton_frame, text=language, variable=radio_var, value=language, command=update_radiobutton_text).pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
