# -*- coding: utf-8 -*-
# 来源：第9章，书内p196；PDF第208页。
# 整理说明：合并跨页代码；去除教材行号和排版换行。
import wx

class LoginFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="登录界面", size=(400, 300))
        panel = wx.Panel(self)

        # 创建用户名输入框
        wx.StaticText(panel, label="用户名：", pos=(50, 50))
        self.username_textctrl = wx.TextCtrl(panel, pos=(150, 50), size=(200, -1))
        self.username_textctrl.SetMaxLength(20)

        # 创建密码输入框（允许按Enter提交）
        wx.StaticText(panel, label="密码：", pos=(50, 100))
        self.password_textctrl = wx.TextCtrl(panel, pos=(150, 100), size=(200, -1), style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        self.password_textctrl.Bind(wx.EVT_TEXT_ENTER, self.on_submit)
        self.password_textctrl.SetMaxLength(20)

        # 显示用户输入的多行只读文本框
        self.log_textctrl = wx.TextCtrl(panel, pos=(50, 200), size=(300, 60), style=wx.TE_MULTILINE | wx.TE_READONLY)

    def on_submit(self, event):
        """处理密码输入框的提交逻辑"""
        password = self.password_textctrl.GetValue()
        username = self.username_textctrl.GetValue()
        self.log_textctrl.AppendText(f"用户名: {username}\n密码: {password}\n")
        self.username_textctrl.Clear()
        self.password_textctrl.Clear()

if __name__ == "__main__":
    app = wx.App(False)
    LoginFrame().Show()
    app.MainLoop()
