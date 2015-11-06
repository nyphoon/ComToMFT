# coding=UTF-8
import subprocess
import env_setting
import time

import wx

def win_show(win_title):
    app = wx.App(redirect=True)
    top = wx.Frame(None, title=win_title, size=(300,200))

    top.Show()

    m_text = wx.StaticText(top, -1, "Hello World!")
    m_text.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
    m_text.SetSize(m_text.GetBestSize())

    top.Add(m_text, 0, wx.ALL, 10)

    return top
    # app.MainLoop()
    # top.Close()
def win_close(frame):
    frame.Close()

def op_wait(path):
    print(path)
    env_setting.msg("start process = "+path[0])
    child = subprocess.Popen(path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    streamdata = child.communicate()
    env_setting.msg(streamdata)
    # return: code , stdout , stderr
    return [child.returncode, streamdata[0], streamdata[1]]


#class interop_monitor(object):
def op_poll(path):
    out = []
    err = []
    child = subprocess.Popen(path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    win = win_show(path[0])
    while child.poll() is None:
        out = out + child.stdout.readlines()
        err = err + child.stderr.readlines()
        # err = err + child.stderr.readlines() or ''
        env_setting.msg_d('polling process id='+str(child.pid))

    win_close(win)

    return [child.returncode, ''.join(out), ''.join(err)]