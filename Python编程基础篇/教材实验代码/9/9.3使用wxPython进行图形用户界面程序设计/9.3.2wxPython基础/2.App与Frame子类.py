# -*- coding: utf-8 -*-
# 来源：第9章，书内p192；PDF第204页。
# 整理说明：合并跨页代码；去除教材行号和排版换行。
import wx


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)  # 创建内容面板

        self.label = wx.StaticText(panel, label="Hello World", pos=(80, 20))


class MyApp(wx.App):
    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame(None, title="Hello World", size=(400, 300))
        frame.Show()
        return True

    def OnExit(self):
        print('应用程序退出。')
        return 0


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
