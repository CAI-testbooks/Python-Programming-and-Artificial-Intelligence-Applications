# -*- coding: utf-8 -*-
# 来源：第9章，书内p179,180；PDF第191,192页。
# 整理说明：校验回调使用%P取得编辑后的候选内容，修复非法字符进入输入框的问题。
import tkinter as tk

def validate_password(val):                            # 执行密码校验操作的函数
    if val.isdigit() or val == "":
        return True
    else:
        label.config(text="密码必须为数字。", fg='red')
        return False

def done():                                               # 确定按钮事件函数
    label.config(text="输入的用户名：%s；密码：%s" % (entry_username.get(), entry_password.get()), fg='black')

root = tk.Tk()
root.title("Login")

label_username = tk.Label(root, text="用户名:")            # 创建用户名标签
label_username.pack(side=tk.TOP, padx=10, pady=5)
entry_username = tk.Entry(root)                           # 创建用户名输入框
entry_username.pack(side=tk.TOP, padx=10, pady=5)

# 创建密码输入框和标签
label_password = tk.Label(root, text="密码:")              # 创建密码标签
label_password.pack(side=tk.TOP, padx=10, pady=5)
entry_password = tk.Entry(root, show="*", validate="key", validatecommand=(root.register(validate_password), '%P'))         # 创建密码输入框
entry_password.pack(side=tk.TOP, padx=10, pady=5)

label = tk.Label(root, text="", fg="black")
label.pack(side=tk.TOP, padx=10, pady=5)

button_confirm = tk.Button(root, text="确定", command=done) # 创建确定按钮
button_confirm.pack(side=tk.TOP, padx=10, pady=10)

root.mainloop()
