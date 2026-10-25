# -*- coding: utf-8 -*-
# 来源：第9章，书内p201；PDF第213页。
# 整理说明：将方向声明片段补成可运行示例。
import wx
app=wx.App(False)
frame=wx.Frame(None,title='BoxSizer方向',size=(360,200))
panel=wx.Panel(frame)
hbox = wx.BoxSizer(wx.HORIZONTAL)   # 设置为水平方向布局
vbox = wx.BoxSizer(wx.VERTICAL)     # 设置为垂直方向布局

hbox.Add(wx.Button(panel,label='左'),0,wx.ALL,5)
hbox.Add(wx.Button(panel,label='右'),0,wx.ALL,5)
vbox.Add(wx.StaticText(panel,label='垂直布局包含水平布局'),0,wx.ALL,5)
vbox.Add(hbox)
panel.SetSizer(vbox)
frame.Show();app.MainLoop()
