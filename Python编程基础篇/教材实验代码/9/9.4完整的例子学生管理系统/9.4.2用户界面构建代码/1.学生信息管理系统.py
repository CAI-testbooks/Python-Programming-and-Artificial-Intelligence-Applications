# -*- coding: utf-8 -*-
# 来源：第9章，书内p208,209,210,211,212；PDF第220,221,222,223,224页。
# 整理说明：保留教材界面结构；修复数据库初始化、金额类型、外键、异常处理及嵌套事件循环。
# -*- coding: utf-8 -*-
# @Time    : 2024/11/18
# @Author  : Ziyi Peng

import tkinter as tk
from tkinter import messagebox
import sqlite3

from student_store import connect_db,reset_database,add_student,delete_student,query_students

def table_query(cur,tab_name,col_names='*',num_line=None):
    if tab_name!='学生表' or col_names!='*':raise ValueError('仅允许查询学生表全部字段')
    if num_line is None:cur.execute('SELECT * FROM 学生表 ORDER BY 学号')
    elif isinstance(num_line,int) and num_line>0:
        cur.execute('SELECT * FROM 学生表 ORDER BY 学号 LIMIT ?',(num_line,))
    else:raise ValueError('请输入一个正整数')
    return cur.fetchall()

def display_results(listbox, results):
    listbox.delete(0, tk.END)
    for row in results:
        formatted_row = [str(item) if item is not None else'NULL'for item in row]
        listbox.insert(tk.END, ' | '.join(formatted_row))

def validate_input(input_text):
    if input_text.isdecimal() and int(input_text) > 0:
        return True
    else:
        messagebox.showerror("输入错误", "请输入一个正整数")
        return False

def Window_Add():
    window = tk.Toplevel()
    window.title("添加学生信息")
    window.geometry('440x460')

    labels = ['学号', '姓名', '性别', '生日', '专业编号', '奖学金', '党员', '备注']
    entries = {}

    for i, label_text in enumerate(labels):
        frame = tk.Frame(window)
        frame.pack(pady=5)

        tk.Label(frame, text=label_text, font=('Arial', 12), width=10).pack(side=tk.LEFT)
        entry = tk.Entry(frame, font=('Arial', 12))
        entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)
        entries[label_text] = entry

    def on_add():
        student_info={label:entry.get() for label,entry in entries.items()}
        try:
            add_student(student_info)
        except (ValueError,sqlite3.Error) as e:
            messagebox.showerror('添加失败',str(e))
        else:
            messagebox.showinfo('添加成功','学生信息已添加')
            window.destroy()

    tk.Button(window, text='添加', bg='silver', font=('Arial', 12), command=on_add, width=10).pack(pady=10)
    # 子窗口由主窗口的唯一事件循环管理。

def Window_Del():
    window = tk.Toplevel()
    window.title("删除学生信息")
    window.geometry('400x300')

    tk.Label(window, text="请输入要删除的学号:", font=('Arial', 12)).pack(pady=10)
    entry = tk.Entry(window, font=('Arial', 12))
    entry.pack(pady=10)

    def on_delete():
        try:
            found=delete_student(entry.get().strip())
        except sqlite3.Error as e:
            messagebox.showerror('删除失败',str(e));return
        if found:
            messagebox.showinfo('删除成功','学生信息已删除');window.destroy()
        else:messagebox.showerror('删除失败','学号不存在')

    tk.Button(window, text='删除', bg='silver', font=('Arial', 12), command= on_delete, width=10).pack(pady=10)
    # 子窗口由主窗口的唯一事件循环管理。

def Window_Ser():
    window = tk.Toplevel()
    window.title("查询学生信息")
    window.geometry('600x400')

    tk.Label(window, text="请输入要查询的数据条数:", font=('Arial', 12)).pack(pady=10)
    entry = tk.Entry(window, font=('Arial', 12))
    entry.pack(pady=10)

    listbox = tk.Listbox(window, font=('Arial', 12), width=80, height=15)
    listbox.pack(pady=10, fill=tk.BOTH, expand=True)

    def on_query():
        input_text=entry.get()
        if validate_input(input_text):
            try:display_results(listbox,query_students(int(input_text)))
            except sqlite3.Error as e:messagebox.showerror('查询失败',str(e))

    tk.Button(window, text='查询', bg='silver', font=('Arial', 12), command=on_query, width=10).pack(pady=10)
    # 子窗口由主窗口的唯一事件循环管理。

def Window_Exit():
    if messagebox.askokcancel("退出管理系统", "您确认离开系统吗？"):
        root.destroy()

def Window_Init():
    if messagebox.askokcancel('确认操作','该操作将重置演示学生数据库，请确认是否继续？'):
        try:reset_database()
        except (OSError,ValueError,sqlite3.Error) as e:messagebox.showerror('初始化失败',str(e))
        else:messagebox.showinfo('初始化成功','演示数据库已初始化')

if __name__ == '__main__':
    root = tk.Tk()
    root.title("学生信息管理系统")
    root.geometry('550x400')

    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.LEFT, padx=20, pady=20)

    tk.Button(button_frame, text='创 建 学 生 数 据 库', bg='silver', font=('Arial', 12), command=Window_Init, width=20).pack(pady=5)
    tk.Button(button_frame, text='添 加 学 生 信 息', bg='silver', font=('Arial', 12), command=Window_Add, width=20).pack(pady=5)
    tk.Button(button_frame, text='删 除 学 生 信 息', bg='silver', font=('Arial', 12), command=Window_Del, width=20).pack(pady=5)
    tk.Button(button_frame, text='展 示 学 生 信 息', bg='silver', font=('Arial', 12), command=Window_Ser, width=20).pack(pady=5)
    tk.Button(button_frame, text='退 出 管 理 系 统', bg='silver', font=('Arial', 12), command=Window_Exit, width=20).pack(pady=5)

    result = tk.StringVar()
    result.set(">>>欢迎使用学生信息管理系统<<<\n@Author:  Ziyi Peng\nComplete Time: 2024/11/18")
    tk.Label(root, bg="white", fg="black", font=("宋体", 12), bd='0', anchor='center', textvariable=result).pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH, expand=True)

    root.mainloop()
