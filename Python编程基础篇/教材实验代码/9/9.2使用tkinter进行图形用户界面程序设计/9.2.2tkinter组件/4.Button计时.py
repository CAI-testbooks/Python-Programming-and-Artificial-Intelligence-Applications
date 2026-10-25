# -*- coding: utf-8 -*-
# 来源：第9章，书内p178,179；PDF第190,191页。
# 整理说明：合并跨页代码；去除教材行号和排版换行。
import tkinter as tk
import time

start_time = 0
elapsed_time = 0
root = tk.Tk()
texts = {'start': '点击按钮开始计时', 'stop': '点击按钮停止计时'}

def start_timer():                                    # 点击按钮开始计时
    global start_time
    start_time = time.time()
    info['text'] = texts['stop']
    btn['command'] = stop_timer                       # 设置停止计时事件处理函数

def stop_timer():                                   # 点击按钮停止计时
    global start_time, elapsed_time
    elapsed_time += time.time() - start_time
    info['text'] = f"记录的时间长度: {elapsed_time:.2f} 秒"   # 得到计时时长
    btn['state'] = tk.DISABLED

info = tk.Label(text=texts['start'], width=50)
info.pack()
btn = tk.Button(text="按钮", command=start_timer)   # 设置开始计时事件处理函数
btn.pack()
root.mainloop()
