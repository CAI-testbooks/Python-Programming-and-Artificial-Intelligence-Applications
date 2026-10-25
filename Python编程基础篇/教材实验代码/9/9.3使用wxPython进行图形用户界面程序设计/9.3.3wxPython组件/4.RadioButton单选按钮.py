# -*- coding: utf-8 -*-
# 来源：第9章，书内p197,198；PDF第209,210页。
# 整理说明：合并跨页代码；去除教材行号和排版换行。
import wx


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        self.languages = ["Python", "Java", "C++", "JavaScript", "Ruby", "Go", "Swift"]
        self.radio_vars = [wx.RadioButton(self, label=lang, style=wx.RB_GROUP if i == 0 else 0) for i, lang in
                           enumerate(self.languages)]
        self.radiobutton_label = wx.StaticText(self, label="你最喜欢的编程语言: ")

        self.setup_ui()    # 设置UI布局
        self.setup_events()    # 绑定事件

    def setup_ui(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL) # 设置BoxSizer布局器，涉及布局管理

        radiobutton_sizer = wx.BoxSizer(wx.HORIZONTAL)
        for radio_var in self.radio_vars:
            radiobutton_sizer.Add(radio_var, 0, wx.ALL, 5)

        main_sizer.Add(self.radiobutton_label, 0, wx.ALL | wx.CENTER, 5)
        main_sizer.Add(radiobutton_sizer, 0, wx.ALL | wx.CENTER, 5)

        self.SetSizer(main_sizer)

    def setup_events(self):
        for radio_var in self.radio_vars:
            radio_var.Bind(wx.EVT_RADIOBUTTON, self.on_radiobutton)

    def on_radiobutton(self, event):
        # 获取选中的编程语言
        selected_language = next(
            lang for lang, radio_var in zip(self.languages, self.radio_vars) if radio_var.GetValue())
        self.radiobutton_label.SetLabel("你最喜欢的编程语言: " + selected_language)
        self.Layout()                         # 更新布局使文本居中

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, title="编程语言选择", size=(600, 120))
    frame.Show()
    app.MainLoop()
