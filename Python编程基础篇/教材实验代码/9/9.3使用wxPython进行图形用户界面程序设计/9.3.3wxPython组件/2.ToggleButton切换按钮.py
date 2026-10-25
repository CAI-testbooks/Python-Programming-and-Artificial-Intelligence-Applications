# -*- coding: utf-8 -*-
# 来源：第9章，书内p194,195；PDF第206,207页。
# 整理说明：合并跨页代码；去除教材行号和排版换行。
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="ToggleButton示例", size=(400, 200))
        panel = wx.Panel(self)

        # 创建ToggleButton
        self.toggle_button = wx.ToggleButton(panel, label="开", pos=(50, 50), size=(100, 30))
        self.toggle_button.Bind(wx.EVT_TOGGLEBUTTON, self.on_toggle) # 绑定事件

        # 创建一个静态文本，用于显示按钮状态
        self.status_label = wx.StaticText(panel, label="按钮状态：关闭", pos=(200, 55))
        self.status_label.SetForegroundColour(wx.Colour(0, 0, 255)) # 设置颜色

        # 设置初始背景颜色
        panel.SetBackgroundColour(wx.Colour(255, 200, 200))

        self.panel = panel

    def on_toggle(self, event):
        """处理ToggleButton的切换事件"""
        if self.toggle_button.GetValue():
            self.toggle_button.SetLabel("关")  # 按钮处于选中状态
            self.status_label.SetLabel("按钮状态：打开")
            self.panel.SetBackgroundColour(wx.Colour(200, 255, 200)) # 改变背景颜色
        else:
            self.toggle_button.SetLabel("开")  # 按钮处于未选中状态
            self.status_label.SetLabel("按钮状态：关闭")
            self.panel.SetBackgroundColour(wx.Colour(255, 200, 200)) # 恢复背景颜色

        self.panel.Refresh()                   # 刷新界面以应用背景颜色更改

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
