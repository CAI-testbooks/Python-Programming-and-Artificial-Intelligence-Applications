# -*- coding: utf-8 -*-
# 来源：第9章，书内p203；PDF第215页。
# 整理说明：合并跨页代码；去除教材行号和排版换行。
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super(MyFrame, self).__init__(parent=None, title="GridSizer布局管理器", size=(300, 300))


        sizer = wx.GridSizer(3, 3, 0, 0)  # 创建一个3行3列无间距的网格

        # 添加按钮到GridSizer中
        for row in range(3):
            for col in range(3):
                button = wx.Button(self, label=f"({row}, {col})")
                sizer.Add(button, 1, wx.EXPAND)

        self.SetSizer(sizer)


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
