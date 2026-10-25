# -*- coding: utf-8 -*-
# 来源：第9章，书内p177；PDF第189页。
# 整理说明：补齐窗口及标签对象。
import tkinter as tk
root=tk.Tk()
label=tk.Label(root,text='字体属性');label.pack()
label.config(font=('黑体',15,'bold italic overstrike'))
root.mainloop()
