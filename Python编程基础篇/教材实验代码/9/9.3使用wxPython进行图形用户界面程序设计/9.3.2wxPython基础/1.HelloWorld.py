# -*- coding: utf-8 -*-
# 来源：第9章，书内p191；PDF第203页。
# 整理说明：合并跨页代码；去除教材行号和排版换行。
import wx
app = wx.App()                                                # 创建应用程序对象
frm = wx.Frame(None, title="Hello World")                     # 创建窗口对象
frm.Show()                                                    # 显示窗口
label = wx.StaticText(frm, label="Hello World", pos=(80, 20)) # 创建静态文本组件
app.MainLoop()                                                # 进入主事件循环
