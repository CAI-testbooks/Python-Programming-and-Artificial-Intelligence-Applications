# -*- coding: utf-8 -*-
# 来源：第9章，书内p204,205；PDF第216,217页。
# 整理说明：合并跨页代码；去除教材行号和排版换行。
import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)


        panel = wx.Panel(self)
        self.static_text = wx.StaticText(panel, label="请点击一个按钮。")
        self.button1 = wx.Button(panel, id=1, label="按钮1")
        self.button2 = wx.Button(panel, id=2, label="按钮2")

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.static_text, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 10)
        vbox.Add(self.button1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        vbox.Add(self.button2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.on_button_click, id=1, id2=2) # 同时绑定两个按钮至on_button_click

    def on_button_click(self, event):
        button_id = event.GetId()   # 获取事件源ID
        if button_id == 1:
            self.static_text.SetLabel("按钮1被点击。")
        elif button_id == 2:
            self.static_text.SetLabel("按钮2被点击。")

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, title="事件处理")
    frame.Show()
    app.MainLoop()
