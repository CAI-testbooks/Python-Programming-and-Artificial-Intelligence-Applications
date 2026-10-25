# -*- coding: utf-8 -*-
# 来源：第9章，书内p190；PDF第202页。
# 整理说明：回调接收event；使用选择变化事件，确保读到本次选择结果。
import tkinter as tk

def update_selection(event=None):                                 # 显示按钮事件处理函数
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

listbox.bind('<<ListboxSelect>>', update_selection)
root.mainloop()
