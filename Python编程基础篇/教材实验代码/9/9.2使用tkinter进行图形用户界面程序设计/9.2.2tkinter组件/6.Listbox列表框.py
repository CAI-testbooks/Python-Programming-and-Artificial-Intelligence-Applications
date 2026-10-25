# -*- coding: utf-8 -*-
# 来源：第9章，书内p181；PDF第193页。
# 整理说明：合并跨页代码；去除教材行号和排版换行。
import tkinter as tk

def update_selection():                                 # 显示按钮事件处理函数
    selected_indices = listbox.curselection()
    label.config(text="curselection(): " + str(selected_indices))

root = tk.Tk()
list_var = tk.StringVar()
list_var.set("Java Python C++ JavaScript Ruby Go Swift")  # 设置控制变量初始值， 作为初始列表项

listbox = tk.Listbox(root, listvariable=list_var, selectmode=tk.MULTIPLE) # 创建列表框，可多选
listbox.pack(padx=10, pady=10)

label = tk.Label(root, text="curselection(): ()")
label.pack(padx=10, pady=5)

label_all = tk.Label(root, text="get(0,END):"+str(listbox.get(0, tk.END)))
label_all.pack(padx=10, pady=5)

button_show = tk.Button(root, text="显示选中", command=update_selection)
button_show.pack(padx=10, pady=5)

root.mainloop()
