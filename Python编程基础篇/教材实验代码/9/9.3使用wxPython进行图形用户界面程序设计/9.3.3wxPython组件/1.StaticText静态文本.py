# -*- coding: utf-8 -*-
# 来源：第9章，书内p194；PDF第206页。
# 整理说明：合并跨页代码；去除教材行号和排版换行。
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="StaticText示例", size=(400,  300))
        panel = wx.Panel(self)

        # 静态文本：多行文本，左对齐，设置颜色和字体
        self.static_text = wx.StaticText(
            parent=panel,
            id=wx.ID_ANY,
            label="这是一个StaticText组件。\n它支持多行文本显示。\n你可以自定义外观样式。",
            pos=(20, 20),
            size=(300, 100),
            style=wx.ALIGN_LEFT
        )
        self.static_text.SetForegroundColour(wx.Colour(0, 0, 255)) # 设置文本颜色为蓝色
        font1 = wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)                              # 设置字体
        self.static_text.SetFont(font1)

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
