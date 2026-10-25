# -*- coding: utf-8 -*-
# 来源：第9章，书内p199,200；PDF第211,212页。
# 整理说明：合并跨页代码；去除教材行号和排版换行。
import wx


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        self.languages = ["Python", "Java", "C++", "JavaScript", "Ruby", "Go", "Swift"]
        # 创建三态复选框
        self.check_vars = [wx.CheckBox(self, label=lang, style=wx.CHK_3STATE | wx.CHK_ALLOW_3RD_STATE_FOR_USER) for lang
                           in self.languages]
        self.radio_vars = [wx.RadioButton(self, label=lang, style=wx.RB_GROUP if i == 0 else 0) for i, lang in
                           enumerate(self.languages)]
        self.checkbutton_label = wx.StaticText(self, label="你喜欢的编程语言: ")
        self.radiobutton_label = wx.StaticText(self, label="你最喜欢的编程语言: ")

        self.setup_ui()                       # 设置UI布局
        self.setup_events()                   # 绑定事件

    def setup_ui(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL) # 设置BoxSizer布局器，涉及布局管理
        checkbutton_sizer = wx.BoxSizer(wx.HORIZONTAL)
        for check_var in self.check_vars:
            checkbutton_sizer.Add(check_var, 0, wx.ALL, 5)

        radiobutton_sizer = wx.BoxSizer(wx.HORIZONTAL)
        for radio_var in self.radio_vars:
            radiobutton_sizer.Add(radio_var, 0, wx.ALL, 5)

        main_sizer.Add(self.checkbutton_label, 0, wx.ALL | wx.CENTER, 5)
        main_sizer.Add(checkbutton_sizer, 0, wx.ALL | wx.CENTER, 5)
        main_sizer.Add(self.radiobutton_label, 0, wx.ALL | wx.CENTER, 5)
        main_sizer.Add(radiobutton_sizer, 0, wx.ALL | wx.CENTER, 5)

        self.SetSizer(main_sizer)

    def setup_events(self):
        for check_var in self.check_vars:
            check_var.Bind(wx.EVT_CHECKBOX, self.on_checkbutton)

        for radio_var in self.radio_vars:
            radio_var.Bind(wx.EVT_RADIOBUTTON, self.on_radiobutton)

    def on_checkbutton(self, event):
        # 获取选中的编程语言
        selected_languages = [lang for lang, check_var in zip(self.languages, self.check_vars) if
                              check_var.Get3StateValue() == wx.CHK_CHECKED]
        self.checkbutton_label.SetLabel("你确定喜欢的编程语言: " + ", ".join (selected_languages))
        self.Layout()   # 更新布局使文本居中

    def on_radiobutton(self, event):
        # 获取选中的编程语言
        selected_language = next(
            lang for lang, radio_var in zip(self.languages, self.radio_vars) if radio_var.GetValue())
        self.radiobutton_label.SetLabel("你最喜欢的编程语言: " + selected_language)
        self.Layout()   # 更新布局使文本居中


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, title="编程语言选择", size=(600, 200))
    frame.Show()
    app.MainLoop()
