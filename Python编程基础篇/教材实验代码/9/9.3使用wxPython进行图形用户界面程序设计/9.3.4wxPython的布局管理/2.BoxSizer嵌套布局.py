# -*- coding: utf-8 -*-
# 来源：第9章，书内p202；PDF第214页。
# 整理说明：合并跨页代码；去除教材行号和排版换行。
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super(MyFrame, self).__init__(parent=None, title="Boxsizer布局器", size=(300, 150))
        self.Centre()                      # 设置窗口居中
        panel = wx.Panel(parent=self)
        vbox = wx.BoxSizer(wx.VERTICAL)    # 创建垂直方向的BoxSizer布局管理器对象
        hbox = wx.BoxSizer(wx.HORIZONTAL)  # 创建水平方向的BoxSizer布局管理器对象

        statictext1 = wx.StaticText(parent=panel, label='请点击按钮。')

        vbox.Add(statictext1, proportion=2, flag=wx.ALIGN_CENTER | wx.TOP, border=10)                     # 设置水平居中且有顶部边框

        btn1 = wx.Button(panel, label="按钮1")
        btn2 = wx.Button(panel, label="按钮2")

        hbox.Add(btn1, proportion=0, flag=wx.ALIGN_CENTER | wx.ALL, border=5) # 设置垂直居中且四边都有边框
        hbox.Add(btn2, proportion=0, flag=wx.ALIGN_CENTER | wx.ALL, border=5) # 设置垂直居中且四边都有边框
        vbox.Add(hbox, proportion=1, flag=wx.ALIGN_CENTER)

        panel.SetSizer(vbox)


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
