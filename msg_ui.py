# coding=UTF-8
import env_setting
import time

import wx
# wxPython Download Page: http://www.wxpython.org/download.php#msw

def ui_show(win_title):
    app = wx.App(redirect=True)
    top = wx.Frame(None, title=win_title, size=(300,200))

    top.Show()

    msg_text = wx.StaticText( top, -1, "Hello World!" )
    msg_text.SetFont( wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD) )
    msg_text.SetSize( msg_text.GetBestSize() )

    app.MainLoop()

if __name__ == '__main__':
    ui_show('test')