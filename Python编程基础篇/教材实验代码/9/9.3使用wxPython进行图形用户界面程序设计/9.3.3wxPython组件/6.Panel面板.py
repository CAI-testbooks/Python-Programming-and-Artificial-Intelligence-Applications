# -*- coding: utf-8 -*-
# 来源：第9章，书内p200；PDF第212页。
# 整理说明：补齐Frame子类及事件循环。
import wx
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, size=(300, 200))
        panel = wx.Panel(parent=self)
        label = wx.StaticText(panel, label="Hello World", pos=(100, 50))

if __name__=='__main__':
    app=wx.App(False)
    frame=MyFrame();frame.Show();app.MainLoop()
